#!/usr/bin/env python3
"""
Task 8.1.4: Extract All Citations from Sources Directory
========================================================

This script systematically extracts all paper titles, authors, and DOIs
from the sources directory to create a comprehensive CSV for citation management.

Author: AI Assistant
Date: 2025-01-20
Task: 8.1.4 List all potential citations
"""

import os
import json
import csv
import re
import glob
from pathlib import Path
from typing import Dict, List, Set, Optional
import pandas as pd

# Configure paths
SOURCES_DIR = "sources"
OUTPUT_CSV = os.path.join(SOURCES_DIR, "8.1.4-all-citations.csv")
LOG_FILE = "tools/8.1.4_extract_all_citations.log"

class CitationExtractor:
    def __init__(self):
        self.citations = []
        self.processed_files = []
        self.errors = []
        self.seen_citations = set()
        
    def log(self, message: str):
        """Log messages to both console and file"""
        print(message)
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{message}\n")
    
    def extract_from_json(self, file_path: str) -> List[Dict]:
        """Extract citations from JSON files"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            citations = []
            
            # Handle different JSON structures
            if isinstance(data, list):
                for item in data:
                    citation = self.parse_json_item(item, file_path)
                    if citation:
                        citations.append(citation)
            elif isinstance(data, dict):
                # Handle nested structures
                citation = self.parse_json_item(data, file_path)
                if citation:
                    citations.append(citation)
                
                # Look for nested papers/references
                for key, value in data.items():
                    if key.lower() in ['papers', 'references', 'citations', 'results', 'literature']:
                        if isinstance(value, list):
                            for item in value:
                                citation = self.parse_json_item(item, file_path)
                                if citation:
                                    citations.append(citation)
            
            return citations
            
        except Exception as e:
            self.errors.append(f"Error processing {file_path}: {str(e)}")
            return []
    
    def parse_json_item(self, item: Dict, source_file: str) -> Optional[Dict]:
        """Parse individual JSON item for citation information"""
        if not isinstance(item, dict):
            return None
        
        title = ""
        authors = ""
        doi = ""
        year = ""
        journal = ""
        url = ""
        
        # Extract title (try multiple field names)
        for title_field in ['title', 'Title', 'paper_title', 'document_title', 'name']:
            if title_field in item and item[title_field]:
                title = str(item[title_field]).strip()
                break
        
        # Extract authors (try multiple field names and formats)
        for author_field in ['authors', 'Authors', 'author', 'Author', 'authorString']:
            if author_field in item and item[author_field]:
                if isinstance(item[author_field], list):
                    # Handle list of authors (may be strings or dicts)
                    author_list = []
                    for author in item[author_field]:
                        if isinstance(author, dict):
                            if 'name' in author:
                                author_list.append(author['name'])
                            elif 'displayName' in author:
                                author_list.append(author['displayName'])
                            elif 'first' in author and 'last' in author:
                                author_list.append(f"{author['first']} {author['last']}")
                        else:
                            author_list.append(str(author))
                    authors = "; ".join(author_list)
                else:
                    authors = str(item[author_field])
                break
        
        # Extract DOI
        for doi_field in ['doi', 'DOI', 'externalIds', 'external_ids']:
            if doi_field in item:
                if isinstance(item[doi_field], dict) and 'DOI' in item[doi_field]:
                    doi = str(item[doi_field]['DOI'])
                elif isinstance(item[doi_field], str):
                    doi = str(item[doi_field])
                break
        
        # Extract year
        for year_field in ['year', 'Year', 'publicationDate', 'published_date', 'date']:
            if year_field in item and item[year_field]:
                year_val = str(item[year_field])
                # Extract year from date strings
                year_match = re.search(r'\b(19|20)\d{2}\b', year_val)
                if year_match:
                    year = year_match.group()
                break
        
        # Extract journal
        for journal_field in ['journal', 'Journal', 'venue', 'Venue', 'publication']:
            if journal_field in item and item[journal_field]:
                if isinstance(item[journal_field], dict) and 'name' in item[journal_field]:
                    journal = str(item[journal_field]['name'])
                else:
                    journal = str(item[journal_field])
                break
        
        # Extract URL
        for url_field in ['url', 'URL', 'link', 'pdf_url', 'openAccessPdf']:
            if url_field in item and item[url_field]:
                if isinstance(item[url_field], dict) and 'url' in item[url_field]:
                    url = str(item[url_field]['url'])
                else:
                    url = str(item[url_field])
                break
        
        # Only create citation if we have at least title
        if title:
            # Clean DOI format
            if doi and not doi.startswith('10.'):
                doi_match = re.search(r'10\.\d+/[^\s]+', doi)
                if doi_match:
                    doi = doi_match.group()
                else:
                    doi = ""
            
            citation = {
                'title': title,
                'authors': authors,
                'doi': doi,
                'year': year,
                'journal': journal,
                'url': url,
                'source_file': source_file
            }
            
            # Check for duplicates using title as key
            citation_key = title.lower().strip()
            if citation_key not in self.seen_citations:
                self.seen_citations.add(citation_key)
                return citation
        
        return None
    
    def extract_from_markdown(self, file_path: str) -> List[Dict]:
        """Extract citations from markdown files using regex patterns"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            citations = []
            
            # Pattern for DOI references
            doi_pattern = r'(?:doi:|DOI:|https?://doi\.org/)?\s*(10\.\d+/[^\s\)]+)'
            dois = re.findall(doi_pattern, content, re.IGNORECASE)
            
            # Pattern for year references
            year_pattern = r'\b(19|20)\d{2}\b'
            years = re.findall(year_pattern, content)
            
            # Pattern for title-like content in quotes or bold
            title_pattern = r'(?:"([^"]+)"|(?:\*\*|__)([^*_]+)(?:\*\*|__))'
            titles = re.findall(title_pattern, content)
            
            # Pattern for author names (Last, First format)
            author_pattern = r'([A-Z][a-z]+,\s[A-Z][a-z\.\s]*(?:,\s[A-Z][a-z]+)*)'
            authors = re.findall(author_pattern, content)
            
            # Create citations from extracted information
            for i, doi in enumerate(dois):
                citation = {
                    'title': titles[i][0] if i < len(titles) and titles[i][0] else "",
                    'authors': authors[i] if i < len(authors) else "",
                    'doi': doi,
                    'year': years[i] if i < len(years) else "",
                    'journal': "",
                    'url': f"https://doi.org/{doi}",
                    'source_file': file_path
                }
                
                citation_key = f"{doi}_{file_path}"
                if citation_key not in self.seen_citations:
                    self.seen_citations.add(citation_key)
                    citations.append(citation)
            
            return citations
            
        except Exception as e:
            self.errors.append(f"Error processing {file_path}: {str(e)}")
            return []
    
    def extract_from_csv(self, file_path: str) -> List[Dict]:
        """Extract citations from CSV files"""
        try:
            df = pd.read_csv(file_path)
            citations = []
            
            # Map common column names
            column_mapping = {
                'title': ['title', 'Title', 'paper_title', 'name', 'Paper Title'],
                'authors': ['authors', 'Authors', 'author', 'Author'],
                'doi': ['doi', 'DOI', 'external_id'],
                'year': ['year', 'Year', 'date', 'publication_year'],
                'journal': ['journal', 'Journal', 'venue', 'publication']
            }
            
            for _, row in df.iterrows():
                title = ""
                authors = ""
                doi = ""
                year = ""
                journal = ""
                
                # Extract data using column mapping
                for field, possible_cols in column_mapping.items():
                    for col in possible_cols:
                        if col in df.columns and not pd.isna(row[col]):
                            if field == 'title':
                                title = str(row[col])
                            elif field == 'authors':
                                authors = str(row[col])
                            elif field == 'doi':
                                doi = str(row[col])
                            elif field == 'year':
                                year_val = str(row[col])
                                year_match = re.search(r'\b(19|20)\d{2}\b', year_val)
                                if year_match:
                                    year = year_match.group()
                            elif field == 'journal':
                                journal = str(row[col])
                            break
                
                if title:
                    citation = {
                        'title': title,
                        'authors': authors,
                        'doi': doi,
                        'year': year,
                        'journal': journal,
                        'url': f"https://doi.org/{doi}" if doi else "",
                        'source_file': file_path
                    }
                    
                    citation_key = title.lower().strip()
                    if citation_key not in self.seen_citations:
                        self.seen_citations.add(citation_key)
                        citations.append(citation)
            
            return citations
            
        except Exception as e:
            self.errors.append(f"Error processing {file_path}: {str(e)}")
            return []
    
    def process_directory(self, directory: str):
        """Process all files in a directory recursively"""
        self.log(f"Processing directory: {directory}")
        
        # Find all relevant files
        json_files = glob.glob(os.path.join(directory, "**/*.json"), recursive=True)
        md_files = glob.glob(os.path.join(directory, "**/*.md"), recursive=True)
        csv_files = glob.glob(os.path.join(directory, "**/*.csv"), recursive=True)
        
        self.log(f"Found {len(json_files)} JSON files, {len(md_files)} markdown files, {len(csv_files)} CSV files")
        
        # Process JSON files
        for json_file in json_files:
            self.log(f"Processing JSON: {json_file}")
            citations = self.extract_from_json(json_file)
            self.citations.extend(citations)
            self.processed_files.append(json_file)
            self.log(f"  Extracted {len(citations)} citations")
        
        # Process CSV files
        for csv_file in csv_files:
            self.log(f"Processing CSV: {csv_file}")
            citations = self.extract_from_csv(csv_file)
            self.citations.extend(citations)
            self.processed_files.append(csv_file)
            self.log(f"  Extracted {len(citations)} citations")
        
        # Process Markdown files
        for md_file in md_files:
            self.log(f"Processing Markdown: {md_file}")
            citations = self.extract_from_markdown(md_file)
            self.citations.extend(citations)
            self.processed_files.append(md_file)
            self.log(f"  Extracted {len(citations)} citations")
    
    def save_to_csv(self, output_file: str):
        """Save all citations to CSV file"""
        try:
            fieldnames = ['title', 'authors', 'doi', 'year', 'journal', 'url', 'source_file']
            
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                # Sort citations by year (descending) and then by title
                sorted_citations = sorted(
                    self.citations, 
                    key=lambda x: (x.get('year', ''), x.get('title', ''))
                )
                
                for citation in sorted_citations:
                    writer.writerow(citation)
            
            self.log(f"Successfully saved {len(self.citations)} citations to {output_file}")
            
        except Exception as e:
            self.log(f"Error saving CSV: {str(e)}")
    
    def generate_summary(self):
        """Generate processing summary"""
        self.log("\n" + "="*50)
        self.log("CITATION EXTRACTION SUMMARY")
        self.log("="*50)
        self.log(f"Total citations extracted: {len(self.citations)}")
        self.log(f"Files processed: {len(self.processed_files)}")
        self.log(f"Errors encountered: {len(self.errors)}")
        
        # Count citations by source type
        source_types = {}
        for citation in self.citations:
            source_file = citation.get('source_file', '')
            if '.json' in source_file:
                source_types['JSON'] = source_types.get('JSON', 0) + 1
            elif '.csv' in source_file:
                source_types['CSV'] = source_types.get('CSV', 0) + 1
            elif '.md' in source_file:
                source_types['Markdown'] = source_types.get('Markdown', 0) + 1
        
        self.log("\nCitations by source type:")
        for source_type, count in source_types.items():
            self.log(f"  {source_type}: {count}")
        
        # Count citations with DOI
        with_doi = sum(1 for c in self.citations if c.get('doi'))
        self.log(f"\nCitations with DOI: {with_doi} ({with_doi/len(self.citations)*100:.1f}%)")
        
        # Count citations with year
        with_year = sum(1 for c in self.citations if c.get('year'))
        self.log(f"Citations with year: {with_year} ({with_year/len(self.citations)*100:.1f}%)")
        
        if self.errors:
            self.log("\nErrors encountered:")
            for error in self.errors:
                self.log(f"  {error}")

def main():
    """Main execution function"""
    # Initialize log file
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Citation Extraction Log - Task 8.1.4\n")
        f.write(f"Started: {pd.Timestamp.now()}\n")
        f.write("="*50 + "\n")
    
    extractor = CitationExtractor()
    extractor.log("Starting citation extraction from sources directory...")
    
    # Process the sources directory
    if os.path.exists(SOURCES_DIR):
        extractor.process_directory(SOURCES_DIR)
        
        # Save results
        extractor.save_to_csv(OUTPUT_CSV)
        
        # Generate summary
        extractor.generate_summary()
        
        extractor.log(f"\nTask 8.1.4 completed successfully!")
        extractor.log(f"Output file: {OUTPUT_CSV}")
        extractor.log(f"Log file: {LOG_FILE}")
        
    else:
        extractor.log(f"Error: Sources directory '{SOURCES_DIR}' not found!")

if __name__ == "__main__":
    main() 
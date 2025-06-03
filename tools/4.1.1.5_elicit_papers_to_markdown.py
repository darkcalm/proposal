#!/usr/bin/env python3

import fitz  # PyMuPDF
import os
import re
import json
from pathlib import Path
from datetime import datetime
import bibtexparser
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PHASE2_OUTPUT_DIR = WORKSPACE_ROOT / "sources" / "4.1.8-elicit-results" / "phase-2-targeted-queries"
DOWNLOADED_PAPERS_DIR = PHASE2_OUTPUT_DIR / "downloaded_papers"
MARKDOWN_PAPERS_DIR = PHASE2_OUTPUT_DIR / "markdown_papers"

def extract_metadata_from_filename(filename):
    """Extract metadata from filename patterns used by the paper downloader."""
    # Remove .pdf extension
    base_name = filename.replace('.pdf', '')
    
    # Extract DOI if present
    doi_match = re.search(r'_DOI_(.+)$', base_name)
    doi = None
    if doi_match:
        doi = doi_match.group(1).replace('-', '.').replace('_', '/')
        # Remove DOI part from title
        base_name = re.sub(r'_DOI_.+$', '', base_name)
    
    # Convert underscores to spaces for title
    title = base_name.replace('_', ' ')
    
    return {
        'filename': filename,
        'title': title,
        'doi': doi,
        'extracted_date': datetime.now().isoformat()
    }

def extract_bibtex_metadata(bib_file_path, title):
    """Extract metadata from BibTeX file for a given paper title."""
    try:
        with open(bib_file_path, 'r', encoding='utf-8') as bibfile:
            bib_database = bibtexparser.load(bibfile)
            
        # Normalize title for comparison
        normalized_target = title.lower().strip()
        
        for entry in bib_database.entries:
            entry_title = entry.get('title', '').replace('{', '').replace('}', '').lower().strip()
            
            # Check for title match
            if normalized_target in entry_title or entry_title in normalized_target:
                return {
                    'bibtex_id': entry.get('ID', ''),
                    'title': entry.get('title', '').replace('{', '').replace('}', ''),
                    'authors': entry.get('author', ''),
                    'year': entry.get('year', ''),
                    'journal': entry.get('journal', ''),
                    'venue': entry.get('booktitle', ''),
                    'doi': entry.get('doi', ''),
                    'url': entry.get('url', ''),
                    'abstract': entry.get('abstract', ''),
                    'keywords': entry.get('keywords', '')
                }
    except Exception as e:
        logging.warning(f"Could not extract BibTeX metadata for '{title}': {e}")
    
    return None

def clean_extracted_text(text):
    """Clean and format extracted PDF text for better readability."""
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n', '\n\n', text)
    
    # Fix common PDF extraction issues
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)  # Add space between words that got joined
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)  # Join hyphenated words across lines
    
    # Clean up extra spaces
    text = re.sub(r' +', ' ', text)
    
    return text.strip()

def pdf_to_markdown_enhanced(pdf_path, metadata, output_path):
    """Convert PDF to markdown with enhanced formatting and metadata."""
    
    try:
        doc = fitz.open(pdf_path)
        
        # Start with metadata header
        markdown_content = f"""# {metadata.get('title', 'Unknown Title')}

## Paper Metadata

- **Filename:** {metadata.get('filename', 'Unknown')}
- **DOI:** {metadata.get('doi', 'Not available')}
- **Authors:** {metadata.get('authors', 'Not available')}
- **Year:** {metadata.get('year', 'Not available')}
- **Journal/Venue:** {metadata.get('journal') or metadata.get('venue', 'Not available')}
- **URL:** {metadata.get('url', 'Not available')}
- **Extraction Date:** {metadata.get('extracted_date', 'Unknown')}
- **Total Pages:** {doc.page_count}

## Abstract

{metadata.get('abstract', 'Abstract not available from BibTeX metadata.')}

## Keywords

{metadata.get('keywords', 'Keywords not available from BibTeX metadata.')}

---

## Full Text Content

"""
        
        # Extract text from each page
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            
            # Extract text with better formatting
            text = page.get_text("text")
            cleaned_text = clean_extracted_text(text)
            
            if cleaned_text.strip():  # Only add pages with content
                markdown_content += f"\n\n### Page {page_num + 1}\n\n"
                markdown_content += cleaned_text
                markdown_content += "\n\n---\n"
        
        doc.close()
        
        # Write markdown file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        logging.info(f"Successfully converted {pdf_path.name} to {output_path.name}")
        return True
        
    except Exception as e:
        logging.error(f"Error converting PDF {pdf_path}: {e}")
        return False

def main():
    """Main function to convert all Elicit.com papers to markdown."""
    
    # Define paths
    pdf_dir = DOWNLOADED_PAPERS_DIR
    output_dir = MARKDOWN_PAPERS_DIR
    
    # Create output directory for markdown papers
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create summary directory for documentation
    docs_output_dir = WORKSPACE_ROOT / "docs"
    docs_output_dir.mkdir(parents=True, exist_ok=True)
    
    if not pdf_dir.exists():
        logging.error(f"PDF directory not found: {pdf_dir}")
        return
    
    # Process all PDF files in all subdirectories
    pdf_files = []
    for research_area_dir in pdf_dir.iterdir():
        if research_area_dir.is_dir():
            pdf_files.extend(list(research_area_dir.glob("*.pdf")))
    
    if not pdf_files:
        logging.warning(f"No PDF files found in {pdf_dir}")
        return
    
    logging.info(f"Found {len(pdf_files)} PDF files to convert")
    
    conversion_results = []
    successful_conversions = 0
    failed_conversions = 0
    
    for pdf_file in pdf_files:
        if pdf_file.name.startswith('.'):  # Skip hidden files
            continue
            
        logging.info(f"Processing: {pdf_file.name}")
        
        # Extract metadata from filename
        file_metadata = extract_metadata_from_filename(pdf_file.name)
        
        # Create output markdown filename
        clean_title = re.sub(r'[^\w\s-]', '', file_metadata['title'])
        clean_title = re.sub(r'\s+', '_', clean_title.strip())
        output_filename = f"{clean_title[:100]}.md"  # Limit filename length
        
        # Create output directory matching the research area
        research_area_dir = pdf_file.parent.name
        output_path = output_dir / research_area_dir / output_filename
        
        # Convert PDF to markdown
        success = pdf_to_markdown_enhanced(pdf_file, file_metadata, output_path)
        
        conversion_results.append({
            'pdf_file': pdf_file.name,
            'markdown_file': output_filename if success else None,
            'title': file_metadata['title'],
            'doi': file_metadata.get('doi'),
            'success': success
        })
        
        if success:
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    # Generate summary report
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    summary_file = docs_output_dir / f"4.1.1.5-elicit-papers-markdown-conversion-summary.md"
    
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write(f"""# Task 4.1.1.5: Elicit.com Papers to Markdown Conversion Summary

**Conversion Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Script Used:** `tools/4.1.1.5_elicit_papers_to_markdown.py`  
**Source Directory:** `{pdf_dir.relative_to(WORKSPACE_ROOT)}`  
**Output Directory:** `{output_dir.relative_to(WORKSPACE_ROOT)}`

## Conversion Results

- **Total PDF files found:** {len(pdf_files)}
- **Successful conversions:** {successful_conversions}
- **Failed conversions:** {failed_conversions}
- **Success rate:** {(successful_conversions/len(pdf_files)*100):.1f}%

## Converted Papers

| PDF File | Markdown File | Title | DOI |
|----------|---------------|-------|-----|
""")
        
        for result in conversion_results:
            f.write(f"| {result['pdf_file']} | {result['markdown_file'] or 'FAILED'} | {result['title'][:50]}{'...' if len(result['title']) > 50 else ''} | {result.get('doi', 'N/A')} |\n")
        
        f.write(f"""

## Output Structure

The converted markdown files are organized by research area:

```
{output_dir.relative_to(WORKSPACE_ROOT)}/
├── 3.1.1-applied-human-factors/
│   ├── [paper_title_1].md
│   └── [paper_title_2].md
├── 3.1.2-industry-academia-collaborative/
│   └── ...
└── ...
```

Each markdown file contains:
- **Paper metadata:** Title, authors, DOI, journal, year, etc.
- **Abstract:** Extracted from PDF
- **Full text content:** Page-by-page extraction from PDF

## Notes

- Text extraction uses PyMuPDF for reliable PDF processing
- File naming uses cleaned paper titles for better organization
- Failed conversions may indicate corrupted or password-protected PDFs
""")
    
    logging.info(f"Conversion complete! Summary saved to {summary_file.relative_to(WORKSPACE_ROOT)}")
    logging.info(f"Results: {successful_conversions} successful, {failed_conversions} failed")
    logging.info(f"Markdown files available in: {output_dir.relative_to(WORKSPACE_ROOT)}")

if __name__ == "__main__":
    main() 
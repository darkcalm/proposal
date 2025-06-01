import requests
import os
import re
import time
from urllib.parse import urlparse
from pathlib import Path
import arxiv
import scholarly
from datetime import datetime
import difflib

def extract_doi(text):
    """Extract DOI from text using regex."""
    doi_pattern = r'10\.\d{4,}/[\w\.-]+'
    match = re.search(doi_pattern, text)
    return match.group(0) if match else None

def get_paper_info(doi):
    """Get paper information from Semantic Scholar API."""
    base_url = "https://api.semanticscholar.org/v1/paper/"
    headers = {
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(f"{base_url}{doi}", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching paper info for DOI {doi}: {e}")
        return None

def search_arxiv(title):
    """Search for paper on arXiv."""
    try:
        search = arxiv.Search(
            query=title,
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
        for result in search.results():
            return result.pdf_url
    except Exception as e:
        print(f"Error searching arXiv: {e}")
    return None

def search_google_scholar(title):
    """Search for paper on Google Scholar."""
    try:
        search_query = scholarly.search_pubs(title)
        paper = next(search_query)
        if paper.get('eprint_url'):
            return paper['eprint_url']
    except Exception as e:
        print(f"Error searching Google Scholar: {e}")
    return None

def download_pdf(url, output_path):
    """Download PDF from URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF from {url}: {e}")
        return False

def find_existing_paper(title, output_dir):
    """Check if a paper with similar title already exists."""
    # Normalize the title for comparison
    normalized_title = title.lower().replace(' ', '_')
    
    # Get list of existing PDFs
    existing_files = list(output_dir.glob('*.pdf'))
    
    # Check for exact match first
    for file in existing_files:
        if file.stem.lower() == normalized_title[:100]:
            return file
    
    # If no exact match, check for similarity
    for file in existing_files:
        similarity = difflib.SequenceMatcher(None, 
            file.stem.lower(), 
            normalized_title[:100]
        ).ratio()
        if similarity > 0.8:  # 80% similarity threshold
            return file
    
    return None

def main():
    # Create output directory
    output_dir = Path("sources/4.1-semantic-search/elicit-results/elicit-review-papers")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Create log file for missing papers
    log_dir = Path("sources/4.1-semantic-search/elicit-results/logs")
    log_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    missing_papers_log = log_dir / f"missing_papers_{timestamp}.txt"
    
    # Read sources file
    sources_file = "sources/4.1-semantic-search/elicit-results/Elicit - Secure Protocols for Distributed Energy Coordinati - Sources.txt"
    
    with open(sources_file, 'r') as f:
        content = f.read()
    
    # Split into individual entries
    entries = content.split('\n\n')
    
    # Track statistics
    total_papers = len(entries)
    found_papers = 0
    existing_papers = 0
    missing_papers = []
    
    print(f"\nProcessing {total_papers} papers...")
    
    for entry in entries:
        if not entry.strip():
            continue
            
        # Extract DOI
        doi = extract_doi(entry)
        if not doi:
            print(f"\nNo DOI found in entry: {entry[:100]}...")
            missing_papers.append({
                'title': entry.split('\n')[0],
                'reason': 'No DOI found',
                'entry': entry
            })
            continue
            
        print(f"\nProcessing DOI: {doi}")
        
        # Get paper info
        paper_info = get_paper_info(doi)
        if not paper_info:
            missing_papers.append({
                'title': entry.split('\n')[0],
                'reason': 'Failed to fetch paper info',
                'doi': doi
            })
            continue
            
        title = paper_info.get('title', 'unknown')
        print(f"Title: {title}")
        
        # Check if paper already exists
        existing_file = find_existing_paper(title, output_dir)
        if existing_file:
            print(f"Paper already exists: {existing_file.name}")
            existing_papers += 1
            continue
        
        # Try multiple sources for PDF
        pdf_url = None
        
        # Try Semantic Scholar first
        pdf_url = paper_info.get('openAccessPdf', {}).get('url')
        
        # Try arXiv if Semantic Scholar fails
        if not pdf_url:
            print("Trying arXiv...")
            pdf_url = search_arxiv(title)
            
        # Try Google Scholar if arXiv fails
        if not pdf_url:
            print("Trying Google Scholar...")
            pdf_url = search_google_scholar(title)
            
        if not pdf_url:
            print(f"No PDF URL found for: {title}")
            missing_papers.append({
                'title': title,
                'reason': 'No PDF URL found in any source',
                'doi': doi
            })
            continue
            
        # Generate filename from title
        filename = f"{title[:100].replace(' ', '_')}.pdf"
        output_path = output_dir / filename
        
        print(f"Downloading: {filename}")
        if download_pdf(pdf_url, output_path):
            print(f"Successfully downloaded: {filename}")
            found_papers += 1
        else:
            print(f"Failed to download: {filename}")
            missing_papers.append({
                'title': title,
                'reason': 'Failed to download PDF',
                'doi': doi,
                'url': pdf_url
            })
            
        # Be nice to the APIs
        time.sleep(2)
    
    # Write missing papers to log file
    with open(missing_papers_log, 'w') as f:
        f.write(f"Missing Papers Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total papers: {total_papers}\n")
        f.write(f"Found papers: {found_papers}\n")
        f.write(f"Existing papers: {existing_papers}\n")
        f.write(f"Missing papers: {len(missing_papers)}\n\n")
        
        for paper in missing_papers:
            f.write(f"Title: {paper['title']}\n")
            f.write(f"Reason: {paper['reason']}\n")
            if 'doi' in paper:
                f.write(f"DOI: {paper['doi']}\n")
            if 'url' in paper:
                f.write(f"URL: {paper['url']}\n")
            if 'entry' in paper:
                f.write(f"Full entry:\n{paper['entry']}\n")
            f.write("\n" + "-"*80 + "\n\n")
    
    print(f"\nSummary:")
    print(f"Total papers: {total_papers}")
    print(f"Found papers: {found_papers}")
    print(f"Existing papers: {existing_papers}")
    print(f"Missing papers: {len(missing_papers)}")
    print(f"\nMissing papers report saved to: {missing_papers_log}")

if __name__ == "__main__":
    main() 
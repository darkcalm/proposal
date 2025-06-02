import requests
import os
import re
import time
from urllib.parse import urlparse, quote
from pathlib import Path
import arxiv
import bibtexparser
from datetime import datetime
import difflib
import logging
import backoff
from tqdm import tqdm
from bs4 import BeautifulSoup
import scholarly
import urllib.parse

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

# Alternative paper sources
PAPER_SOURCES = {
    'semantic_scholar': {
        'base_url': 'https://api.semanticscholar.org/graph/v1/paper/',
        'fields': 'title,authors,year,abstract,openAccessPdf,url'
    },
    'arxiv': {
        'base_url': 'http://export.arxiv.org/api/query'
    },
    'unpaywall': {
        'base_url': 'https://api.unpaywall.org/v2/'
    },
    'core': {
        'base_url': 'https://core.ac.uk/api/v2/search/works'
    },
    'researchgate': {
        'base_url': 'https://www.researchgate.net/search/publication?q=',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    },
    'google_scholar': {
        'base_url': 'https://scholar.google.com/scholar?q=',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    }
}

def clean_title_for_filename(title: str) -> str:
    """Clean title to be suitable for a filename."""
    if not title:
        return "unknown_title"
    # Remove curly braces commonly found in BibTeX titles
    title = title.replace('{', '').replace('}', '')
    # Replace spaces with underscores and remove/replace other problematic characters
    title = re.sub(r'[\\/*?:"<>|]', '_', title)
    title = title.replace(' ', '_')
    # Truncate to a reasonable length
    return title[:150]

def extract_doi_from_bibtex_entry(entry):
    """Extract DOI from a bibtexparser entry dictionary."""
    # Common fields for DOI
    doi_fields = ['doi', 'DOI']
    for field in doi_fields:
        if field in entry:
            return entry[field].strip()
    
    # Sometimes DOI is in the 'url' field or 'note'
    url_fields = ['url', 'URL', 'link']
    for field in url_fields:
        if field in entry:
            url_val = entry[field]
            match = re.search(r'10\.\d{4,}/[\w\.-]+', url_val)
            if match:
                return match.group(0)
                
    if 'note' in entry:
        match = re.search(r'10\.\d{4,}/[\w\.-]+', entry['note'])
        if match:
            return match.group(0)
            
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def get_paper_info_from_semantic_scholar(doi):
    """Get paper information from Semantic Scholar API using DOI with retry logic."""
    headers = {
        "Accept": "application/json",
        "User-Agent": "ProposalHelper/1.0 (contact@example.com; for academic research)" 
    }
    
    try:
        url = f"{PAPER_SOURCES['semantic_scholar']['base_url']}{doi.upper()}"
        params = {'fields': PAPER_SOURCES['semantic_scholar']['fields']}
        
        logging.info(f"Querying Semantic Scholar for DOI: {doi}")
        response = requests.get(url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching paper info for DOI {doi}: {e}")
        return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def get_paper_info_from_unpaywall(doi):
    """Get paper information from Unpaywall API using DOI with retry logic."""
    headers = {
        "Accept": "application/json",
        "User-Agent": "ProposalHelper/1.0 (contact@example.com; for academic research)" 
    }
    
    try:
        url = f"{PAPER_SOURCES['unpaywall']['base_url']}{doi}"
        logging.info(f"Querying Unpaywall for DOI: {doi}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching paper info from Unpaywall for DOI {doi}: {e}")
        return None

def search_arxiv_by_title(title):
    """Search for paper on arXiv by title."""
    try:
        logging.info(f"Searching arXiv for title: {title}")
        search = arxiv.Search(
            query=f'ti:"{title}"', # Search for exact title
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
        client = arxiv.Client()
        results = list(client.results(search))
        if results:
            logging.info(f"Found on arXiv: {results[0].entry_id}")
            return results[0].pdf_url
    except Exception as e:
        logging.error(f"Error searching arXiv for '{title}': {e}")
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def download_pdf_from_url(url, output_path: Path):
    """Download PDF from URL with retry logic and progress bar."""
    try:
        logging.info(f"Attempting to download PDF from: {url}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f, tqdm(
            desc=output_path.name,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        logging.info(f"Successfully downloaded to: {output_path.name}")
        return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading PDF from {url}: {e}")
        return False

def normalize_title(title: str) -> str:
    """Normalize title for comparison by removing special characters, converting to lowercase,
    and standardizing common variations."""
    if not title:
        return ""
    
    # Convert to lowercase
    title = title.lower()
    
    # Remove special characters and extra spaces
    title = re.sub(r'[^\w\s-]', ' ', title)
    title = re.sub(r'\s+', ' ', title)
    
    # Standardize common variations
    replacements = {
        'distributed energy resource': 'der',
        'distributed energy resources': 'der',
        'der': 'der',
        'agent communication protocol': 'acp',
        'agent-to-agent': 'a2a',
        'agent to agent': 'a2a',
        'a2a': 'a2a',
        'internet of energy': 'ioe',
        'ioe': 'ioe',
        'smart grid': 'sg',
        'sg': 'sg',
        'microgrid': 'mg',
        'mg': 'mg',
        'demand response': 'dr',
        'dr': 'dr',
        'blockchain': 'bc',
        'bc': 'bc',
        'artificial intelligence': 'ai',
        'ai': 'ai',
        'machine learning': 'ml',
        'ml': 'ml',
        'internet of things': 'iot',
        'iot': 'iot'
    }
    
    # Apply replacements
    for old, new in replacements.items():
        title = re.sub(r'\b' + re.escape(old) + r'\b', new, title)
    
    # Remove common words that don't add meaning
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by'}
    words = title.split()
    words = [w for w in words if w not in stop_words]
    
    return ' '.join(words)

def find_existing_paper_by_title(title: str, output_dir: Path):
    """Check if a paper with a similar title already exists in the output directory."""
    if not title:
        return None
    
    normalized_query_title = normalize_title(title)
    best_match = None
    best_similarity = 0.7  # Lower threshold for initial matching
    
    for existing_pdf in output_dir.glob('*.pdf'):
        # Extract title from filename (remove DOI part and file extension)
        filename_title = existing_pdf.stem
        if '_DOI_' in filename_title:
            filename_title = filename_title.split('_DOI_')[0]
        
        normalized_existing_title = normalize_title(filename_title)
        
        # Calculate similarity using difflib
        similarity = difflib.SequenceMatcher(None, normalized_query_title, normalized_existing_title).ratio()
        
        # Additional checks for partial matches
        if similarity < best_similarity:
            # Check if one title contains the other
            if normalized_query_title in normalized_existing_title or normalized_existing_title in normalized_query_title:
                similarity = 0.8  # Boost similarity for contained titles
        
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = existing_pdf
    
    if best_match:
        logging.info(f"Found existing similar paper: {best_match.name} (similarity: {best_similarity:.2f})")
        return best_match
    
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def search_researchgate(title):
    """Search for paper on ResearchGate by title."""
    try:
        logging.info(f"Searching ResearchGate for title: {title}")
        encoded_title = quote(title)
        url = f"{PAPER_SOURCES['researchgate']['base_url']}{encoded_title}"
        
        response = requests.get(url, headers=PAPER_SOURCES['researchgate']['headers'], timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Look for PDF links in the search results
        pdf_links = soup.find_all('a', href=re.compile(r'\.pdf$'))
        
        if pdf_links:
            # Get the first PDF link
            pdf_url = pdf_links[0]['href']
            if not pdf_url.startswith('http'):
                pdf_url = f"https://www.researchgate.net{pdf_url}"
            return pdf_url
    except Exception as e:
        logging.error(f"Error searching ResearchGate for '{title}': {e}")
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def search_google_scholar(title):
    """Search for paper on Google Scholar by title."""
    try:
        logging.info(f"Searching Google Scholar for title: {title}")
        encoded_title = quote(title)
        url = f"{PAPER_SOURCES['google_scholar']['base_url']}{encoded_title}"
        
        response = requests.get(url, headers=PAPER_SOURCES['google_scholar']['headers'], timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        # Look for PDF links in the search results
        pdf_links = soup.find_all('a', href=re.compile(r'\.pdf$'))
        
        if pdf_links:
            # Get the first PDF link
            pdf_url = pdf_links[0]['href']
            return pdf_url
    except Exception as e:
        logging.error(f"Error searching Google Scholar for '{title}': {e}")
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3)
def search_core_by_title(title):
    """Search for paper on CORE by title."""
    try:
        logging.info(f"Searching CORE for title: {title}")
        encoded_title = quote(title)
        url = f"{PAPER_SOURCES['core']['base_url']}?q={encoded_title}"
        
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if data.get('results'):
            # Get the first result's PDF URL
            first_result = data['results'][0]
            if first_result.get('downloadUrl'):
                return first_result['downloadUrl']
    except Exception as e:
        logging.error(f"Error searching CORE for '{title}': {e}")
    return None

def find_pdf_url(doi, title):
    """Find PDF URL from multiple sources."""
    pdf_urls = []
    
    # Try Semantic Scholar
    s2_info = get_paper_info_from_semantic_scholar(doi)
    if s2_info:
        if s2_info.get('openAccessPdf') and s2_info['openAccessPdf'].get('url'):
            pdf_urls.append(('Semantic Scholar OpenAccessPDF', s2_info['openAccessPdf']['url']))
        elif s2_info.get('url') and s2_info['url'].lower().endswith('.pdf'):
            pdf_urls.append(('Semantic Scholar main URL', s2_info['url']))
    
    # Try Unpaywall
    unpaywall_info = get_paper_info_from_unpaywall(doi)
    if unpaywall_info:
        if unpaywall_info.get('best_oa_location') and unpaywall_info['best_oa_location'].get('url'):
            pdf_urls.append(('Unpaywall', unpaywall_info['best_oa_location']['url']))
    
    # Try arXiv
    arxiv_url = search_arxiv_by_title(title)
    if arxiv_url:
        pdf_urls.append(('arXiv', arxiv_url))
    
    # Try ResearchGate
    researchgate_url = search_researchgate(title)
    if researchgate_url:
        pdf_urls.append(('ResearchGate', researchgate_url))
    
    # Try Google Scholar
    google_scholar_url = search_google_scholar(title)
    if google_scholar_url:
        pdf_urls.append(('Google Scholar', google_scholar_url))
    
    # Try CORE
    core_url = search_core_by_title(title)
    if core_url:
        pdf_urls.append(('CORE', core_url))
    
    return pdf_urls

def main():
    # Define paths relative to workspace root
    bib_file_path = WORKSPACE_ROOT / "sources" / "4.1.1-elicit-results" / "Elicit - Decentralized Health Data Exchange in DERs - Sources.bib"
    output_papers_dir = WORKSPACE_ROOT / "sources" / "4.1.1-elicit-results" / "elicit-papers"
    log_dir = WORKSPACE_ROOT / "sources" / "4.1.1-elicit-results" / "logs"

    output_papers_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    missing_papers_log_file = log_dir / f"elicit_downloader_missing_papers_{timestamp}.txt"
    download_summary_log_file = log_dir / f"elicit_downloader_summary_{timestamp}.txt"

    if not bib_file_path.exists():
        logging.error(f"BibTeX file not found: {bib_file_path}")
        return

    with open(bib_file_path, 'r', encoding='utf-8') as bibfile:
        try:
            bib_database = bibtexparser.load(bibfile)
        except Exception as e:
            logging.error(f"Error parsing BibTeX file: {e}")
            return
            
    entries = bib_database.entries
    
    total_entries = len(entries)
    papers_downloaded_count = 0
    papers_existed_count = 0
    papers_info_missing_count = 0
    papers_pdf_url_missing_count = 0
    papers_download_failed_count = 0
    
    missing_papers_details = []

    logging.info(f"Processing {total_entries} BibTeX entries from {bib_file_path.name}...")
    
    for i, entry in enumerate(entries):
        logging.info(f"--- Processing entry {i+1}/{total_entries} ---")
        
        title = entry.get('title', 'Unknown Title')
        cleaned_title = title.replace('{', '').replace('}', '').strip()
        logging.info(f"BibTeX Title: {cleaned_title}")

        doi = extract_doi_from_bibtex_entry(entry)
        
        if not doi:
            logging.warning(f"No DOI found for entry: {entry.get('ID', 'N/A')} - Title: {cleaned_title}")
            papers_info_missing_count += 1
            missing_papers_details.append({
                'id': entry.get('ID', 'N/A'),
                'title': cleaned_title,
                'doi': 'N/A',
                'reason': 'No DOI found'
            })
            continue

        # Check if paper already exists
        if find_existing_paper_by_title(cleaned_title, output_papers_dir):
            logging.info(f"Paper '{cleaned_title}' likely already exists. Skipping.")
            papers_existed_count += 1
            continue

        # Find PDF URLs from multiple sources
        pdf_urls = find_pdf_url(doi, cleaned_title)
        
        if not pdf_urls:
            logging.warning(f"No PDF URL found for: {cleaned_title} (DOI: {doi}) from any source.")
            papers_pdf_url_missing_count += 1
            missing_papers_details.append({
                'id': entry.get('ID', 'N/A'),
                'title': cleaned_title,
                'doi': doi,
                'reason': 'No PDF URL found in any attempted source'
            })
            continue

        # Try downloading from each source until successful
        download_success = False
        for source_name, url in pdf_urls:
            safe_doi_filename_part = doi.replace('/', '_').replace('.', '-')
            final_filename = clean_title_for_filename(cleaned_title) + f"_DOI_{safe_doi_filename_part}.pdf"
            output_path = output_papers_dir / final_filename
            
            if download_pdf_from_url(url, output_path):
                papers_downloaded_count += 1
                download_success = True
                break
            else:
                logging.warning(f"Failed to download from {source_name}: {url}")
        
        if not download_success:
            papers_download_failed_count += 1
            missing_papers_details.append({
                'id': entry.get('ID', 'N/A'),
                'title': cleaned_title,
                'doi': doi,
                'reason': f'Failed to download PDF from all attempted sources',
                'attempted_urls': [url for _, url in pdf_urls]
            })
        
        time.sleep(1)  # Be nice to APIs
    
    # Write summary log
    summary_content = f"""Elicit Paper Download Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
==================================================
Processed BibTeX File: {bib_file_path.name}
Total BibTeX Entries: {total_entries}
--------------------------------------------------
Papers Successfully Downloaded: {papers_downloaded_count}
Papers Already Existed (Skipped): {papers_existed_count}
--------------------------------------------------
Failures & Missing Information:
  Entries Missing DOI & Not Found on arXiv: {papers_info_missing_count}
  Entries with DOI but No PDF URL Found: {papers_pdf_url_missing_count}
  PDF Download Failures (URL was found): {papers_download_failed_count}
==================================================
Log for missing paper details: {missing_papers_log_file.name}
Output directory for downloaded papers: {output_papers_dir}
"""
    
    with open(download_summary_log_file, 'w', encoding='utf-8') as f_summary:
        f_summary.write(summary_content)

    # Write missing papers log
    if missing_papers_details:
        with open(missing_papers_log_file, 'w', encoding='utf-8') as f_missing:
            f_missing.write(f"""Missing/Failed Papers Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total BibTeX Entries: {total_entries}
Successfully Downloaded: {papers_downloaded_count}
Already Existed: {papers_existed_count}
Total Missing/Failed: {len(missing_papers_details)}

""")
            
            for paper_detail in missing_papers_details:
                f_missing.write(f"""ID: {paper_detail.get('id', 'N/A')}
  Title: {paper_detail['title']}
  DOI: {paper_detail.get('doi', 'N/A')}
  Reason: {paper_detail['reason']}
""")
                if 'attempted_urls' in paper_detail:
                    f_missing.write("  Attempted URLs:\n")
                    for url in paper_detail['attempted_urls']:
                        f_missing.write(f"    - {url}\n")
                f_missing.write("-" * 40 + "\n")

if __name__ == "__main__":
    main() 
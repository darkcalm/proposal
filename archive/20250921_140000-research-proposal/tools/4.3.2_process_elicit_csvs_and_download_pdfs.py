#!/usr/bin/env python3

import csv
import logging
import re
import time
from pathlib import Path
from urllib.parse import urlparse, quote, unquote
import requests
import backoff # type: ignore
from tqdm import tqdm # type: ignore
import scholarly # type: ignore
import arxiv # type: ignore
import hashlib
import difflib
from typing import Optional, Dict, List, Tuple, Any, Set, Union

# --- Configuration ---\"
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ELICIT_RESULTS_BASE_DIR = WORKSPACE_ROOT / "sources" / "4.3.1-elicit-results"
PDF_OUTPUT_DIR = ELICIT_RESULTS_BASE_DIR / "downloaded_pdfs"
LOG_FILE_PATH = WORKSPACE_ROOT / "tools" / f"{Path(__file__).stem}.log"

# PDF download settings (from 4.1.7.2)
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
MIN_PDF_SIZE_BYTES = 10 * 1024  # 10 KB
GENERAL_CALLS_PER_SECOND = 2
GENERAL_CALLS_PER_MINUTE = 50
CROSSREF_CALLS_PER_SECOND = 10

S2_API_KEY = "0nUWTSm5ih4l1k5xXdVeL7YMYWjakdAy8F25ySsQ"

# --- Logging Setup ---\"
def setup_logging():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')

    file_handler = logging.FileHandler(LOG_FILE_PATH, mode='w') # Overwrite log each run
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

setup_logging()
logger = logging.getLogger(__name__)

# --- Helper Functions (Adapted from tools/4.1.7.2_optimized_pdf_downloader.py) ---

def get_file_hash(file_path: Path) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def clean_title_for_filename(title: str) -> str:
    if not title:
        return "unknown_title"
    title = str(title)
    title = title.replace('{', '').replace('}', '')
    title = re.sub(r'[\\/*?:;"<>|]', '_', title)
    title = title.replace(':', '-') # Replace colon with hyphen
    title = title.replace(' ', '_')
    # Remove any remaining characters that are not alphanumeric, underscore, or hyphen
    title = re.sub(r'[^a-zA-Z0-9_-]', '', title)
    title = re.sub(r'_+', '_', title) # Replace multiple underscores with single
    title = title.strip('_')
    return title[:180] # Max filename length is often around 255, keep some margin

def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s-]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_doi(doi: Optional[str]) -> Optional[str]:
    if not doi: return None
    doi = str(doi).lower()
    doi = doi.replace("https://doi.org/", "")
    doi = doi.replace("http://doi.org/", "")
    doi = doi.replace("doi:", "")
    return doi.strip()

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, jitter=backoff.full_jitter, factor=2)
def download_pdf(url: str, output_path: Path, source_name: str = "Unknown") -> bool:
    logger.info(f"[{source_name}] Attempting to download PDF from: {url} to {output_path.name}")
    try:
        headers = {'User-Agent': USER_AGENT, 'Accept': 'application/pdf,application/x-pdf,application/octet-stream,*/*'}
        
        # Use stream=True for efficient download of large files
        response = requests.get(url, stream=True, timeout=60, headers=headers, allow_redirects=True)
        response.raise_for_status()

        final_content_type = response.headers.get('Content-Type', '').lower()
        is_pdf_content_type = 'application/pdf' in final_content_type
        is_octet_stream = 'octet-stream' in final_content_type # Often used for PDFs too
        is_pdf_extension = url.lower().endswith('.pdf')

        if not (is_pdf_content_type or is_octet_stream or is_pdf_extension):
            if 'text/html' in final_content_type:
                logger.warning(f"[{source_name}] URL {url} returned HTML content. Skipping download.")
                return False
            logger.warning(f"[{source_name}] URL {url} has unusual Content-Type: {final_content_type}. Will proceed but validate.")

        total_size = int(response.headers.get('content-length', 0))
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'wb') as f, tqdm(
            desc=output_path.name[:50], total=total_size, unit='iB', unit_scale=True, unit_divisor=1024, disable=total_size==0 or total_size < MIN_PDF_SIZE_BYTES
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        downloaded_size = output_path.stat().st_size
        if downloaded_size < MIN_PDF_SIZE_BYTES:
            logger.warning(f"[{source_name}] Downloaded file {output_path.name} is too small ({downloaded_size}B). Deleting.")
            output_path.unlink(missing_ok=True)
            return False
            
        with open(output_path, 'rb') as f_check:
            header = f_check.read(4)
            if header != b'%PDF':
                f_check.seek(0)
                first_kb = f_check.read(1024).decode('utf-8', errors='ignore').lower()
                if '<html' in first_kb or '<!doctype html' in first_kb:
                    logger.error(f"[{source_name}] File {output_path.name} from {url} is HTML, not PDF. Deleting.")
                    output_path.unlink(missing_ok=True)
                    return False
                logger.warning(f"[{source_name}] File {output_path.name} from {url} lacks %PDF header. Kept with warning.")

        file_hash = get_file_hash(output_path)
        logger.info(f"[{source_name}] Successfully downloaded: {output_path.name} (Size: {downloaded_size}B, SHA-256: {file_hash[:8]})")
        time.sleep(0.5) # Brief pause
        return True
        
    except requests.exceptions.Timeout as e_timeout:
        logger.error(f"[{source_name}] Timeout for {url}: {e_timeout}")
    except requests.exceptions.HTTPError as e_http:
        logger.error(f"[{source_name}] HTTP error {e_http.response.status_code} for {url}: {e_http}")
    except requests.exceptions.RequestException as e_req:
        logger.error(f"[{source_name}] Request error for {url}: {e_req}")
    except Exception as e_gen:
        logger.error(f"[{source_name}] Unexpected error for {url}: {e_gen}")
    
    if output_path.exists():
        output_path.unlink(missing_ok=True)
    return False

# --- PDF Source Specific Functions (Adapted) ---

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_unpaywall(doi: str) -> Optional[str]:
    if not doi: return None
    normalized_doi = normalize_doi(doi)
    if not normalized_doi: return None
    try:
        url = f"https://api.unpaywall.org/v2/{normalized_doi}?email=test@example.com" # Replace with actual email if needed
        logger.debug(f"[Unpaywall] Querying for DOI: {normalized_doi}")
        response = requests.get(url, timeout=10, headers={'User-Agent': USER_AGENT})
        response.raise_for_status()
        data = response.json()
        if data.get('best_oa_location') and data['best_oa_location'].get('url_for_pdf'):
            pdf_url = data['best_oa_location']['url_for_pdf']
            logger.info(f"[Unpaywall] Found PDF URL: {pdf_url} for DOI: {doi}")
            return pdf_url
        # Check other locations if best_oa_location is not there or has no pdf url
        oa_locations = data.get('oa_locations', [])
        for loc in oa_locations:
            if loc.get('url_for_pdf'):
                pdf_url = loc['url_for_pdf']
                logger.info(f"[Unpaywall] Found PDF URL (alternative location): {pdf_url} for DOI: {doi}")
                return pdf_url
    except Exception as e:
        logger.warning(f"[Unpaywall] Error getting PDF for DOI {doi}: {e}")
    return None

@backoff.on_exception(backoff.expo, (requests.exceptions.RequestException, arxiv.ArxivError), max_tries=2)
def get_from_arxiv(title: Optional[str] = None, arxiv_id: Optional[str] = None) -> Optional[str]:
    query = arxiv_id if arxiv_id else (f'ti:"{title}"' if title else None)
    if not query: return None
    try:
        logger.debug(f"[arXiv] Searching for: {query}")
        search = arxiv.Search(query=query, max_results=1, sort_by=arxiv.SortCriterion.Relevance)
        client = arxiv.Client(page_size=1, delay_seconds=3.0, num_retries=3) # From arxiv lib docs
        results = list(client.results(search))
        if results and results[0].pdf_url:
            logger.info(f"[arXiv] Found PDF URL: {results[0].pdf_url} for query: {query}")
            return results[0].pdf_url
    except Exception as e:
        logger.warning(f"[arXiv] Error getting PDF for query '{query}': {e}")
    return None
    
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_core(doi: Optional[str] = None, title: Optional[str] = None) -> Optional[str]:
    if not doi and not title: return None
    try:
        if doi:
            query = f'doi:"{normalize_doi(doi)}"'
        elif title:
            query = f'title:"{quote(title)}"' # URL encode title
        else:
            return None
            
        search_url = f"https://core.ac.uk/api-v2/search/works?q={query}&apiKey=FeJVa6KG3ISf8iqN7sZw9RCHBgQPTxW2"
        
        logger.debug(f"[CORE] Querying for: {query} using API key.")
        
        response = requests.get(search_url, timeout=15, headers={'User-Agent': USER_AGENT})
        response.raise_for_status()
        data = response.json()
        
        # Check if 'results' is present and is a list
        results = data.get("data", []) # CORE API v2 uses "data" for results array
        if not isinstance(results, list):
             results = [] # ensure results is a list to prevent error if API returns unexpected type

        if results: # If there are any results
            # Iterate through results to find one with a downloadUrl
            for item in results:
                if isinstance(item, dict) and item.get("downloadUrl"):
                    pdf_url = item["downloadUrl"]
                    # Ensure it's actually a PDF link if possible, though CORE usually provides direct PDF links
                    if isinstance(pdf_url, str) and (pdf_url.lower().endswith('.pdf') or 'application/pdf' in response.headers.get('Content-Type', '').lower()):
                        logger.info(f"[CORE] Found PDF URL: {pdf_url} for query: {query}")
                        return pdf_url
                    else:
                        logger.debug(f"[CORE] Found downloadUrl, but it might not be a direct PDF: {pdf_url}")
            # If no direct PDF link was found in results with downloadUrl
            logger.debug(f"[CORE] Results found, but no direct PDF downloadUrl among them for query: {query}")
        else:
            logger.debug(f"[CORE] No results found for query: {query}")

    except requests.exceptions.HTTPError as e_http:
        if e_http.response.status_code == 401: # Unauthorized
            logger.error(f"[CORE] API Key is invalid or unauthorized for query '{query}'. Please check the key.")
        else:
            logger.warning(f"[CORE] HTTP Error {e_http.response.status_code} for query '{query}': {e_http}")
    except Exception as e:
        logger.warning(f"[CORE] Error getting PDF for query '{query}': {e}")
    return None


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_crossref(doi: str) -> Optional[str]:
    if not doi: return None
    normalized_doi = normalize_doi(doi)
    if not normalized_doi: return None
    try:
        url = f"https://api.crossref.org/works/{normalized_doi}"
        logger.debug(f"[Crossref] Querying for DOI: {normalized_doi}")
        response = requests.get(url, timeout=10, headers={'User-Agent': USER_AGENT})
        response.raise_for_status()
        data = response.json()
        if data.get('message') and data['message'].get('link'):
            for link_info in data['message']['link']:
                if link_info.get('content-type') == 'application/pdf' and link_info.get('URL'):
                    pdf_url = link_info['URL']
                    logger.info(f"[Crossref] Found PDF URL: {pdf_url} for DOI: {doi}")
                    return pdf_url
    except Exception as e:
        logger.warning(f"[Crossref] Error getting PDF for DOI {doi}: {e}")
    return None

@backoff.on_exception(backoff.expo, Exception, max_tries=2) # Catch broad exceptions from scholarly
def get_from_google_scholar(title: str, enable_scholar_search: bool = False) -> Optional[str]:
    if not title or not enable_scholar_search: return None
    try:
        logger.debug(f"[Google Scholar] Searching for title: {title}")
        # Configure scholarly to use a less aggressive approach or a specific user agent if needed
        # For now, default settings. Be mindful of Google's rate limits.
        pg = scholarly.scholarly.search_pubs(title)
        pub = next(pg, None)
        if pub and 'pub_url' in pub and pub['pub_url'].lower().endswith('.pdf'):
            logger.info(f"[Google Scholar] Found PDF URL: {pub['pub_url']} for title: {title}")
            return pub['pub_url']
        elif pub and 'eprint_url' in pub and pub['eprint_url'].lower().endswith('.pdf'): # Check eprint_url too
             logger.info(f"[Google Scholar] Found PDF URL (eprint): {pub['eprint_url']} for title: {title}")
             return pub['eprint_url']
    except StopIteration:
        logger.debug(f"[Google Scholar] No results for title: {title}")
    except Exception as e:
        logger.warning(f"[Google Scholar] Error searching for title '{title}': {e}")
    return None
    
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_semantic_scholar(doi: str, api_key: str) -> Optional[str]:
    if not doi or not api_key:
        return None
    normalized_doi = normalize_doi(doi)
    if not normalized_doi:
        return None
    
    headers = {
        "Accept": "application/json",
        "User-Agent": USER_AGENT # Use the globally defined USER_AGENT
    }
    if api_key:
        headers['x-api-key'] = api_key

    try:
        # S2 API prefers uppercase DOIs in some contexts, though it often works with lowercase too.
        # The normalize_doi function already lowercases it; S2 API should handle it.
        url = f"https://api.semanticscholar.org/graph/v1/paper/{quote(normalized_doi)}?fields=openAccessPdf,title"
        logger.debug(f"[SemanticScholar] Querying for DOI: {normalized_doi}")
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if data.get('openAccessPdf') and isinstance(data['openAccessPdf'], dict) and data['openAccessPdf'].get('url'):
            pdf_url = data['openAccessPdf']['url']
            logger.info(f"[SemanticScholar] Found PDF URL: {pdf_url} for DOI: {doi} (Title: {data.get('title')})")
            return pdf_url
        else:
            logger.debug(f"[SemanticScholar] No openAccessPdf found or URL missing for DOI: {doi} (Title: {data.get('title')})")
            
    except requests.exceptions.HTTPError as e_http:
        if e_http.response.status_code == 404:
            logger.debug(f"[SemanticScholar] Paper with DOI {doi} not found (404).")
        elif e_http.response.status_code == 403: # Forbidden, potentially API key issue
             logger.warning(f"[SemanticScholar] API request forbidden (403) for DOI {doi}. Check API key permissions or usage.")
        else:
            logger.warning(f"[SemanticScholar] HTTP error {e_http.response.status_code} for DOI {doi}: {e_http}")
    except Exception as e:
        logger.warning(f"[SemanticScholar] Error getting PDF for DOI {doi}: {e}")
    return None

# --- CSV Processing and Main Logic ---

POSSIBLE_TITLE_COLUMNS = ['title', 'Title', 'Paper Title', 'publication_title']
POSSIBLE_DOI_COLUMNS = ['doi', 'DOI']
POSSIBLE_PDF_URL_COLUMNS = [
    'pdf url', 'PDF', 'Full text links', 'Primary PDF link', 
    'Open Access Link', 'FullTextURL', 'pdfUrl', 'openAccessPdf'
]

def get_col_value(row: Dict, col_names: List[str], is_url_search: bool = False) -> Optional[str]:
    for col_candidate in col_names:
        if col_candidate in row and row[col_candidate]:
            value = row[col_candidate]

            if not isinstance(value, str): # All our target values (title, doi, url) should be strings from CSV.
                logger.debug(f"Value in column '{col_candidate}' is not a string: {value}. Skipping.")
                continue

            # If we are searching for a URL, and this column is 'Full text links'
            if is_url_search and col_candidate == 'Full text links':
                try:
                    # Elicit sometimes has a string representation of a list of dicts
                    links_list = eval(value) 
                    if isinstance(links_list, list):
                        for link_item in links_list:
                            if isinstance(link_item, dict) and link_item.get('type') == 'PDF' and link_item.get('url'):
                                return link_item['url'] # Return first valid PDF URL
                    # If no PDF URL found after eval, this candidate ('Full text links') is exhausted for eval path.
                    # Do not proceed to treat `value` as a simple URL string below for this specific column.
                    continue # Move to the next col_candidate in col_names
                except Exception as e: # eval can be risky, catch errors
                    logger.debug(f"Could not eval 'Full text links' content '{value}': {e}. This column will not be treated as a simple URL string if eval fails.")
                    continue # Treat this candidate as exhausted if eval fails
            
            # General case for all columns (title, doi, or other url columns)
            if is_url_search:
                # If we expect a URL, it must look like one.
                if value.lower().startswith('http') or value.lower().startswith('www.'):
                    return value
                else:
                    # This string from a URL column candidate doesn't look like a URL.
                    logger.debug(f"Column '{col_candidate}' was expected to yield a URL, but value '{value}' is not a URL. Skipping this value.")
                    continue # to the next col_candidate
            else:
                # If we are not specifically searching for a URL (e.g., for title or DOI),
                # then any non-empty string is acceptable.
                return value
    return None


def load_papers_from_csvs(input_base_dir: Path) -> List[Dict[str, Any]]:
    all_papers: List[Dict[str, Any]] = []
    csv_files_found = 0
    logger.info(f"Scanning for CSV files in subdirectories of: {input_base_dir}")

    for subdir in input_base_dir.iterdir():
        if subdir.is_dir() and not subdir.name.startswith(('.', '_')) and subdir.name != PDF_OUTPUT_DIR.name:
            logger.info(f"Processing directory: {subdir.name}")
            for csv_file in subdir.glob("*.csv"):
                csv_files_found += 1
                logger.info(f"  Reading CSV: {csv_file.name}")
                try:
                    with open(csv_file, 'r', encoding='utf-8-sig') as f: # utf-8-sig for BOM
                        reader = csv.DictReader(f)
                        for row_num, row in enumerate(reader):
                            title = get_col_value(row, POSSIBLE_TITLE_COLUMNS, is_url_search=False)
                            if not title:
                                logger.warning(f"    Skipping row {row_num+1} in {csv_file.name} (line {reader.line_num}) due to missing or invalid title.")
                                continue
                            
                            paper_info = {
                                'title': title,
                                'doi': get_col_value(row, POSSIBLE_DOI_COLUMNS, is_url_search=False),
                                'direct_pdf_url': get_col_value(row, POSSIBLE_PDF_URL_COLUMNS, is_url_search=True),
                                'source_csv': csv_file.name,
                                'original_row': dict(row) # Keep original for reference if needed
                            }
                            all_papers.append(paper_info)
                except Exception as e:
                    logger.error(f"  Error reading CSV file {csv_file.name}: {e}")
    
    logger.info(f"Found {csv_files_found} CSV files in total.")
    return all_papers

def deduplicate_papers(papers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    unique_papers_dict: Dict[str, Dict[str, Any]] = {}
    duplicates_found = 0
    for paper in papers:
        normalized_title = normalize_text(paper['title'])
        if not normalized_title: # Should not happen if title check is done in load_papers
            continue

        if normalized_title not in unique_papers_dict:
            unique_papers_dict[normalized_title] = paper
        else:
            duplicates_found += 1
            # Prioritization: prefer entry with DOI, then direct_pdf_url
            current_entry = unique_papers_dict[normalized_title]
            if not current_entry.get('doi') and paper.get('doi'):
                unique_papers_dict[normalized_title] = paper
            elif not current_entry.get('direct_pdf_url') and paper.get('direct_pdf_url') and not paper.get('doi'):
                 unique_papers_dict[normalized_title] = paper
    
    logger.info(f"Removed {duplicates_found} duplicate entries based on title.")
    return list(unique_papers_dict.values())

def find_existing_pdf_by_title(title: str, output_dir: Path) -> Optional[Path]:
    """Checks if a PDF with a similar title already exists."""
    if not title: return None
    normalized_query_title = normalize_text(title)
    
    for existing_pdf in output_dir.glob('*.pdf'):
        # Extract title from filename (remove .pdf extension)
        filename_title_part = existing_pdf.stem 
        normalized_existing_title = normalize_text(filename_title_part.replace('_',' ')) # Convert underscores back to spaces for comparison
        
        similarity = difflib.SequenceMatcher(None, normalized_query_title, normalized_existing_title).ratio()
        if similarity > 0.95: # High similarity threshold
            logger.info(f"Found existing PDF by title similarity ({similarity:.2f}): {existing_pdf.name} for query title: {title}")
            return existing_pdf
    return None


def main():
    # Create output directory if it doesn't exist
    PDF_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Load and deduplicate papers
    papers = load_papers_from_csvs(ELICIT_RESULTS_BASE_DIR)
    unique_papers = deduplicate_papers(papers)
    logger.info(f"Found {len(unique_papers)} unique papers after deduplication")
    
    # Track papers that need URLs
    papers_without_urls = []
    
    # Process each paper
    for paper in unique_papers:
        title = paper.get('title')
        if not title:
            continue
            
        # Check if PDF already exists
        existing_pdf = find_existing_pdf_by_title(title, PDF_OUTPUT_DIR)
        if existing_pdf:
            logger.info(f"PDF already exists for: {title}")
            continue
            
        # Get direct PDF URL if available
        pdf_url = paper.get('direct_pdf_url')
        
        if not pdf_url:
            papers_without_urls.append({
                'title': title,
                'doi': paper.get('doi'),
                'source_csv': paper.get('source_csv')
            })
    
    # Save papers that need URLs to a CSV
    if papers_without_urls:
        not_found_csv_path = ELICIT_RESULTS_BASE_DIR / "papers_needing_urls.csv"
        with open(not_found_csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'doi', 'source_csv'])
            writer.writeheader()
            writer.writerows(papers_without_urls)
        logger.info(f"Saved {len(papers_without_urls)} papers that need URLs to: {not_found_csv_path}")
        print(f"\nPapers that need URLs have been saved to: {not_found_csv_path}")
        print(f"Absolute path: {not_found_csv_path.absolute()}")
        print(f"File URL: file://{not_found_csv_path.absolute()}")
    
    logger.info("CSV processing completed")

if __name__ == "__main__":
    main() 
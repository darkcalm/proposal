#!/usr/bin/env python3

import requests
import os
import re
import time
from urllib.parse import urlparse, quote, unquote
from pathlib import Path
import arxiv # type: ignore
import difflib
import logging
import backoff # type: ignore
from tqdm import tqdm # type: ignore
from bs4 import BeautifulSoup # type: ignore
import scholarly # type: ignore
import json
from datetime import datetime
import concurrent.futures
from ratelimit import limits, sleep_and_retry # type: ignore
import hashlib
from typing import Optional, Dict, List, Tuple, Any, Set
import argparse

# --- Global Configuration & Constants ---

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PDF_DIR = WORKSPACE_ROOT / "sources" / "4.1.7-semantic-scholar-dynamic-results" # Changed output path
DOCS_DIR = WORKSPACE_ROOT / "docs"
LOG_FILE_PATH = Path(__file__).resolve().parent / f"{Path(__file__).stem}.log"

# Rate limiting constants (can be adjusted)
# General API calls
GENERAL_CALLS_PER_SECOND = 2
GENERAL_CALLS_PER_MINUTE = 50 # Increased from 30, to align with S2 dynamic search potential output

# Crossref specific (more generous free tier)
CROSSREF_CALLS_PER_SECOND = 10 # Check actual limits if issues arise

# User Agent for requests
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

# Minimum PDF size to consider valid (in bytes)
MIN_PDF_SIZE_BYTES = 10 * 1024 # 10 KB

# --- Logging Setup ---
def setup_logging():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s')
    
    # File handler for the script's log
    file_handler = logging.FileHandler(LOG_FILE_PATH)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

setup_logging() # Initialize logging

# --- Helper Functions (Hashing, Filename Cleaning, Normalization) ---

def get_file_hash(file_path: Path) -> str:
    """Calculate SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def clean_title_for_filename(title: str) -> str:
    """Clean title to be suitable for a filename."""
    if not title:
        return "unknown_title"
    title = title.replace('{', '').replace('}', '')
    title = re.sub(r'[\\/*?:;"<>|]', '_', title)
    title = title.replace(' ', '_')
    title = title.replace(':', '_')
    return title[:150]

def normalize_text(text: str) -> str:
    """Normalize text for comparison: lowercase, remove special chars (keep hyphens, alphanumeric)."""
    if not text:
        return ""
    text = str(text).lower()
    text = re.sub(r'[^a-z0-9\s-]', ' ', text) # Keep alphanumeric, spaces, hyphens
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def normalize_doi(doi: str) -> str | None:
    """Normalize a DOI string."""
    if not doi: return None
    # Remove common prefixes and convert to lowercase
    doi = doi.lower()
    doi = doi.replace("https://doi.org/", "")
    doi = doi.replace("http://doi.org/", "")
    doi = doi.replace("doi:", "")
    return doi.strip()


def find_existing_paper(title: str | None, doi: str | None, output_dir: Path) -> Path | None:
    """Check if a paper with a similar title or matching DOI already exists."""
    if not title and not doi:
        return None

    normalized_query_title = normalize_text(title) if title else ""
    normalized_query_doi = normalize_doi(doi) if doi else ""

    for existing_pdf in output_dir.glob('*.pdf'):
        filename_stem = existing_pdf.stem
        
        # Try to extract DOI from filename (e.g., title_DOI_xxxx.pdf or DOI_xxxx.pdf)
        # Updated regex to be more flexible
        doi_in_filename_match = re.search(r'(?:_DOI_|DOI_)([^_.]+(?:/[^_. ]+)?)(?:_|\.)?$', filename_stem, re.IGNORECASE)
        if doi_in_filename_match:
            normalized_existing_doi = normalize_doi(unquote(doi_in_filename_match.group(1)))
            if normalized_query_doi and normalized_query_doi == normalized_existing_doi:
                logging.info(f"Found existing paper by DOI in filename: {existing_pdf.name} (Query DOI: {normalized_query_doi})")
                return existing_pdf
        
        if title: 
            # Extract title part from filename more robustly
            title_part_in_filename = filename_stem
            if doi_in_filename_match: # If DOI was in filename, remove it to get title part
                 title_part_in_filename = filename_stem[:doi_in_filename_match.start()]
            title_part_in_filename = title_part_in_filename.replace('_', ' ')
            normalized_existing_title = normalize_text(title_part_in_filename)
            
            if normalized_query_title and normalized_existing_title:
                similarity = difflib.SequenceMatcher(None, normalized_query_title, normalized_existing_title).ratio()
                if similarity > 0.9: 
                    logging.info(f"Found existing paper by title similarity ({similarity:.2f}): {existing_pdf.name} (Query Title: {normalized_query_title})")
                    return existing_pdf
    return None

# --- PDF Download and Validation ---
@sleep_and_retry
@limits(calls=GENERAL_CALLS_PER_SECOND, period=1) # General rate limit for downloads
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, jitter=backoff.full_jitter)
def download_pdf(url: str, output_path: Path, pbar_desc: str | None = None, source_name: str = "Unknown") -> bool:
    """Download PDF from URL with retry, rate limiting, progress, and validation."""
    try:
        desc = pbar_desc or output_path.name
        logging.info(f"[{source_name}] Attempting to download PDF from: {url} to {output_path.name}")
        
        headers = {'User-Agent': USER_AGENT, 'Accept': 'application/pdf,application/x-pdf,application/octet-stream,*/*'}
        
        head_response = requests.head(url, timeout=15, headers=headers, allow_redirects=True)
        content_type = head_response.headers.get('Content-Type', '').lower()
        content_length = int(head_response.headers.get('Content-Length', 0))

        if head_response.status_code >= 400:
            logging.warning(f"[{source_name}] HTTP error {head_response.status_code} during HEAD request for {url}")
            return False
            
        is_pdf_content_type = 'application/pdf' in content_type or 'octet-stream' in content_type
        is_pdf_extension = url.lower().endswith('.pdf')
        is_likely_pdf = is_pdf_content_type or is_pdf_extension

        if not is_likely_pdf:
            if 'text/html' in content_type:
                logging.warning(f"[{source_name}] URL {url} returned HTML content (HEAD). Skipping download.")
                # TODO: Optionally, could attempt to scrape this HTML page for a PDF link here
                return False
            logging.warning(f"[{source_name}] URL {url} has unusual Content-Type: {content_type} and no .pdf extension. Will attempt download cautiously.")

        # If Content-Length is very small (and from HEAD), it might not be the full PDF
        if content_length > 0 and content_length < MIN_PDF_SIZE_BYTES // 2 and is_pdf_content_type:
            logging.warning(f"[{source_name}] URL {url} has very small Content-Length ({content_length}B) from HEAD. May not be full PDF.")

        response = requests.get(url, stream=True, timeout=90, headers=headers, allow_redirects=True) # Increased timeout for GET
        response.raise_for_status()
        
        # Re-check content type from GET response as HEAD might differ or be unavailable
        final_content_type = response.headers.get('Content-Type', '').lower()
        if not ('application/pdf' in final_content_type or 'octet-stream' in final_content_type) and not url.lower().endswith('.pdf'):
            if 'text/html' in final_content_type:
                logging.warning(f"[{source_name}] URL {url} returned HTML content (GET). Skipping download.")
                # Try to save the HTML for inspection if it's small
                if int(response.headers.get('content-length', 0)) < 1024*50: # < 50KB
                    try:
                        html_output_path = output_path.with_suffix('.html.txt')
                        with open(html_output_path, 'wb') as f_html:
                            f_html.write(response.content)
                        logging.info(f"[{source_name}] Saved HTML content from {url} to {html_output_path.name}")
                    except Exception as e_html:
                        logging.error(f"[{source_name}] Failed to save HTML content: {e_html}")
                return False
            logging.warning(f"[{source_name}] URL {url} (GET) has unusual Content-Type: {final_content_type}. Proceeding.")

        total_size = int(response.headers.get('content-length', 0))
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'wb') as f, tqdm(
            desc=desc, total=total_size, unit='iB', unit_scale=True, unit_divisor=1024, disable=total_size==0
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        downloaded_size = output_path.stat().st_size
        if downloaded_size < MIN_PDF_SIZE_BYTES:
            logging.warning(f"[{source_name}] Downloaded file {output_path.name} is very small ({downloaded_size}B). Deleting.")
            output_path.unlink(missing_ok=True)
            return False
            
        with open(output_path, 'rb') as f_check:
            header = f_check.read(4)
            if header != b'%PDF':
                f_check.seek(0)
                first_kb = f_check.read(1024).decode('utf-8', errors='ignore').lower()
                if '<html' in first_kb or '<!doctype html' in first_kb:
                    logging.error(f"[{source_name}] File {output_path.name} from {url} appears to be HTML, not PDF. Deleting.")
                    output_path.unlink(missing_ok=True)
                    return False
                logging.warning(f"[{source_name}] File {output_path.name} from {url} does not have %PDF header. Keeping with warning.")

        file_hash = get_file_hash(output_path)
        logging.info(f"[{source_name}] Successfully downloaded: {output_path.name} (Size: {downloaded_size}B, SHA-256: {file_hash})")
        return True
        
    except requests.exceptions.Timeout as e_timeout:
        logging.error(f"[{source_name}] Timeout downloading PDF from {url}: {e_timeout}")
    except requests.exceptions.HTTPError as e_http:
        logging.error(f"[{source_name}] HTTP error {e_http.response.status_code} downloading PDF from {url}: {e_http}")
    except requests.exceptions.RequestException as e_req:
        logging.error(f"[{source_name}] Request error downloading PDF from {url}: {e_req}")
    except Exception as e_gen:
        logging.error(f"[{source_name}] An unexpected error occurred during download from {url}: {e_gen}")
    
    if output_path.exists(): # If download failed but file was created, remove it
        output_path.unlink(missing_ok=True)
    return False

# --- PDF Source Specific Functions ---

@sleep_and_retry
@limits(calls=GENERAL_CALLS_PER_MINUTE, period=60) # Unpaywall is generally okay with this rate
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_unpaywall(doi: str) -> Optional[str]:
    """Get PDF URL from Unpaywall using DOI."""
    if not doi: return None
    normalized_doi = normalize_doi(doi)
    if not normalized_doi: return None
    try:
        email = os.getenv("UNPAYWALL_EMAIL", "tech@example.com") # Use a placeholder or your actual email
        url = f"https://api.unpaywall.org/v2/{quote(normalized_doi)}?email={email}"
        logging.info(f"[Unpaywall] Querying for DOI: {normalized_doi}")
        response = requests.get(url, timeout=20, headers={'User-Agent': USER_AGENT})
        response.raise_for_status()
        data = response.json()
        
        best_loc = data.get('best_oa_location')
        if best_loc and best_loc.get('url_for_pdf'):
            pdf_url = best_loc['url_for_pdf']
            logging.info(f"[Unpaywall] Found PDF for {normalized_doi} at: {pdf_url} (Best OA)")
            return pdf_url
        
        if data.get('oa_locations'):
            for loc in data['oa_locations']:
                if loc.get('url_for_pdf'):
                    pdf_url = loc['url_for_pdf']
                    logging.info(f"[Unpaywall] Found PDF (alternative OA) for {normalized_doi} at: {pdf_url}")
                    return pdf_url
        logging.info(f"[Unpaywall] No direct PDF URL found for DOI: {normalized_doi}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.info(f"[Unpaywall] DOI {normalized_doi} not found.")
        else:
            logging.warning(f"[Unpaywall] HTTP error for DOI {normalized_doi}: {e}")
    except Exception as e:
        logging.error(f"[Unpaywall] Error for DOI {normalized_doi}: {e}")
    return None

@sleep_and_retry
@limits(calls=GENERAL_CALLS_PER_MINUTE, period=60) # arXiv is generally okay with this rate
@backoff.on_exception(backoff.expo, (requests.exceptions.RequestException, arxiv.ArxivError), max_tries=2)
def get_from_arxiv(title: Optional[str] = None, arxiv_id: Optional[str] = None) -> Optional[str]:
    """Search arXiv by title or arXiv ID."""
    if not title and not arxiv_id:
        logging.warning("[arXiv] Title and arXiv ID are both missing.")
        return None

    search_query = ""
    search_type = ""

    if arxiv_id:
        # Normalize arxiv_id (e.g., remove "arXiv:", "v1")
        arxiv_id_match = re.search(r'(\d{4}\.\d{4,5}(v\d+)?)', arxiv_id)
        if arxiv_id_match:
            arxiv_id = arxiv_id_match.group(1)
            search_query = arxiv_id
            search_type = "ID"
            logging.info(f"[arXiv] Searching by ID: {arxiv_id}")
        else:
            logging.warning(f"[arXiv] Could not parse arXiv ID: {arxiv_id}. Will try title if available.")
            if not title: return None # If ID was bad and no title, exit
            # Fall through to title search if ID parsing failed but title exists
    
    if not search_query and title: # If ID search didn't happen or wasn't provided, use title
        search_query = f'ti:"{title}"' # arXiv specific title search format
        search_type = "title"
        logging.info(f"[arXiv] Searching by title: {title[:100]}...")
    
    if not search_query: return None

    try:
        search = arxiv.Search(
            query=search_query,
            max_results=1,
            sort_by=arxiv.SortCriterion.Relevance
        )
        results = list(search.results()) # Convert generator to list
        if results:
            paper = results[0]
            if paper.pdf_url:
                logging.info(f"[arXiv] Found PDF for {search_type} '{search_query}' at: {paper.pdf_url}")
                return paper.pdf_url
            else:
                logging.warning(f"[arXiv] Found paper for {search_type} '{search_query}' but no PDF URL (Title: {paper.title}).")
        else:
            logging.info(f"[arXiv] No results found for {search_type}: '{search_query}'")            
    except Exception as e:
        logging.error(f"[arXiv] Error searching for {search_type} '{search_query}': {e}")
    return None

@sleep_and_retry
@limits(calls=GENERAL_CALLS_PER_MINUTE, period=60) # CORE API rate limits
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_core(doi: Optional[str] = None, title: Optional[str] = None) -> Optional[str]:
    """Search CORE API v3 by DOI (preferred) or title."""
    api_key = os.getenv('CORE_API_KEY')
    if not api_key:
        logging.warning("[CORE] CORE_API_KEY not set. Skipping CORE search.")
        return None
    
    headers = {"Authorization": f"Bearer {api_key}", 'User-Agent': USER_AGENT}
    core_v3_base = "https://api.core.ac.uk/v3"
    
    query_params = []
    search_log_str = ""

    if doi:
        normalized_doi = normalize_doi(doi)
        if normalized_doi:
            # Try direct PDF link endpoint first
            try:
                pdf_link_url = f"{core_v3_base}/get-pdf-link?doi={quote(normalized_doi)}"
                logging.info(f"[CORE] Attempting direct PDF link for DOI: {normalized_doi}")
                response = requests.get(pdf_link_url, headers=headers, timeout=15, allow_redirects=False) # Don't follow redirect here
                if response.status_code == 200 and 'application/pdf' in response.headers.get('Content-Type','').lower():
                    logging.info(f"[CORE] Found direct PDF URL (200 OK) for DOI {normalized_doi}: {response.url}") # response.url has the final redirect if any
                    return response.url # This might be the PDF itself or a redirect to it
                elif response.status_code == 302: # Found, redirecting to PDF
                    redirect_url = response.headers.get('Location')
                    if redirect_url and redirect_url.lower().endswith('.pdf'):
                        logging.info(f"[CORE] Found direct PDF URL (302 redirect) for DOI {normalized_doi}: {redirect_url}")
                        return redirect_url
                    else:
                        logging.info(f"[CORE] Direct PDF link for DOI {normalized_doi} gave 302 but not to PDF: {redirect_url}")
                elif response.status_code == 404:
                    logging.info(f"[CORE] Direct PDF link for DOI {normalized_doi} not found (404). Will try search.")
                else:
                    logging.warning(f"[CORE] Direct PDF link for DOI {normalized_doi} returned {response.status_code}. Content: {response.text[:200]}")
            except Exception as e_direct:
                logging.error(f"[CORE] Error getting direct PDF link for DOI {normalized_doi}: {e_direct}")
            
            query_params.append(f'doi:"{normalized_doi}"')
            search_log_str = f"DOI: {normalized_doi}"

    if not query_params and title: # Fallback to title if DOI search not done or failed to form query
        # Sanitize title for query: escape special Lucene characters like :, ", etc.
        sanitized_title = re.sub(r'([+\-!(){}\[\]^"~*?:\\])', r'\\\1', title)
        query_params.append(f'title:("{sanitized_title}")') # Exact phrase for title
        search_log_str = f"Title: {title[:100]}..."
    
    if not query_params:
        logging.warning("[CORE] No DOI or Title provided for search.")
        return None

    search_url = f"{core_v3_base}/search/works"
    # Construct query string: join multiple conditions with AND if needed in future
    full_query_string = " AND ".join(query_params)
    
    payload = {"q": full_query_string, "limit": 1} # Get top 1 result

    try:
        logging.info(f"[CORE] Searching works with: {search_log_str}")
        response = requests.post(search_url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()

        if data.get("results"):
            work = data["results"][0]
            # Check for downloadUrl first, then other potential PDF links
            if work.get("downloadUrl") and work["downloadUrl"].lower().endswith(".pdf"):
                logging.info(f"[CORE] Found downloadUrl for '{search_log_str}': {work['downloadUrl']}")
                return work["downloadUrl"]
            
            # Check other locations if available (e.g., from fulltextUrls or similar fields in CORE v3)
            # This part would need specific knowledge of CORE v3 response structure for PDFs beyond downloadUrl
            pdf_urls = work.get("pdfUrls", []) # Hypothetical field, adjust to actual CORE v3 response
            if isinstance(pdf_urls, list) and pdf_urls:
                 logging.info(f"[CORE] Found pdfUrls for '{search_log_str}': {pdf_urls[0]}")
                 return pdf_urls[0]
            
            # Check OAI link if it leads to a PDF (less common for direct PDF)
            oai_link = work.get('oaiPmhUrl') # Example, check actual field
            if oai_link and "pdf" in oai_link.lower(): # very heuristic
                logging.info(f"[CORE] Found potential PDF in OAI link for '{search_log_str}': {oai_link}")
                return oai_link

            logging.info(f"[CORE] Found work for '{search_log_str}' (Title: {work.get('title')}) but no direct PDF URL in expected fields.")
        else:
            logging.info(f"[CORE] No results found for '{search_log_str}'. Response: {data}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.info(f"[CORE] Search for '{search_log_str}' not found (404).")
        else:
             logging.warning(f"[CORE] HTTP error searching for '{search_log_str}': {e.response.status_code} - {e.response.text[:200]}")
    except Exception as e:
        logging.error(f"[CORE] Error searching for '{search_log_str}': {e}")
    return None

@sleep_and_retry
@limits(calls=CROSSREF_CALLS_PER_SECOND, period=1) # Crossref is more permissive
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_from_crossref(doi: str) -> Optional[str]:
    """Query Crossref API for a DOI to find potential PDF links."""
    if not doi: return None
    normalized_doi = normalize_doi(doi)
    if not normalized_doi: return None
    
    try:
        url = f"https://api.crossref.org/works/{quote(normalized_doi)}"
        logging.info(f"[Crossref] Querying for DOI: {normalized_doi}")
        # Add mailto for polite pool as per Crossref docs
        # Get from env var or use a generic one
        mailto = os.getenv("CROSSREF_MAILTO", "tech@example.com")
        headers = {'User-Agent': f'{USER_AGENT} (mailto:{mailto})'}

        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        data = response.json()
        
        if data.get("message") and data["message"].get("link"):
            for link_info in data["message"]["link"]:
                link_url = link_info.get("URL")
                content_type = link_info.get("content-type", "").lower()
                intended_application = link_info.get("intended-application", "").lower()

                if link_url and (
                    content_type == "application/pdf" or 
                    intended_application == "text-mining" or # Often PDFs
                    intended_application == "similarity-checking" or # Often PDFs
                    link_url.lower().endswith(".pdf")
                ):
                    logging.info(f"[Crossref] Found potential PDF link for {normalized_doi} via 'link' field: {link_url}")
                    return link_url
        
        # Check resource.primary.URL as a fallback (less common for direct PDF but worth checking)
        if data.get("message") and data["message"].get("resource", {}).get("primary", {}).get("URL"):
            primary_url = data["message"]["resource"]["primary"]["URL"]
            if primary_url.lower().endswith(".pdf"):
                 logging.info(f"[Crossref] Found potential PDF link for {normalized_doi} via 'resource.primary.URL': {primary_url}")
                 return primary_url
            # Sometimes the primary URL is a landing page that might contain the PDF
            # We could try fetching this primary_url and looking for PDF links inside it, but that's more complex scraping.
            # For now, only return if it directly ends with .pdf.

        logging.info(f"[Crossref] No direct PDF link found in Crossref metadata for DOI: {normalized_doi}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.info(f"[Crossref] DOI {normalized_doi} not found.")
        else:
            logging.warning(f"[Crossref] HTTP error for DOI {normalized_doi}: {e}")
    except Exception as e:
        logging.error(f"[Crossref] Error for DOI {normalized_doi}: {e}")
    return None

# --- Scholarly (Google Scholar) - Optional, use with caution ---
# This section is kept separate as it's web scraping and can be unstable.
@sleep_and_retry
@limits(calls=5, period=60) # Be very conservative with Google Scholar
@backoff.on_exception(backoff.expo, Exception, max_tries=2) # Catch broad exceptions from scholarly
def get_from_google_scholar(title: str, enable_scholar: bool = False) -> Optional[str]:
    """Search Google Scholar using the `scholarly` library if enabled."""
    if not enable_scholar or not title:
        return None
    logging.info(f"[GoogleScholar] Searching for title: {title[:100]}...")
    try:
        # Configure scholarly to be less aggressive if possible (refer to its docs for proxy/UA settings)
        # scholarly.use_proxy(http_proxy, https_proxy) # Example
        search_query = scholarly.search_pubs(title)
        pub = next(search_query, None)
        if pub and pub.get('eprint_url'): # 'eprint_url' often leads to PDF
            pdf_url = pub['eprint_url']
            if pdf_url.lower().endswith('.pdf'): # Check if it directly points to a PDF
                logging.info(f"[GoogleScholar] Found eprint_url (PDF): {pdf_url} for title '{title[:50]}...'")
                return pdf_url
            else: # If not ending with .pdf, try to see if it's a known domain that hosts PDFs
                # This is heuristic. A better way is to fetch and check content-type.
                if any(domain in pdf_url for domain in ["arxiv.org", "openreview.net", "acm.org/doi/pdf", "ieee.org/document"]):
                    logging.info(f"[GoogleScholar] Found eprint_url (likely PDF page): {pdf_url} for title '{title[:50]}...'")
                    return pdf_url # Return even if not ending with .pdf if it's a known good source page
        elif pub and pub.get('pub_url'): # 'pub_url' is the publisher link, less likely to be direct PDF
            logging.info(f"[GoogleScholar] Found pub_url: {pub['pub_url']} for title '{title[:50]}...' (less likely direct PDF).")
            # Could try to download and check if it's a PDF, but risky for a general pub_url.
            if pub['pub_url'].lower().endswith('.pdf'):
                 return pub['pub_url']

        logging.info(f"[GoogleScholar] No direct PDF link found for title: {title[:100]}...")
    except StopIteration:
        logging.info(f"[GoogleScholar] No results found for title: {title[:100]}...")
    except Exception as e:
        logging.error(f"[GoogleScholar] Error searching for title '{title[:100]}...': {e}")
    return None

# --- Master PDF URL Finder ---
def find_pdf_main(paper_s2_data: Dict[str, Any], enable_google_scholar: bool = False) -> Tuple[Optional[str], str]:
    """
    Tries to find a PDF URL for a paper using various sources.
    Returns a tuple: (pdf_url, source_name_if_found)
    """
    title = paper_s2_data.get("title")
    doi = paper_s2_data.get("externalIds", {}).get("DOI")
    arxiv_id_s2 = paper_s2_data.get("externalIds", {}).get("ArXiv") # S2 often provides this as "ArXiv:xxxx.xxxx"
    
    # 0. Try direct S2 openAccessPdf link first
    s2_oa_pdf_info = paper_s2_data.get("openAccessPdf")
    if isinstance(s2_oa_pdf_info, dict) and s2_oa_pdf_info.get("url"):
        logging.info(f"Source: S2 openAccessPdf. URL: {s2_oa_pdf_info['url']}")
        return s2_oa_pdf_info["url"], "Semantic Scholar openAccessPdf"

    # 1. If DOI is available, prioritize DOI-based searches
    if doi:
        normalized_doi = normalize_doi(doi)
        if normalized_doi:
            # 1a. Unpaywall (DOI)
            pdf_url = get_from_unpaywall(normalized_doi)
            if pdf_url: return pdf_url, "Unpaywall"

            # 1b. CORE API v3 (DOI)
            pdf_url = get_from_core(doi=normalized_doi, title=title) # CORE can use title as fallback too
            if pdf_url: return pdf_url, "CORE API"

            # 1c. Crossref (DOI)
            pdf_url = get_from_crossref(normalized_doi)
            if pdf_url: return pdf_url, "Crossref"
            
            # 1d. Try to get arXiv ID from DOI (if DOI is an arXiv DOI like 10.48550/arXiv.xxxx.xxxxx)
            # and then search arXiv by ID.
            if not arxiv_id_s2: # Only if S2 didn't already provide it
                arxiv_doi_match = re.match(r"10\.48550/arxiv\.(.+)", normalized_doi, re.IGNORECASE)
                if arxiv_doi_match:
                    derived_arxiv_id = arxiv_doi_match.group(1)
                    logging.info(f"Derived arXiv ID {derived_arxiv_id} from DOI {normalized_doi}")
                    pdf_url = get_from_arxiv(arxiv_id=derived_arxiv_id)
                    if pdf_url: return pdf_url, "arXiv (from DOI)"
    
    # 2. If arXiv ID is available (either from S2 or derived from DOI and failed above)
    if arxiv_id_s2: # Prefer S2 provided ArXiv ID
        pdf_url = get_from_arxiv(arxiv_id=arxiv_id_s2)
        if pdf_url: return pdf_url, "arXiv (from S2 externalId)"

    # 3. Fallback to title-based searches if no DOI or DOI searches failed
    if title:
        # 3a. arXiv (Title) - run if not already found via ID
        pdf_url = get_from_arxiv(title=title)
        if pdf_url: return pdf_url, "arXiv (Title)"
        
        # 3b. CORE API (Title) - run if not already found via DOI
        # (get_from_core can take title, so this might be redundant if DOI was present but yielded no CORE result)
        # To avoid re-running if DOI was present, we ensure DOI search happened first or DOI is None.
        if not doi: # Only run CORE by title if DOI was not available for a CORE DOI search
            pdf_url = get_from_core(title=title)
            if pdf_url: return pdf_url, "CORE API (Title)"

        # 3c. Google Scholar (Title) - Optional
        if enable_google_scholar:
            pdf_url = get_from_google_scholar(title, enable_google_scholar=True)
            if pdf_url: return pdf_url, "Google Scholar"
            
    # 4. If S2 URL field exists and looks like a PDF (final fallback)
    s2_url = paper_s2_data.get("url")
    if s2_url and (s2_url.lower().endswith(".pdf") or "arxiv.org/pdf" in s2_url.lower()):
        logging.info(f"Fallback: Trying S2 paper URL: {s2_url}")
        return s2_url, "Semantic Scholar paper.url"
        
    return None, "No Source Found"

# --- Main Processing Logic ---
def load_input_json_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """Loads the input JSON file containing scored papers from the dynamic search."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logging.info(f"Successfully loaded input data from {file_path}")
        # Expecting format: {"metadata": ..., "papers": [{"original_data": ..., "relevance_score": ...}, ...]}
        if "papers" in data and isinstance(data["papers"], list):
            return data
        else:
            logging.error(f"Input JSON {file_path} is not in the expected format (missing 'papers' list).")
            return None
    except FileNotFoundError:
        logging.error(f"Input JSON file not found: {file_path}")
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from input file: {file_path}")
    except Exception as e:
        logging.error(f"An unexpected error occurred loading input file {file_path}: {e}")
    return None

def process_single_paper(
    paper_wrapper_entry: Dict[str, Any], 
    output_dir: Path, 
    min_relevance_for_download: float,
    enable_gscholar: bool,
    processed_dois: Set[str], # To track DOIs processed in this run
    processed_titles: Set[str] # To track titles processed in this run
) -> Dict[str, Any]:
    """Processes a single paper entry: checks relevance, finds PDF, downloads."""
    
    # paper_wrapper_entry is like: {"original_data": s2_paper_dict, "relevance_score": float, ...}
    s2_paper_data = paper_wrapper_entry.get("original_data")
    if not isinstance(s2_paper_data, dict):
        logging.warning(f"Skipping entry due to missing or invalid 'original_data'. Entry: {str(paper_wrapper_entry)[:200]}")
        return {'status': 'error_bad_input_data'}

    title = s2_paper_data.get("title", "Unknown Title")
    paper_id = s2_paper_data.get("paperId", None)
    doi = s2_paper_data.get("externalIds", {}).get("DOI")
    relevance_score = paper_wrapper_entry.get("relevance_score", 0.0)
    normalized_doi = normalize_doi(doi) if doi else None # Normalize DOI early
    # Define filename_base early using normalized_doi and the original title for cleaning
    filename_base = f"DOI_{normalized_doi.replace('/', '-')}" if normalized_doi else clean_title_for_filename(title)

    status_obj = {
        'paperId': paper_id,
        'title': title,
        'doi': doi,
        'relevance_score': relevance_score,
        'status': 'skipped_below_threshold',
        'pdf_url_found': None,
        'source_of_pdf': None,
        'downloaded_path': None,
        'file_hash': None,
        'error_message': None,
        'abstract_saved_path': None # New field for abstract path
    }

    if relevance_score < min_relevance_for_download:
        logging.info(f"Skipping paper '{title[:50]}...' (Score: {relevance_score:.2f} < {min_relevance_for_download:.2f})")
        return status_obj
    
    status_obj['status'] = 'attempted_download' # Update status

    # Deduplication for this run (if multiple entries for same paper were in input)
    # This is slightly different from find_existing_paper which checks file system
    # normalized_doi defined above
    normalized_title = normalize_text(title) # Ensure title is normalized for processing and set lookups
    # filename_base definition moved up to be available for all paths.
    
    if normalized_doi and normalized_doi in processed_dois:
        logging.info(f"Paper with DOI {normalized_doi} already processed in this run. Skipping duplicate fetch attempt.")
        status_obj['status'] = 'skipped_duplicate_in_run_doi'
        return status_obj
    if not normalized_doi and normalized_title in processed_titles: # Only use title for de-dup if no DOI
        logging.info(f"Paper with Title '{normalized_title[:50]}...' (no DOI) already processed in this run. Skipping.")
        status_obj['status'] = 'skipped_duplicate_in_run_title'
        return status_obj

    # Check if already exists in output directory
    existing_path = find_existing_paper(title, doi, output_dir)
    if existing_path:
        logging.info(f"PDF for '{title[:50]}...' already exists: {existing_path.name}")
        status_obj['status'] = 'already_exists'
        status_obj['downloaded_path'] = str(existing_path.relative_to(WORKSPACE_ROOT))
        status_obj['file_hash'] = get_file_hash(existing_path)
        if normalized_doi: processed_dois.add(normalized_doi)
        if normalized_title: processed_titles.add(normalized_title)
        return status_obj

    pdf_url, source_name = find_pdf_main(s2_paper_data, enable_google_scholar=enable_gscholar)
    status_obj['pdf_url_found'] = pdf_url
    status_obj['source_of_pdf'] = source_name

    if pdf_url:
        # filename_base already defined above
        output_filename = f"{filename_base}.pdf"
        output_filepath = output_dir / output_filename
        
        # Additional check to prevent re-downloading if a similarly named file (maybe from a parallel process) was created
        if output_filepath.exists():
            logging.info(f"PDF {output_filepath.name} seems to have been downloaded by another process. Skipping.")
            status_obj['status'] = 'already_exists_race_condition'
            status_obj['downloaded_path'] = str(output_filepath.relative_to(WORKSPACE_ROOT))
            status_obj['file_hash'] = get_file_hash(output_filepath)
            if normalized_doi: processed_dois.add(normalized_doi)
            if normalized_title: processed_titles.add(normalized_title)
            return status_obj

        pbar_description = f"{title[:30]}... (Score: {relevance_score:.2f})"
        if download_pdf(pdf_url, output_filepath, pbar_desc=pbar_description, source_name=source_name):
            status_obj['status'] = 'download_success'
            status_obj['downloaded_path'] = str(output_filepath.relative_to(WORKSPACE_ROOT))
            status_obj['file_hash'] = get_file_hash(output_filepath)
        else:
            status_obj['status'] = 'download_failed'
            status_obj['error_message'] = f"Failed to download from {pdf_url} via {source_name}"
            logging.error(f"Failed to download PDF for '{title[:50]}...' from {source_name} URL: {pdf_url}")
            # Attempt to save abstract if PDF download failed
            abstract_text = s2_paper_data.get("abstract")
            if abstract_text:
                abstract_filename = f"{filename_base}_abstract.txt"
                abstract_filepath = output_dir / abstract_filename
                try:
                    with open(abstract_filepath, 'w', encoding='utf-8') as f_abs:
                        f_abs.write(abstract_text)
                    logging.info(f"Saved abstract for '{title[:50]}...' (PDF download failed) to {abstract_filepath.name}")
                    status_obj['abstract_saved_path'] = str(abstract_filepath.relative_to(WORKSPACE_ROOT)) # Path relative to workspace
                except Exception as e_abs:
                    logging.error(f"Failed to save abstract for '{title[:50]}...' (PDF download failed): {e_abs}")
    else:
        status_obj['status'] = 'no_pdf_url_found'
        status_obj['error_message'] = "No PDF URL found by any method."
        logging.warning(f"Could not find PDF URL for '{title[:50]}...' (DOI: {doi})")
        # Attempt to save abstract if no PDF URL was found
        abstract_text = s2_paper_data.get("abstract")
        if abstract_text:
            abstract_filename = f"{filename_base}_abstract.txt" # Use filename_base defined earlier
            abstract_filepath = output_dir / abstract_filename
            try:
                with open(abstract_filepath, 'w', encoding='utf-8') as f_abs:
                    f_abs.write(abstract_text)
                logging.info(f"Saved abstract for '{title[:50]}...' (no PDF URL) to {abstract_filepath.name}")
                status_obj['abstract_saved_path'] = str(abstract_filepath.relative_to(WORKSPACE_ROOT)) # Path relative to workspace
            except Exception as e_abs:
                logging.error(f"Failed to save abstract for '{title[:50]}...' (no PDF URL): {e_abs}")

    if normalized_doi: processed_dois.add(normalized_doi)
    if normalized_title: processed_titles.add(normalized_title) # Add normalized title after processing
    return status_obj


def generate_fetch_summary_report(
    output_dir: Path,
    input_file_path: Path,
    num_total_papers_in_input: int,
    num_considered_for_download: int, # papers meeting relevance threshold
    attempt_results: List[Dict[str, Any]],
    min_relevance_score: float,
    report_path: Path
):
    num_download_success = sum(1 for r in attempt_results if r['status'] == 'download_success')
    num_already_exist = sum(1 for r in attempt_results if r['status'] == 'already_exists' or r['status'] == 'already_exists_race_condition')
    num_no_url_found = sum(1 for r in attempt_results if r['status'] == 'no_pdf_url_found')
    num_download_failed = sum(1 for r in attempt_results if r['status'] == 'download_failed')
    num_skipped_duplicate = sum(1 for r in attempt_results if 'skipped_duplicate_in_run' in r['status'])
    num_error_bad_data = sum(1 for r in attempt_results if r['status'] == 'error_bad_input_data')
    num_abstracts_saved = sum(1 for r in attempt_results if r.get('abstract_saved_path')) # Count saved abstracts

    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Task 4.1.7.2: Optimized PDF Discovery Summary\n\n")
        f.write(f"**Completion Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Script Used:** `tools/{Path(__file__).name}`\n")
        # Ensure input_file_path is treated as relative to workspace root if it is already relative
        input_display_path = str(input_file_path) if not input_file_path.is_absolute() else str(input_file_path.relative_to(WORKSPACE_ROOT))
        f.write(f"**Input Scored Papers File:** `{input_display_path}`\n")
        # Ensure output_dir is treated as relative to workspace root if it is already relative
        output_dir_display_path = str(output_dir) if not output_dir.is_absolute() else str(output_dir.relative_to(WORKSPACE_ROOT))
        f.write(f"**Output PDF Directory:** `{output_dir_display_path}`\n")
        f.write(f"**Minimum Relevance Score for Download:** {min_relevance_score:.2f}\n\n")
        f.write(f"## Fetching Statistics\n\n")
        f.write(f"- **Total papers in input file:** {num_total_papers_in_input}\n")
        f.write(f"- **Papers meeting relevance threshold (>= {min_relevance_score:.2f}):** {num_considered_for_download}\n")
        f.write(f"- **Download attempts made (for non-existing, non-duplicate papers):** {len(attempt_results) - num_already_exist - num_skipped_duplicate - num_error_bad_data}\n") # Should match sum of success, no_url, failed
        f.write(f"  - **Successfully downloaded new PDFs:** {num_download_success}\n")
        f.write(f"  - **Already existing in output directory (skipped download):** {num_already_exist}\n")
        f.write(f"  - **Skipped as duplicate within this run (DOI/Title):** {num_skipped_duplicate}\n")
        f.write(f"  - **No PDF URL found by any method:** {num_no_url_found}\n")
        f.write(f"  - **Failed download attempts (URL found but download failed):** {num_download_failed}\n")
        f.write(f"  - **Skipped due to bad input data:** {num_error_bad_data}\n")
        f.write(f"  - **Abstracts saved (when PDF not obtained/downloaded):** {num_abstracts_saved}\n\n")

        # Source attribution for successful downloads
        source_counts: Dict[str, int] = {}
        for r in attempt_results:
            if r['status'] == 'download_success' and r.get('source_of_pdf'):
                source = r['source_of_pdf']
                source_counts[source] = source_counts.get(source, 0) + 1
        if source_counts:
            f.write(f"### Sources of Successfully Downloaded PDFs\n\n")
            for source, count in sorted(source_counts.items(), key=lambda item: item[1], reverse=True):
                f.write(f"- **{source}:** {count} paper(s)\n")
            f.write("\n")

        f.write(f"## Unsuccessful PDF Searches/Downloads\n\n")
        f.write("The following papers met the relevance criteria but could not be downloaded automatically:\n\n")
        f.write("| # | Title | DOI | Relevance Score | Status | Error/Details | PDF URL Tried |\n")
        f.write("|---|-------|-----|-----------------|--------|---------------|---------------|\n")
        count_failed_detailed = 0
        for i, result in enumerate(attempt_results):
            if result['status'] not in ['download_success', 'already_exists', 'skipped_below_threshold', 'skipped_duplicate_in_run_doi', 'skipped_duplicate_in_run_title']:
                count_failed_detailed +=1
                title_short = normalize_text(result.get('title', 'Unknown Title'))[:70]
                doi_val = result.get('doi', 'N/A')
                score_val = f"{result.get('relevance_score', 0.0):.2f}" # Provide default for score
                status_val = result.get('status', 'error_unknown') # Provide default for status
                error_val = result.get('error_message', 'N/A')[:100]
                url_tried = result.get('pdf_url_found', 'N/A')
                if url_tried and len(url_tried) > 70: url_tried = url_tried[:67] + "..."
                f.write(f"| {count_failed_detailed} | {title_short} | {doi_val} | {score_val} | {status_val} | {error_val} | {url_tried} |\n")
        f.write("\n## Notes\n\n")
        f.write("- This report summarizes the automated PDF fetching process based on the provided relevance scores.\n")
        f.write("- Manual searching may be required for papers that could not be downloaded or found.\n")

    logging.info(f"Generated PDF fetch summary report: {report_path}")


def main():
    parser = argparse.ArgumentParser(description="Optimized PDF Downloader for Semantic Scholar papers.")
    parser.add_argument(
        "input_json_path", 
        type=str, 
        help="Path to the input JSON file from the dynamic search (e.g., consolidated_dynamic_search_complete_session1.json)"
    )
    parser.add_argument(
        "--output_dir", 
        type=str, 
        default=str(OUTPUT_PDF_DIR),
        help=f"Directory to save downloaded PDFs. Default: {OUTPUT_PDF_DIR}"
    )
    parser.add_argument(
        "--min_relevance", 
        type=float, 
        default=0.30, 
        help="Minimum relevance score for a paper to be considered for download. Default: 0.30"
    )
    parser.add_argument(
        "--max_workers", 
        type=int, 
        default=5, 
        help="Number of concurrent workers for downloading. Default: 5"
    )
    parser.add_argument(
        "--enable_google_scholar",
        action="store_true",
        help="Enable searching Google Scholar for PDFs (use with caution, can be unstable/blocked)."
    )
    # No new CLI args for session ID, it will be inferred from input file name

    args = parser.parse_args()

    input_file = Path(args.input_json_path)
    
    # Determine session ID from input file name
    session_id_match = re.search(r"session(?:-)?(\d+)", input_file.name, re.IGNORECASE) # Use input_file.name and updated regex
    session_id_str = "unknown_session"
    if session_id_match:
        session_id_str = session_id_match.group(1)
        logging.info(f"Inferred session ID: {session_id_str}")
    else:
        logging.warning(f"Could not infer session ID from input file name: {input_file.name}. Using default '{session_id_str}'.")

    # Create session-specific output directory
    base_output_dir = Path(args.output_dir)
    session_output_dir = base_output_dir / f"session-{session_id_str}"
    session_output_dir.mkdir(parents=True, exist_ok=True)
    
    # Use session_output_dir for all subsequent operations
    output_pdf_path = session_output_dir

    logging.info(f"Starting Optimized PDF Downloader.")
    logging.info(f"Input JSON: {input_file}")
    logging.info(f"Output PDF/Abstract Directory: {output_pdf_path}") # Updated log message
    logging.info(f"Minimum Relevance Score: {args.min_relevance}")
    logging.info(f"Max Workers: {args.max_workers}")
    logging.info(f"Google Scholar Enabled: {args.enable_google_scholar}")
    if not os.getenv('CORE_API_KEY'):
        logging.warning("CORE_API_KEY environment variable not set. CORE searches will be skipped or limited.")
    if not os.getenv('UNPAYWALL_EMAIL'):
        logging.warning("UNPAYWALL_EMAIL environment variable not set. Using default, which might be rate-limited more strictly.")

    input_data = load_input_json_file(input_file)
    if not input_data:
        logging.critical("Failed to load or parse input JSON file. Exiting.")
        # Ensure summary report path uses the correct (potentially sessioned) output_pdf_path context
        # if session_id_str is "unknown_session", report will be at top level of DOCS_DIR.
        # If input_file.stem doesn't include "session-X", the output dir is session-unknown_session
        # Summary file name is based on input_file.stem which is fine.
        summary_report_path = DOCS_DIR / f"{Path(__file__).stem}_summary_{input_file.stem}.md"
        generate_fetch_summary_report(output_pdf_path, input_file, 0, 0, [], args.min_relevance, summary_report_path)
        return
        
    papers_to_process = input_data.get("papers", [])
    num_total_in_input = len(papers_to_process)
    if num_total_in_input == 0:
        logging.info("No papers found in the input JSON file.")
        # Generate an empty summary report
        summary_report_path = DOCS_DIR / f"{Path(__file__).stem}_summary_{input_file.stem}.md"
        generate_fetch_summary_report(output_pdf_path, input_file, 0, 0, [], args.min_relevance, summary_report_path)
        return
        
    # Filter by relevance score before processing
    relevant_papers = [p for p in papers_to_process if p.get("relevance_score", 0.0) >= args.min_relevance]
    num_relevant_for_download = len(relevant_papers)

    logging.info(f"Total papers in input: {num_total_in_input}. Papers meeting relevance score >= {args.min_relevance}: {num_relevant_for_download}")

    all_attempt_results: List[Dict[str, Any]] = []
    processed_dois_in_run: Set[str] = set()
    processed_titles_in_run: Set[str] = set() # For papers without DOIs

    if relevant_papers:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as executor:
            future_to_paper_title = {
                executor.submit(
                    process_single_paper, 
                    paper_entry, 
                    output_pdf_path, # Pass the session-specific output path
                    args.min_relevance, 
                    args.enable_google_scholar,
                    processed_dois_in_run, 
                    processed_titles_in_run
                ): paper_entry.get("original_data",{}).get("title", "Unknown") 
                for paper_entry in relevant_papers
            }
            
            # Progress bar for futures
            for future in tqdm(concurrent.futures.as_completed(future_to_paper_title), total=len(relevant_papers), desc="Processing papers"):
                paper_title_desc = future_to_paper_title[future][:50] # Short title for progress
                try:
                    result = future.result()
                    all_attempt_results.append(result)
                except Exception as exc:
                    logging.error(f"Paper '{paper_title_desc}...' generated an exception: {exc}")
                    # Construct a basic error result, ensuring all keys accessed by summary are present or defaulted there
                    all_attempt_results.append({
                        'title': paper_title_desc, # Keep title for identification
                        'paperId': None, # Add paperId, though it might not be available easily here from paper_wrapper_entry
                        'doi': None, # Add doi
                        'relevance_score': 0.0, # Default relevance score
                        'status': 'error_processing_future',
                        'error_message': str(exc),
                        'abstract_saved_path': None
                    })

    # Generate final summary report
    summary_filename = f"{Path(__file__).stem}_summary_{input_file.stem}.md" # e.g., 4.1.7.2_optimized_pdf_downloader_summary_consolidated_dynamic_search_complete_session1.md
    summary_report_path = DOCS_DIR / summary_filename
    generate_fetch_summary_report(
        output_pdf_path, 
        input_file, 
        num_total_in_input,
        num_relevant_for_download,
        all_attempt_results, 
        args.min_relevance,
        summary_report_path
    )
    
    logging.info("Optimized PDF Downloader finished.")

if __name__ == "__main__":
    # Ensure re is available if not already globally imported at the top, though it should be.
    # import re # Not needed here if top-level import is present.
    main()
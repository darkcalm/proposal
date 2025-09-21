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
from ratelimit import limits, sleep_and_retry
import hashlib
from typing import Optional, Dict, List, Tuple

# Setup basic logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.FileHandler('paper_download.log'),
        logging.StreamHandler()
    ]
)

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PDF_DIR = WORKSPACE_ROOT / "sources" / "4.1.6-semantic-scholar-relevant-papers"
DOCS_DIR = WORKSPACE_ROOT / "docs"

# Rate limiting constants
CALLS_PER_SECOND = 1
CALLS_PER_MINUTE = 30

# --- Functions adapted from tools/4.1.1.4_elicit_paper_downloader.py ---
# PAPER_SOURCES dictionary for find_pdf_url function
PAPER_SOURCES = {
    'semantic_scholar': {
        'base_url': 'https://api.semanticscholar.org/graph/v1/paper/',
        'fields': 'title,authors,year,abstract,openAccessPdf,url'
    },
    'unpaywall': {
        'base_url': 'https://api.unpaywall.org/v2/'
    },
    'arxiv': {
        'base_url': 'http://export.arxiv.org/api/query'
    },
    'core': {
        'base_url': 'https://core.ac.uk/api/v2/search/works',
        'api_key': os.getenv('CORE_API_KEY') # Add your CORE API key to environment variables if you have one
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
    title = re.sub(r'[\\/*?:;"<>|]', '_', title) # Replaced " with ; to avoid conflict with quoting
    title = title.replace(' ', '_')
    title = title.replace(':', '_') # Colons also problematic
    return title[:150]

def normalize_text_for_comparison(text: str) -> str:
    """Normalize text for comparison by removing special characters, converting to lowercase."""
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', ' ', text) # Keep hyphens
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def find_existing_paper_by_title_and_doi(title: str, doi: str | None, output_dir: Path) -> Path | None:
    """Check if a paper with a similar title or matching DOI already exists."""
    if not title and not doi:
        return None

    normalized_query_title = normalize_text_for_comparison(title) if title else ""
    normalized_query_doi = normalize_text_for_comparison(doi) if doi else ""

    for existing_pdf in output_dir.glob('*.pdf'):
        filename_stem = existing_pdf.stem
        
        # Try to extract DOI from filename (e.g., title_DOI_xxxx.pdf)
        existing_doi_match = re.search(r'_DOI_([^_]+)$', filename_stem)
        if existing_doi_match:
            normalized_existing_doi = normalize_text_for_comparison(unquote(existing_doi_match.group(1)))
            if normalized_query_doi and normalized_query_doi == normalized_existing_doi:
                logging.info(f"Found existing paper by DOI match: {existing_pdf.name}")
                return existing_pdf
        
        # Compare titles if DOI didn't match or not present in query/filename
        if title: # Only compare titles if a query title is provided
            filename_title_part = filename_stem.split('_DOI_')[0] if '_DOI_' in filename_stem else filename_stem
            normalized_existing_title = normalize_text_for_comparison(filename_title_part.replace('_', ' '))
            
            if normalized_query_title and normalized_existing_title:
                similarity = difflib.SequenceMatcher(None, normalized_query_title, normalized_existing_title).ratio()
                if similarity > 0.9: # High threshold for title similarity
                    logging.info(f"Found existing paper by title similarity ({similarity:.2f}): {existing_pdf.name}")
                    return existing_pdf
    return None

@sleep_and_retry
@limits(calls=CALLS_PER_SECOND, period=1)
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, jitter=backoff.full_jitter)
def download_pdf_from_url(url: str, output_path: Path, pbar_desc: str | None = None) -> bool:
    """Download PDF from URL with retry logic, progress bar, and rate limiting."""
    try:
        desc = pbar_desc or output_path.name
        logging.info(f"Attempting to download PDF from: {url} to {output_path.name}")
        
        # Some URLs might have User-Agent restrictions
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/pdf,application/x-pdf,application/octet-stream,*/*'
        }
        
        # First check if the URL is accessible and returns a PDF
        head_response = requests.head(url, timeout=10, headers=headers, allow_redirects=True)
        content_type = head_response.headers.get('Content-Type', '').lower()
        
        if head_response.status_code >= 400:
            logging.error(f"HTTP error {head_response.status_code} checking URL {url}")
            return False
            
        if not ('application/pdf' in content_type or 'octet-stream' in content_type) and not url.lower().endswith('.pdf'):
            if 'text/html' in content_type:
                logging.warning(f"URL {url} returned HTML content, not PDF. Skipping.")
                return False
            logging.warning(f"URL {url} has unusual Content-Type: {content_type}. Proceeding with download attempt.")

        # Proceed with download
        response = requests.get(url, stream=True, timeout=60, headers=headers, allow_redirects=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f, tqdm(
            desc=desc,
            total=total_size,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
            disable=total_size==0 # Disable pbar if no content-length
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        # Verify if the downloaded file is a valid PDF
        if output_path.stat().st_size == 0:
            logging.error(f"Downloaded file {output_path.name} is empty. Deleting.")
            output_path.unlink()
            return False
            
        # Check PDF header
        with open(output_path, 'rb') as f_check:
            header = f_check.read(4)
            if header != b'%PDF':
                logging.warning(f"File {output_path.name} from {url} does not appear to be a valid PDF (missing %PDF header).")
                # Check if it's an error page
                f_check.seek(0)
                content = f_check.read(1024).decode('utf-8', errors='ignore')
                if '<html' in content.lower() or '<!doctype' in content.lower():
                    logging.error(f"Downloaded file appears to be an HTML error page. Deleting.")
                    output_path.unlink()
                    return False
                # If not HTML, keep the file but log warning
                logging.warning(f"Keeping potentially invalid PDF file: {output_path.name}")

        # Calculate file hash for verification
        file_hash = get_file_hash(output_path)
        logging.info(f"Successfully downloaded: {output_path.name} (SHA-256: {file_hash})")
        return True
        
    except requests.exceptions.Timeout:
        logging.error(f"Timeout downloading PDF from {url}")
        return False
    except requests.exceptions.RequestException as e:
        logging.error(f"Error downloading PDF from {url}: {e}")
        return False
    except Exception as e:
        logging.error(f"An unexpected error occurred during download from {url}: {e}")
        return False

@sleep_and_retry
@limits(calls=CALLS_PER_MINUTE, period=60)
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def get_unpaywall_pdf_url(doi: str) -> str | None:
    """Get PDF URL from Unpaywall using DOI with rate limiting."""
    if not doi: return None
    try:
        email = os.getenv("UNPAYWALL_EMAIL", "gusp@test.com")
        url = f"{PAPER_SOURCES['unpaywall']['base_url']}{quote(doi)}?email={email}"
        logging.info(f"Querying Unpaywall for DOI: {doi}")
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        data = response.json()
        
        if data.get('best_oa_location') and data['best_oa_location'].get('url_for_pdf'):
            pdf_url = data['best_oa_location']['url_for_pdf']
            logging.info(f"Unpaywall found PDF for {doi} at: {pdf_url}")
            return pdf_url
        elif data.get('oa_locations'):
            for loc in data['oa_locations']:
                if loc.get('url_for_pdf'):
                    pdf_url = loc['url_for_pdf']
                    logging.info(f"Unpaywall found PDF (alternative) for {doi} at: {pdf_url}")
                    return pdf_url
        logging.info(f"No direct PDF URL found on Unpaywall for DOI: {doi}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logging.info(f"DOI {doi} not found on Unpaywall.")
        elif e.response.status_code == 422:
            logging.warning(f"Unpaywall returned 422 for DOI {doi}. It might be an invalid DOI.")
        else:
            logging.error(f"Unpaywall HTTP error for DOI {doi}: {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Unpaywall request error for DOI {doi}: {e}")
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON response from Unpaywall for DOI {doi}")
    return None

def search_arxiv_by_title(title: str) -> str | None:
    """Search for paper on arXiv by title."""
    if not title: return None
    try:
        logging.info(f"Searching arXiv for title: '{title}'")
        # Use more specific query terms if title is generic
        # Using `ti:"exact title"` and `abs:"part of title"` or keywords from title
        search_query = f'ti:"{title}"'
        search = arxiv.Search(query=search_query, max_results=1, sort_by=arxiv.SortCriterion.Relevance)
        client = arxiv.Client(page_size=1, delay_seconds=3.0, num_retries=2) # Be respectful to arXiv API
        results = list(client.results(search))
        
        if results and results[0].pdf_url:
            # Validate title similarity
            arxiv_title = results[0].title
            similarity = difflib.SequenceMatcher(None, normalize_text_for_comparison(title), normalize_text_for_comparison(arxiv_title)).ratio()
            if similarity > 0.85: # досить високий поріг
                logging.info(f"Found on arXiv (Title: '{arxiv_title}', Similarity: {similarity:.2f}): {results[0].pdf_url}")
                return results[0].pdf_url
            else:
                logging.info(f"arXiv result title '{arxiv_title}' too dissimilar (Similarity: {similarity:.2f}) to query '{title}'. Skipping.")
        else:
            logging.info(f"No direct PDF found on arXiv for title: '{title}'")
    except Exception as e: # Catch broad exceptions from arxiv library
        logging.error(f"Error searching arXiv for '{title}': {e}")
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def search_core_by_title(title: str) -> str | None:
    """Search CORE for a paper by title and try to get a PDF link."""
    if not title: return None
    api_key = PAPER_SOURCES['core'].get('api_key')
    if not api_key:
        logging.warning("CORE API key not set. CORE search will be skipped.")
        return None
    
    try:
        logging.info(f"Searching CORE for title: {title}")
        url = f"{PAPER_SOURCES['core']['base_url']}"
        # CORE API query for exact title can be tricky, use a broader search and filter
        params = {'q': f'title:("{title}")', 'apiKey': api_key, 'limit': 5}
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()

        if data.get("status") == "OK" and data.get("data"):
            for item in data["data"]:
                core_title = item.get("title", "")
                similarity = difflib.SequenceMatcher(None, normalize_text_for_comparison(title), normalize_text_for_comparison(core_title)).ratio()
                if similarity > 0.9: # High similarity for title match
                    if item.get("downloadUrl"):
                        pdf_url = item["downloadUrl"]
                        # CORE often provides direct PDF links or links to landing pages that then link to PDFs.
                        # Ensure it's a direct PDF link if possible.
                        if pdf_url.endswith('.pdf'):
                             logging.info(f"Found PDF on CORE for '{title}' (Similarity: {similarity:.2f}): {pdf_url}")
                             return pdf_url
                        else: # Try to get it from fulltextUrls if downloadUrl is not a PDF
                            fulltext_urls = item.get("fulltextUrls", [])
                            for ft_url in fulltext_urls:
                                if ft_url.endswith(".pdf"):
                                    logging.info(f"Found PDF (fulltextUrls) on CORE for '{title}' (Similarity: {similarity:.2f}): {ft_url}")
                                    return ft_url
                    # If no direct downloadUrl, check identifiers for arXiv links etc.
                    identifiers = item.get('identifiers', [])
                    for identifier in identifiers:
                        if 'arxiv:' in identifier.lower():
                            arxiv_id = identifier.split(':')[-1]
                            arxiv_pdf_url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
                            logging.info(f"Found arXiv link via CORE for '{title}': {arxiv_pdf_url}")
                            return arxiv_pdf_url
            logging.info(f"No direct PDF download link found on CORE for title: {title} among top results.")
        else:
            logging.info(f"No results or error from CORE for title: {title}. Status: {data.get('status')}")

    except requests.exceptions.HTTPError as e:
        logging.error(f"CORE HTTP error for title '{title}': {e}")
    except requests.exceptions.RequestException as e:
        logging.error(f"CORE request error for title '{title}': {e}")
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON response from CORE for title {title}")
    return None

# ResearchGate and Google Scholar scraping can be unreliable and ethically questionable. Use with caution.
# For this script, we will attempt them as last resorts.
@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=2, jitter=backoff.full_jitter)
def search_researchgate(title: str) -> str | None:
    """Attempt to find a PDF link on ResearchGate by title (scraping, unreliable)."""
    if not title: return None
    try:
        logging.info(f"Searching ResearchGate for title: {title}")
        search_url = f"{PAPER_SOURCES['researchgate']['base_url']}{quote(title)}"
        response = requests.get(search_url, headers=PAPER_SOURCES['researchgate']['headers'], timeout=20)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # This is highly dependent on ResearchGate's HTML structure
        # Look for links that might be PDF downloads associated with the title
        # Prioritize links with "download" or "pdf" in text or href
        for link in soup.find_all('a', href=True):
            href = link['href']
            link_text = link.get_text().lower()
            # Check if the link text or href strongly suggests it's a download for the paper
            # This is a heuristic and might need significant refinement
            if (('pdf' in href or 'download' in href) and 
                (normalize_text_for_comparison(title)[:30] in normalize_text_for_comparison(link_text) or 
                 normalize_text_for_comparison(title)[:30] in normalize_text_for_comparison(href))):
                # Resolve relative URLs
                if href.startswith('/'):
                    href = "https://www.researchgate.net" + href
                
                # Further check if this link is likely a direct PDF
                # This check is very basic
                if href.lower().endswith('.pdf'):
                    logging.info(f"Potential PDF link found on ResearchGate: {href}")
                    return href
        logging.info(f"No obvious PDF link found on ResearchGate for: {title}")
    except Exception as e:
        logging.error(f"Error searching ResearchGate for '{title}': {e}")
    return None

def search_google_scholar(title: str) -> str | None:
    """Search Google Scholar using 'scholarly' and look for PDF links."""
    if not title: return None
    try:
        logging.info(f"Searching Google Scholar for title: {title}")
        # Configure scholarly to be less aggressive if needed, or use proxies
        # For now, default usage. This can get blocked by CAPTCHAs.
        search_query = scholarly.search_pubs(title)
        publication = next(search_query, None)
        
        if publication:
            pub_title = publication.get('bib', {}).get('title', '')
            similarity = difflib.SequenceMatcher(None, normalize_text_for_comparison(title), normalize_text_for_comparison(pub_title)).ratio()

            if similarity > 0.9: # High similarity needed
                logging.info(f"Found on Google Scholar: '{pub_title}' (Similarity: {similarity:.2f})")
                if publication.get('eprint_url'): # Often a direct PDF link
                    pdf_url = publication['eprint_url']
                    logging.info(f"Google Scholar eprint_url: {pdf_url}")
                    return pdf_url
                # Check bib for other URLs, though 'eprint_url' is usually the best bet
                # Some publications might have 'pub_url' leading to a page with PDF.
                # This part can be expanded if 'eprint_url' is often missing.
            else:
                logging.info(f"Google Scholar result '{pub_title}' (Similarity: {similarity:.2f}) too dissimilar to '{title}'.")
        else:
            logging.info(f"No results from Google Scholar for: {title}")
            
    except Exception as e:
        logging.error(f"Error searching Google Scholar for '{title}': {e}")
    return None

def find_pdf_url(doi: str | None, title: str) -> str | None:
    """Try to find a PDF URL from various sources, prioritizing DOI-based if DOI is available."""
    pdf_url = None
    attempted_sources_log = []

    # 1. Unpaywall (needs DOI)
    if doi:
        pdf_url = get_unpaywall_pdf_url(doi)
        attempted_sources_log.append(f"Unpaywall (DOI: {doi}): {'Found' if pdf_url else 'Not found'}")
        if pdf_url: return pdf_url

    # 2. arXiv (needs title)
    if title:
        pdf_url = search_arxiv_by_title(title)
        attempted_sources_log.append(f"arXiv (Title: {title[:50]}...): {'Found' if pdf_url else 'Not found'}")
        if pdf_url: return pdf_url
    
    # 3. CORE (needs title and API key)
    if title and PAPER_SOURCES['core'].get('api_key'):
        pdf_url = search_core_by_title(title)
        attempted_sources_log.append(f"CORE (Title: {title[:50]}...): {'Found' if pdf_url else 'Not found or API key missing'}")
        if pdf_url: return pdf_url
    elif title and not PAPER_SOURCES['core'].get('api_key'):
        attempted_sources_log.append(f"CORE (Title: {title[:50]}...): Skipped, API key missing")


    # Potentially less reliable / more aggressive methods last:
    # 4. ResearchGate (scraping, needs title)
    # if title:
    #     pdf_url = search_researchgate(title)
    #     attempted_sources_log.append(f"ResearchGate (Title: {title[:50]}...): {'Found' if pdf_url else 'Not found'}")
    #     if pdf_url: return pdf_url

    # 5. Google Scholar (scraping via scholarly, needs title)
    # if title:
    #     pdf_url = search_google_scholar(title)
    #     attempted_sources_log.append(f"Google Scholar (Title: {title[:50]}...): {'Found' if pdf_url else 'Not found'}")
    #     if pdf_url: return pdf_url
    
    logging.info(f"PDF search attempts for '{title[:50]}...' / DOI '{doi}': {'; '.join(attempted_sources_log)}")
    return None

# --- End of adapted functions ---

def load_json_file(file_path: Path):
    """Load a JSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error: Could not decode JSON from {file_path}")
        return None

def generate_summary_report(
    output_dir: Path,
    num_total_scored_papers: int,
    num_relevant_papers: int,
    num_attempted: int,
    num_downloaded: int,
    num_already_exist: int,
    num_failed: int,
    min_relevance_score: float,
    report_path: Path
):
    """Generate a markdown summary report of the fetching process."""
    
    report_content = f"""# Task 4.1.6: Fetch Relevant Semantic Scholar API Papers Summary

**Completion Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Script Used:** `tools/4.1.6_fetch_relevant_semantic_scholar_papers.py`  
**Input Scored Papers:** `sources/4.1.5-semantic-scholar-scored-papers/all_scored_papers_iter1-4.json` ({num_total_scored_papers} papers)  
**Input Relevance Criteria:** `sources/4.1.3-relevance-criteria/relevance_criteria.json`  
**Output PDF Directory:** `{output_dir.relative_to(WORKSPACE_ROOT)}`  

## Process Overview

1. Loaded relevance criteria to determine the minimum relevance score for fetching.
2. Loaded all previously scored Semantic Scholar papers.
3. Filtered papers meeting the minimum overall relevance score threshold (>= {min_relevance_score:.2f}).
4. For each relevant paper:
    a. Generated a standardized filename based on its title and DOI.
    b. Checked if a similar paper (by title or DOI) already existed in the output directory.
    c. If not existing, attempted to download the PDF, prioritizing `openAccessPdf` links from Semantic Scholar data, then using a multi-source search strategy (`Unpaywall`, `arXiv`, `CORE`).
5. Logged all successes, failures, and existing papers.

## Fetching Statistics

- **Total scored Semantic Scholar papers considered:** {num_total_scored_papers}
- **Minimum relevance score for fetching:** {min_relevance_score:.2f}
- **Number of papers meeting this relevance threshold:** {num_relevant_papers}
- **Number of download attempts made (for non-existing papers):** {num_attempted}
- **Successfully downloaded new PDFs:** {num_downloaded}
- **Papers already existing in output directory (skipped download):** {num_already_exist}
- **Failed download attempts:** {num_failed}

## Notes

- The definition of "relevant" for this fetching task was based on the overall relevance score being >= {min_relevance_score:.2f}.
- PDF discovery relied on `openAccessPdf` fields in Semantic Scholar data and a series of external services (Unpaywall, arXiv, CORE). The reliability of these services can vary.
- ResearchGate and Google Scholar search functions (commented out in `find_pdf_url`) were not used in this run to avoid potential instability from scraping. They can be enabled if necessary but may require more robust error handling or proxy setups.
- Filename normalization and existing paper checks were performed to avoid duplicates and ensure usability.

## Next Steps

- Review the downloaded PDFs in `{output_dir.relative_to(WORKSPACE_ROOT)}`.
- For papers that failed to download, manual searching might be required if they are critical.
- Proceed with Task 4.2 (Focused Literature Analysis), incorporating these fetched Semantic Scholar papers along with the Elicit papers.
"""
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    logging.info(f"Summary report saved to: {report_path}")


def process_paper(paper_entry: Dict, output_dir: Path, index: int, total: int) -> Tuple[bool, bool, bool]:
    """Process a single paper entry for downloading."""
    original_data = paper_entry.get('original_data', {})
    title = original_data.get('title')
    doi = original_data.get('doi')
    paper_id = original_data.get('paperId')
    relevance_score = paper_entry.get('relevance_score', 0)

    if not title:
        logging.warning(f"Skipping paper entry {paper_id or 'Unknown ID'} due to missing title (Paper {index+1}/{total}).")
        return False, False, False

    logging.info(f"Processing paper {index+1}/{total}: '{title}' (Score: {relevance_score})")

    cleaned_title = clean_title_for_filename(title)
    safe_doi_suffix = f"_DOI_{quote(doi, safe='')}" if doi else ""
    pdf_filename = f"{cleaned_title}{safe_doi_suffix}.pdf"
    output_path = output_dir / pdf_filename

    # Check if already exists
    existing_file = find_existing_paper_by_title_and_doi(title, doi, output_dir)
    if existing_file:
        logging.info(f"Paper '{title}' already exists as '{existing_file.name}'. Skipping download.")
        return False, True, False

    downloaded_successfully = False

    # 1. Try Semantic Scholar's openAccessPdf link first
    open_access_pdf_info = original_data.get('openAccessPdf')
    if open_access_pdf_info and open_access_pdf_info.get('url'):
        s2_pdf_url = open_access_pdf_info['url']
        parsed_s2_url = urlparse(s2_pdf_url)
        if 'doi.org' in parsed_s2_url.netloc:
            logging.info(f"Found openAccessPdf URL (possibly DOI link): {s2_pdf_url}")
            if download_pdf_from_url(s2_pdf_url, output_path, pbar_desc=output_path.name):
                downloaded_successfully = True
            else:
                logging.info(f"Download from openAccessPdf URL {s2_pdf_url} failed. Will try find_pdf_url.")
        elif s2_pdf_url.lower().endswith('.pdf') or 'application/pdf' in requests.head(s2_pdf_url, timeout=10, allow_redirects=True).headers.get('Content-Type','').lower():
            if download_pdf_from_url(s2_pdf_url, output_path, pbar_desc=output_path.name):
                downloaded_successfully = True
        else:
            logging.info(f"openAccessPdf URL {s2_pdf_url} doesn't seem to be a direct PDF. Will try find_pdf_url.")

    # 2. If S2 openAccessPdf didn't work or wasn't there, use find_pdf_url
    if not downloaded_successfully:
        pdf_search_url = find_pdf_url(doi, title)
        if pdf_search_url:
            if download_pdf_from_url(pdf_search_url, output_path, pbar_desc=output_path.name):
                downloaded_successfully = True
        else:
            logging.warning(f"Could not find any PDF URL for '{title}' using find_pdf_url.")

    return downloaded_successfully, False, not downloaded_successfully

def main():
    """Main function to orchestrate fetching relevant Semantic Scholar papers."""
    logging.info("Starting Task 4.1.6: Fetch Relevant Semantic Scholar API Papers")
    
    criteria_file = WORKSPACE_ROOT / "sources" / "4.1.3-relevance-criteria" / "relevance_criteria.json"
    scored_papers_file = WORKSPACE_ROOT / "sources" / "4.1.5-semantic-scholar-scored-papers" / "all_scored_papers_iter1-4.json"
    summary_report_file = DOCS_DIR / "4.1.6-semantic-scholar-paper-fetch-summary.md"

    OUTPUT_PDF_DIR.mkdir(parents=True, exist_ok=True)

    criteria = load_json_file(criteria_file)
    if not criteria:
        logging.error("Failed to load relevance criteria. Exiting.")
        return

    all_scored_papers_data = load_json_file(scored_papers_file)
    if not all_scored_papers_data:
        logging.error("Failed to load scored Semantic Scholar papers. Exiting.")
        return
    
    num_total_scored_papers = len(all_scored_papers_data)
    min_relevance_score = criteria.get('inclusion_thresholds', {}).get('minimum_score', 0.3)

    relevant_papers = [
        p for p in all_scored_papers_data 
        if p.get('relevance_score', 0) >= min_relevance_score
    ]
    num_relevant_to_fetch = len(relevant_papers)
    logging.info(f"Found {num_relevant_to_fetch} papers meeting relevance score >= {min_relevance_score} (out of {num_total_scored_papers} scored papers).")

    # Sort by relevance score, highest first
    relevant_papers.sort(key=lambda p: p.get('relevance_score', 0), reverse=True)

    # Use ThreadPoolExecutor for parallel processing
    successful_downloads = 0
    already_exist_count = 0
    failed_downloads = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_paper = {
            executor.submit(process_paper, paper, OUTPUT_PDF_DIR, i, num_relevant_to_fetch): paper
            for i, paper in enumerate(relevant_papers)
        }

        for future in concurrent.futures.as_completed(future_to_paper):
            paper = future_to_paper[future]
            try:
                downloaded, existed, failed = future.result()
                if downloaded:
                    successful_downloads += 1
                if existed:
                    already_exist_count += 1
                if failed:
                    failed_downloads += 1
            except Exception as e:
                logging.error(f"Error processing paper '{paper.get('original_data', {}).get('title', 'Unknown')}': {e}")
                failed_downloads += 1

    logging.info("--- Fetching Complete ---")
    logging.info(f"Total relevant papers identified: {num_relevant_to_fetch}")
    logging.info(f"Successfully downloaded: {successful_downloads}")
    logging.info(f"Already existed: {already_exist_count}")
    logging.info(f"Failed downloads: {failed_downloads}")

    generate_summary_report(
        output_dir=OUTPUT_PDF_DIR,
        num_total_scored_papers=num_total_scored_papers,
        num_relevant_papers=num_relevant_to_fetch,
        num_attempted=successful_downloads + failed_downloads,
        num_downloaded=successful_downloads,
        num_already_exist=already_exist_count,
        num_failed=failed_downloads,
        min_relevance_score=min_relevance_score,
        report_path=summary_report_file
    )
    logging.info("Task 4.1.6 script execution finished.")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3

import os
import csv
import json
import re
import logging
from pathlib import Path
import time
from urllib.parse import urlparse, quote
from datetime import datetime
import difflib
import backoff
from tqdm import tqdm
import requests
import fitz  # PyMuPDF
# Note: For arxiv, scholarly, BeautifulSoup - these would be external dependencies.
# Assuming they are available if the original scripts ran.
# If not, they would need to be installed.
try:
    import arxiv
except ImportError:
    print("arxiv library not found. Please install: pip install arxiv")
    arxiv = None
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup library not found. Please install: pip install beautifulsoup4")
    BeautifulSoup = None


# --- Configuration ---
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
PHASE1_DISCOVERY_DIR = WORKSPACE_ROOT / "sources" / "4.1.8-elicit-results" / "phase-1-broad-discovery"
PHASE2_OUTPUT_DIR = WORKSPACE_ROOT / "sources" / "4.1.8-elicit-results" / "phase-2-targeted-queries"
DOWNLOADED_PAPERS_DIR = PHASE2_OUTPUT_DIR / "downloaded_papers"
MARKDOWN_PAPERS_DIR = PHASE2_OUTPUT_DIR / "markdown_papers"
ANALYSIS_OUTPUT_DIR = PHASE2_OUTPUT_DIR / "analysis_output"

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Constants for Downloader ---
PAPER_SOURCES = {
    'semantic_scholar': {
        'base_url': 'https://api.semanticscholar.org/graph/v1/paper/',
        'fields': 'title,authors,year,abstract,openAccessPdf,url,externalIds' # Added externalIds
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
    'google_scholar': { # Use with caution due to potential IP blocks
        'base_url': 'https://scholar.google.com/scholar?q=',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    }
}

# --- ADAPTED PDF Downloader Module (from 4.1.1.4_elicit_paper_downloader.py) ---

def clean_title_for_filename(title: str) -> str:
    if not title:
        return "unknown_title"
    title = title.replace('{', '').replace('}', '')
    title = re.sub(r'[\\/*?:"<>|]', '_', title)
    title = title.replace(' ', '_')
    return title[:150]

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, factor=5)
def _make_request_with_retry(url, headers=None, params=None, timeout=30, stream=False):
    response = requests.get(url, headers=headers, params=params, timeout=timeout, stream=stream)
    response.raise_for_status()
    return response

def get_paper_info_from_semantic_scholar(identifier, is_doi=True):
    headers = {"Accept": "application/json", "User-Agent": "ProposalHelper/1.0 (contact@example.com; for academic research)"}
    try:
        # S2 API prefers DOIs to be uppercase, but can also search by title if no DOI
        search_term = identifier.upper() if is_doi and identifier else quote(identifier)
        url = f"{PAPER_SOURCES['semantic_scholar']['base_url']}{search_term}"
        params = {'fields': PAPER_SOURCES['semantic_scholar']['fields']}
        if not is_doi and identifier: # If it's a title search
             url = f"{PAPER_SOURCES['semantic_scholar']['base_url']}search"
             params = {'query': identifier, 'fields': PAPER_SOURCES['semantic_scholar']['fields'], 'limit': 1}


        logger.info(f"Querying Semantic Scholar for {'DOI' if is_doi else 'Title'}: {identifier}")
        response = _make_request_with_retry(url, headers=headers, params=params)
        data = response.json()
        if not is_doi and 'data' in data and data['data']: # Handle search results format
            return data['data'][0]
        return data
    except requests.exceptions.RequestException as e:
        logger.error(f"Semantic Scholar error for {'DOI' if is_doi else 'Title'} {identifier}: {e}")
    except json.JSONDecodeError as e:
        logger.error(f"Semantic Scholar JSON decode error for {identifier}: {e}. Response text: {response.text if 'response' in locals() else 'N/A'}")
    return None


@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, factor=5)
def get_paper_info_from_unpaywall(doi):
    if not doi: return None
    headers = {"Accept": "application/json", "User-Agent": "ProposalHelper/1.0 (contact@example.com; for academic research)"}
    try:
        url = f"{PAPER_SOURCES['unpaywall']['base_url']}{doi.lower()}?email=contact@example.com" # Unpaywall requires email
        logger.info(f"Querying Unpaywall for DOI: {doi}")
        response = _make_request_with_retry(url, headers=headers)
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Unpaywall error for DOI {doi}: {e}")
    return None

def search_arxiv_by_title(title):
    if not arxiv or not title: return None
    try:
        logger.info(f"Searching arXiv for title: {title}")
        search = arxiv.Search(query=f'ti:"{title}"', max_results=1, sort_by=arxiv.SortCriterion.Relevance)
        client = arxiv.Client()
        results = list(client.results(search))
        if results:
            logger.info(f"Found on arXiv: {results[0].entry_id} -> {results[0].pdf_url}")
            return results[0].pdf_url
    except Exception as e:
        logger.error(f"Error searching arXiv for '{title}': {e}")
    return None

@backoff.on_exception(backoff.expo, requests.exceptions.RequestException, max_tries=3, factor=5)
def download_pdf_from_url(url, output_path: Path):
    try:
        logger.info(f"Attempting to download PDF from: {url}")
        # Some URLs might be relative, try to fix common cases from ResearchGate
        if url.startswith('/publication/') and 'researchgate.net' not in url:
            url = f"https://www.researchgate.net{url}"

        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            logger.warning(f"URL '{url}' has no scheme, attempting with https.")
            url = f"https://{url}"

        headers = PAPER_SOURCES['google_scholar']['headers'] # Generic browser headers
        response = _make_request_with_retry(url, headers=headers, stream=True)
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f, tqdm(
            desc=output_path.name, total=total_size, unit='iB', unit_scale=True, unit_divisor=1024, leave=False
        ) as pbar:
            for chunk in response.iter_content(chunk_size=block_size):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        logger.info(f"Successfully downloaded to: {output_path.name}")
        return True
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading PDF from {url}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error downloading PDF from {url}: {e}")
    return False

def normalize_title_for_comparison(title: str) -> str:
    if not title: return ""
    title = title.lower()
    title = re.sub(r'[^\w\s-]', '', title) # Keep hyphens
    title = re.sub(r'\s+', ' ', title).strip()
    return title

def find_existing_paper_by_title(title_to_check: str, output_dir: Path):
    if not title_to_check: return None
    normalized_query_title = normalize_title_for_comparison(title_to_check)
    if not normalized_query_title: return None

    for subdir in output_dir.rglob('*'): # Check subdirectories as well
        if subdir.is_dir():
            for existing_pdf in subdir.glob('*.pdf'):
                filename_title = existing_pdf.stem
                if '_DOI_' in filename_title:
                    filename_title = filename_title.split('_DOI_')[0]
                normalized_existing_title = normalize_title_for_comparison(filename_title.replace('_', ' '))
                
                if normalized_existing_title and difflib.SequenceMatcher(None, normalized_query_title, normalized_existing_title).ratio() > 0.9:
                    logger.info(f"Found existing similar paper: {existing_pdf.resolve()}")
                    return existing_pdf.resolve()
    return None

def find_pdf_urls_for_paper(title, doi=None):
    pdf_options = []
    s2_info = None

    if doi:
        s2_info = get_paper_info_from_semantic_scholar(doi, is_doi=True)
        if s2_info and s2_info.get('openAccessPdf') and s2_info['openAccessPdf'].get('url'):
            pdf_options.append({'source': 'S2 OpenAccess', 'url': s2_info['openAccessPdf']['url']})
        elif s2_info and s2_info.get('url') and isinstance(s2_info['url'], str) and s2_info['url'].lower().endswith('.pdf'):
             pdf_options.append({'source': 'S2 Main URL', 'url': s2_info['url']})

        unpaywall_info = get_paper_info_from_unpaywall(doi)
        if unpaywall_info and unpaywall_info.get('best_oa_location') and unpaywall_info['best_oa_location'].get('url_for_pdf'):
            pdf_options.append({'source': 'Unpaywall', 'url': unpaywall_info['best_oa_location']['url_for_pdf']})
        elif unpaywall_info and unpaywall_info.get('best_oa_location') and unpaywall_info['best_oa_location'].get('url'): # Fallback
            pdf_options.append({'source': 'Unpaywall (non-PDF URL)', 'url': unpaywall_info['best_oa_location']['url']})


    if not s2_info and title: # If DOI failed or no DOI, try S2 title search
        s2_info_title = get_paper_info_from_semantic_scholar(title, is_doi=False)
        if s2_info_title:
            s2_info = s2_info_title # use this for author/year if found
            if s2_info.get('openAccessPdf') and s2_info['openAccessPdf'].get('url'):
                pdf_options.append({'source': 'S2 (Title Search) OpenAccess', 'url': s2_info['openAccessPdf']['url']})
            elif s2_info.get('url') and isinstance(s2_info['url'], str) and s2_info['url'].lower().endswith('.pdf'):
                pdf_options.append({'source': 'S2 (Title Search) Main URL', 'url': s2_info['url']})
            # Extract DOI if found by title search
            if not doi and s2_info.get('externalIds') and s2_info['externalIds'].get('DOI'):
                doi = s2_info['externalIds']['DOI']


    if title:
        arxiv_url = search_arxiv_by_title(title)
        if arxiv_url: pdf_options.append({'source': 'arXiv', 'url': arxiv_url})
    
    # Add more sources like CORE, ResearchGate, Google Scholar if needed and reliable
    # For now, focusing on direct DOI/S2/Unpaywall/arXiv.

    # Deduplicate URLs
    seen_urls = set()
    unique_pdf_options = []
    for option in pdf_options:
        if option['url'] not in seen_urls:
            unique_pdf_options.append(option)
            seen_urls.add(option['url'])
            
    return unique_pdf_options, doi, s2_info # Return updated DOI and S2 info

def download_paper(paper_meta, base_output_dir):
    title = paper_meta.get('title')
    doi = paper_meta.get('doi')
    
    if not title:
        logger.warning("Paper has no title, skipping.")
        return None, 'no_title'

    # Check if paper already exists (search across all subdirs of base_output_dir)
    existing_path = find_existing_paper_by_title(title, base_output_dir)
    if existing_path:
        logger.info(f"Paper '{title}' already exists at {existing_path}. Skipping download.")
        return existing_path, 'existed'

    pdf_urls, updated_doi, s2_info = find_pdf_urls_for_paper(title, doi)
    paper_meta['doi'] = updated_doi # Update DOI if found via S2 title search

    if not pdf_urls:
        logger.warning(f"No PDF URL found for: {title} (DOI: {doi})")
        return None, 'no_pdf_url'

    year = paper_meta.get('year') or (s2_info.get('year') if s2_info else None)
    authors_list = paper_meta.get('authors') or (s2_info.get('authors') if s2_info else [])
    first_author_lastname = ""
    if authors_list and isinstance(authors_list, list) and authors_list[0].get('name'):
        first_author_lastname = authors_list[0]['name'].split(' ')[-1]
    elif isinstance(authors_list, str): # if authors is a string
        first_author_lastname = authors_list.split(',')[0].split(' ')[-1]


    filename_base = f"{first_author_lastname}{year}_" if first_author_lastname and year else ""
    filename_base += clean_title_for_filename(title)
    safe_doi_part = f"_DOI_{updated_doi.replace('/', '_').replace('.', '-')}" if updated_doi else ""
    final_filename = f"{filename_base}{safe_doi_part}.pdf"
    
    # Determine specific output path including research area
    research_area_slug = paper_meta.get('research_area_slug', 'general')
    specific_output_dir = base_output_dir / research_area_slug
    specific_output_dir.mkdir(parents=True, exist_ok=True)
    output_pdf_path = specific_output_dir / final_filename
    
    for option in pdf_urls:
        logger.info(f"Trying to download from {option['source']}: {option['url']}")
        if download_pdf_from_url(option['url'], output_pdf_path):
            return output_pdf_path, 'downloaded'
        time.sleep(0.5) # Be nice

    logger.error(f"Failed to download PDF for {title} from all sources.")
    return None, 'download_failed'

# --- ADAPTED PDF to Markdown Converter Module (from 4.1.1.5_elicit_papers_to_markdown.py) ---

def extract_metadata_from_pdf_filename(filename_str):
    base_name = filename_str.replace('.pdf', '')
    doi = None
    title_part = base_name
    if '_DOI_' in base_name:
        parts = base_name.split('_DOI_')
        title_part = parts[0]
        doi_part = parts[1]
        doi = doi_part.replace('_', '/').replace('-', '.') # Convert back
    
    # Attempt to extract author-year prefix if present
    # e.g., Smith2023_Actual_Title_Part
    author_year_match = re.match(r'^([A-Za-z]+)(\d{4})_', title_part)
    first_author = None
    year_str = None
    if author_year_match:
        first_author = author_year_match.group(1)
        year_str = author_year_match.group(2)
        # Remove author-year from title_part for cleaning
        title_part = re.sub(r'^[A-Za-z]+\d{4}_', '', title_part)

    cleaned_title = title_part.replace('_', ' ')
    
    return {
        'filename': filename_str,
        'title_from_filename': cleaned_title,
        'doi_from_filename': doi,
        'author_from_filename': first_author,
        'year_from_filename': year_str,
        'extracted_date': datetime.now().isoformat()
    }

def clean_extracted_text_for_markdown(text):
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text) # Consolidate multiple blank lines
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text) # Convert single newlines within paragraphs to spaces
    text = re.sub(r'-\s*\n\s*', '', text) # Join hyphenated words across lines
    text = re.sub(r' +', ' ', text)
    # Attempt to identify headings (lines with few words, title case, often bold in PDF)
    # This is heuristic and may need refinement.
    # For now, we rely on page breaks primarily.
    return text.strip()

def convert_pdf_to_markdown_file(pdf_path: Path, markdown_output_dir: Path, paper_master_meta: dict):
    try:
        file_meta = extract_metadata_from_pdf_filename(pdf_path.name)
        # Combine master metadata (from CSV) with filename metadata (as fallback)
        final_meta = {**file_meta, **paper_master_meta}


        title = final_meta.get('title', file_meta.get('title_from_filename', 'Unknown Title'))
        doi = final_meta.get('doi', file_meta.get('doi_from_filename'))
        authors = final_meta.get('authors_str', 'N/A') # Assuming authors_str from CSV processing
        year = final_meta.get('year', file_meta.get('year_from_filename','N/A'))
        abstract = final_meta.get('abstract', 'N/A')
        
        doc = fitz.open(pdf_path)
        
        markdown_content = f"# {title}\\n\\n"
        markdown_content += f"## Paper Metadata\\n\\n"
        markdown_content += f"- **Original PDF:** `{pdf_path.name}`\\n"
        markdown_content += f"- **Title:** {title}\\n"
        markdown_content += f"- **DOI:** {doi or 'Not available'}\\n"
        markdown_content += f"- **Authors:** {authors}\\n"
        markdown_content += f"- **Year:** {year}\\n"
        markdown_content += f"- **Abstract:**\\n{abstract}\\n\\n"
        markdown_content += f"- **Markdown Conversion Date:** {datetime.now().isoformat()}\\n"
        markdown_content += f"- **Total Pages (PDF):** {doc.page_count}\\n"
        markdown_content += "---\\n\\n"
        markdown_content += "## Full Text Content (Extracted from PDF)\\n\\n"
        
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            cleaned_text = clean_extracted_text_for_markdown(text)
            if cleaned_text:
                markdown_content += f"### Page {page_num + 1}\\n\\n"
                markdown_content += cleaned_text + "\\n\\n---\\n\\n"
        
        doc.close()
        
        md_filename_base = clean_title_for_filename(title)
        md_filename = f"{md_filename_base}.md"
        
        # Ensure markdown_output_dir includes the research_area_slug
        research_area_slug = paper_master_meta.get('research_area_slug', 'general')
        specific_md_output_dir = markdown_output_dir / research_area_slug
        specific_md_output_dir.mkdir(parents=True, exist_ok=True)
        output_md_path = specific_md_output_dir / md_filename
        
        with open(output_md_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        logger.info(f"Successfully converted {pdf_path.name} to {output_md_path.name}")
        return output_md_path
    except Exception as e:
        logger.error(f"Error converting PDF {pdf_path.name}: {e}", exc_info=True)
    return None

# --- Markdown Analysis Module (New) ---
def analyze_markdown_content(markdown_path: Path, paper_meta: dict):
    logger.info(f"Analyzing markdown: {markdown_path.name}")
    analysis = {
        'source_markdown_file': str(markdown_path.relative_to(WORKSPACE_ROOT)),
        'title': paper_meta.get('title', 'N/A'),
        'doi': paper_meta.get('doi', 'N/A'),
        'extracted_contexts': {
            "organizations_companies": [],
            "technologies_systems": [],
            "practical_challenges": [],
            "commercial_solutions_vendors": [],
            "standards_protocols": []
        },
        "keywords_phrases": [] # For general relevant terms
    }
    try:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read().lower() # Analyze in lowercase

        # Define regex patterns (examples, need refinement)
        # More specific patterns are better. This is very generic.
        org_patterns = [
            r'\b(?:[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*\s+(?:Inc|Ltd|Corp|LLC|GmbH|University|Institute|Laboratory|Labs|Energy|Electric|Power|Solutions|Systems))\b',
            r'\b(?:EPRI|NREL|DOE|FERC|IEEE|IEC)\b' # Common org acronyms
        ]
        tech_patterns = [
            r'\b(?:SCADA|DERMS|ADMS|VPP|EMS|DMS|GIS|IoT|AI|ML)\b', # Acronyms
            r'\b(?:blockchain|smart contract|python|java|sql|api)\b', # Technologies
            r'(?:[a-zA-Z0-9]+(?:Platform|Suite|Framework|System|Software|Grid\b))' # Product-like names
        ]
        challenge_patterns = [
            r'\b(?:challenge(?:s)? of|difficult(?:y|ies)|issue(?:s)? with|problem(?:s)? of|bottleneck|inefficien(?:cy|ies)|gap(?:s)? in|lack of|barrier(?:s)? to|concern(?:s)? about|risk(?:s)? of|human error)\b',
            r'(?:communication.*(?:breakdown|gap|issue))',
            r'(?:data.*(?:integration|quality|silo|sharing.*problem))'
        ]
        # Solutions/Vendors often overlap with Organizations
        # Standards/Protocols
        standard_patterns = [
            r'\b(?:IEEE\s*(?:P?\d{3,}(?:\.\d{1,2}\w?)?)|IEC\s*\d{4,}(?:-\d+)*|ISO\s*\d{4,})\b',
            r'\b(?:OpenADR|DNP3|Modbus|OPC-UA|MQTT|CoAP|Zigbee|LoRaWAN|SunSpec)\b'
        ]
        keyword_patterns = [ # From Angle 6 focus
            r'\b(?:human factor(?:s)?|operator|technician|field crew|control room|manual process(?:es)?|automation|communication|coordination|protocol(?:s)?|agent(?:s)?|multi-agent system(?:s)?|DER|distributed energy|microgrid|renewable(?:s)?|solar|wind|battery|storage|grid)\b'
        ]

        for category, patterns in [
            ("organizations_companies", org_patterns),
            ("technologies_systems", tech_patterns),
            ("practical_challenges", challenge_patterns),
            ("standards_protocols", standard_patterns),
            ("keywords_phrases", keyword_patterns)
        ]:
            found_terms = set()
            for pattern in patterns:
                # Use re.IGNORECASE if original content wasn't lowercased
                # Using raw strings r'...' for patterns is good practice
                try:
                    # For phrases with spaces, we need to be careful with word boundaries
                    # This simplistic approach might find substrings.
                    # For more accuracy, use word boundaries \b where appropriate in patterns.
                    matches = re.findall(pattern, content, re.IGNORECASE) # Content is already lower, but keep for pattern def.
                    for match in matches:
                        if isinstance(match, tuple): # some patterns might return tuples
                            match = next(m for m in match if m) # get first non-empty group
                        found_terms.add(match.strip())
                except re.error as re_err:
                    logger.error(f"Regex error for pattern '{pattern}' in category '{category}': {re_err}")

            analysis['extracted_contexts'][category] = sorted(list(found_terms))
            if category == "organizations_companies": # Also add to commercial_solutions_vendors
                 analysis['extracted_contexts']["commercial_solutions_vendors"] = sorted(list(set(analysis['extracted_contexts'].get("commercial_solutions_vendors", []) + list(found_terms))))


    except Exception as e:
        logger.error(f"Error analyzing markdown {markdown_path.name}: {e}", exc_info=True)
    return analysis

# --- Main Orchestration ---
def process_elicit_csv(csv_path: Path, research_area_slug: str):
    papers_metadata = []
    try:
        with open(csv_path, 'r', encoding='utf-8-sig') as f: # utf-8-sig for potential BOM
            reader = csv.DictReader(f)
            for row in reader:
                title = row.get('title') or row.get('Title') # Common column names
                doi = row.get('doi') or row.get('DOI')
                authors_str = row.get('authors') or row.get('Authors') # Assuming it's a string
                year = row.get('year') or row.get('Year')
                abstract = row.get('abstract') or row.get('Abstract')
                
                if title:
                    papers_metadata.append({
                        'title': title.strip(),
                        'doi': doi.strip() if doi else None,
                        'authors_str': authors_str.strip() if authors_str else None,
                        'year': year.strip() if year else None,
                        'abstract': abstract.strip() if abstract else None,
                        'source_csv': csv_path.name,
                        'research_area_slug': research_area_slug # For folder structure
                    })
    except Exception as e:
        logger.error(f"Error processing CSV {csv_path.name}: {e}")
    return papers_metadata

def analyze_missing_markdown_files():
    logger.info("Starting analysis of markdown files without JSON analysis...")
    
    # Get all markdown files
    markdown_files = list(MARKDOWN_PAPERS_DIR.rglob('*.md'))
    logger.info(f"Found {len(markdown_files)} total markdown files")
    
    # Get all existing analysis files
    analysis_files = list(ANALYSIS_OUTPUT_DIR.rglob('*_analysis.json'))
    existing_analysis_bases = {f.stem.replace('_analysis', '') for f in analysis_files}
    logger.info(f"Found {len(analysis_files)} existing analysis files")
    
    # Find markdown files without analysis
    missing_analysis = []
    for md_file in markdown_files:
        base_name = md_file.stem
        if base_name not in existing_analysis_bases:
            missing_analysis.append(md_file)
    
    logger.info(f"Found {len(missing_analysis)} markdown files without analysis")
    
    # Process each missing analysis
    for md_file in missing_analysis:
        try:
            logger.info(f"Analyzing markdown file: {md_file.name}")
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract metadata from markdown content
            title = None
            doi = None
            authors = None
            year = None
            
            # Try to extract metadata from markdown header
            metadata_section = content.split('---')[0] if '---' in content else content.split('\n\n')[0]
            for line in metadata_section.split('\n'):
                if line.startswith('title:'):
                    title = line.replace('title:', '').strip()
                elif line.startswith('doi:'):
                    doi = line.replace('doi:', '').strip()
                elif line.startswith('authors:'):
                    authors = line.replace('authors:', '').strip()
                elif line.startswith('year:'):
                    year = line.replace('year:', '').strip()
            
            # Create analysis
            analysis = {
                'source_markdown_file': str(md_file.relative_to(WORKSPACE_ROOT)),
                'title': title or md_file.stem,
                'doi': doi or 'N/A',
                'extracted_contexts': {
                    "organizations_companies": [],
                    "technologies_systems": [],
                    "practical_challenges": [],
                    "commercial_solutions_vendors": [],
                    "standards_protocols": []
                },
                "keywords_phrases": []
            }
            
            # Analyze content
            content_lower = content.lower()
            
            # Define regex patterns (reusing from existing analyze_markdown_content function)
            org_patterns = [
                r'\b(?:[A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)*\s+(?:Inc|Ltd|Corp|LLC|GmbH|University|Institute|Laboratory|Labs|Energy|Electric|Power|Solutions|Systems))\b',
                r'\b(?:EPRI|NREL|DOE|FERC|IEEE|IEC)\b'
            ]
            tech_patterns = [
                r'\b(?:SCADA|DERMS|ADMS|VPP|EMS|DMS|GIS|IoT|AI|ML)\b',
                r'\b(?:blockchain|smart contract|python|java|sql|api)\b',
                r'(?:[a-zA-Z0-9]+(?:Platform|Suite|Framework|System|Software|Grid\b))'
            ]
            challenge_patterns = [
                r'\b(?:challenge(?:s)? of|difficult(?:y|ies)|issue(?:s)? with|problem(?:s)? of|bottleneck|inefficien(?:cy|ies)|gap(?:s)? in|lack of|barrier(?:s)? to|concern(?:s)? about|risk(?:s)? of|human error)\b',
                r'(?:communication.*(?:breakdown|gap|issue))',
                r'(?:data.*(?:integration|quality|silo|sharing.*problem))'
            ]
            standard_patterns = [
                r'\b(?:IEEE\s*(?:P?\d{3,}(?:\.\d{1,2}\w?)?)|IEC\s*\d{4,}(?:-\d+)*|ISO\s*\d{4,})\b',
                r'\b(?:OpenADR|DNP3|Modbus|OPC-UA|MQTT|CoAP|Zigbee|LoRaWAN|SunSpec)\b'
            ]
            keyword_patterns = [
                r'\b(?:human factor(?:s)?|operator|technician|field crew|control room|manual process(?:es)?|automation|communication|coordination|protocol(?:s)?|agent(?:s)?|multi-agent system(?:s)?|DER|distributed energy|microgrid|renewable(?:s)?|solar|wind|battery|storage|grid)\b'
            ]
            
            # Process each category
            for category, patterns in [
                ("organizations_companies", org_patterns),
                ("technologies_systems", tech_patterns),
                ("practical_challenges", challenge_patterns),
                ("standards_protocols", standard_patterns),
                ("keywords_phrases", keyword_patterns)
            ]:
                found_terms = set()
                for pattern in patterns:
                    try:
                        matches = re.findall(pattern, content_lower, re.IGNORECASE)
                        for match in matches:
                            if isinstance(match, tuple):
                                match = next(m for m in match if m)
                            found_terms.add(match.strip())
                    except re.error as re_err:
                        logger.error(f"Regex error for pattern '{pattern}' in category '{category}': {re_err}")
                
                analysis['extracted_contexts'][category] = sorted(list(found_terms))
                if category == "organizations_companies":
                    analysis['extracted_contexts']["commercial_solutions_vendors"] = sorted(list(set(analysis['extracted_contexts'].get("commercial_solutions_vendors", []) + list(found_terms))))
            
            # Save analysis
            output_dir = ANALYSIS_OUTPUT_DIR / md_file.parent.name
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{md_file.stem}_analysis.json"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analysis, f, indent=2)
            
            logger.info(f"Created analysis file: {output_file}")
            
        except Exception as e:
            logger.error(f"Error analyzing markdown file {md_file.name}: {e}", exc_info=True)
    
    logger.info("Finished analyzing missing markdown files")

def perform_cross_referencing_validation():
    logger.info("Starting Phase 3: Cross-Referencing and Validation...")
    
    # Create a mapping of papers by research area
    research_areas = {
        '3.1.1-applied-human-factors': [],
        '3.1.2-industry-academia-collaborative': [],
        '3.1.3-applied-ai-automation': [],
        '3.1.4-safety-training': []
    }
    
    # Load all analysis files
    for area in research_areas.keys():
        analysis_dir = ANALYSIS_OUTPUT_DIR / area
        if analysis_dir.exists():
            for analysis_file in analysis_dir.glob('*_analysis.json'):
                try:
                    with open(analysis_file, 'r', encoding='utf-8') as f:
                        analysis = json.load(f)
                        research_areas[area].append(analysis)
                except Exception as e:
                    logger.error(f"Error loading analysis file {analysis_file}: {e}")
    
    # Create cross-reference report
    report_path = ANALYSIS_OUTPUT_DIR / "_cross_reference_validation.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Cross-Reference and Validation Report\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n\n")
        
        # 1. Industry Implementations vs Lab Studies
        f.write("## 1. Industry Implementations vs Lab Studies\n\n")
        for area, papers in research_areas.items():
            f.write(f"### {area}\n\n")
            industry_impl = []
            lab_studies = []
            
            for paper in papers:
                title = paper.get('title', 'N/A')
                contexts = paper.get('extracted_contexts', {})
                orgs = contexts.get('organizations_companies', [])
                techs = contexts.get('technologies_systems', [])
                
                # Check for industry implementation indicators
                has_industry = any('inc' in org.lower() or 'ltd' in org.lower() or 'corp' in org.lower() for org in orgs)
                has_commercial = any('commercial' in tech.lower() or 'deployment' in tech.lower() for tech in techs)
                
                if has_industry or has_commercial:
                    industry_impl.append(title)
                else:
                    lab_studies.append(title)
            
            f.write("#### Industry Implementations\n")
            for title in industry_impl:
                f.write(f"- {title}\n")
            f.write("\n#### Lab Studies\n")
            for title in lab_studies:
                f.write(f"- {title}\n")
            f.write("\n")
        
        # 2. Industry Standards and Commercial Products
        f.write("## 2. Industry Standards and Commercial Products\n\n")
        standards_products = {}
        for area, papers in research_areas.items():
            for paper in papers:
                title = paper.get('title', 'N/A')
                contexts = paper.get('extracted_contexts', {})
                standards = contexts.get('standards_protocols', [])
                vendors = contexts.get('commercial_solutions_vendors', [])
                
                if standards or vendors:
                    standards_products[title] = {
                        'standards': standards,
                        'vendors': vendors
                    }
        
        for title, data in standards_products.items():
            f.write(f"### {title}\n\n")
            if data['standards']:
                f.write("#### Standards/Protocols\n")
                for std in data['standards']:
                    f.write(f"- {std}\n")
            if data['vendors']:
                f.write("\n#### Commercial Products/Vendors\n")
                for vendor in data['vendors']:
                    f.write(f"- {vendor}\n")
            f.write("\n")
        
        # 3. Industry-Academia Collaborations
        f.write("## 3. Industry-Academia Collaborations\n\n")
        for area, papers in research_areas.items():
            f.write(f"### {area}\n\n")
            collaborations = []
            
            for paper in papers:
                title = paper.get('title', 'N/A')
                contexts = paper.get('extracted_contexts', {})
                orgs = contexts.get('organizations_companies', [])
                
                # Check for both academic and industry organizations
                has_university = any('university' in org.lower() or 'institute' in org.lower() for org in orgs)
                has_industry = any('inc' in org.lower() or 'ltd' in org.lower() or 'corp' in org.lower() for org in orgs)
                
                if has_university and has_industry:
                    collaborations.append(title)
            
            for title in collaborations:
                f.write(f"- {title}\n")
            f.write("\n")
    
    logger.info(f"Cross-reference validation complete. Report saved to: {report_path}")

def main():
    logger.info("Starting Targeted Query Developer Script (File Check Mode)...")
    ANALYSIS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # First run the original file check
    all_papers_to_process = []
    for research_area_dir in PHASE1_DISCOVERY_DIR.iterdir():
        if research_area_dir.is_dir():
            research_area_slug = research_area_dir.name
            logger.info(f"Scanning Phase 1 Elicit exports in: {research_area_dir.name}")
            for csv_file in research_area_dir.glob('*.csv'):
                logger.info(f"Processing Elicit export file: {csv_file.name}")
                papers_from_csv = process_elicit_csv(csv_file, research_area_slug)
                if papers_from_csv:
                    all_papers_to_process.extend(papers_from_csv)
    
    if not all_papers_to_process:
        logger.info("No papers found in Elicit exports. Exiting.")
        return

    logger.info(f"Found a total of {len(all_papers_to_process)} paper entries to check from CSVs.")

    # Track status of each paper
    paper_status = []
    missing_papers = []

    for paper_meta in all_papers_to_process:
        title = paper_meta.get('title')
        doi = paper_meta.get('doi')
        research_area_slug = paper_meta.get('research_area_slug', 'general')
        
        # Check for PDF
        pdf_dir = DOWNLOADED_PAPERS_DIR / research_area_slug
        pdf_exists = False
        if pdf_dir.exists():
            for pdf_file in pdf_dir.glob('*.pdf'):
                if clean_title_for_filename(title) in pdf_file.stem:
                    pdf_exists = True
                    break

        # Check for Markdown
        md_dir = MARKDOWN_PAPERS_DIR / research_area_slug
        md_exists = False
        if md_dir.exists():
            for md_file in md_dir.glob('*.md'):
                if clean_title_for_filename(title) in md_file.stem:
                    md_exists = True
                    break

        # Check for Analysis
        analysis_dir = ANALYSIS_OUTPUT_DIR / research_area_slug
        analysis_exists = False
        if analysis_dir.exists():
            for analysis_file in analysis_dir.glob('*_analysis.json'):
                if clean_title_for_filename(title) in analysis_file.stem:
                    analysis_exists = True
                    break

        status = {
            'title': title,
            'doi': doi,
            'research_area': research_area_slug,
            'pdf_exists': pdf_exists,
            'md_exists': md_exists,
            'analysis_exists': analysis_exists
        }
        paper_status.append(status)

        if not (pdf_exists and md_exists and analysis_exists):
            missing_papers.append(status)

    # Generate summary report
    summary_report_path = ANALYSIS_OUTPUT_DIR / "_summary_report_targeted_query_developer.md"
    with open(summary_report_path, 'w', encoding='utf-8') as f:
        f.write(f"# Targeted Query Developer - File Check Summary Report\n\n")
        f.write(f"**Date:** {datetime.now().isoformat()}\n")
        f.write(f"**Total Paper Entries from CSVs:** {len(all_papers_to_process)}\n\n")
        
        f.write("## File Status Summary\n")
        total_pdfs = sum(1 for p in paper_status if p['pdf_exists'])
        total_mds = sum(1 for p in paper_status if p['md_exists'])
        total_analyses = sum(1 for p in paper_status if p['analysis_exists'])
        f.write(f"- PDFs Found: {total_pdfs} / {len(paper_status)}\n")
        f.write(f"- Markdown Files Found: {total_mds} / {len(paper_status)}\n")
        f.write(f"- Analysis Files Found: {total_analyses} / {len(paper_status)}\n\n")

        if missing_papers:
            f.write("## Missing Files\n\n")
            f.write("| Title | DOI | Research Area | Missing Files |\n")
            f.write("|-------|-----|---------------|---------------|\n")
            for paper in missing_papers:
                missing_types = []
                if not paper['pdf_exists']: missing_types.append('PDF')
                if not paper['md_exists']: missing_types.append('Markdown')
                if not paper['analysis_exists']: missing_types.append('Analysis')
                missing_str = ', '.join(missing_types)
                title = paper['title'][:70] + ('...' if len(paper['title']) > 70 else '')
                f.write(f"| {title} | {paper['doi'] or 'N/A'} | {paper['research_area']} | {missing_str} |\n")

    logger.info(f"Script finished. Summary report at: {summary_report_path}")
    logger.info(f"Found {len(missing_papers)} papers with missing files out of {len(all_papers_to_process)} total papers.")
    
    # Now analyze missing markdown files
    analyze_missing_markdown_files()
    
    # Perform cross-referencing and validation
    perform_cross_referencing_validation()

if __name__ == "__main__":
    if arxiv is None or BeautifulSoup is None:
        logger.error("Missing critical libraries (arxiv or beautifulsoup4). Please install them.")
    else:
        main() 
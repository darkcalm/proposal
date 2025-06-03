#!/usr/bin/env python3

import json
import os
from pathlib import Path
import time
import logging
from datetime import datetime
import requests
import fitz  # PyMuPDF
from urllib.parse import urlparse, urljoin
import re
import difflib
from typing import Optional, Dict, Any
import backoff  # For retrying failed requests

class SearchResultsProcessor:
    def __init__(
        self,
        iteration: int = 1,
        base_dir: Path = None,
        output_dir: Path = None
    ):
        # Set up directories
        if base_dir is None:
            self.base_dir = Path(__file__).parent.parent / "sources" / "4.1-semantic-search"
        else:
            self.base_dir = Path(base_dir)
            
        if output_dir is None:
            self.iteration_dir = self.base_dir / f"semantic-scholar-search-iteration-{iteration}"
        else:
            self.iteration_dir = Path(output_dir)
        
        # Create directory structure
        self.papers_dir = self.iteration_dir / "semantic-scholar-review-papers"
        self.papers_dir.mkdir(parents=True, exist_ok=True)
        
        # Create logs directory
        self.logs_dir = self.iteration_dir / "logs"
        self.logs_dir.mkdir(exist_ok=True)
        
        # Set up logging
        self._setup_logging()
        
        # Set up session for requests
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })

    def _sanitize_filename(self, filename: str) -> str:
        """Sanitize filename to be valid across operating systems."""
        # Replace problematic characters with underscores
        sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # Replace multiple underscores with a single one
        sanitized = re.sub(r'_+', '_', sanitized)
        # Remove leading/trailing underscores
        sanitized = sanitized.strip('_')
        # Truncate to reasonable length (100 chars)
        sanitized = sanitized[:100]
        return sanitized

    def _setup_logging(self):
        """Configure logging with both file and console handlers"""
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # Remove any existing handlers
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        # Create formatters
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # File handler
        log_file = self.logs_dir / f'processing_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    def _resolve_doi(self, doi: str) -> Optional[str]:
        """Resolve DOI to PDF URL using various methods."""
        if not doi:
            return None
            
        # Try different DOI resolution methods
        methods = [
            self._resolve_doi_direct,
            self._resolve_doi_doi_org,
            self._resolve_doi_sci_hub
        ]
        
        for method in methods:
            try:
                url = method(doi)
                if url:
                    return url
            except Exception as e:
                logging.warning(f"DOI resolution method {method.__name__} failed: {e}")
                continue
                
        return None

    def _resolve_doi_direct(self, doi: str) -> Optional[str]:
        """Try to resolve DOI directly from publisher."""
        # Common publisher patterns
        publishers = {
            'ieee': f'https://ieeexplore.ieee.org/document/{doi}/pdf',
            'mdpi': f'https://www.mdpi.com/{doi}/pdf',
            'wiley': f'https://onlinelibrary.wiley.com/doi/pdfdirect/{doi}',
            'springer': f'https://link.springer.com/content/pdf/{doi}.pdf',
            'sciencedirect': f'https://www.sciencedirect.com/science/article/pii/{doi}/pdfft',
            'tandfonline': f'https://www.tandfonline.com/doi/pdf/{doi}',
            'acm': f'https://dl.acm.org/doi/pdf/{doi}',
            'rsc': f'https://pubs.rsc.org/en/content/articlepdf/{doi}',
            'iop': f'https://iopscience.iop.org/article/{doi}/pdf',
            'aip': f'https://aip.scitation.org/doi/pdf/{doi}',
            'aps': f'https://journals.aps.org/pr/pdf/{doi}',
            'nature': f'https://www.nature.com/articles/{doi}.pdf',
            'science': f'https://www.science.org/doi/pdf/{doi}',
            'jstor': f'https://www.jstor.org/stable/{doi}/pdf',
            'cambridge': f'https://www.cambridge.org/core/services/aop-cambridge-core/content/view/{doi}.pdf',
            'oxford': f'https://academic.oup.com/{doi}/pdf',
            'sage': f'https://journals.sagepub.com/doi/pdf/{doi}',
            'hindawi': f'https://downloads.hindawi.com/journals/{doi}.pdf',
            'frontiers': f'https://www.frontiersin.org/articles/{doi}/pdf',
            'bmc': f'https://bmc{doi}.pdf',
            'plos': f'https://journals.plos.org/plosone/article/file?id={doi}&type=printable',
            'copernicus': f'https://www.copernicus.org/articles/{doi}/pdf',
            'copernicus_esd': f'https://www.earth-syst-dynam.net/{doi}/pdf',
            'copernicus_esd_discuss': f'https://www.earth-syst-dynam-discuss.net/{doi}/pdf',
            'copernicus_esl': f'https://www.earth-syst-sci-data.net/{doi}/pdf',
            'copernicus_esl_discuss': f'https://www.earth-syst-sci-data-discuss.net/{doi}/pdf',
            'copernicus_esl_discuss_net': f'https://www.earth-syst-sci-data-discuss.net/{doi}/pdf',
            'copernicus_esl_net': f'https://www.earth-syst-sci-data.net/{doi}/pdf',
            'copernicus_esl_discuss_net_articles': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf',
            'copernicus_esl_net_articles': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf',
            'copernicus_esl_discuss_net_articles_pdf': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf',
            'copernicus_esl_net_articles_pdf': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf',
            'copernicus_esl_discuss_net_articles_pdf_version': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version={int(time.time())}',
            'copernicus_esl_net_articles_pdf_version': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version={int(time.time())}',
            'copernicus_esl_discuss_net_articles_pdf_version_1': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=1',
            'copernicus_esl_net_articles_pdf_version_1': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=1',
            'copernicus_esl_discuss_net_articles_pdf_version_2': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=2',
            'copernicus_esl_net_articles_pdf_version_2': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=2',
            'copernicus_esl_discuss_net_articles_pdf_version_3': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=3',
            'copernicus_esl_net_articles_pdf_version_3': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=3',
            'copernicus_esl_discuss_net_articles_pdf_version_4': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=4',
            'copernicus_esl_net_articles_pdf_version_4': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=4',
            'copernicus_esl_discuss_net_articles_pdf_version_5': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=5',
            'copernicus_esl_net_articles_pdf_version_5': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=5',
            'copernicus_esl_discuss_net_articles_pdf_version_6': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=6',
            'copernicus_esl_net_articles_pdf_version_6': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=6',
            'copernicus_esl_discuss_net_articles_pdf_version_7': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=7',
            'copernicus_esl_net_articles_pdf_version_7': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=7',
            'copernicus_esl_discuss_net_articles_pdf_version_8': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=8',
            'copernicus_esl_net_articles_pdf_version_8': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=8',
            'copernicus_esl_discuss_net_articles_pdf_version_9': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=9',
            'copernicus_esl_net_articles_pdf_version_9': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=9',
            'copernicus_esl_discuss_net_articles_pdf_version_10': f'https://www.earth-syst-sci-data-discuss.net/articles/{doi}/pdf?version=10',
            'copernicus_esl_net_articles_pdf_version_10': f'https://www.earth-syst-sci-data.net/articles/{doi}/pdf?version=10',
        }
        
        for publisher, url_pattern in publishers.items():
            try:
                url = url_pattern.format(doi=doi)
                response = self.session.head(url, allow_redirects=True, timeout=10)
                if response.status_code == 200 and 'application/pdf' in response.headers.get('content-type', ''):
                    return url
            except Exception as e:
                logging.debug(f"Failed to resolve DOI with {publisher}: {e}")
                continue
                
        return None

    def _resolve_doi_doi_org(self, doi: str) -> Optional[str]:
        """Try to resolve DOI through doi.org."""
        try:
            url = f'https://doi.org/{doi}'
            response = self.session.get(url, allow_redirects=True, timeout=10)
            if response.status_code == 200:
                # Check if the final URL ends with .pdf
                final_url = response.url
                if final_url.endswith('.pdf'):
                    return final_url
                # Try to find PDF link in the page
                pdf_links = re.findall(r'href=[\'"]?([^\'" >]+\.pdf)', response.text)
                if pdf_links:
                    return urljoin(final_url, pdf_links[0])
        except Exception as e:
            logging.debug(f"Failed to resolve DOI through doi.org: {e}")
        return None

    def _resolve_doi_sci_hub(self, doi: str) -> Optional[str]:
        """Try to resolve DOI through Sci-Hub."""
        try:
            # Try different Sci-Hub domains
            sci_hub_domains = [
                'https://sci-hub.se/',
                'https://sci-hub.st/',
                'https://sci-hub.ru/',
                'https://sci-hub.ee/',
                'https://sci-hub.shop/',
                'https://sci-hub.ren/',
                'https://sci-hub.wf/',
                'https://sci-hub.fun/',
                'https://sci-hub.si/',
                'https://sci-hub.shop/',
                'https://sci-hub.ren/',
                'https://sci-hub.wf/',
                'https://sci-hub.fun/',
                'https://sci-hub.si/',
                'https://sci-hub.se/',
                'https://sci-hub.st/',
                'https://sci-hub.ru/',
                'https://sci-hub.ee/',
                'https://sci-hub.shop/',
                'https://sci-hub.ren/',
                'https://sci-hub.wf/',
                'https://sci-hub.fun/',
                'https://sci-hub.si/',
            ]
            
            for domain in sci_hub_domains:
                try:
                    url = f'{domain}{doi}'
                    response = self.session.get(url, allow_redirects=True, timeout=10)
                    if response.status_code == 200:
                        # Look for PDF URL in the page
                        pdf_urls = re.findall(r'https?://[^\s<>"]+?/pdf/[^\s<>"]+?\.pdf', response.text)
                        if pdf_urls:
                            return pdf_urls[0]
                except Exception as e:
                    logging.debug(f"Failed to resolve DOI through Sci-Hub domain {domain}: {e}")
                    continue
        except Exception as e:
            logging.debug(f"Failed to resolve DOI through Sci-Hub: {e}")
        return None

    def _get_pdf_url(self, paper: Dict[str, Any]) -> Optional[str]:
        """Get PDF URL from paper data using multiple methods."""
        # Try direct PDF URL first
        pdf_url = paper.get('openAccessPdf', {}).get('url')
        if pdf_url:
            return pdf_url
            
        # Try DOI resolution
        doi = paper.get('doi')
        if doi:
            pdf_url = self._resolve_doi(doi)
            if pdf_url:
                return pdf_url
                
        # Try URL from paper
        url = paper.get('url')
        if url:
            try:
                response = self.session.get(url, allow_redirects=True, timeout=10)
                if response.status_code == 200:
                    # Look for PDF links in the page
                    pdf_links = re.findall(r'href=[\'"]?([^\'" >]+\.pdf)', response.text)
                    if pdf_links:
                        return urljoin(url, pdf_links[0])
            except Exception as e:
                logging.debug(f"Failed to get PDF URL from paper URL: {e}")
                
        return None

    @backoff.on_exception(
        backoff.expo,
        (requests.exceptions.RequestException, requests.exceptions.HTTPError),
        max_tries=3
    )
    def download_pdf(self, url: str, output_path: Path) -> bool:
        """Download PDF from URL with retry logic."""
        try:
            response = self.session.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Verify it's actually a PDF
            content_type = response.headers.get('content-type', '').lower()
            if 'application/pdf' not in content_type and not url.endswith('.pdf'):
                logging.warning(f"URL {url} does not appear to be a PDF (content-type: {content_type})")
                return False
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Error downloading PDF from {url}: {e}")
            return False

    def find_existing_paper(self, title: str) -> Path:
        """Check if a paper with similar title already exists."""
        # Normalize the title for comparison
        normalized_title = self._sanitize_filename(title.lower())
        
        # Get list of existing PDFs
        existing_files = list(self.papers_dir.glob('*.pdf'))
        
        # Check for exact match first
        for file in existing_files:
            if file.stem.lower() == normalized_title:
                return file
        
        # If no exact match, check for similarity
        for file in existing_files:
            similarity = difflib.SequenceMatcher(None, 
                file.stem.lower(), 
                normalized_title
            ).ratio()
            if similarity > 0.8:  # 80% similarity threshold
                return file
        
        return None

    def pdf_to_markdown(self, pdf_path: Path, output_path: Path) -> bool:
        """Convert PDF to markdown format."""
        markdown_content = ""
        try:
            doc = fitz.open(pdf_path)
            for page_num in range(doc.page_count):
                page = doc.load_page(page_num)
                text = page.get_text("text")
                markdown_content += f"\n\n---\n\nPage {page_num + 1}\n\n---\n\n"
                markdown_content += text
            doc.close()
        except Exception as e:
            logging.error(f"Error processing PDF {pdf_path}: {e}")
            return False

        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            logging.info(f"Successfully converted {pdf_path} to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Error writing markdown file {output_path}: {e}")
            return False

    def process_paper(self, paper: dict) -> bool:
        """Process a single paper: download PDF and convert to markdown."""
        title = paper.get('title', 'unknown')
        logging.info(f"\nProcessing paper: {title}")
        
        # Check if paper already exists
        existing_file = self.find_existing_paper(title)
        if existing_file:
            logging.info(f"Paper already exists: {existing_file.name}")
            return True
        
        # Try to get PDF URL
        pdf_url = self._get_pdf_url(paper)
        if not pdf_url:
            logging.warning(f"No PDF URL found for: {title}")
            return False
            
        # Generate filenames
        filename = self._sanitize_filename(title)
        pdf_path = self.papers_dir / f"{filename}.pdf"
        md_path = self.papers_dir / f"{filename}.md"
        
        # Download PDF
        logging.info(f"Downloading PDF: {filename}.pdf")
        if not self.download_pdf(pdf_url, pdf_path):
            return False
            
        # Convert to markdown
        logging.info(f"Converting to markdown: {filename}.md")
        if not self.pdf_to_markdown(pdf_path, md_path):
            return False
            
        return True

    def process_results(self):
        """Process all papers from semantic scholar search results."""
        consolidated_file = self.iteration_dir / "semantic_scholar_search_results.json"
        if not consolidated_file.exists():
            logging.error(f"Semantic Scholar search results file not found: {consolidated_file}")
            return
            
        try:
            with open(consolidated_file, 'r') as f:
                results = json.load(f)
        except Exception as e:
            logging.error(f"Error reading consolidated results: {e}")
            return
            
        # Track statistics
        total_papers = 0
        processed_papers = 0
        failed_papers = []
        
        # Process papers from each category
        for category in ['primary', 'secondary', 'tertiary']:
            papers = results.get(category, [])
            total_papers += len(papers)
            
            logging.info(f"\nProcessing {len(papers)} {category} papers...")
            for paper in papers:
                if self.process_paper(paper):
                    processed_papers += 1
                else:
                    failed_papers.append({
                        'title': paper.get('title', 'unknown'),
                        'category': category,
                        'url': paper.get('url', 'unknown'),
                        'doi': paper.get('doi', 'unknown')
                    })
                time.sleep(2)  # Be nice to the servers
        
        # Write processing report
        report_file = self.logs_dir / f'processing_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        with open(report_file, 'w') as f:
            f.write(f"Paper Processing Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Total papers: {total_papers}\n")
            f.write(f"Successfully processed: {processed_papers}\n")
            f.write(f"Failed to process: {len(failed_papers)}\n\n")
            
            if failed_papers:
                f.write("Failed Papers:\n")
                f.write("-" * 80 + "\n")
                for paper in failed_papers:
                    f.write(f"Title: {paper['title']}\n")
                    f.write(f"Category: {paper['category']}\n")
                    f.write(f"URL: {paper['url']}\n")
                    f.write(f"DOI: {paper['doi']}\n")
                    f.write("\n")
        
        logging.info(f"\nProcessing complete!")
        logging.info(f"Total papers: {total_papers}")
        logging.info(f"Successfully processed: {processed_papers}")
        logging.info(f"Failed to process: {len(failed_papers)}")
        logging.info(f"Report saved to: {report_file}")

def main():
    processor = SearchResultsProcessor(iteration=1)
    processor.process_results()

if __name__ == "__main__":
    main() 
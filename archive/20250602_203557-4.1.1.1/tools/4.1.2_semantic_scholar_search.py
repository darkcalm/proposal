#!/usr/bin/env python3

import requests
import json
import time
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging
from datetime import datetime
import os

class SemanticScholarSearch:
    def __init__(
        self,
        api_key: str = None,
        iteration: int = 1,
        base_dir: Optional[Path] = None,
        output_dir: Optional[Path] = None
    ):
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["x-api-key"] = api_key
        
        # Set up directories
        if base_dir is None:
            # Default to sources/4.1-semantic-search if no base_dir provided
            self.base_dir = Path(__file__).parent.parent / "sources" / "4.1-semantic-search"
        else:
            self.base_dir = Path(base_dir)
            
        if output_dir is None:
            # Default to semantic-scholar-search-iteration-{n} in base_dir
            self.iteration_dir = self.base_dir / f"semantic-scholar-search-iteration-{iteration}"
        else:
            self.iteration_dir = Path(output_dir)
        
        # Create directory structure
        self.iteration_dir.mkdir(parents=True, exist_ok=True)
        
        # Create search type directories
        for subdir in ['primary', 'secondary', 'tertiary']:
            (self.iteration_dir / subdir).mkdir(exist_ok=True)
        
        # Create logs directory
        self.logs_dir = self.iteration_dir / 'logs'
        self.logs_dir.mkdir(exist_ok=True)
        
        # Set up logging
        self._setup_logging()

    def _setup_logging(self):
        """Configure logging with both file and console handlers"""
        # Create a logger
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
        log_file = self.logs_dir / f'search_log_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # Also log to a general log file in the tools directory
        tools_log = Path(__file__).parent / 'semantic_scholar.log'
        tools_handler = logging.FileHandler(tools_log)
        tools_handler.setFormatter(formatter)
        logger.addHandler(tools_handler)

    def consolidate_results(self) -> Dict[str, Any]:
        """
        Consolidate results from all search types into a single report
        """
        consolidated = {
            'timestamp': datetime.now().isoformat(),
            'primary': [],
            'secondary': [],
            'tertiary': [],
            'summary': {
                'total_papers': 0,
                'papers_by_type': {
                    'primary': 0,
                    'secondary': 0,
                    'tertiary': 0
                }
            }
        }
        
        # Process each search type
        for search_type in ['primary', 'secondary', 'tertiary']:
            search_dir = self.iteration_dir / search_type
            for result_file in search_dir.glob('search_results_*.json'):
                try:
                    with open(result_file, 'r') as f:
                        data = json.load(f)
                        papers = data.get('data', [])
                        consolidated[search_type].extend(papers)
                        consolidated['summary']['papers_by_type'][search_type] += len(papers)
                        consolidated['summary']['total_papers'] += len(papers)
                except Exception as e:
                    logging.error(f"Error processing {result_file}: {e}")
        
        # Save consolidated results
        output_file = self.iteration_dir / 'semantic_scholar_search_results.json'
        with open(output_file, 'w') as f:
            json.dump(consolidated, f, indent=2)
        
        # Generate summary report
        summary_file = self.iteration_dir / 'search_summary.txt'
        with open(summary_file, 'w') as f:
            f.write(f"Semantic Scholar Search Summary - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Total papers found: {consolidated['summary']['total_papers']}\n")
            f.write("\nBreakdown by search type:\n")
            for search_type, count in consolidated['summary']['papers_by_type'].items():
                f.write(f"- {search_type}: {count} papers\n")
            f.write("\nDetailed results are available in semantic_scholar_search_results.json\n")
        
        logging.info(f"Semantic Scholar search results saved to {output_file}")
        logging.info(f"Summary report saved to {summary_file}")
        return consolidated

    def search_papers(
        self,
        query: str,
        search_type: str,
        limit: int = 100,
        fields: List[str] = None,
        year_range: tuple = None
    ) -> List[Dict[str, Any]]:
        """
        Search for papers using Semantic Scholar API
        
        Args:
            query: Search query string
            search_type: Type of search (primary/secondary/tertiary)
            limit: Maximum number of results to return
            fields: List of fields to return
            year_range: Tuple of (start_year, end_year)
        
        Returns:
            List of paper results
        """
        if fields is None:
            fields = [
                "title", "abstract", "year", "authors", "venue",
                "citationCount", "openAccessPdf", "url", "tldr"
            ]

        params = {
            "query": query,
            "limit": limit,
            "fields": ",".join(fields)
        }

        if year_range:
            params["year"] = f"{year_range[0]}-{year_range[1]}"

        try:
            response = requests.get(
                f"{self.base_url}/paper/search",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            results = response.json()
            
            # Save results to file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.iteration_dir / search_type / f"search_results_{timestamp}.json"
            
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            
            num_results = len(results.get('data', []))
            logging.info(f"Found {num_results} results for {search_type} search: {query[:100]}...")
            if num_results == 0:
                logging.warning(f"No results found for query: {query[:100]}...")
            
            return results.get('data', [])
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error searching papers: {e}")
            return []

    def get_paper_details(self, paper_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific paper
        
        Args:
            paper_id: Semantic Scholar paper ID
        
        Returns:
            Paper details
        """
        try:
            response = requests.get(
                f"{self.base_url}/paper/{paper_id}",
                headers=self.headers,
                params={
                    "fields": "title,abstract,year,authors,venue,citationCount,"
                             "openAccessPdf,url,tldr,references,citations"
                }
            )
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error getting paper details: {e}")
            return {}

def main():
    # Example usage with custom paths
    base_dir = Path(__file__).parent.parent / "sources" / "4.1-semantic-search"
    output_dir = base_dir / "semantic-scholar-search-iteration-1"
    
    # Initialize search with custom paths
    searcher = SemanticScholarSearch(
        iteration=1,
        base_dir=base_dir,
        output_dir=output_dir
    )
    
    # Primary search query
    primary_query = """
    How can Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
    be applied for secure, scalable, and interoperable communication in decentralized 
    predictive maintenance coordination among multi-owner Distributed Energy Resources (DERs)?
    """
    
    # Secondary search queries
    secondary_queries = [
        "What are the key requirements and challenges in adapting ACP and A2A protocols for energy sector applications?",
        "How can agent communication protocols be enhanced to ensure security and scalability in multi-owner distributed energy systems?",
        "What are the current approaches and challenges in implementing predictive maintenance coordination for distributed energy resources?",
        "How can interoperability be achieved between different types of distributed energy resources using agent communication protocols?",
        "What metrics and frameworks are used to evaluate the performance of communication protocols in distributed energy systems?"
    ]
    
    # Tertiary search queries
    tertiary_queries = [
        "Distributed Energy Resources maintenance coordination",
        "Agent Communication Protocol security",
        "Predictive maintenance in energy systems",
        "Multi-owner DER management",
        "Communication protocol performance evaluation"
    ]
    
    # Execute searches with 3-second delay between requests
    logging.info("Starting primary search...")
    primary_results = searcher.search_papers(
        primary_query,
        "primary",
        limit=100,
        year_range=(2018, 2024)
    )
    time.sleep(3)  # Rate limiting
    
    logging.info("Starting secondary searches...")
    for i, query in enumerate(secondary_queries, 1):
        logging.info(f"Executing secondary search {i}...")
        searcher.search_papers(
            query,
            "secondary",
            limit=50,
            year_range=(2018, 2024)
        )
        time.sleep(3)  # Rate limiting
    
    logging.info("Starting tertiary searches...")
    for i, query in enumerate(tertiary_queries, 1):
        logging.info(f"Executing tertiary search {i}...")
        searcher.search_papers(
            query,
            "tertiary",
            limit=30,
            year_range=(2018, 2024)
        )
        time.sleep(3)  # Rate limiting
    
    # Consolidate results
    logging.info("Consolidating results...")
    consolidated_results = searcher.consolidate_results()
    logging.info("Search complete!")

if __name__ == "__main__":
    main() 
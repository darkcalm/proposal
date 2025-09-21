#!/usr/bin/env python3

import requests
import json
import time
from pathlib import Path
import logging
from datetime import datetime
import os
import argparse
from typing import List, Dict, Any, Optional

class SemanticScholarSearch:
    def __init__(
        self,
        api_key: Optional[str] = None,
        iteration: int = 1
    ):
        self.iteration = iteration
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if api_key:
            self.headers["x-api-key"] = api_key
        
        # Determine workspace root assuming script is in tools/
        self.workspace_root = Path(__file__).resolve().parent.parent

        self.results_base_dir = self.workspace_root / "sources" / "4.1.2-semantic-scholar-results"
        self.docs_base_dir = self.workspace_root / "docs"
        
        self.results_iteration_dir = self.results_base_dir / f"iteration-{self.iteration}"
        
        # Create directory structure for results
        self.results_iteration_dir.mkdir(parents=True, exist_ok=True)
        for subdir in ['primary', 'secondary', 'tertiary']:
            (self.results_iteration_dir / subdir).mkdir(exist_ok=True)
        
        self.logs_dir = self.results_iteration_dir / 'logs'
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        # Ensure docs directory exists for summary
        self.docs_base_dir.mkdir(parents=True, exist_ok=True)
        
        self._setup_logging()

    def _setup_logging(self):
        logger = logging.getLogger()
        if logger.hasHandlers():
            logger.handlers.clear()
            
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        iteration_log_file = self.logs_dir / f'search_log_iter{self.iteration}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_handler = logging.FileHandler(iteration_log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        tools_log_dir = Path(__file__).resolve().parent # tools/
        script_log_file = tools_log_dir / '4.1.2.2_semantic_scholar.log'
        tools_file_handler = logging.FileHandler(script_log_file) # General log for this script
        tools_file_handler.setFormatter(formatter)
        logger.addHandler(tools_file_handler)

    def search_papers(
        self,
        query: str,
        search_type: str,
        limit: int = 100,
        fields: Optional[List[str]] = None,
        year_range: Optional[tuple[int, int]] = None
    ) -> List[Dict[str, Any]]:
        if fields is None:
            fields = [
                "title", "abstract", "year", "authors", "venue",
                "citationCount", "openAccessPdf", "url", "tldr", "paperId"
            ]

        params: Dict[str, Any] = {
            "query": query,
            "limit": limit,
            "fields": ",".join(fields)
        }

        if year_range and len(year_range) == 2:
            params["year"] = f"{year_range[0]}-{year_range[1]}"

        try:
            logging.info(f"Executing {search_type} search for: '{query[:100]}...' with limit {limit}")
            response = requests.get(
                f"{self.base_url}/paper/search",
                headers=self.headers,
                params=params
            )
            response.raise_for_status()
            results = response.json()
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = self.results_iteration_dir / search_type / f"search_results_{search_type}_{timestamp}.json"
            
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            
            num_results = len(results.get('data', []))
            logging.info(f"Found {num_results} results for {search_type} search. Saved to {output_file.relative_to(self.workspace_root)}")
            if num_results == 0:
                logging.warning(f"No results found for query: {query}")
            
            return results.get('data', [])
            
        except requests.exceptions.RequestException as e:
            logging.error(f"Error searching papers for query '{query}': {e}")
            if hasattr(e, 'response') and e.response is not None:
                logging.error(f"Response content: {e.response.text}")
            return []
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON response for query '{query}': {e}")
            logging.error(f"Response content: {response.text if 'response' in locals() else 'N/A'}")
            return []


    def consolidate_results(self) -> Dict[str, Any]:
        consolidated: Dict[str, Any] = {
            'metadata': {
                'iteration': self.iteration,
                'timestamp': datetime.now().isoformat(),
                'script_used': 'tools/4.1.2.2_semantic_scholar_search.py'
            },
            'summary': {
                'total_papers': 0,
                'papers_by_type': {
                    'primary': 0, 'secondary': 0, 'tertiary': 0
                },
                'unique_paper_ids': 0
            },
            'results': {
                'primary': [], 'secondary': [], 'tertiary': []
            }
        }
        
        all_paper_ids = set()

        for search_type in ['primary', 'secondary', 'tertiary']:
            search_dir = self.results_iteration_dir / search_type
            search_type_papers = []
            for result_file in sorted(search_dir.glob('search_results_*.json')): # sorted for deterministic order
                try:
                    with open(result_file, 'r') as f:
                        data = json.load(f)
                        papers = data.get('data', [])
                        search_type_papers.extend(papers)
                        for paper in papers:
                            if paper.get('paperId'):
                                all_paper_ids.add(paper['paperId'])
                except Exception as e:
                    logging.error(f"Error processing result file {result_file}: {e}")
            
            consolidated['results'][search_type] = search_type_papers
            count = len(search_type_papers)
            consolidated['summary']['papers_by_type'][search_type] = count
            consolidated['summary']['total_papers'] += count
        
        consolidated['summary']['unique_paper_ids'] = len(all_paper_ids)

        # Save consolidated JSON results
        json_output_file = self.results_iteration_dir / f'consolidated_search_results_iter{self.iteration}.json'
        with open(json_output_file, 'w') as f:
            json.dump(consolidated, f, indent=2)
        logging.info(f"Consolidated JSON results saved to {json_output_file.relative_to(self.workspace_root)}")
        
        # Generate summary report in Markdown
        md_summary_file_path = self.docs_base_dir / f"4.1.2.2-semantic-scholar-summary-iteration-{self.iteration}.md"
        json_results_md_path = json_output_file.relative_to(self.workspace_root)

        with open(md_summary_file_path, 'w') as f:
            f.write(f"# Semantic Scholar Search Summary - Iteration {self.iteration}\n\n")
            f.write(f"**Timestamp:** {consolidated['metadata']['timestamp']}\n")
            f.write(f"**Script Used:** `{consolidated['metadata']['script_used']}`\n")
            f.write(f"**Raw Consolidated JSON Results:** `{json_results_md_path}`\n")
            f.write(f"**Individual search type JSON files located in:** `{self.results_iteration_dir.relative_to(self.workspace_root)}/[primary|secondary|tertiary]/`\n\n")
            
            f.write(f"## Summary of Results\n\n")
            f.write(f"- **Total papers retrieved (sum of all searches):** {consolidated['summary']['total_papers']}\n")
            f.write(f"- **Number of unique papers (by paperId):** {consolidated['summary']['unique_paper_ids']}\n")
            f.write(f"- **Papers by search type:**\n")
            for st, count in consolidated['summary']['papers_by_type'].items():
                f.write(f"  - {st.capitalize()}: {count} papers\n")
            f.write("\n## Notes\n\n")
            f.write("This summary provides an overview of the papers retrieved using the Semantic Scholar API. "
                    "For detailed information, refer to the consolidated JSON results file and individual search type files linked above.\n")

        logging.info(f"Markdown summary report saved to {md_summary_file_path.relative_to(self.workspace_root)}")
        return consolidated

def main():
    parser = argparse.ArgumentParser(description="Run Semantic Scholar search for a given iteration.")
    parser.add_argument(
        "--iteration", 
        type=int, 
        default=1, 
        help="Search iteration number. Determines output subdirectories. Default: 1"
    )
    parser.add_argument(
        "--limit_primary", type=int, default=50, help="Limit for primary search results."
    )
    parser.add_argument(
        "--limit_secondary", type=int, default=20, help="Limit for secondary search results."
    )
    parser.add_argument(
        "--limit_tertiary", type=int, default=20, help="Limit for tertiary search results."
    )
    args = parser.parse_args()

    iteration_num = args.iteration

    # Initialize logging early to capture messages from __init__ or API key checks
    # BasicConfig for initial log before class instance if needed, but class handles it
    
    api_key = os.getenv("SEMANTIC_SCHOLAR_API_KEY")
    if not api_key:
        logging.warning("SEMANTIC_SCHOLAR_API_KEY environment variable not set. Searches may be rate-limited or fail.")
        # The script will proceed without an API key; Semantic Scholar might allow some queries.

    searcher = SemanticScholarSearch(
        api_key=api_key,
        iteration=iteration_num
    )
    logging.info(f"Semantic Scholar Search Script - Iteration {iteration_num}")
    if not api_key:
         logging.warning("Running without Semantic Scholar API key.")

    # ===== TASK 4.1.2.4: Wide range of alternative expressions for all three levels =====
    
    # PRIMARY QUERIES: Alternative expressions of the main research question
    primary_queries = [
        # Original query
        "What are the existing operational measures, key considerations, and conceptual frameworks for decentralized Distributed Energy Resource (DER) health data exchange and predictive maintenance task initiation between DER agents and maintenance provider agents?",
        
        # Focus on agent communication protocols
        "How can Agent Communication Protocol and Agent-to-Agent Protocol enable secure health data exchange and predictive maintenance coordination in decentralized Distributed Energy Resource networks?",
        
        # Focus on multi-agent systems
        "Multi-agent systems for distributed energy resource health monitoring and predictive maintenance coordination in decentralized smart grid environments",
        
        # Focus on communication frameworks
        "Communication frameworks for decentralized distributed energy resource predictive maintenance using agent-based protocols and health data exchange",
        
        # Focus on interoperability
        "Interoperable communication protocols for distributed energy resource health data exchange and automated maintenance task coordination between multiple stakeholders",
        
        # Focus on conceptual models
        "Conceptual models and operational frameworks for agent-based health data communication in distributed energy resource predictive maintenance systems"
    ]
    
    # SECONDARY QUERIES: Expanded with domain synonyms and alternative phrasings
    secondary_queries = [
        # Conceptual frameworks - multiple expressions
        "What are established conceptual frameworks for decentralized data exchange in energy systems?",
        "Architectural patterns for distributed data sharing in smart grid and renewable energy networks",
        "Design patterns for decentralized information exchange in distributed energy resource management",
        "Conceptual models for peer-to-peer data communication in energy system coordination",
        
        # Agent protocols - various phrasings
        "How is Agent-to-Agent Protocol (A2A) used for task delegation and coordination in distributed environments?",
        "Multi-agent communication protocols for task coordination and delegation in distributed systems",
        "Agent Communication Protocol applications in distributed system coordination and task management",
        "FIPA agent communication standards for distributed task coordination and workflow management",
        
        # Security and protocols - domain specific
        "What are secure protocols for decentralized health data exchange from Distributed Energy Resources (DERs)?",
        "Secure communication protocols for asset health monitoring in distributed energy systems",
        "Cybersecurity frameworks for health data transmission in smart grid distributed energy resources",
        "Privacy-preserving protocols for condition monitoring data exchange in decentralized energy networks",
        
        # Predictive maintenance - industrial focus
        "How are predictive maintenance tasks initiated in decentralized industrial systems?",
        "Automated maintenance scheduling and task initiation in distributed industrial asset management",
        "Condition-based maintenance coordination in decentralized energy asset management systems",
        "Maintenance workflow automation and task delegation in distributed energy resource networks"
    ]
    
    # TERTIARY QUERIES: Keyword combinations with broader coverage
    tertiary_queries = [
        # Core concepts - various combinations
        "conceptual model AND decentralized systems AND data exchange",
        "architectural framework AND distributed systems AND data sharing",
        "design pattern AND peer-to-peer AND information exchange",
        "conceptual design AND decentralized network AND communication",
        
        # Agent protocols - multiple standards and terms
        "Agent Communication Protocol AND FIPA AND message patterns",
        "multi-agent communication AND protocol AND coordination",
        "agent-to-agent protocol AND distributed systems AND coordination",
        "FIPA-ACL AND agent communication AND distributed coordination",
        "multi-agent systems AND communication protocol AND task delegation",
        
        # DER and health monitoring - energy domain specific
        "DER AND health data AND predictive maintenance AND agent-based",
        "distributed energy resource AND condition monitoring AND agent system",
        "renewable energy AND asset health AND multi-agent coordination",
        "smart grid AND distributed generation AND health monitoring",
        "energy asset AND condition monitoring AND distributed system",
        
        # Predictive maintenance - various expressions
        "predictive maintenance AND task initiation AND automated maintenance",
        "condition-based maintenance AND task coordination AND distributed system",
        "asset health monitoring AND maintenance scheduling AND automation",
        "predictive analytics AND maintenance coordination AND distributed network",
        "maintenance workflow AND task delegation AND distributed system",
        
        # Communication and coordination - broader terms
        "secure communication AND distributed energy AND health data",
        "interoperable protocol AND energy system AND data exchange",
        "communication framework AND smart grid AND distributed coordination",
        "message passing AND distributed energy AND coordination protocol",
        
        # Multi-owner and stakeholder focus
        "multi-stakeholder AND energy system AND communication protocol",
        "multi-owner AND distributed energy AND coordination framework",
        "stakeholder coordination AND energy asset AND communication system",
        
        # Performance and evaluation
        "protocol performance AND distributed energy AND communication evaluation",
        "communication efficiency AND smart grid AND distributed system",
        "protocol evaluation AND energy system AND performance metrics"
    ]

    # Execute PRIMARY searches with multiple query variations
    logging.info("--- Starting Primary Searches with Alternative Expressions ---")
    for i, query in enumerate(primary_queries):
        logging.info(f"Primary search {i+1}/{len(primary_queries)}")
        searcher.search_papers(query, "primary", limit=args.limit_primary)
        if i < len(primary_queries) - 1:
            logging.info("Sleeping for 3 seconds between primary queries...")
            time.sleep(3)
    
    # Execute SECONDARY searches with expanded variations
    logging.info("--- Starting Secondary Searches with Alternative Expressions ---")
    for i, query in enumerate(secondary_queries):
        logging.info(f"Secondary search {i+1}/{len(secondary_queries)}")
        searcher.search_papers(query, "secondary", limit=args.limit_secondary)
        if i < len(secondary_queries) - 1:
            logging.info("Sleeping for 3 seconds between secondary queries...")
            time.sleep(3)

    # Execute TERTIARY searches with broad keyword coverage
    logging.info("--- Starting Tertiary Searches with Alternative Expressions ---")
    for i, query in enumerate(tertiary_queries):
        logging.info(f"Tertiary search {i+1}/{len(tertiary_queries)}")
        searcher.search_papers(query, "tertiary", limit=args.limit_tertiary)
        if i < len(tertiary_queries) - 1:
            logging.info("Sleeping for 3 seconds between tertiary queries...")
            time.sleep(3)
            
    logging.info("--- Consolidating Results ---")
    searcher.consolidate_results()
    
    logging.info(f"Semantic Scholar search script for iteration {iteration_num} finished successfully.")
    logging.info(f"Total primary queries executed: {len(primary_queries)}")
    logging.info(f"Total secondary queries executed: {len(secondary_queries)}")
    logging.info(f"Total tertiary queries executed: {len(tertiary_queries)}")

if __name__ == "__main__":
    main() 
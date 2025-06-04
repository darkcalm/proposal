#!/usr/bin/env python3
"""
Download methodology papers referenced in the research proposal.
"""

import os
import json
import requests
import time
from pathlib import Path
import logging
from typing import Dict, List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
SEMANTIC_SCHOLAR_API = "https://api.semanticscholar.org/graph/v1/paper/search"
OUTPUT_DIR = Path("sources/5.3-methodology-papers")
S2_API_KEY = "0nUWTSm5ih4l1k5xXdVeL7YMYWjakdAy8F25ySsQ"

# Papers to search for with more specific queries
PAPERS = [
    {
        "title": "A systematic review of Digital Twin methodologies",
        "authors": ["Carrión", "Pastor"],
        "year": 2023,  # Recent systematic review
        "keywords": ["digital twin", "systematic review", "methodology"]
    },
    {
        "title": "Digital Twin functional requirements framework",
        "authors": ["Ma"],
        "year": 2022,  # Recent framework paper
        "keywords": ["digital twin", "functional requirements", "framework"]
    },
    {
        "title": "Situational awareness principles",
        "authors": ["Chen"],
        "year": 2021,  # Recent human factors paper
        "keywords": ["situational awareness", "human factors", "principles"]
    },
    {
        "title": "Methods for capturing informal communication patterns",
        "authors": ["Carvalho"],
        "year": 2022,  # Recent communication patterns paper
        "keywords": ["informal communication", "patterns", "methods"]
    },
    {
        "title": "Survey of agent interoperability protocols",
        "authors": ["Ehtesham"],
        "year": 2023,  # Recent survey paper
        "keywords": ["agent", "interoperability", "protocols", "survey"]
    }
]

def search_paper(query: str) -> Optional[Dict]:
    """Search for a paper using Semantic Scholar API with authentication."""
    params = {
        "query": query,
        "fields": "title,authors,url,year,openAccessPdf,abstract",
        "limit": 5  # Get more results to find the best match
    }
    headers = {
        "x-api-key": S2_API_KEY
    }
    try:
        response = requests.get(SEMANTIC_SCHOLAR_API, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data.get("data"):
            # Return the first result that has a PDF
            for paper in data["data"]:
                if paper.get("openAccessPdf", {}).get("url"):
                    return paper
        return None
    except Exception as e:
        logger.error(f"Error searching for paper: {e}")
        return None

def download_pdf(url: str, filename: str) -> bool:
    """Download a PDF file from a URL."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except Exception as e:
        logger.error(f"Error downloading PDF: {e}")
        return False

def main():
    """Main execution function."""
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Search and download each paper
    for paper in PAPERS:
        # Construct search query with more specific terms
        query = f"{paper['title']} {' '.join(paper['authors'])} {' '.join(paper['keywords'])} {paper['year']}"
        
        logger.info(f"Searching for: {query}")
        result = search_paper(query)
        
        if result:
            title = result.get('title', 'unknown')
            year = result.get('year', 'unknown')
            pdf_url = result.get('openAccessPdf', {}).get('url')
            
            if pdf_url:
                # Create filename from title
                filename = f"{title[:50]}_{year}.pdf"
                filename = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in filename)
                filename = filename.replace(' ', '_')
                filepath = OUTPUT_DIR / filename
                
                logger.info(f"Downloading: {title} ({year})")
                if download_pdf(pdf_url, str(filepath)):
                    logger.info(f"Successfully downloaded to: {filepath}")
                else:
                    logger.error(f"Failed to download: {title}")
            else:
                logger.warning(f"No PDF available for: {title}")
        else:
            logger.warning(f"No results found for: {query}")
        
        # Add delay between requests to avoid rate limiting
        time.sleep(5)

if __name__ == "__main__":
    main() 
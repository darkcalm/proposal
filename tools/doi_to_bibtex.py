#!/usr/bin/env python3
"""
Simple DOI to BibTeX converter for research proposal citations
"""

import requests
import sys
from typing import Optional

def doi_to_bibtex(doi: str) -> Optional[str]:
    """
    Convert a DOI to BibTeX format using CrossRef API
    """
    # Clean up DOI
    if doi.startswith('https://doi.org/'):
        doi = doi.replace('https://doi.org/', '')
    elif doi.startswith('doi:'):
        doi = doi.replace('doi:', '')
    
    # CrossRef API endpoint
    url = f"https://api.crossref.org/works/{doi}/transform/application/x-bibtex"
    
    headers = {
        'Accept': 'application/x-bibtex',
        'User-Agent': 'ResearchProposal/1.0 (mailto:student@university.edu)'
    }
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text.strip()
        else:
            print(f"Error fetching DOI {doi}: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Error processing DOI {doi}: {e}")
        return None

def main():
    """Main function for CLI usage"""
    if len(sys.argv) != 2:
        print("Usage: python doi_to_bibtex.py <DOI>")
        print("Example: python doi_to_bibtex.py 10.1109/ACCESS.2024.3387400")
        sys.exit(1)
    
    doi = sys.argv[1]
    bibtex = doi_to_bibtex(doi)
    
    if bibtex:
        print(bibtex)
    else:
        print(f"Failed to convert DOI: {doi}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
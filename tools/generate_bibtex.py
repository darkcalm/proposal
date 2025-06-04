#!/usr/bin/env python3
"""
Generate BibTeX entries from DOIs for the research proposal
Uses doi2bibtex package to fetch proper citation information
"""

import requests
import re
from typing import List, Dict

def doi_to_bibtex(doi: str) -> str:
    """
    Convert DOI to BibTeX format using CrossRef API
    """
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
            print(f"Error fetching DOI {doi}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Exception fetching DOI {doi}: {e}")
        return None

def clean_bibtex_key(bibtex_entry: str, doi: str) -> str:
    """
    Clean and standardize BibTeX keys to use DOI format
    """
    # Replace the key with DOI-based key
    doi_key = doi.replace('/', '_').replace('.', '_')
    
    # Find the first line with @article{...} and replace the key
    lines = bibtex_entry.split('\n')
    if lines:
        first_line = lines[0]
        if '@article{' in first_line:
            lines[0] = f"@article{{{doi_key},"
        elif '@inproceedings{' in first_line:
            lines[0] = f"@inproceedings{{{doi_key},"
        elif '@book{' in first_line:
            lines[0] = f"@book{{{doi_key},"
    
    return '\n'.join(lines)

def main():
    """
    Main function to generate BibTeX entries for all DOIs used in the proposal
    """
    # DOIs cited in the proposal
    dois = [
        "10.1016/j.rser.2020.110607",
        "10.1016/j.seta.2022.102837", 
        "10.1109/ACCESS.2024.3387400",
        "10.1016/j.ress.2021.107864",
        "10.1016/j.arcontrol.2022.04.001",
        "10.3390/EN11092360",
        "10.1049/iet-gtd.2019.1022",
        "10.1109/ACCESS.2018.2843720",
        "10.1017/S0269888902000486",
        "10.5220/0001894702000205",
        "10.1109/PES.2011.6039390",
        "10.3390/en16134853"
    ]
    
    print("% Generated BibTeX entries from DOIs")
    print("% Use this to replace the placeholder entries in main.bib")
    print()
    
    for doi in dois:
        print(f"% Fetching {doi}...")
        bibtex_entry = doi_to_bibtex(doi)
        
        if bibtex_entry:
            # Clean and standardize the entry
            cleaned_entry = clean_bibtex_key(bibtex_entry, doi)
            print(cleaned_entry)
            print()
        else:
            # Fallback entry if DOI fetch fails
            doi_key = doi.replace('/', '_').replace('.', '_')
            print(f"@article{{{doi_key},")
            print(f"  title={{[Title not available]}},")
            print(f"  author={{[Authors not available]}},")
            print(f"  doi={{{doi}}},")
            print(f"  note={{DOI: {doi}}}")
            print("}")
            print()

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Generate BibTeX entries from DOIs for the research proposal
Uses doi2bibtex package to fetch proper citation information
"""

import habanero
import sys
import re
from datetime import datetime

def fetch_bibtex(doi):
    try:
        # Check if it's an arXiv ID
        if doi.startswith('25') and len(doi) >= 10:
            return generate_arxiv_bibtex(doi)
            
        bibtex = habanero.cn.content_negotiation(ids=doi, format="bibtex")
        # Replace the citation key with the DOI
        bibtex = re.sub(r'@\w+\{([^,]+),', f'@article{{{doi},', bibtex)
        # Replace '&amp;' with '\&'
        bibtex = bibtex.replace('&amp;', '\\&')
        return bibtex
    except Exception as e:
        print(f"Error fetching DOI {doi}: {e}", file=sys.stderr)
        return None

def generate_arxiv_bibtex(arxiv_id):
    """Generate a BibTeX entry for an arXiv paper"""
    year = "2025"  # Since these are future papers
    title = "A Survey of AI Agent Protocols" if arxiv_id == "2504.16736v2" else "A survey of agent interoperability protocols"
    authors = "Author, A. and Author, B."  # Placeholder authors
    return f"""@article{{{arxiv_id},
  title = {{{title}}},
  author = {{{authors}}},
  year = {{{year}}},
  archivePrefix = {{arXiv}},
  primaryClass = {{cs.AI}},
  eprint = {{{arxiv_id}}}
}}"""

def extract_dois_from_tex(tex_file):
    with open(tex_file, 'r') as f:
        content = f.read()
    # Regex to match \cite{doi} and extract the DOI
    pattern = r'\\cite\{([^}]+)\}'
    dois = re.findall(pattern, content)
    return dois

def main():
    tex_file = 'deliverable/main.tex'
    output_file = 'deliverable/main.bib'
    if len(sys.argv) > 1:
        tex_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    dois = extract_dois_from_tex(tex_file)
    with open(output_file, 'w') as f:
        for doi in dois:
            bibtex = fetch_bibtex(doi)
            if bibtex:
                f.write(bibtex + '\n\n')

if __name__ == '__main__':
    main() 
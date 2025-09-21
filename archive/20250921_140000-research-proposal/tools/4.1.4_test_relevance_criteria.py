#!/usr/bin/env python3

import json
import os
import random
from pathlib import Path
from datetime import datetime
import logging
import re

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

def load_json_file(file_path):
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

def load_markdown_file(file_path):
    """Load a markdown file's content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        logging.error(f"Error: Markdown file not found at {file_path}")
        return None

def extract_text_from_ss_paper(paper_data):
    """Extract title, abstract, and TLDR from Semantic Scholar paper data."""
    title = paper_data.get('title', '')
    abstract = paper_data.get('abstract', '')
    tldr = paper_data.get('tldr', {}).get('text', '') if paper_data.get('tldr') else ''
    
    text_content = f"{title} {abstract} {tldr}".lower()
    return text_content

def extract_text_from_md_paper(md_content):
    """Extract text from markdown content (simple lowercase conversion)."""
    # Basic cleaning: remove markdown headers, lists, etc. for keyword matching
    text = re.sub(r'#+\s.*', '', md_content) # Remove headers
    text = re.sub(r'[-\*]\s', '', text)    # Remove list markers
    text = re.sub(r'\s+', ' ', text)         # Normalize whitespace
    return text.lower()

def score_paper(text_content, criteria):
    """Score a paper based on relevance criteria using keyword matching."""
    paper_score = 0
    dimension_scores = {}

    scoring_meta = criteria.get('scoring_methodology', {}).get('keyword_matching', {}).get('scoring', {})
    title_weight = float(scoring_meta.get('title_match', '1').replace('x weight',''))
    abstract_weight = float(scoring_meta.get('abstract_match', '1').replace('x weight',''))
    # Keyword field matching is not directly applicable here as we combine title/abstract/tldr
    
    for dim_key, dimension in criteria.get('relevance_dimensions', {}).items():
        dim_score = 0
        dim_weight = dimension.get('weight', 0)
        matched_keywords_in_dim = {}

        if 'subcriteria' in dimension:
            for sub_key, subcrit in dimension['subcriteria'].items():
                sub_score = 0
                sub_weight = subcrit.get('weight', 0)
                keywords = subcrit.get('keywords', [])
                current_matched = []

                if sub_key == 'publication_year': # Handle year scoring
                    # This is a simplified test; actual year extraction from text is complex.
                    # For this test, we'll assign a default mid-score if not explicitly found.
                    # A full implementation would parse year from metadata.
                    year_score_value = 0.5 # Default if no year logic
                    if 'scoring' in subcrit: # Check if scoring dict exists
                         # Simplified: assume current year for test, or a mid-range score
                        year_score_value = subcrit['scoring'].get("2021-2022", 0.5) # default
                    sub_score = year_score_value * sub_weight
                    if year_score_value > 0:
                         matched_keywords_in_dim[sub_key] = [f"Assumed year score: {year_score_value}"]

                elif sub_key in ['venue_quality', 'citation_count']:
                     # Simplified for testing: assign a default mid-score
                    quality_score_value = 0.5
                    sub_score = quality_score_value * sub_weight
                    if quality_score_value > 0:
                        matched_keywords_in_dim[sub_key] = [f"Assumed quality/citation score: {quality_score_value}"]
                else:
                    for kw in keywords:
                        # Basic keyword presence check
                        # Title matches get higher weight (simplified for combined text)
                        if f" {kw.lower()} " in text_content: # Check for whole word
                            sub_score += 1 
                            current_matched.append(kw)
                    
                    if current_matched:
                        # Normalize sub_score by number of keywords (max score of 1 for the subcriterion if any keyword hits)
                        # This is a simple presence based score, not frequency.
                        sub_score = (1 * sub_weight) if sub_score > 0 else 0
                        matched_keywords_in_dim[sub_key] = list(set(current_matched))
                
                dim_score += sub_score
        
        dimension_scores[dim_key] = {
            "score": round(dim_score, 3), 
            "weight": dim_weight, 
            "weighted_score": round(dim_score * dim_weight, 3),
            "matched_keywords": matched_keywords_in_dim
        }
        paper_score += dim_score * dim_weight
        
    return round(paper_score, 3), dimension_scores

def select_sample_papers(elicit_markdown_dir, ss_results_file, num_samples=3):
    """Select a small random sample of papers from Elicit and Semantic Scholar."""
    sample_papers = []
    
    # Elicit samples
    md_files = list(Path(elicit_markdown_dir).glob("*.md"))
    if md_files:
        selected_md_files = random.sample(md_files, min(num_samples, len(md_files)))
        for md_file in selected_md_files:
            sample_papers.append({"source": "elicit", "type": "markdown", "path": md_file, "title": md_file.stem})
            
    # Semantic Scholar samples
    ss_data = load_json_file(ss_results_file)
    if ss_data:
        all_ss_papers = []
        for paper_type in ['primary', 'secondary', 'tertiary']:
            all_ss_papers.extend(ss_data.get('results', {}).get(paper_type, []))
        
        if all_ss_papers:
            # Ensure unique papers by paperId if duplicates exist across types
            unique_ss_papers = {p['paperId']: p for p in all_ss_papers}.values()
            selected_ss_papers_data = random.sample(list(unique_ss_papers), min(num_samples, len(unique_ss_papers)))
            for paper_data in selected_ss_papers_data:
                sample_papers.append({"source": "semantic_scholar", "type": "json_record", "data": paper_data, "title": paper_data.get("title", "Unknown SS Title")})
                
    return sample_papers

def main():
    """Main function to test relevance criteria."""
    criteria_file = WORKSPACE_ROOT / "sources" / "4.1.3-relevance-criteria" / "relevance_criteria.json"
    elicit_markdown_dir = WORKSPACE_ROOT / "sources" / "4.1.1-elicit-results" / "elicit-papers-markdown"
    ss_results_file = WORKSPACE_ROOT / "sources" / "4.1.2-semantic-scholar-results" / "iteration-4" / "consolidated_search_results_iter4.json"
    
    output_docs_dir = WORKSPACE_ROOT / "docs"
    output_docs_dir.mkdir(parents=True, exist_ok=True)
    test_summary_file = output_docs_dir / "4.1.4-relevance-criteria-test-summary.md"

    logging.info(f"Loading relevance criteria from: {criteria_file}")
    criteria = load_json_file(criteria_file)
    if not criteria:
        return

    logging.info("Selecting sample papers for testing...")
    # Select 2 from Elicit, 3 from Semantic Scholar for a total of 5
    sample_papers = select_sample_papers(elicit_markdown_dir, ss_results_file, num_samples=3) 
    # Adjust num_samples if different Elicit/SS counts are desired. The current select_sample_papers takes one num_samples for both.
    # For specific counts (e.g. 2 Elicit, 3 SS):
    elicit_sample_count = 2
    semantic_scholar_sample_count = 3
    
    final_sample_papers = []
    md_files = list(Path(elicit_markdown_dir).glob("*.md"))
    if md_files:
        selected_md_files = random.sample(md_files, min(elicit_sample_count, len(md_files)))
        for md_file in selected_md_files:
            final_sample_papers.append({"source": "elicit", "type": "markdown", "path": md_file, "title": md_file.stem})

    ss_data = load_json_file(ss_results_file)
    if ss_data:
        all_ss_papers = []
        for paper_type in ['primary', 'secondary', 'tertiary']:
            all_ss_papers.extend(ss_data.get('results', {}).get(paper_type, []))
        
        if all_ss_papers:
            unique_ss_papers_dict = {p['paperId']: p for p in all_ss_papers}
            # Ensure we don't try to sample more than available unique papers
            actual_ss_sample_count = min(semantic_scholar_sample_count, len(unique_ss_papers_dict))
            if len(unique_ss_papers_dict) > 0 :
                 selected_ss_papers_data = random.sample(list(unique_ss_papers_dict.values()), actual_ss_sample_count)
                 for paper_data in selected_ss_papers_data:
                     final_sample_papers.append({"source": "semantic_scholar", "type": "json_record", "data": paper_data, "title": paper_data.get("title", "Unknown SS Title")})
            else:
                logging.warning("No Semantic Scholar papers found to sample.")
    
    if not final_sample_papers:
        logging.error("No sample papers selected. Exiting.")
        return
    
    logging.info(f"Selected {len(final_sample_papers)} papers for testing.")

    test_results = []
    for paper_info in final_sample_papers:
        text_content = ""
        if paper_info['type'] == 'markdown':
            md_content = load_markdown_file(paper_info['path'])
            if md_content:
                text_content = extract_text_from_md_paper(md_content)
        elif paper_info['type'] == 'json_record':
            text_content = extract_text_from_ss_paper(paper_info['data'])
        
        if not text_content:
            logging.warning(f"Could not extract text for paper: {paper_info['title']}")
            test_results.append({
                "title": paper_info['title'], 
                "source": paper_info['source'],
                "score": 0, 
                "dimension_scores": {}, 
                "error": "Failed to extract text"
            })
            continue
            
        score, dimension_scores_detail = score_paper(text_content, criteria)
        logging.info(f"Paper: {paper_info['title']} | Source: {paper_info['source']} | Score: {score}")
        test_results.append({
            "title": paper_info['title'], 
            "source": paper_info['source'],
            "score": score, 
            "dimension_scores": dimension_scores_detail
        })

    # Generate summary report
    summary_content = f"""# Task 4.1.4: Relevance Criteria Test Summary

**Test Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Criteria Used:** `sources/4.1.3-relevance-criteria/relevance_criteria.json`  
**Script Used:** `tools/4.1.4_test_relevance_criteria.py`  
**Number of Sample Papers Tested:** {len(final_sample_papers)}

## Overview

This document summarizes the results of testing the relevance criteria (developed in Task 4.1.3) against a sample of papers from Elicit.com (markdown format) and Semantic Scholar (JSON results). The goal was to perform an initial validation of the criteria's ability to distinguish relevant literature based on keyword matching and weighted dimensions.

## Sample Papers and Scores

"""
    for result in test_results:
        summary_content += f"### {result['title']} ({result['source']})\n\n"
        summary_content += f"- **Overall Score:** {result['score']}\n"
        if 'dimension_scores' in result and result['dimension_scores']:
            for dim_key, dim_data in result['dimension_scores'].items():
                dim_name = dim_key.split('_', 1)[1].replace('_', ' ').title()
                summary_content += f"  - **{dim_name}**: Score={dim_data['score']}, Weight={dim_data['weight']}, Weighted Score={dim_data['weighted_score']}\n"
                if dim_data.get('matched_keywords'):
                    for sub_crit_key, kws in dim_data['matched_keywords'].items():
                        sub_crit_name = sub_crit_key.replace('_', ' ').title()
                        summary_content += f"    - _{sub_crit_name}_: {', '.join(kws)}\n"
        elif 'error' in result:
            summary_content += f"- **Error:** {result['error']}\n"
        summary_content += "\n---\n\n"

    summary_content += f"""## Initial Assessment and Observations

**Scoring Logic:**
The current scoring is based on keyword presence within the combined text (title, abstract, TLDR for Semantic Scholar; cleaned full text for Elicit markdown).
- Year, venue quality, and citation count scoring are currently simplified for this test (default scores assigned). A full implementation would require parsing this metadata accurately.
- Keyword matches are weighted simply by presence; more advanced NLP techniques (e.g., TF-IDF, embeddings) were not used in this initial test.

**Effectiveness of Criteria:**
- (TODO: Add manual assessment here after reviewing the scores. How well do the scores align with intuitive relevance? Are keywords effective? Are weights appropriate?)
- (TODO: Identify any obvious false positives or false negatives based on the sample.)
- (TODO: Assess if the dimensions capture relevance adequately.)

**Potential Refinements based on this Test:**
- **Keyword List:** Review and expand/refine keyword lists for each subcriterion. Some important terms might be missing, or some might be too broad/narrow.
- **Weighting:** Adjust weights for dimensions and subcriteria if scores seem misaligned with perceived relevance.
- **Year/Quality Scoring:** Implement more robust parsing of publication year and potentially integrate with external APIs or local databases for venue/citation data if feasible for a more automated quality assessment.
- **Negative Keywords:** Consider adding negative keywords for exclusion if certain themes consistently lead to irrelevant results.
- **Scoring Algorithm:** Explore more sophisticated text matching or NLP techniques if basic keyword matching proves insufficient. For example, consider stemming or lemmatization.
- **Contextual Analysis:** For markdown papers, the current text extraction is basic. More advanced parsing to identify sections (abstract, introduction, conclusion) could allow for more targeted keyword application (e.g., higher weight for keywords in abstract/conclusion).

## Next Steps

1. **Manual Review of Test Results:** Thoroughly analyze the scores and matched keywords for each sample paper to assess the criteria's performance.
2. **Refine Criteria:** Based on the manual review, update `sources/4.1.3-relevance-criteria/relevance_criteria.json` (and re-run Task 4.1.3 script if structure changes significantly).
3. **Re-test (Optional):** If major changes are made to criteria, re-run this test script with the updated criteria.
4. **Proceed to Task 4.1.5:** Implement Semantic Scholar API papers storage, incorporating the refined relevance scoring.
5. **Proceed to Task 4.2.1:** Apply criteria systematically to all Elicit and Semantic Scholar papers.

This initial test provides valuable insights into the practical application of the relevance criteria and highlights areas for potential improvement before full-scale literature screening.
"""
    with open(test_summary_file, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    logging.info(f"Relevance criteria test summary saved to: {test_summary_file}")
    logging.info(f"Task 4.1.4 testing script completed. Please review the summary document and manually assess results.")

if __name__ == "__main__":
    main() 
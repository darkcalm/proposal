#!/usr/bin/env python3

import json
import os
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

def extract_text_from_ss_paper(paper_data):
    """Extract title, abstract, and TLDR from Semantic Scholar paper data for keyword matching."""
    title = paper_data.get('title', '') or ""
    abstract = paper_data.get('abstract', '') or ""
    tldr = paper_data.get('tldr', {}).get('text', '') if paper_data.get('tldr') else ""
    
    # Concatenate and lowercase for keyword search
    text_content = f"{title} {abstract} {tldr}".lower()
    return text_content

def score_paper_fuzzy(paper_data, criteria):
    """Score a paper based on relevance criteria using keyword substring matching and available metadata."""
    paper_score = 0
    dimension_scores = {}
    text_content = extract_text_from_ss_paper(paper_data)

    year = paper_data.get('year')
    citation_count = paper_data.get('citationCount', 0)

    for dim_key, dimension in criteria.get('relevance_dimensions', {}).items():
        dim_score = 0
        dim_weight = dimension.get('weight', 0)
        matched_keywords_in_dim = {}

        if 'subcriteria' in dimension:
            for sub_key, subcrit in dimension['subcriteria'].items():
                sub_item_score = 0 # Score for this specific subcriterion item
                sub_weight = subcrit.get('weight', 0)
                keywords = subcrit.get('keywords', [])
                current_matched_for_sub = []

                if sub_key == 'publication_year' and year is not None:
                    year_score_value = 0.0
                    year_scoring_rules = subcrit.get('scoring', {})
                    if year >= 2023: year_score_value = year_scoring_rules.get("2023-2024", 1.0)
                    elif year >= 2021: year_score_value = year_scoring_rules.get("2021-2022", 0.8)
                    elif year >= 2019: year_score_value = year_scoring_rules.get("2019-2020", 0.6)
                    elif year == 2018: year_score_value = year_scoring_rules.get("2018", 0.4)
                    elif year >= 2015: year_score_value = year_scoring_rules.get("2015-2017", 0.2)
                    else: year_score_value = year_scoring_rules.get("before_2015", 0.1)
                    sub_item_score = year_score_value * sub_weight
                    if year_score_value > 0:
                        matched_keywords_in_dim[sub_key] = [f"Year: {year} (Score: {year_score_value})"]
                
                elif sub_key == 'citation_count':
                    citation_score_value = 0.0
                    citation_thresholds = subcrit.get('thresholds', {})
                    if citation_count > 100: citation_score_value = 1.0 # Corresponds to 'high'
                    elif citation_count >= 20: citation_score_value = 0.6 # Corresponds to 'medium'
                    else: citation_score_value = 0.2 # Corresponds to 'low'
                    sub_item_score = citation_score_value * sub_weight
                    if citation_score_value > 0:
                         matched_keywords_in_dim[sub_key] = [f"Citations: {citation_count} (Score: {citation_score_value})"]

                elif sub_key == 'venue_quality':
                    # Simplified: actual venue quality requires external data/APIs
                    venue_score_value = 0.5 # Default placeholder score
                    sub_item_score = venue_score_value * sub_weight
                    if venue_score_value > 0:
                        matched_keywords_in_dim[sub_key] = [f"Assumed Venue Quality Score: {venue_score_value}"]
                
                else: # Keyword-based subcriteria
                    matched_this_sub = False
                    for kw in keywords:
                        # Using substring matching for basic fuzziness
                        if kw.lower() in text_content:
                            matched_this_sub = True
                            current_matched_for_sub.append(kw)
                    
                    if matched_this_sub:
                        sub_item_score = 1.0 * sub_weight # Max score for subcriterion if any keyword hits
                        matched_keywords_in_dim[sub_key] = list(set(current_matched_for_sub))
                
                dim_score += sub_item_score # Add this subcriterion's score to the dimension score
        
        dimension_scores[dim_key] = {
            "score": round(dim_score, 3), # This is the sum of weighted sub_item_scores for the dimension
            "dimension_weight": dim_weight, 
            "weighted_score": round(dim_score * dim_weight, 3),
            "matched_keywords_detail": matched_keywords_in_dim
        }
        paper_score += dim_score * dim_weight # Add weighted dimension score to total paper score
        
    return round(paper_score, 3), dimension_scores

def process_semantic_scholar_files(ss_results_dir, criteria):
    """Process all Semantic Scholar JSON files from all iterations, apply criteria, and score papers."""
    all_scored_papers = {}
    papers_processed_count = 0

    for iteration_dir in sorted(Path(ss_results_dir).iterdir()):
        if iteration_dir.is_dir() and iteration_dir.name.startswith("iteration-"):
            try:
                iteration_number = iteration_dir.name.split('-')[-1]
                consolidated_file = iteration_dir / f"consolidated_search_results_iter{iteration_number}.json"
            except IndexError:
                logging.warning(f"Could not parse iteration number from directory: {iteration_dir.name}")
                continue

            if not consolidated_file.exists():
                logging.warning(f"Consolidated file not found: {consolidated_file} in {iteration_dir}")
                # Fallback for old naming, just in case, though unlikely needed based on current creator script
                fallback_name1 = iteration_dir / f"consolidated_search_results_{iteration_dir.name.replace('-', '')}.json"
                fallback_name2 = iteration_dir / f"consolidated_search_results_{iteration_dir.name}.json"
                if fallback_name1.exists():
                    consolidated_file = fallback_name1
                    logging.info(f"Found using fallback name: {consolidated_file}")
                elif fallback_name2.exists():
                    consolidated_file = fallback_name2
                    logging.info(f"Found using fallback name: {consolidated_file}")
                else:
                    logging.warning(f"Still not found after checking fallbacks in {iteration_dir}")
                    continue
            
            logging.info(f"Processing file: {consolidated_file}")
            iteration_data = load_json_file(consolidated_file)
            if not iteration_data or 'results' not in iteration_data:
                logging.warning(f"No results found or error loading {consolidated_file}")
                continue

            for paper_type in ['primary', 'secondary', 'tertiary']:
                papers_in_type = iteration_data['results'].get(paper_type, [])
                for paper_data in papers_in_type:
                    papers_processed_count +=1
                    paper_id = paper_data.get('paperId')
                    if not paper_id:
                        logging.warning(f"Skipping paper without paperId: {paper_data.get('title', 'Unknown Title')}")
                        continue

                    # Score only if not already scored (to keep first encounter, typically from higher priority search type or earlier iter)
                    # Or, if a more complete record is found (e.g. one with abstract vs one without)
                    if paper_id not in all_scored_papers or (paper_data.get('abstract') and not all_scored_papers[paper_id].get('abstract')) :
                        score, dimension_scores_detail = score_paper_fuzzy(paper_data, criteria)
                        all_scored_papers[paper_id] = {
                            "original_data": paper_data,
                            "relevance_score": score,
                            "dimension_scores": dimension_scores_detail,
                            "source_iteration": iteration_dir.name,
                            "source_search_type": paper_type
                        }
    
    logging.info(f"Total raw paper entries processed: {papers_processed_count}")
    logging.info(f"Total unique papers scored: {len(all_scored_papers)}")
    return list(all_scored_papers.values())

def save_scored_papers(scored_papers, output_path):
    """Save the list of scored papers to a JSON file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(scored_papers, f, indent=2, ensure_ascii=False)
    logging.info(f"All scored papers saved to: {output_path}")

def generate_summary_report(scored_papers, criteria, output_path):
    """Generate a markdown summary report of the storage and scoring process."""
    
    num_papers = len(scored_papers)
    min_threshold = criteria.get('inclusion_thresholds', {}).get('minimum_score', 0.3)
    core_concept_threshold = criteria.get('inclusion_thresholds', {}).get('core_concept_requirement', 0.2)
    
    papers_meeting_min_threshold = 0
    papers_meeting_core_threshold = 0
    papers_meeting_both = 0
    
    score_distribution = {f"{i/10:.1f}-{(i+1)/10:.1f}": 0 for i in range(10)}

    for paper in scored_papers:
        score = paper['relevance_score']
        # For score distribution
        bin_idx = int(score * 10)
        if bin_idx >= 10: bin_idx = 9 # Cap at max bin for scores >= 1.0
        if bin_idx < 0: bin_idx = 0 # Cap at min bin for scores < 0
        score_distribution[f"{bin_idx/10:.1f}-{(bin_idx+1)/10:.1f}"] +=1

        dim_1_score = 0
        if paper['dimension_scores'] and '1_core_concepts' in paper['dimension_scores']:
            # The 'score' in dimension_scores is the sum of weighted sub_item_scores for that dimension
            # We need the raw sum of sub_item_scores / sum of sub_weights for that dimension to compare with core_concept_requirement
            core_concepts_dim = paper['dimension_scores']['1_core_concepts']
            # This calculation is a bit off, as 'score' is already weighted by sub-criteria weights.
            # A more accurate way would be to re-calculate the unweighted average score for the dimension if needed.
            # For now, using the stored 'score' as a proxy, assuming sub-weights sum to 1 for the dimension.
            dim_1_score = core_concepts_dim.get('score',0) 
            
        meets_min = score >= min_threshold
        meets_core = dim_1_score >= core_concept_threshold 
        # Note: The core_concept_requirement in criteria (0.2) refers to the weighted score of the dimension.
        # The current dim_1_score is the sum of (sub_criterion_score * sub_criterion_weight). To compare with 0.2 directly,
        # it should be dim_1_score * dimension_weight for 1_core_concepts.
        # Correct comparison for core concept req: paper['dimension_scores']['1_core_concepts'].get('weighted_score',0) >= core_concept_threshold
        
        # Re-evaluating meets_core based on weighted dimension score
        core_concepts_weighted_score = paper['dimension_scores'].get('1_core_concepts',{}).get('weighted_score',0)
        meets_core_corrected = core_concepts_weighted_score >= core_concept_threshold

        if meets_min:
            papers_meeting_min_threshold += 1
        if meets_core_corrected:
            papers_meeting_core_threshold +=1
        if meets_min and meets_core_corrected:
            papers_meeting_both +=1
            
    report_content = f"""# Task 4.1.5: Semantic Scholar Papers Storage and Relevance Scoring Summary

**Completion Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Script Used:** `tools/4.1.5_store_scraped_semantic_scholar_papers.py`  
**Criteria Used:** `sources/4.1.3-relevance-criteria/relevance_criteria.json`  
**Input Data:** All iterations in `sources/4.1.2-semantic-scholar-results/`  
**Output File:** `sources/4.1.5-semantic-scholar-scored-papers/all_scored_papers_iter1-4.json`

## Process Overview

1. Loaded relevance criteria.
2. Iterated through Semantic Scholar search results from all iterations (1-4).
3. For each unique paper, extracted title, abstract, TLDR, publication year, and citation count.
4. Applied relevance criteria using keyword substring matching for basic fuzziness.
5. Calculated a relevance score based on weighted dimensions, incorporating available metadata (year, citation count).
6. Stored all unique papers with their original data, relevance score, and dimension scores.

## Scoring Statistics

- **Total unique papers processed and scored:** {num_papers}
- **Minimum relevance score threshold for inclusion:** {min_threshold}
- **Core concept dimension (1_core_concepts) minimum weighted score requirement:** {core_concept_threshold}

- **Papers meeting minimum overall score threshold (>= {min_threshold}):** {papers_meeting_min_threshold}
- **Papers meeting core concept weighted score requirement (>= {core_concept_threshold}):** {papers_meeting_core_threshold}
- **Papers meeting BOTH minimum overall and core concept thresholds:** {papers_meeting_both}

### Relevance Score Distribution (Unique Papers)

| Score Range     | Paper Count |
|-----------------|-------------|
"""
    for score_range, count in score_distribution.items():
        report_content += f"| {score_range.ljust(15)} | {str(count).ljust(11)} |\n"
    
    report_content += """

## Notes and Limitations

- **Keyword Fuzziness:** Implemented basic substring matching. More advanced NLP techniques (stemming, lemmatization, embeddings) could improve accuracy but were not used.
- **Venue Quality Scoring:** This remains a simplified placeholder (default score 0.5). Accurate scoring requires external data or APIs.
- **Core Concept Requirement:** The check against `core_concept_requirement` uses the *weighted score* of the '1_core_concepts' dimension.
- **Completeness of Metadata:** Scoring relies on the availability of `year` and `citationCount` in the Semantic Scholar data. Missing data might affect scores for some papers.

## Next Steps

- **Manual Review:** Review high-scoring papers and those near thresholds to validate scoring accuracy and criteria effectiveness.
- **Refine Criteria (if needed):** Based on review, update `sources/4.1.3-relevance-criteria/relevance_criteria.json`.
- **Proceed to Task 4.2.1:** Review papers markdowns from Elicit.com and now the scored Semantic Scholar papers to apply relevance criteria more broadly.

This process provides a consolidated and scored dataset of Semantic Scholar literature, ready for further analysis and review.
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
    logging.info(f"Summary report saved to: {output_path}")

def main():
    """Main function to orchestrate the Semantic Scholar paper storage and scoring."""
    criteria_file = WORKSPACE_ROOT / "sources" / "4.1.3-relevance-criteria" / "relevance_criteria.json"
    ss_results_dir = WORKSPACE_ROOT / "sources" / "4.1.2-semantic-scholar-results"
    
    output_storage_dir = WORKSPACE_ROOT / "sources" / "4.1.5-semantic-scholar-scored-papers"
    output_storage_file = output_storage_dir / "all_scored_papers_iter1-4.json"
    
    docs_dir = WORKSPACE_ROOT / "docs"
    summary_report_file = docs_dir / "4.1.5-semantic-scholar-storage-summary.md"

    logging.info(f"Loading relevance criteria from: {criteria_file}")
    criteria = load_json_file(criteria_file)
    if not criteria:
        logging.error("Failed to load relevance criteria. Exiting.")
        return

    logging.info(f"Processing Semantic Scholar files from: {ss_results_dir}")
    scored_papers = process_semantic_scholar_files(ss_results_dir, criteria)

    if not scored_papers:
        logging.warning("No papers were scored. Check input files and criteria.")
    else:
        save_scored_papers(scored_papers, output_storage_file)
        generate_summary_report(scored_papers, criteria, summary_report_file)
        logging.info(f"Successfully processed and stored {len(scored_papers)} unique Semantic Scholar papers.")

    logging.info("Task 4.1.5 script execution finished.")

if __name__ == "__main__":
    main() 
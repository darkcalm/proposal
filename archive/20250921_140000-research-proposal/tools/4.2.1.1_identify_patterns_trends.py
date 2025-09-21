#!/usr/bin/env python3

import json
import logging
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime
import re

# --- Configuration ---
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
ANALYSIS_INPUT_DIR = WORKSPACE_ROOT / "sources" / "4.1.8-elicit-results" / "phase-2-targeted-queries" / "analysis_output"
OUTPUT_DOCS_DIR = WORKSPACE_ROOT / "docs"
OUTPUT_FILENAME = "4.2.1.1-patterns-trends-analysis.md"

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
logger = logging.getLogger(__name__)

def load_json_analysis_files(analysis_dir: Path):
    """Loads all JSON analysis files from the specified directory and its subdirectories."""
    json_files_data = []
    research_area_dirs = [d for d in analysis_dir.iterdir() if d.is_dir() and not d.name.startswith('_')]
    
    for area_dir in research_area_dirs:
        logger.info(f"Scanning analysis files in research area: {area_dir.name}")
        for json_file in area_dir.glob("*_analysis.json"):
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data['research_area'] = area_dir.name # Add research area to the data
                    # Try to extract year from title if possible, very heuristic
                    title = data.get('title', '')
                    year_match = re.search(r'(\d{4})', title) # Simple regex for a 4-digit year
                    data['year_from_title'] = year_match.group(1) if year_match else None
                    json_files_data.append(data)
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON from file: {json_file}")
            except Exception as e:
                logger.error(f"Error loading file {json_file}: {e}")
    logger.info(f"Loaded {len(json_files_data)} JSON analysis files.")
    return json_files_data

def aggregate_extracted_contexts(papers_data):
    """Aggregates all extracted terms from the 'extracted_contexts' field."""
    aggregated_counts = defaultdict(Counter)
    
    # Categories to aggregate from extracted_contexts
    # Ensure these match the keys in your JSON files
    context_categories = [
        "organizations_companies",
        "technologies_systems",
        "practical_challenges",
        "commercial_solutions_vendors",
        "standards_protocols",
        "keywords_phrases" # General keywords from Angle 6
    ]

    for paper in papers_data:
        contexts = paper.get("extracted_contexts", {})
        for category in context_categories:
            terms = contexts.get(category, [])
            # Normalize terms slightly: lowercase and strip whitespace
            normalized_terms = [term.lower().strip() for term in terms if isinstance(term, str)]
            aggregated_counts[category].update(normalized_terms)
            
    return aggregated_counts

def analyze_trends_over_time(papers_data, aggregated_counts):
    """Analyzes trends of top terms over time if year data is available."""
    # This is a placeholder for more sophisticated trend analysis.
    # Requires reliable 'year' data for each paper.
    # For now, it will just list top terms.
    # Example: Count occurrences of top N terms per year.
    
    trends_summary = defaultdict(lambda: defaultdict(int))
    # Let's pick top 5 terms from 'technologies_systems' as an example
    top_tech_terms = [term for term, count in aggregated_counts.get("technologies_systems", Counter()).most_common(5)]

    for paper in papers_data:
        year = paper.get('year_from_title') # Using heuristically extracted year
        if year:
            contexts = paper.get("extracted_contexts", {})
            tech_terms_in_paper = [term.lower().strip() for term in contexts.get("technologies_systems", [])]
            for top_term in top_tech_terms:
                if top_term in tech_terms_in_paper:
                    trends_summary[year][top_term] += 1
    
    # Convert to a more reportable format
    reportable_trends = "### Technology Mentions Over Time (Top 5 Example - Based on Year in Filename)\\n\\n"
    if not trends_summary:
        reportable_trends += "No sufficient year data found in filenames for trend analysis.\\n"
    else:
        for year in sorted(trends_summary.keys()):
            reportable_trends += f"**{year}:**\\n"
            for tech, count in trends_summary[year].items():
                reportable_trends += f"- {tech}: {count} mentions\\n"
            reportable_trends += "\\n"
    return reportable_trends


def generate_patterns_trends_report(papers_data, aggregated_counts, trends_summary_md):
    """Generates a markdown report summarizing patterns and trends."""
    report_content = f"# Patterns and Trends Analysis from Elicit Search (Angle 6)\n\n"
    report_content += f"**Date Generated:** {datetime.now().isoformat()}\n"
    report_content += f"**Source Directory:** `{ANALYSIS_INPUT_DIR}` (JSON analysis files)\n"
    report_content += f"**Script Used:** `tools/4.2.1.1_identify_patterns_trends.py`\n"
    report_content += f"**Total Papers Analyzed:** {len(papers_data)}\n\n"

    report_content += "## Methodology\n"
    report_content += "This report identifies patterns and trends by aggregating entities and keywords extracted from the JSON analysis files. These JSON files were generated from markdown versions of academic papers relevant to industry applications in DER, human factors, and AI.\n\n"
    
    report_content += "## I. High-Frequency Terms by Category\n\n"
    for category, counts in aggregated_counts.items():
        report_content += f"### Top 20 Most Common {category.replace('_', ' ').title()}:\n"
        if not counts:
            report_content += "- No data found for this category.\n"
        else:
            for term, count in counts.most_common(20):
                report_content += f"- {term} ({count} mentions)\n"
        report_content += "\n"
        
    report_content += "## II. Trends Over Time (Experimental)\n\n"
    report_content += trends_summary_md + "\n"
    
    report_content += "## III. Cross-Category Co-occurrences (Future Work)\n"
    report_content += "Further analysis could explore the co-occurrence of terms across different categories (e.g., specific technologies associated with particular challenges or organizations).\n\n"

    report_content += "## IV. Observations and Potential Insights (Preliminary)\n"
    report_content += "- (Manual interpretation based on the aggregated data will be added here after reviewing the output. For example, note any dominant technologies, recurring challenges that span multiple papers, or types of organizations most active.)\n\n"
    
    return report_content

def main():
    logger.info("Starting script to identify patterns and trends...")
    OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    
    papers_data = load_json_analysis_files(ANALYSIS_INPUT_DIR)
    if not papers_data:
        logger.warning("No JSON analysis files loaded. Exiting.")
        # Create an empty report or a report stating no data
        report_path = OUTPUT_DOCS_DIR / OUTPUT_FILENAME
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# Patterns and Trends Analysis - No Data\n\nNo JSON analysis files were found or loaded from {ANALYSIS_INPUT_DIR}.\n")
        logger.info(f"Empty report generated at {report_path}")
        return

    aggregated_counts = aggregate_extracted_contexts(papers_data)
    
    # Attempt basic trend analysis
    # Note: The 'year' extraction is very basic and might not be reliable.
    # A proper 'year' field in the JSON metadata would be much better.
    trends_summary_md = analyze_trends_over_time(papers_data, aggregated_counts)
    
    report_markdown = generate_patterns_trends_report(papers_data, aggregated_counts, trends_summary_md)
    
    report_path = OUTPUT_DOCS_DIR / OUTPUT_FILENAME
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_markdown)
        
    logger.info(f"Patterns and trends report generated at: {report_path}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Task 5.1.5: Research Emerging Methodologies (Updated)

Focus: Investigation of emerging research methodologies relevant to ACP/A2A protocol research,
       based on scanning literature and an internal knowledge base.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
         for DER predictive maintenance coordination

Based on:
- Markdown papers from specified directories.
- Internal knowledge base of emerging methodologies (adapted from archive).
- Updates docs/5.1.1-relevant-methodologies.json with findings.
"""

import json
from datetime import datetime
from pathlib import Path
import os
import re
from collections import defaultdict

# Configuration
RELEVANT_METHODOLOGIES_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.1.1-relevant-methodologies.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
LOG_FILE = Path(__file__).resolve().parent / "5.1.5_research_emerging_methodologies_updated.log"
MARKDOWN_DIRS_CONFIG = [
    {"path": Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers", "recursive": False},
    {"path": Path(__file__).resolve().parent.parent / "sources" / "4.1.8-elicit-results" / "phase-2-targeted-queries" / "markdown_papers", "recursive": True}
]
CONTEXT_SNIPPET_LENGTH = 300  # Characters around the keyword

# Internal knowledge base for Emerging Methodologies (adapted from archive/20250602_203557-4.1.1.1/tools/5.1.5_research_emerging_methodologies.py)
EMERGING_METHODOLOGIES_KB = {
    "digital_twin_methodology": {
        "name": "Digital Twin Methodology", "emergence_period": "2018-2024", "classification": "Simulation-Based Technology Methodology",
        "paradigm": "Pragmatic with strong empirical validation", "purpose": "Create digital replicas for testing, validation, and optimization of real-world systems",
        "philosophical_foundations": {"epistemology": "Empirical realism", "ontology": "Virtual-physical duality", "methodology_philosophy": "Continuous validation", "validation_approach": "Real-world calibration"},
        "application_to_acp_a2a": {"protocol_modeling": "Create digital twins of DER maintenance systems", "value_proposition": "Enables comprehensive protocol testing"},
        "strengths_for_protocol_research": ["Enables comprehensive testing", "Supports iterative development", "Risk-free experimentation"],
        "limitations_considerations": ["Significant modeling effort", "Model fidelity limitations", "High computational requirements"],
        "timeline_assessment": {"total_duration": "14-18 weeks", "feasibility_20_weeks": "Good", "technical_complexity": "High"},
        "suitability_for_acp_a2a": {"research_alignment": "High", "overall_recommendation": "Highly Recommended"}
    },
    "human_ai_collaboration_methodology": {
        "name": "Human-AI Collaboration Methodology", "emergence_period": "2020-2024", "classification": "Hybrid Intelligence Research Methodology",
        "paradigm": "Socio-technical systems approach", "purpose": "Investigate and design effective collaboration between human and artificial intelligence systems",
        "application_to_acp_a2a": {"stakeholder_involvement": "Engage DER personnel in protocol design", "value_proposition": "Ensures protocols are designed for effective human-AI collaboration"},
        "strengths_for_protocol_research": ["Ensures real-world needs met", "Builds stakeholder acceptance"],
        "limitations_considerations": ["Requires significant stakeholder coordination", "Time-intensive"],
        "timeline_assessment": {"total_duration": "12-17 weeks", "feasibility_20_weeks": "Good"},
        "suitability_for_acp_a2a": {"research_alignment": "Moderate", "overall_recommendation": "Consider for stakeholder validation"}
    },
    "ai_explainability_methodology": {
        "name": "AI Explainability and Interpretability Methodology", "emergence_period": "2019-2024", "classification": "Explainable AI Research Methodology",
        "paradigm": "Transparency and accountability in AI systems", "purpose": "Develop and evaluate methods for making AI systems transparent, interpretable, and accountable",
        "application_to_acp_a2a": {"protocol_transparency": "Develop explanations for protocol decision-making", "value_proposition": "Enhances protocol acceptance through transparency"},
        "strengths_for_protocol_research": ["Enhances transparency and trust", "Supports debugging"],
        "limitations_considerations": ["Additional system complexity", "Balancing detail with comprehensibility"],
        "timeline_assessment": {"total_duration": "12-16 weeks", "feasibility_20_weeks": "Good"},
        "suitability_for_acp_a2a": {"research_alignment": "Moderate", "overall_recommendation": "Consider as enhancement"}
    },
    "rapid_prototyping_methodology": {
        "name": "Rapid Prototyping and Iterative Development Methodology", "emergence_period": "2018-2024 (evolved)", "classification": "Agile Technology Development Methodology",
        "paradigm": "Iterative and incremental development", "purpose": "Rapidly develop, test, and refine technical solutions through continuous iteration",
        "application_to_acp_a2a": {"protocol_development": "Rapidly develop and test ACP/A2A implementations", "value_proposition": "Enables fast development and validation"},
        "strengths_for_protocol_research": ["Accelerates development cycles", "Early challenge identification", "Continuous validation"],
        "limitations_considerations": ["May sacrifice depth for speed", "Requires strong project management"],
        "timeline_assessment": {"total_duration": "Flexible - 8-20 weeks", "feasibility_20_weeks": "Excellent"},
        "suitability_for_acp_a2a": {"research_alignment": "Very High", "overall_recommendation": "Highly Recommended as development approach"}
    },
    "living_lab_methodology": {
        "name": "Living Lab Methodology", "emergence_period": "2016-2024 (evolved)", "classification": "Real-World Innovation Testing Methodology",
        "paradigm": "Open innovation in real-life environments", "purpose": "Develop and test innovations in real-world settings with active stakeholder participation",
        "application_to_acp_a2a": {"real_world_testing": "Test protocols in actual DER environments", "value_proposition": "Provides real-world validation"},
        "strengths_for_protocol_research": ["Real-world validation", "Stakeholder co-creation"],
        "limitations_considerations": ["Requires real-world access", "Complex coordination", "Timeline uncertainty"],
        "timeline_assessment": {"total_duration": "15-25 weeks", "feasibility_20_weeks": "Challenging"},
        "suitability_for_acp_a2a": {"research_alignment": "High", "overall_recommendation": "Consider for future work"}
    },
    "computational_social_science_methodology": {
        "name": "Computational Social Science Methodology", "emergence_period": "2020-2024", "classification": "Data-Driven Social Systems Analysis",
        "paradigm": "Computational analysis of social phenomena", "purpose": "Apply computational methods to understand social systems",
        "application_to_acp_a2a": {"limited_relevance": "Limited direct relevance to technical protocol research"},
        "strengths_for_protocol_research": ["Useful for analyzing adoption if social factors are key"],
        "limitations_considerations": ["Primarily social, not technical focus"],
        "timeline_assessment": {"total_duration": "12-18 weeks", "feasibility_20_weeks": "Moderate"},
        "suitability_for_acp_a2a": {"research_alignment": "Low", "overall_recommendation": "Not recommended for primary technical research"}
    }
}

EMERGING_METHODOLOGY_KEYWORDS = {
    "digital_twin_methodology": [r"digital twin", r"digital replica", r"cyber-physical system model"],
    "human_ai_collaboration_methodology": [r"human-AI collaboration", r"human-agent collaboration", r"hybrid intelligence", r"human-in-the-loop AI", r"centaur model"],
    "ai_explainability_methodology": [r"AI explainability", r"interpretable AI", r"XAI", r"explainable artificial intelligence", r"transparent AI"],
    "rapid_prototyping_methodology": [r"rapid prototyping", r"iterative development", r"agile development methodology"], # "agile development" is broad, use with care
    "living_lab_methodology": [r"living lab", r"real-world innovation testing", r"co-creation environment"],
    "computational_social_science_methodology": [r"computational social science", r"CSS", r"social data analytics"]
}

def write_log(message):
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

def load_json_file(filepath: Path) -> dict:
    if not filepath.exists():
        write_log(f"Warning: File not found at {filepath}, returning empty dict.")
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        write_log(f"Error loading or parsing {filepath}: {e}")
        return {}

def save_json_file(data: dict, filepath: Path):
    """Save data to a JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

def scan_markdown_files(markdown_dirs_config: list, methodology_keywords: dict) -> dict:
    scan_results = defaultdict(lambda: {"count": 0, "papers": set(), "contexts": []})
    processed_files = set()

    for dir_info in markdown_dirs_config:
        dir_path = dir_info["path"]
        recursive = dir_info["recursive"]
        
        if not dir_path.exists():
            write_log(f"Markdown directory not found: {dir_path}")
            continue

        glob_pattern = "**/*.md" if recursive else "*.md"
        for md_file in dir_path.glob(glob_pattern):
            if md_file in processed_files:
                continue
            processed_files.add(md_file)
            
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                for meth_key, keywords in methodology_keywords.items():
                    for keyword_pattern in keywords:
                        try:
                            # Case-insensitive search
                            for match in re.finditer(keyword_pattern, content, re.IGNORECASE):
                                scan_results[meth_key]["count"] += 1
                                scan_results[meth_key]["papers"].add(md_file.name)
                                
                                start = max(0, match.start() - CONTEXT_SNIPPET_LENGTH // 2)
                                end = min(len(content), match.end() + CONTEXT_SNIPPET_LENGTH // 2)
                                context_snippet = content[start:end].strip().replace('\n', ' ')
                                scan_results[meth_key]["contexts"].append(f"...{context_snippet}...")
                        except re.error as re_e:
                            write_log(f"Regex error for pattern '{keyword_pattern}' in {md_file.name}: {re_e}")

            except Exception as e:
                write_log(f"Error processing file {md_file.name}: {e}")

    # Convert sets to lists for JSON serialization
    for meth_key in scan_results:
        scan_results[meth_key]["papers"] = sorted(list(scan_results[meth_key]["papers"]))
        # Limit contexts to avoid excessively large JSON
        scan_results[meth_key]["contexts"] = scan_results[meth_key]["contexts"][:10] 
    return dict(scan_results)


def main():
    OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    # Initialize log file
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.1.5 (Research Emerging Methodologies - Updated) at {datetime.now().isoformat()}\n")

    print("🔬 Task 5.1.5 (Updated): Researching Emerging Methodologies from Literature")
    print("=" * 70)

    # 1. Load existing relevant methodologies (from 5.1.1)
    relevant_methodologies_data = load_json_file(RELEVANT_METHODOLOGIES_INPUT_JSON)
    if not relevant_methodologies_data: # Handle case where 5.1.1.json doesn't exist or is empty
        relevant_methodologies_data = {"identified_methodologies": {}}
        write_log(f"Initialized empty structure for {RELEVANT_METHODOLOGIES_INPUT_JSON.name} as it was not found or empty.")
    
    # Ensure 'identified_methodologies' key exists
    if "identified_methodologies" not in relevant_methodologies_data:
        relevant_methodologies_data["identified_methodologies"] = {}
    
    all_identified_methodologies = relevant_methodologies_data["identified_methodologies"]


    # 2. Scan markdown files for emerging methodology keywords
    write_log("Starting markdown scan for emerging methodologies...")
    emerging_scan_results = scan_markdown_files(MARKDOWN_DIRS_CONFIG, EMERGING_METHODOLOGY_KEYWORDS)
    write_log(f"Markdown scan complete. Found mentions for {len(emerging_scan_results)} emerging methodology types.")

    # 3. Update all_identified_methodologies (from 5.1.1.json) with emerging_scan_results
    for meth_key, scan_data in emerging_scan_results.items():
        if scan_data["count"] == 0:
            continue

        kb_entry = EMERGING_METHODOLOGIES_KB.get(meth_key)
        if not kb_entry:
            write_log(f"Warning: Scanned methodology {meth_key} not in EMERGING_METHODOLOGIES_KB. Skipping update for this key in 5.1.1.json.")
            continue

        if meth_key in all_identified_methodologies:
            # Update existing entry
            entry = all_identified_methodologies[meth_key]
            entry["count"] = entry.get("count", 0) + scan_data["count"]
            existing_papers = set(entry.get("papers", []))
            existing_papers.update(scan_data["papers"])
            entry["papers"] = sorted(list(existing_papers))
            
            existing_contexts = entry.get("contexts", [])
            existing_contexts.extend(scan_data["contexts"])
            entry["contexts"] = existing_contexts[:10] # Keep context list manageable

            original_category = entry.get("details", {}).get("category")
            if original_category and original_category.lower() not in ["general", "emerging"] and not original_category.lower().startswith("emerging/"):
                new_category = f"Emerging/{original_category}"
            else:
                new_category = "Emerging"
            if "details" not in entry: entry["details"] = {}
            entry["details"]["category"] = new_category
            entry["details"]["source"] = entry["details"].get("source", "") + "; 5.1.5_emerging_scan"

        else:
            # Add new entry for emerging methodology
            all_identified_methodologies[meth_key] = {
                "count": scan_data["count"],
                "papers": scan_data["papers"],
                "contexts": scan_data["contexts"],
                "details": {
                    "name": kb_entry.get("name", meth_key.replace("_", " ").title()),
                    "description": kb_entry.get("purpose", "N/A"),
                    "category": "Emerging",
                    "keywords_example": EMERGING_METHODOLOGY_KEYWORDS.get(meth_key, [])[:2],
                    "source": "5.1.5_emerging_scan"
                }
            }
        write_log(f"Updated/Added {meth_key} in all_identified_methodologies (5.1.1 data). New count: {all_identified_methodologies[meth_key]['count']}")

    relevant_methodologies_data["identified_methodologies"] = all_identified_methodologies
    relevant_methodologies_data["metadata"] = relevant_methodologies_data.get("metadata", {})
    relevant_methodologies_data["metadata"]["last_updated_by_task"] = "5.1.5"
    relevant_methodologies_data["metadata"]["last_updated_timestamp"] = datetime.now().isoformat()
    
    save_json_file(relevant_methodologies_data, RELEVANT_METHODOLOGIES_INPUT_JSON)
    print(f"Updated relevant methodologies in: {RELEVANT_METHODOLOGIES_INPUT_JSON}")

    # 4. Prepare data for 5.1.5-emerging-methodologies.json
    documented_emerging_methodologies = {}
    emerging_count = 0
    for kb_meth_key, kb_details in EMERGING_METHODOLOGIES_KB.items():
        current_meth_doc = kb_details.copy() # Start with full KB details
        
        # Augment with scan results if found and categorized as Emerging by this script or earlier
        scan_info_from_511 = all_identified_methodologies.get(kb_meth_key)
        
        if scan_info_from_511 and "emerging" in scan_info_from_511.get("details", {}).get("category", "").lower():
            current_meth_doc["mentions_in_current_literature"] = {
                "count": scan_info_from_511.get("count", 0),
                "papers": scan_info_from_511.get("papers", []),
                "example_contexts": scan_info_from_511.get("contexts", [])[:2] # Show first 2 contexts
            }
            emerging_count +=1
        else: # Not found in scan, or not categorized as Emerging
             current_meth_doc["mentions_in_current_literature"] = {
                "count": 0, "papers": [], "example_contexts": ["Not prominently found in the scanned literature with defined keywords."]
            }

        documented_emerging_methodologies[kb_meth_key] = current_meth_doc
        
    output_data_515 = {
        "task": "5.1.5 - Research Emerging Methodologies (Updated)",
        "timestamp": datetime.now().isoformat(),
        "literature_source_info_from_scan": [str(d["path"]) for d in MARKDOWN_DIRS_CONFIG],
        "knowledge_base_source": "Internal KB (adapted from archive)",
        "updated_central_methodology_file": str(RELEVANT_METHODOLOGIES_INPUT_JSON.name),
        "total_emerging_methodologies_in_kb": len(EMERGING_METHODOLOGIES_KB),
        "total_emerging_methodologies_found_or_confirmed_in_scan": emerging_count,
        "emerging_methodologies_details": documented_emerging_methodologies,
        "next_steps": [
            "Proceed to Task 5.2.1: Create comprehensive methodology comparison matrix",
            "Review updated 5.1.1-relevant-methodologies.json for consolidated findings"
        ]
    }

    json_file_path_515 = OUTPUT_DOCS_DIR / "5.1.5-emerging-methodologies.json"
    save_json_file(output_data_515, json_file_path_515)
    print(f"Detailed JSON analysis for emerging methodologies saved to: {json_file_path_515}")

    # 5. Generate Markdown summary (5.1.5-emerging-methodologies.md)
    md_content_parts = []
    md_content_parts.append(f"""# Emerging Methodologies Research & Scan (Task 5.1.5 - Updated)

*Generated: {output_data_515['timestamp']}*
*Scanned Literature Sources: {', '.join(output_data_515['literature_source_info_from_scan'])}*
*Knowledge Base: {output_data_515['knowledge_base_source']}*
*Central methodology list updated: `{output_data_515['updated_central_methodology_file']}`*

This document provides details for **{output_data_515['total_emerging_methodologies_in_kb']}** emerging research methodologies from the knowledge base,
augmented with findings from scanning the project's literature corpus.
**{output_data_515['total_emerging_methodologies_found_or_confirmed_in_scan']}** of these were found or confirmed in the literature scan.
""")
    if not documented_emerging_methodologies:
        md_content_parts.append("**No emerging methodologies were detailed from the KB or scan.**\n")
    else:
        for key, meth in sorted(documented_emerging_methodologies.items(), key=lambda item: item[1]['name']):
            md_content_parts.append(f"\n## {meth['name']}\n")
            md_content_parts.append(f"- **Emergence Period**: {meth.get('emergence_period', 'N/A')}\n")
            md_content_parts.append(f"- **Classification**: {meth.get('classification', 'N/A')}\n")
            md_content_parts.append(f"- **Purpose**: {meth.get('purpose', 'N/A')}\n")

            mentions = meth.get("mentions_in_current_literature")
            if mentions:
                md_content_parts.append(f"- **Mentions in Scanned Literature**: {mentions['count']}")
                if mentions['count'] > 0 and mentions['papers']:
                    papers_str = ', '.join(mentions['papers'][:2])
                    ellipsis_str = '...' if len(mentions['papers']) > 2 else ''
                    md_content_parts.append(f" (in {len(mentions['papers'])} papers: {papers_str}{ellipsis_str})\n")
                else:
                    md_content_parts.append("\n")
                if mentions['example_contexts'] and mentions['count'] > 0:
                    md_content_parts.append(f"  - *Example Context (from literature scan):* {mentions['example_contexts'][0]}\n")
            
            strengths = meth.get('strengths_for_protocol_research', [])
            if strengths:
                strengths_str = '; '.join(strengths[:2])
                ellipsis_str = '...' if len(strengths) > 2 else ''
                md_content_parts.append(f"- **Key Strengths for Protocol Research (from KB)**: {strengths_str}{ellipsis_str}\n")
            
            limitations = meth.get('limitations_considerations', [])
            if limitations:
                limitations_str = '; '.join(limitations[:2])
                ellipsis_str = '...' if len(limitations) > 2 else ''
                md_content_parts.append(f"- **Limitations/Considerations (from KB)**: {limitations_str}{ellipsis_str}\n")
            
            timeline = meth.get('timeline_assessment', {})
            if timeline.get('total_duration'):
                 md_content_parts.append(f"- **Typical Duration (from KB)**: {timeline['total_duration']} (Feasibility for 20 weeks: {timeline.get('feasibility_20_weeks', 'N/A')})\n")
            md_content_parts.append("\n")

    md_content_parts.append("\n## Next Steps\n\n")
    for step in output_data_515['next_steps']:
        md_content_parts.append(f"- {step}\n")
    md_content_parts.append("\n---\n*End of Task 5.1.5 (Updated) Report.*\n")

    md_content = "".join(md_content_parts)
    md_file_path_515 = OUTPUT_DOCS_DIR / "5.1.5-emerging-methodologies.md"
    try:
        with open(md_file_path_515, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown summary for emerging methodologies saved to: {md_file_path_515}")
        write_log(f"Markdown summary for emerging methodologies saved to {md_file_path_515}")
    except Exception as e:
        write_log(f"Error saving Markdown {md_file_path_515}: {e}")

    write_log(f"Finished Task 5.1.5 (Updated) at {datetime.now().isoformat()}")
    print("\n🎯 Task 5.1.5 (Updated) complete.")

if __name__ == "__main__":
    main() 
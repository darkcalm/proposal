#!/usr/bin/env python3
"""
Task 5.1.4: Evaluate Mixed Methodologies (Updated)

Focus: Detailed evaluation of mixed research methodologies identified as relevant.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Relevant methodologies from docs/5.1.1-relevant-methodologies.json (newly generated)
- Internal knowledge base of mixed methodologies (adapted from archive)
- Considers integration with DSR (as primary quantitative) and Case Study (as potential qualitative)
"""

import json
from datetime import datetime
from pathlib import Path
import os

# Configuration
RELEVANT_METHODOLOGIES_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.1.1-relevant-methodologies.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
LOG_FILE = Path(__file__).resolve().parent / "5.1.4_evaluate_mixed_methodologies_updated.log"

# Internal knowledge base for Mixed Methodologies
MIXED_METHODOLOGIES_KB = {
    "sequential_explanatory": { # Key matches 5.1.1 KNOWN_METHODOLOGIES
        "name": "Sequential Explanatory Mixed Methods",
        "category_in_kb": "Mixed Methods",
        "classification": "Sequential Integration Mixed Methodology",
        "paradigm": "Pragmatic with post-positivist foundations",
        "purpose": "Use quantitative data to drive and explain qualitative investigation for deeper understanding",
        "philosophical_foundations": {
            "epistemology": "Pragmatic - combines objectivist and constructivist ways of knowing",
            "methodology_philosophy": "Sequential integration - quantitative findings inform and guide qualitative exploration",
        },
        "detailed_phases": {
            "phase_1_quantitative_primary": {"description": "Primary quantitative data collection and analysis (e.g., DSR)", "timeline_weeks": "12-14"},
            "phase_2_interface_design": {"description": "Design qualitative phase based on quantitative results", "timeline_weeks": "1-2"},
            "phase_3_qualitative_explanatory": {"description": "Qualitative data collection and analysis (e.g., Case Study)", "timeline_weeks": "5-7"},
            "phase_4_integration_interpretation": {"description": "Integrate quantitative and qualitative findings", "timeline_weeks": "2-3"}
        },
        "integration_patterns": {"building_pattern": {"description": "Qualitative results explain or elaborate quantitative findings"}},
        "strengths_for_protocol_research": ["Provides comprehensive evaluation combining technical performance with contextual understanding", "Strong validation through methodological triangulation"],
        "limitations_considerations": ["Requires successful completion of quantitative phase before qualitative", "Timeline risk if quantitative phase encounters delays"],
        "application_to_acp_a2a": {"quantitative_phase": "DSR to develop and evaluate ACP/A2A adaptation framework"},
        "timeline_breakdown": {"total_duration": "20-26 weeks", "feasibility_20_weeks": "Challenging but possible"},
        "resource_requirements": {"quantitative_skills": "High", "qualitative_skills": "Moderate"}
    },
    "sequential_exploratory": {
        "name": "Sequential Exploratory Mixed Methods",
        "category_in_kb": "Mixed Methods",
        "classification": "Sequential Development Mixed Methodology",
        "paradigm": "Pragmatic with constructivist foundations",
        "purpose": "Use qualitative exploration to inform and develop quantitative investigation",
        "strengths_for_protocol_research": ["Ensures protocol design is grounded in real-world needs and contexts"],
        "limitations_considerations": ["Front-loads qualitative work which may not align with technical protocol focus"],
        "timeline_breakdown": {"total_duration": "19-25 weeks", "feasibility_20_weeks": "Requires efficient qualitative execution"}
    },
    "convergent_parallel": {
        "name": "Convergent Parallel Mixed Methods",
        "category_in_kb": "Mixed Methods",
        "classification": "Simultaneous Integration Mixed Methodology",
        "paradigm": "Pragmatic with equal quantitative/qualitative emphasis",
        "purpose": "Collect quantitative and qualitative data simultaneously to compare and integrate findings",
        "strengths_for_protocol_research": ["Provides comprehensive evaluation from multiple perspectives simultaneously", "Efficient use of research time through parallel execution"],
        "limitations_considerations": ["Complex coordination of parallel methodologies", "Resource intensive"],
        "timeline_breakdown": {"total_duration": "17-22 weeks", "feasibility_20_weeks": "Good feasibility with efficient parallel execution"}
    },
    "mixed_methods_research": { # General term, if found by 5.1.1
        "name": "Mixed Methods Research (General)",
        "category_in_kb": "Mixed Methods",
        "classification": "General Mixed Methodology Approach",
        "paradigm": "Pragmatic",
        "purpose": "Integrating quantitative and qualitative data to provide a more complete understanding of a research problem.",
        "strengths_for_protocol_research": ["Can offer triangulation of findings", "May provide richer insights than a single method alone"],
        "limitations_considerations": ["Requires expertise in both quantitative and qualitative methods", "Can be time-consuming and complex to integrate findings meaningfully"],
        "timeline_breakdown": {"total_duration": "Varies greatly depending on specific design"}
    }
}

def load_relevant_methodologies(filepath: Path) -> dict:
    if not filepath.exists():
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error: Relevant methodologies file not found at {filepath} for Task 5.1.4\n")
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("identified_methodologies", {})
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error loading or parsing {filepath} for Task 5.1.4: {e}\n")
        return {}

def main():
    """Main execution function"""
    OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.1.4 (Evaluate Mixed Methodologies - Updated) at {datetime.now().isoformat()}\n")

    print("🔄 Task 5.1.4 (Updated): Evaluating Relevant Mixed Methodologies")
    print("=" * 70)

    relevant_methodologies_from_511 = load_relevant_methodologies(RELEVANT_METHODOLOGIES_INPUT_JSON)
    if not relevant_methodologies_from_511:
        print("No relevant methodologies loaded from 5.1.1 output. Cannot proceed with 5.1.4.")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write("Aborted Task 5.1.4: No relevant methodologies from 5.1.1 output.\n")
        # Create empty output files
        output_data_empty = {
            "task": "5.1.4 - Evaluate Mixed Methodologies (Updated)", "timestamp": datetime.now().isoformat(),
            "literature_source_info_from": str(RELEVANT_METHODOLOGIES_INPUT_JSON.name),
            "total_mixed_methodologies_documented": 0, "mixed_methodologies": {},
            "next_steps": ["Proceed with caution or re-evaluate 5.1.1"]
        }
        with open(OUTPUT_DOCS_DIR / "5.1.4-mixed-methodologies.json", 'w', encoding='utf-8') as f_json:
            json.dump(output_data_empty, f_json, indent=2, ensure_ascii=False)
        with open(OUTPUT_DOCS_DIR / "5.1.4-mixed-methodologies.md", 'w', encoding='utf-8') as f_md:
            f_md.write("# Mixed Methodologies Evaluation (Task 5.1.4 - Updated)\n\nNo mixed methodologies were identified or detailed based on input from 5.1.1.\n")
        return

    documented_mixed_methodologies = {}
    count = 0
    for meth_key_from_511, meth_data_from_511 in relevant_methodologies_from_511.items():
        kb_details = MIXED_METHODOLOGIES_KB.get(meth_key_from_511)
        category_from_511 = meth_data_from_511.get("details", {}).get("category", "").lower()

        is_mixed = False
        if kb_details and kb_details.get("category_in_kb", "").lower() == "mixed methods":
            is_mixed = True
        elif "mixed" in category_from_511: # Catches "mixed methods" or "emerging/mixed methods"
            is_mixed = True
        
        if is_mixed:
            if kb_details:
                current_meth_doc = kb_details.copy()
            else: 
                details_511 = meth_data_from_511.get("details", {})
                current_meth_doc = {
                    "name": details_511.get("name", meth_key_from_511.replace("_", " ").title()),
                    "category_in_kb": "Mixed Methods (from 5.1.1 scan)",
                    "classification": "Mixed Methodology (from literature scan)",
                    "purpose": details_511.get("description", "To be further defined based on literature context."),
                    "strengths_for_protocol_research": ["Identified as relevant in literature for mixed method aspects"],
                    "limitations_considerations": ["Detailed characteristics require further research"],
                    "timeline_breakdown": {"total_duration": details_511.get("timeline_fit", "Varies")}
                }

            current_meth_doc["mentions_in_current_literature"] = {
                "count": meth_data_from_511.get("count", 0),
                "papers": meth_data_from_511.get("papers", []),
                "example_contexts": meth_data_from_511.get("contexts", [])[:2]
            }
            documented_mixed_methodologies[meth_key_from_511] = current_meth_doc
            count += 1

    output_data = {
        "task": "5.1.4 - Evaluate Mixed Methodologies (Updated)",
        "timestamp": datetime.now().isoformat(),
        "literature_source_info_from": str(RELEVANT_METHODOLOGIES_INPUT_JSON.name),
        "total_mixed_methodologies_documented": count,
        "mixed_methodologies": documented_mixed_methodologies,
        "next_steps": ["Research emerging methodologies (Task 5.1.5)", "Create comprehensive methodology comparison matrix (Task 5.2.1)"]
    }

    json_file_path = OUTPUT_DOCS_DIR / "5.1.4-mixed-methodologies.json"
    try:
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"Detailed JSON analysis saved to: {json_file_path}")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Detailed JSON for mixed methodologies saved to {json_file_path}\n")
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error saving JSON {json_file_path}: {e}\n")

    md_content = f"""# Mixed Methodologies Evaluation (Task 5.1.4 - Updated)

*Generated: {output_data['timestamp']}*
*Based on methodologies identified in: `{output_data['literature_source_info_from']}`*

This document provides detailed descriptions for the **{output_data['total_mixed_methodologies_documented']}** mixed research methodologies identified as relevant from the current literature review.

"""
    if not documented_mixed_methodologies:
        md_content += "**No mixed methodologies were identified or detailed based on the input from 5.1.1.**\n"
    else:
        for key, meth in sorted(documented_mixed_methodologies.items(), key=lambda item: item[1]['name']):
            md_content += f"\n## {meth['name']}\n"
            md_content += f"- **Classification**: {meth.get('classification', 'N/A')}\n"
            md_content += f"- **Paradigm**: {meth.get('paradigm', 'N/A')}\n"
            md_content += f"- **Purpose**: {meth.get('purpose', 'N/A')}\n"
            
            mentions = meth.get("mentions_in_current_literature")
            if mentions:
                md_content += f"- **Mentions in Current Literature**: {mentions['count']} (in {len(mentions['papers'])} papers)\n"
                if mentions['example_contexts']:
                    md_content += "  - *Example Context (from literature):* " + mentions['example_contexts'][0] + "\n"

            strengths = meth.get('strengths_for_protocol_research', [])
            if strengths:
                md_content += "- **Key Strengths for Protocol Research (from KB)**: " + "; ".join(strengths) + "\n"
            
            limitations = meth.get('limitations_considerations', [])
            if limitations:
                md_content += "- **Limitations/Considerations (from KB)**: " + "; ".join(limitations) + "\n"

            timeline_info = meth.get('timeline_breakdown', {})
            if timeline_info.get('total_duration'):
                 md_content += f"- **Typical Duration (from KB)**: {timeline_info['total_duration']}\n"
            md_content += "\n"

    md_content += "\n## Next Steps\n\n"
    for step in output_data['next_steps']:
        md_content += f"- {step}\n"
    md_content += f"\n---\n*End of Task 5.1.4 Report.*\n"

    md_file_path = OUTPUT_DOCS_DIR / "5.1.4-mixed-methodologies.md"
    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file_path}")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Markdown summary for mixed methodologies saved to {md_file_path}\n")
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error saving Markdown {md_file_path}: {e}\n")

    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Finished Task 5.1.4 (Updated) at {datetime.now().isoformat()}\n")
    print("\n🎯 Task 5.1.4 (Updated) complete.")

if __name__ == "__main__":
    main() 
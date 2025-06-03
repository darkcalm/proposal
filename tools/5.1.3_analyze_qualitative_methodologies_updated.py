#!/usr/bin/env python3
"""
Task 5.1.3: Analyze Qualitative Methodologies (Updated)

Focus: Detailed analysis of qualitative research methodologies identified as relevant.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Relevant methodologies from docs/5.1.1-relevant-methodologies.json (newly generated)
- Internal knowledge base of qualitative methodologies (adapted from archive)
"""

import json
from datetime import datetime
from pathlib import Path
import os

# Configuration
RELEVANT_METHODOLOGIES_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.1.1-relevant-methodologies.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
LOG_FILE = Path(__file__).resolve().parent / "5.1.3_analyze_qualitative_methodologies_updated.log"

# Internal knowledge base for Qualitative Methodologies
QUALITATIVE_METHODOLOGIES_KB = {
    "case_study": { # Key matches 5.1.1 KNOWN_METHODOLOGIES
        "name": "Case Study Methodology",
        "category_in_kb": "Qualitative",
        "classification": "Primary Qualitative Methodology",
        "paradigm": "Interpretivist with some positivist elements",
        "purpose": "Provide in-depth understanding of real-world phenomena within their natural context",
        "philosophical_foundations": {
            "epistemology": "Constructivist - knowledge constructed through interaction between researcher and context",
            "ontology": "Relativist - reality is context-dependent and socially constructed",
        },
        "detailed_phases": {
            "phase_1_case_selection": {"description": "Strategic selection of cases for investigation", "timeline_weeks": "2-3"},
            "phase_2_data_collection": {"description": "Collect multiple forms of evidence from selected cases", "timeline_weeks": "4-6"},
            "phase_3_within_case_analysis": {"description": "Analyze data within each individual case", "timeline_weeks": "3-4"},
            "phase_4_cross_case_analysis": {"description": "Compare patterns and insights across multiple cases", "timeline_weeks": "2-3"},
            "phase_5_theory_building": {"description": "Build theoretical understanding from case evidence", "timeline_weeks": "2-3"}
        },
        "case_study_types": {"single_case_study": {"description": "In-depth investigation of one case"}},
        "data_collection_methods": {"interviews": {"types": ["Structured", "Semi-structured"]}},
        "analytical_techniques": {"pattern_matching": {"description": "Compare observed patterns with predicted patterns"}},
        "strengths_for_protocol_research": ["Provides real-world context for protocol usage and adaptation", "Captures stakeholder perspectives"],
        "limitations_considerations": ["Limited generalizability to other contexts", "Potential for researcher bias"],
        "application_to_acp_a2a": {"case_selection": "Select 1-2 DER organizations actively using communication protocols"},
        "timeline_breakdown": {"total_duration": "13-19 weeks"},
        "quality_criteria": {"construct_validity": "Use multiple sources of evidence"}
    },
    "grounded_theory": {
        "name": "Grounded Theory Methodology",
        "category_in_kb": "Qualitative",
        "classification": "Theory-Building Qualitative Methodology",
        "paradigm": "Interpretivist with systematic analytical procedures",
        "purpose": "Generate theory grounded in systematically collected and analyzed data",
        "strengths_for_protocol_research": ["Generates novel theoretical insights about protocol adaptation"],
        "limitations_considerations": ["Extremely time-intensive", "May not align well with technical protocol research objectives"],
        "timeline_breakdown": {"total_duration": "16-21 weeks"}
    },
    "phenomenological_research": {
        "name": "Phenomenological Research Methodology",
        "category_in_kb": "Qualitative",
        "classification": "Experience-Focused Qualitative Methodology",
        "paradigm": "Phenomenological/Interpretivist",
        "purpose": "Understand the lived experiences and meanings of phenomena from participants' perspectives",
        "strengths_for_protocol_research": ["Provides deep understanding of user experiences with protocols"],
        "limitations_considerations": ["Not appropriate for technical protocol research objectives", "Limited direct applicability to protocol design"],
        "timeline_breakdown": {"total_duration": "10-15 weeks"}
    },
    "ethnography": {
        "name": "Ethnography",
        "category_in_kb": "Qualitative",
        "classification": "Cultural Immersion Methodology",
        "paradigm": "Interpretivist/Constructivist",
        "purpose": "Studying people in their own environment to understand their culture, behaviors, and social structures.",
        "strengths_for_protocol_research": ["Rich contextual understanding of protocol use in situ", "Can uncover tacit knowledge and informal practices"],
        "limitations_considerations": ["Typically long-term and immersive, challenging for short thesis", "Observer bias potential"],
        "timeline_breakdown": {"total_duration": "Often 6+ months, can be adapted for shorter exploratory studies"}
    },
    "action_research": {
        "name": "Action Research Methodology",
        "category_in_kb": "Qualitative", # Can be mixed but often strong qualitative component
        "classification": "Participatory Problem-Solving Methodology",
        "paradigm": "Pragmatic/Critical",
        "purpose": "Methodology involving stakeholders in identifying problems and developing solutions collaboratively.",
        "strengths_for_protocol_research": ["High practical relevance and stakeholder buy-in", "Iterative improvement cycles"],
        "limitations_considerations": ["Requires significant stakeholder commitment and time", "Can be difficult to control scope"],
        "timeline_breakdown": {"total_duration": "Variable, often long-term (16-24 weeks for a cycle)"}
    },
    "narrative_inquiry": {
        "name": "Narrative Inquiry",
        "category_in_kb": "Qualitative",
        "classification": "Story-based Interpretive Methodology",
        "paradigm": "Constructivist/Interpretivist",
        "purpose": "Research that examines experience through the stories people tell.",
        "strengths_for_protocol_research": ["Rich insights into individual experiences and perspectives on protocol use"],
        "limitations_considerations": ["Highly subjective, generalizability is limited", "May not directly address technical performance"],
        "timeline_breakdown": {"total_duration": "Moderate to Long, depends on depth of narrative collection"}
    },
    "content_analysis": {
        "name": "Content Analysis (Qualitative)", 
        "category_in_kb": "Qualitative",
        "classification": "Textual Analysis Methodology",
        "paradigm": "Interpretivist (when qualitative)",
        "purpose": "Systematically analyzing the content of communications to identify patterns, themes, biases, and meanings.",
        "strengths_for_protocol_research": ["Useful for analyzing protocol documentation, communication logs, or stakeholder feedback"],
        "limitations_considerations": ["Interpretation can be subjective if not rigorously applied", "Limited to available textual data"],
        "timeline_breakdown": {"total_duration": "Good, can be efficient depending on data volume"}
    },
    "thematic_analysis": {
        "name": "Thematic Analysis", 
        "category_in_kb": "Qualitative",
        "classification": "Pattern Identification Methodology",
        "paradigm": "Interpretivist/Constructivist",
        "purpose": "Identifying, analyzing, and reporting patterns (themes) within qualitative data.",
        "strengths_for_protocol_research": ["Flexible approach applicable to various qualitative data sources (interviews, case studies)", "Useful for understanding stakeholder needs related to protocols"],
        "limitations_considerations": ["Requires careful theme development to avoid subjectivity", "Can be time-consuming with large datasets"],
        "timeline_breakdown": {"total_duration": "Good, adaptable to project scope"}
    }
    # Note: survey_research_qual, discourse_analysis, historical_research, hermeneutics from 5.1.1 KNOWN_METHODOLOGIES
    # are not included here as this KB is focused on the primary methodologies from the archived script 5.1.3.
    # The script will pick them up if 5.1.1 identified them as qualitative.
}

def load_relevant_methodologies(filepath: Path) -> dict:
    if not filepath.exists():
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error: Relevant methodologies file not found at {filepath} for Task 5.1.3\n")
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data.get("identified_methodologies", {})
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error loading or parsing {filepath} for Task 5.1.3: {e}\n")
        return {}

def main():
    """Main execution function"""
    OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.1.3 (Analyze Qualitative Methodologies - Updated) at {datetime.now().isoformat()}\n")

    print("🔍 Task 5.1.3 (Updated): Analyzing Relevant Qualitative Methodologies")
    print("=" * 70)

    relevant_methodologies_from_511 = load_relevant_methodologies(RELEVANT_METHODOLOGIES_INPUT_JSON)
    if not relevant_methodologies_from_511:
        print("No relevant methodologies loaded from 5.1.1 output. Cannot proceed with 5.1.3.")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write("Aborted Task 5.1.3: No relevant methodologies from 5.1.1 output.\n")
        # Create empty output files
        output_data_empty = {
            "task": "5.1.3 - Analyze Qualitative Methodologies (Updated)", "timestamp": datetime.now().isoformat(),
            "literature_source_info_from": str(RELEVANT_METHODOLOGIES_INPUT_JSON.name),
            "total_qualitative_methodologies_documented": 0, "qualitative_methodologies": {},
            "next_steps": ["Proceed with caution or re-evaluate 5.1.1"]
        }
        with open(OUTPUT_DOCS_DIR / "5.1.3-qualitative-methodologies.json", 'w', encoding='utf-8') as f_json:
            json.dump(output_data_empty, f_json, indent=2, ensure_ascii=False)
        with open(OUTPUT_DOCS_DIR / "5.1.3-qualitative-methodologies.md", 'w', encoding='utf-8') as f_md:
            f_md.write("# Qualitative Methodologies Analysis (Task 5.1.3 - Updated)\n\nNo qualitative methodologies were identified or detailed based on input from 5.1.1.\n")
        return

    documented_qualitative_methodologies = {}
    count = 0
    for meth_key_from_511, meth_data_from_511 in relevant_methodologies_from_511.items():
        kb_details = QUALITATIVE_METHODOLOGIES_KB.get(meth_key_from_511)
        category_from_511 = meth_data_from_511.get("details", {}).get("category", "").lower()

        is_qualitative = False
        if kb_details and kb_details.get("category_in_kb", "").lower() == "qualitative":
            is_qualitative = True
        elif "qualitative" in category_from_511: # Catches general "qualitative" or "emerging/qualitative"
            is_qualitative = True
        
        if is_qualitative:
            if kb_details:
                current_meth_doc = kb_details.copy()
            else: # Not in rich KB but identified as qualitative by 5.1.1
                details_511 = meth_data_from_511.get("details", {})
                current_meth_doc = {
                    "name": details_511.get("name", meth_key_from_511.replace("_", " ").title()),
                    "category_in_kb": "Qualitative (from 5.1.1 scan)",
                    "classification": "Qualitative Methodology (from literature scan)",
                    "purpose": details_511.get("description", "To be further defined based on literature context."),
                    "strengths_for_protocol_research": ["Identified as relevant in literature for qualitative aspects"],
                    "limitations_considerations": ["Detailed characteristics require further research"],
                    "timeline_breakdown": {"total_duration": details_511.get("timeline_fit", "Varies")}
                }

            current_meth_doc["mentions_in_current_literature"] = {
                "count": meth_data_from_511.get("count", 0),
                "papers": meth_data_from_511.get("papers", []),
                "example_contexts": meth_data_from_511.get("contexts", [])[:2]
            }
            documented_qualitative_methodologies[meth_key_from_511] = current_meth_doc
            count += 1

    output_data = {
        "task": "5.1.3 - Analyze Qualitative Methodologies (Updated)",
        "timestamp": datetime.now().isoformat(),
        "literature_source_info_from": str(RELEVANT_METHODOLOGIES_INPUT_JSON.name),
        "total_qualitative_methodologies_documented": count,
        "qualitative_methodologies": documented_qualitative_methodologies,
        "next_steps": [
            "Evaluate mixed methodologies (Task 5.1.4)",
            "Research emerging methodologies (Task 5.1.5)"
        ]
    }

    json_file_path = OUTPUT_DOCS_DIR / "5.1.3-qualitative-methodologies.json"
    try:
        with open(json_file_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"Detailed JSON analysis saved to: {json_file_path}")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Detailed JSON for qualitative methodologies saved to {json_file_path}\n")
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error saving JSON {json_file_path}: {e}\n")

    md_content = f"""# Qualitative Methodologies Analysis (Task 5.1.3 - Updated)

*Generated: {output_data['timestamp']}*
*Based on methodologies identified in: `{output_data['literature_source_info_from']}`*

This document provides detailed descriptions for the **{output_data['total_qualitative_methodologies_documented']}** qualitative research methodologies identified as relevant from the current literature review.

"""
    if not documented_qualitative_methodologies:
        md_content += "**No qualitative methodologies were identified or detailed based on the input from 5.1.1.**\n"
    else:
        for key, meth in sorted(documented_qualitative_methodologies.items(), key=lambda item: item[1]['name']):
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

            if "detailed_phases" in meth and meth["detailed_phases"]:
                md_content += "- **Key Phases (from KB)**:\n"
                for phase_key, phase_data in list(meth["detailed_phases"].items())[:2]: 
                    md_content += f"  - *{phase_data.get('description', phase_key)}:* (Timeline: {phase_data.get('timeline_weeks','N/A')} weeks)\n"
            md_content += "\n"

    md_content += "\n## Next Steps\n\n"
    for step in output_data['next_steps']:
        md_content += f"- {step}\n"
    md_content += f"\n---\n*End of Task 5.1.3 Report.*\n"

    md_file_path = OUTPUT_DOCS_DIR / "5.1.3-qualitative-methodologies.md"
    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file_path}")
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Markdown summary for qualitative methodologies saved to {md_file_path}\n")
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error saving Markdown {md_file_path}: {e}\n")

    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Finished Task 5.1.3 (Updated) at {datetime.now().isoformat()}\n")
    print("\n🎯 Task 5.1.3 (Updated) complete.")

if __name__ == "__main__":
    main() 
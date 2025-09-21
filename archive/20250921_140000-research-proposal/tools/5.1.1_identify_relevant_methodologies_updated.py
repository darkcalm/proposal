#!/usr/bin/env python3
"""
Task 5.1.1: Identify Relevant Research Methodologies (Updated)

Focus: Research METHODOLOGIES (overarching approaches) not methods (specific tools)
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Analysis of current literature in sources/4.3.1-elicit-results/markdown_papers/
- Internal knowledge base of research methodologies
- Research direction from docs/3.1.2-research-direction-selection.md (implicitly, by focusing on relevant methodology types)
"""

import json
from datetime import datetime
import os
from pathlib import Path
import re
from collections import defaultdict

# Configuration
# Path to the directory containing markdown paper files, relative to the script's location (tools/)
CURRENT_LITERATURE_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
# Path to the output directory for documents, relative to the script's location (tools/)
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
# Path to the output directory for source files (if any), relative to the script's location (tools/)
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.1.1_identify_relevant_methodologies_updated.log"


# Internal knowledge base of methodologies (condensed from the original archived script)
# This defines what we *know* about various methodologies.
# The script will then check which of these are mentioned in the current literature.
KNOWN_METHODOLOGIES = {
    "design_science_research": {
        "name": "Design Science Research (DSR)", "category": "Quantitative",
        "keywords": ["design science research", "DSR", "design science methodology", "artifact development", "constructive research"],
        "description": "Methodology for designing and evaluating artifacts (protocols, frameworks, systems) to solve identified problems.",
        "suitability_for_protocols": "Very High", "timeline_fit": "Excellent (12-16 weeks)"
    },
    "experimental_research": {
        "name": "Experimental Research Methodology", "category": "Quantitative",
        "keywords": ["experimental research", "experimental methodology", "experiment", "controlled experiment", "experimental design"],
        "description": "Methodology based on controlled experiments to test hypotheses about protocol performance.",
        "suitability_for_protocols": "High", "timeline_fit": "Good (8-12 weeks)"
    },
    "comparative_research": {
        "name": "Comparative Research Methodology", "category": "Quantitative",
        "keywords": ["comparative research", "comparative study", "comparative analysis", "benchmarking study"],
        "description": "Methodology for systematic comparison of different approaches, protocols, or solutions.",
        "suitability_for_protocols": "High", "timeline_fit": "Excellent (6-10 weeks)"
    },
    "case_study": {
        "name": "Case Study Methodology", "category": "Qualitative",
        "keywords": ["case study", "case study methodology", "case study research", "multiple case study", "single case study"],
        "description": "Methodology for in-depth investigation of real-world contexts and applications.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Moderate (10-16 weeks)"
    },
    "grounded_theory": {
        "name": "Grounded Theory Methodology", "category": "Qualitative",
        "keywords": ["grounded theory", "grounded theory methodology"],
        "description": "Methodology for building theory from systematic data collection and analysis.",
        "suitability_for_protocols": "Low", "timeline_fit": "Poor (16-24 weeks)"
    },
    "phenomenological_research": {
        "name": "Phenomenological Research Methodology", "category": "Qualitative",
        "keywords": ["phenomenological", "phenomenological research"],
        "description": "Methodology for understanding lived experiences and meanings.",
        "suitability_for_protocols": "Very Low", "timeline_fit": "Poor"
    },
    "sequential_explanatory": {
        "name": "Sequential Explanatory Mixed Methods", "category": "Mixed Methods",
        "keywords": ["sequential explanatory"], # Note: "mixed methods" is broad, specific design names are better
        "description": "Methodology using quantitative phase followed by qualitative phase for explanation.",
        "suitability_for_protocols": "High", "timeline_fit": "Moderate (14-18 weeks)"
    },
    "sequential_exploratory": {
        "name": "Sequential Exploratory Mixed Methods", "category": "Mixed Methods",
        "keywords": ["sequential exploratory"],
        "description": "Methodology using qualitative exploration followed by quantitative validation.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Moderate (14-18 weeks)"
    },
    "convergent_parallel": {
        "name": "Convergent Parallel Mixed Methods", "category": "Mixed Methods",
        "keywords": ["convergent parallel", "convergent design"],
        "description": "Methodology collecting quantitative and qualitative data simultaneously for triangulation.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Good (12-16 weeks)"
    },
     "mixed_methods_research": { # General term
        "name": "Mixed Methods Research", "category": "Mixed Methods",
        "keywords": ["mixed methods", "mixed methodology"],
        "description": "General approach combining quantitative and qualitative techniques.",
        "suitability_for_protocols": "Moderate to High (depends on specific design)", "timeline_fit": "Varies"
    },
    "action_research": {
        "name": "Action Research Methodology", "category": "Specialized/Qualitative",
        "keywords": ["action research", "participatory action research"],
        "description": "Methodology involving stakeholders in identifying problems and developing solutions.",
        "suitability_for_protocols": "Low", "timeline_fit": "Poor (16-24 weeks)"
    },
    "delphi_methodology": {
        "name": "Delphi Methodology", "category": "Specialized",
        "keywords": ["delphi method", "delphi technique", "delphi study"],
        "description": "Methodology for achieving expert consensus through iterative rounds.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Moderate (8-12 weeks)"
    },
    "systematic_literature_review": {
        "name": "Systematic Literature Review Methodology", "category": "Specialized",
        "keywords": ["systematic review", "systematic literature review", "meta-analysis", "scoping review"], # Added meta-analysis & scoping review
        "description": "Methodology for systematically reviewing and synthesizing existing research.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Good (8-12 weeks for focused review)"
    },
    # From archive script's `methodology_keywords` which were more granular / method-like
    "simulation_modeling": {
        "name": "Simulation Modeling", "category": "Quantitative/Emerging", # Can be seen as a method within DSR or Experimental, or an emerging methodology itself
        "keywords": ["simulation", "simulation modeling", "simulation study", "computer simulation", "modeling and simulation", "discrete event simulation"],
        "description": "Using computer models to imitate real-world systems or processes.",
        "suitability_for_protocols": "Very High", "timeline_fit": "Good (part of larger methodology)"
    },
    "digital_twin": {
        "name": "Digital Twin Methodology", "category": "Emerging",
        "keywords": ["digital twin", "digital twins", "digital twin methodology", "virtual twin"],
        "description": "Creating digital replicas for testing, validation, and optimization.",
        "suitability_for_protocols": "Very High", "timeline_fit": "Good (14-18 weeks)"
    },
    "agent_based_modeling": {
        "name": "Agent-Based Modeling (ABM)", "category": "Quantitative/Emerging",
        "keywords": ["agent-based modeling", "agent-based simulation", "multi-agent system", "ABM"],
        "description": "Simulating actions and interactions of autonomous agents.",
        "suitability_for_protocols": "Very High", "timeline_fit": "Good (part of larger methodology)"
    },
    "optimization_research": {
        "name": "Optimization Research", "category": "Quantitative",
        "keywords": ["optimization", "mathematical optimization", "optimization algorithm"],
        "description": "Finding the best solution from a set of available alternatives based on criteria.",
        "suitability_for_protocols": "High", "timeline_fit": "Good (part of larger methodology)"
    },
    "rapid_prototyping": {
        "name": "Rapid Prototyping & Iterative Development", "category": "Emerging",
        "keywords": ["rapid prototyping", "iterative development", "agile methodology"],
        "description": "Rapidly develop and refine solutions through continuous iteration.",
        "suitability_for_protocols": "Very High", "timeline_fit": "Excellent (8-20 weeks)"
    },
    "living_lab": {
        "name": "Living Lab Methodology", "category": "Emerging/Qualitative",
        "keywords": ["living lab", "living laboratory", "real-world testing", "field testing"],
        "description": "Test innovations in real-world settings with active stakeholder participation.",
        "suitability_for_protocols": "Moderate to High (for validation)", "timeline_fit": "Challenging (15-25 weeks)"
    },
    # Added from 5.1 identify_research_methodologies.py
    "ethnography": {
        "name": "Ethnography", "category": "Qualitative",
        "keywords": ["ethnography", "ethnographic research"],
        "description": "Studying people in their own environment to understand their culture, behaviors, and social structures.",
        "suitability_for_protocols": "Low to Moderate", "timeline_fit": "Poor (typically long-term)"
    },
    "hermeneutics": {
        "name": "Hermeneutics", "category": "Qualitative",
        "keywords": ["hermeneutics", "hermeneutic research"],
        "description": "The theory and methodology of interpretation, especially the interpretation of texts.",
        "suitability_for_protocols": "Low", "timeline_fit": "Varies, can be lengthy"
    },
    "narrative_inquiry": {
        "name": "Narrative Inquiry", "category": "Qualitative",
        "keywords": ["narrative inquiry"],
        "description": "Research that examines experience through the stories people tell.",
        "suitability_for_protocols": "Low", "timeline_fit": "Moderate to Long"
    },
     "survey_research_qual": { # Distinguish if primarily qualitative context for survey
        "name": "Survey Research (Qualitative Focus)", "category": "Qualitative",
        "keywords": ["survey research", "survey methodology", "questionnaire survey"], # Same keywords, context determines
        "description": "Using surveys with open-ended questions to gather qualitative insights and experiences.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Good"
    },
    "historical_research": {
        "name": "Historical Research", "category": "Qualitative",
        "keywords": ["historical research"],
        "description": "Systematic collection and evaluation of data related to past occurrences.",
        "suitability_for_protocols": "Low", "timeline_fit": "Varies"
    },
    "content_analysis": {
        "name": "Content Analysis", "category": "Qualitative", # Can be quantitative too, but listed in qual
        "keywords": ["content analysis"],
        "description": "Systematically analyzing the content of communications.",
        "suitability_for_protocols": "Moderate (for analyzing documents)", "timeline_fit": "Good"
    },
    "discourse_analysis": {
        "name": "Discourse Analysis", "category": "Qualitative",
        "keywords": ["discourse analysis"],
        "description": "Analyzing language use beyond the sentence level.",
        "suitability_for_protocols": "Low", "timeline_fit": "Moderate to Long"
    },
    "thematic_analysis": {
        "name": "Thematic Analysis", "category": "Qualitative",
        "keywords": ["thematic analysis"],
        "description": "Identifying, analyzing, and reporting patterns (themes) within data.",
        "suitability_for_protocols": "Moderate (for qualitative data from case studies etc.)", "timeline_fit": "Good"
    },
    # From 5.1 quantitative
    "quasi_experimental_design": {
        "name": "Quasi-Experimental Design", "category": "Quantitative",
        "keywords": ["quasi-experimental design"],
        "description": "Similar to experimental research but lacks random assignment.",
        "suitability_for_protocols": "Moderate to High", "timeline_fit": "Good"
    },
    "correlational_research": {
        "name": "Correlational Research", "category": "Quantitative",
        "keywords": ["correlational research"],
        "description": "Determining the extent to which two or more variables are related.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Good"
    },
    "causal_comparative_research": {
        "name": "Causal-Comparative Research", "category": "Quantitative",
        "keywords": ["causal-comparative research", "ex post facto research"],
        "description": "Attempting to determine the cause or reason for existing differences in groups of individuals.",
        "suitability_for_protocols": "Moderate", "timeline_fit": "Good"
    },
    # From 5.1 emerging
     "digital_ethnography": {
        "name": "Digital Ethnography", "category": "Emerging/Qualitative",
        "keywords": ["digital ethnography", "netnography"], # Added netnography
        "description": "Ethnographic study of online communities and cultures.",
        "suitability_for_protocols": "Low to Moderate", "timeline_fit": "Varies"
    },
    "q_methodology": {
        "name": "Q Methodology", "category": "Emerging/Mixed Methods",
        "keywords": ["q methodology", "q-sort"],
        "description": "Study of subjectivity, viewpoint, or perspective.",
        "suitability_for_protocols": "Low", "timeline_fit": "Moderate"
    },
    "participatory_design": {
        "name": "Participatory Design", "category": "Emerging/Qualitative",
        "keywords": ["participatory design", "co-design"],
        "description": "Involving all stakeholders in the design process.",
        "suitability_for_protocols": "Moderate to High (for requirements/validation)", "timeline_fit": "Moderate"
    },
    "critical_design": {
        "name": "Critical Design", "category": "Emerging",
        "keywords": ["critical design"],
        "description": "Using design fiction and speculative proposals to challenge assumptions and conceptions about the role of objects in everyday life.",
        "suitability_for_protocols": "Low", "timeline_fit": "Varies"
    },
    "speculative_design": {
        "name": "Speculative Design", "category": "Emerging",
        "keywords": ["speculative design"],
        "description": "Proposing future scenarios and products as a means of cultural critique and discussion.",
        "suitability_for_protocols": "Low", "timeline_fit": "Varies"
    },
    "research_through_design": {
        "name": "Research through Design (RtD)", "category": "Emerging",
        "keywords": ["research through design", "RtD"],
        "description": "Using design practice as a method of inquiry.",
        "suitability_for_protocols": "Moderate to High (similar to DSR in some aspects)", "timeline_fit": "Moderate to Long"
    }
}


def find_methodologies_in_current_literature():
    """
    Analyzes markdown files in CURRENT_LITERATURE_DIR to identify mentions of KNOWN_METHODOLOGIES.
    Returns a dictionary of found methodologies with their mention counts and example contexts.
    """
    found_methodologies_data = defaultdict(lambda: {"count": 0, "papers": set(), "contexts": [], "details": {}})
    
    # Ensure the script is run from the workspace root or adjust path accordingly
    # CURRENT_LITERATURE_DIR should point to proposal/sources/4.3.1-elicit-results/markdown_papers
    script_dir = Path(__file__).resolve().parent
    workspace_root = script_dir.parent
    actual_literature_dir = workspace_root / "sources" / "4.3.1-elicit-results" / "markdown_papers"

    if not actual_literature_dir.exists() or not actual_literature_dir.is_dir():
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error: Literature directory not found at {actual_literature_dir}\n")
        return dict(found_methodologies_data)

    files_processed = 0
    for filepath in actual_literature_dir.glob("*.md"):
        files_processed += 1
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read().lower() # Process content in lowercase for case-insensitive matching
            
            for key, meth_details in KNOWN_METHODOLOGIES.items():
                for keyword in meth_details["keywords"]:
                    keyword_pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
                    matches = list(re.finditer(keyword_pattern, content))
                    
                    if matches:
                        found_methodologies_data[key]["count"] += len(matches)
                        found_methodologies_data[key]["papers"].add(filepath.name)
                        if not found_methodologies_data[key]["details"]: 
                             found_methodologies_data[key]["details"] = meth_details
                        
                        if len(found_methodologies_data[key]["contexts"]) < 5: 
                            match = matches[0] 
                            context_start = max(0, match.start() - 150)
                            context_end = min(len(content), match.end() + 150)
                            context_snippet = content[context_start:context_end].strip().replace("\n", " ")
                            highlighted_snippet = context_snippet.replace(match.group(0), f"**{match.group(0)}**")
                            found_methodologies_data[key]["contexts"].append(f"{filepath.name}: ...{highlighted_snippet}...")
        except Exception as e:
            with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                log_f.write(f"Error processing file {filepath.name}: {e}\n")
    
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Processed {files_processed} markdown files from {actual_literature_dir}.\n")
        log_f.write(f"Found {len(found_methodologies_data)} unique methodologies mentioned.\n")

    for key in found_methodologies_data:
        found_methodologies_data[key]["papers"] = sorted(list(found_methodologies_data[key]["papers"]))
        
    return dict(found_methodologies_data)

def generate_output_files(identified_methodologies_data):
    """Generate output files with identified methodologies data."""
    output_dir = Path("sources")
    output_dir.mkdir(exist_ok=True)
    
    # Save main methodologies file
    main_output_path = output_dir / "5.1.1-relevant-methodologies.json"
    with open(main_output_path, "w") as f:
        json.dump(identified_methodologies_data, f, indent=2)

    # --- Prepare data for Markdown output ---
    md_content = f"""# Relevant Research Methodologies Identified (Task 5.1.1 - Updated)

*Generated: {datetime.now().isoformat()}*
*Literature Source: `../sources/4.3.1-elicit-results/markdown_papers/`*

This document summarizes the research methodologies identified as relevant through an analysis of the current literature. The analysis scanned papers for keywords associated with established and emerging research methodologies.

## Summary of Identified Methodologies

- **Total Unique Methodologies Mentioned**: {len(identified_methodologies_data)}

"""
    if not identified_methodologies_data:
        md_content += "\n**No methodologies matching the internal knowledge base were explicitly identified in the scanned literature.**\n"
    else:
        sorted_methodologies = sorted(identified_methodologies_data.items(), key=lambda item: item[1]['details']['name'])

        for key, data in sorted_methodologies:
            details = data['details']
            md_content += f"\n### {details['name']}\n"
            md_content += f"- **Category**: {details['category']}\n"
            md_content += f"- **Description (from knowledge base)**: {details['description']}\n"
            md_content += f"- **Keywords Searched**: {', '.join(details['keywords'])}\n"
            md_content += f"- **Mention Count in Current Literature**: {data['count']}\n"
            md_content += f"- **Found in Papers**: {', '.join(data['papers']) if data['papers'] else 'None'}\n"
            if data['contexts']:
                md_content += f"- **Example Contexts (up to 5 from literature)**:\n"
                for ctx in data['contexts'][:5]:
                    md_content += f"  - {ctx}\n"
            md_content += "\n"

    md_content += "## Next Steps\n\n"
    md_content += f"- Document each identified methodology category in detail (Tasks 5.1.2-5.1.5)\n"
    md_content += f"- Create comprehensive comparison matrix (Task 5.2.1)\n"
    
    md_content += f"\n---\n*End of Task 5.1.1 Report - Methodologies identified based on keywords in current literature.*\n"

    # Save Markdown summary
    md_file_path = output_dir / "5.1.1-relevant-methodologies.md"
    try:
        with open(md_file_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown summary saved to: {md_file_path}")
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error saving Markdown file {md_file_path}: {e}\n")


def main():
    """Main execution function"""
    # Ensure output directories exist
    # These paths are relative to the script (tools/), so ../docs is proposal/docs
    (Path(__file__).resolve().parent.parent / "sources").mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, 'w', encoding='utf-8') as log_f: 
        log_f.write(f"Starting Task 5.1.1 (Identify Relevant Methodologies - Updated) at {datetime.now().isoformat()}\n")
        # Use actual_literature_dir for logging the correct path being scanned.
        script_dir = Path(__file__).resolve().parent
        workspace_root = script_dir.parent
        actual_literature_dir = workspace_root / "sources" / "4.3.1-elicit-results" / "markdown_papers"
        log_f.write(f"Scanning literature in: {actual_literature_dir}\n")

    print("🔍 Task 5.1.1 (Updated): Identifying Relevant Research Methodologies from Current Literature")
    print("=" * 70)
    
    identified_methodologies = find_methodologies_in_current_literature()
    
    if identified_methodologies:
        print(f"Found {len(identified_methodologies)} methodologies mentioned in the literature.")
        generate_output_files(identified_methodologies)
    else:
        print("No methodologies (from the internal knowledge base) were found in the current literature.")
        generate_output_files({})


    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Finished Task 5.1.1 at {datetime.now().isoformat()}\n")
    
    print("\n🎯 Task 5.1.1 (Updated) complete. Ready for subsequent 5.1.x tasks based on these findings.")

if __name__ == "__main__":
    main() 
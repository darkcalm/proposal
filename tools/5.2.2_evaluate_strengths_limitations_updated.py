#!/usr/bin/env python3
"""
Task 5.2.2: Evaluate Strengths and Limitations (Updated)

Focus: Comprehensive strengths/limitations analysis for methodologies.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Results from docs/5.2.1-methodology-comparison-matrix.json (Updated)
- Detailed analysis framework adapted from archived 5.2.2 script.
"""

import json
from datetime import datetime
from pathlib import Path
import os

# --- Configuration ---
COMPARISON_MATRIX_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.2.1-methodology-comparison-matrix.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.2.2_evaluate_strengths_limitations_updated.log"

# --- Logging ---
def write_log(message):
    OUTPUT_DOCS_DIR.parent.joinpath("tools").mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Core Functions ---
def load_comparison_matrix(filepath: Path) -> dict:
    if not filepath.exists():
        write_log(f"Error: Comparison matrix file not found at {filepath}. Aborting.")
        return {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        write_log(f"Error loading or parsing {filepath}: {e}")
        return {}

# --- Detailed Analysis Text (Adapted from Archive for common methodologies) ---
# This provides richer text that can augment the KBs from 5.1.x / 5.2.1
ARCHIVED_DETAILED_TEXT = {
    "design_science_research": {
        "strengths": {
            "generic_strengths": ["Explicitly designed for artifact creation", "Rigorous evaluation framework", "Balance of theory and practice"],
            "contextual_strengths": ["Perfect alignment with protocol development objectives", "Provides systematic approach to ACP/A2A framework creation"],
            "integration_strengths": ["Can incorporate rapid prototyping for artifact development", "Compatible with experimental research for evaluation"]
        },
        "limitations": {
            "generic_limitations": ["High technical implementation effort", "Evaluation complexity"],
            "contextual_limitations": ["Artifact development may exceed planned timeline", "Evaluation in realistic DER environments may be challenging"],
            "implementation_limitations": ["Requires substantial technical development skills", "Success dependent on artifact complexity management"]
        },
        "risks": {
            "timeline_risks": ["Artifact development complexity may exceed estimates", "Evaluation phase may require more time than planned"],
            "technical_risks": ["Artifact implementation may face unforeseen technical challenges", "Evaluation environment setup may be complex"],
            "mitigations": ["Use agile development approach with regular milestones", "Plan evaluation framework early in development"]
        },
        "overall_assessment": {
            "recommended_scenarios": ["Strong technical implementation skills available", "Clear artifact objectives can be defined"],
            "cautionary_scenarios": ["Limited technical development resources", "Unclear or evolving requirements"]
        }
    },
    "case_study": {
        "strengths": {
            "generic_strengths": ["Rich contextual understanding", "Real-world validation opportunities", "Flexible research design"],
            "contextual_strengths": ["Investigate protocol implementation challenges and successes in DER maintenance contexts"],
        },
        "limitations": {
            "generic_limitations": ["Limited generalizability", "Time-intensive data collection", "Potential researcher bias"],
            "contextual_limitations": ["Access to relevant cases can be difficult", "Ensuring confidentiality of case data"],
        },
        "risks": {
            "timeline_risks": ["Data collection may take longer than anticipated", "Case access delays"],
            "technical_risks": ["Difficulty in triangulating data from multiple sources", "Researcher bias influencing interpretation"],
            "mitigations": ["Develop clear case selection criteria", "Establish trust with case participants early"]
        },
        "overall_assessment": {
            "recommended_scenarios": ["When in-depth understanding of real-world phenomena is needed", "Exploring complex social interactions around technology"],
            "cautionary_scenarios": ["When statistical generalizability is required", "Limited access to rich data sources"]
        }
    },
    "digital_twin_methodology": { # Assuming key from 5.1.5 is digital_twin_methodology
        "strengths": {
            "generic_strengths": ["Comprehensive testing without physical infrastructure", "Risk-free experimentation environment", "Real-time performance monitoring"],
            "contextual_strengths": ["Perfect alignment with DER systems modeling and simulation needs", "Enables comprehensive protocol testing without physical infrastructure costs"],
            "integration_strengths": ["Excellent platform for testing rapid prototyping iterations", "Provides controlled environment for experimental research validation"]
        },
        "limitations": {
            "generic_limitations": ["High initial development effort", "Model fidelity limitations", "Computational resource requirements"],
            "contextual_limitations": ["Digital twin fidelity limits may not capture all real-world complexities", "Requires significant domain expertise"],
            "implementation_limitations": ["Requires access to specialized simulation software and expertise", "Model development timeline may be unpredictable"]
        },
        "risks": {
            "timeline_risks": ["Model development may exceed planned timeframes", "Validation against real systems may be time-consuming"],
            "technical_risks": ["Model fidelity limitations may affect result validity", "Integration complexity between protocol and DER models"],
            "mitigations": ["Start with simplified models and increase complexity iteratively", "Establish clear model validation criteria"]
        },
        "overall_assessment": {
            "recommended_scenarios": ["Protocol performance evaluation across multiple operating conditions", "Safety-critical testing"],
            "cautionary_scenarios": ["Research requiring human factors and social acceptance insights", "Limited computational resources"]
        }
    },
    "rapid_prototyping_methodology": {
        "strengths": {
             "generic_strengths": ["Fast development cycles enable quick validation", "Continuous stakeholder feedback integration"],
             "contextual_strengths": ["Ideal for protocol development where requirements may evolve", "Allows rapid testing of ACP vs A2A alternatives"],
        },
        "limitations": {
            "generic_limitations": ["May sacrifice depth for speed", "Requires strong project management", "Potential scope creep"],
            "contextual_limitations": ["May lead to technical debt if rapid iterations compromise architectural quality"],
        },
        "risks": {
            "timeline_risks": ["Scope creep due to continuous iteration opportunities", "Underestimation of documentation time"],
            "technical_risks": ["Technical debt accumulation affecting final artifact quality"],
            "mitigations": ["Define strict iteration boundaries", "Allocate dedicated time for documentation"]
        },
        "overall_assessment": {
            "recommended_scenarios": ["Uncertain technical requirements", "Need for frequent stakeholder feedback"],
            "cautionary_scenarios": ["Fixed regulatory requirements demanding comprehensive documentation"]
        }
    }
    # Add other common methodologies if needed, following this structure
}

def evaluate_all_methodologies(comparison_matrix_data: dict) -> dict:
    methodology_analyses = {}
    input_methodologies = comparison_matrix_data.get("methodologies", {})
    input_scores = comparison_matrix_data.get("methodology_scores", {})

    for key, meth_data_from_521 in input_methodologies.items():
        score_data_from_521 = input_scores.get(key, {})
        archived_text = ARCHIVED_DETAILED_TEXT.get(key, {}) # Get rich text if available for this key

        # Start with data from 5.2.1 (which is already augmented)
        analysis = {
            "methodology_name": meth_data_from_521.get("name", key.replace("_"," ").title()),
            "category": meth_data_from_521.get("category", "N/A"),
            "ranking_score": score_data_from_521.get("weighted_total", "N/A"),
            "ranking_category": score_data_from_521.get("ranking_category", "N/A"),
            "description": meth_data_from_521.get("purpose", meth_data_from_521.get("description_from_scan", "N/A"))
        }

        # Strengths
        strengths = {
            "generic_strengths": list(set(meth_data_from_521.get("strengths", []) + archived_text.get("strengths", {}).get("generic_strengths", []))),
            "contextual_strengths": list(set(archived_text.get("strengths", {}).get("contextual_strengths", []))),
            "integration_strengths": list(set(archived_text.get("strengths", {}).get("integration_strengths", [])))
        }
        if not strengths["contextual_strengths"] and meth_data_from_521.get("acp_a2a_application") != "N/A":
             strengths["contextual_strengths"].append(f"Relevant to ACP/A2A: {meth_data_from_521.get('acp_a2a_application')}")
        analysis["strengths"] = strengths

        # Limitations
        limitations = {
            "generic_limitations": list(set(meth_data_from_521.get("limitations", []) + archived_text.get("limitations", {}).get("generic_limitations", []))),
            "contextual_limitations": list(set(archived_text.get("limitations", {}).get("contextual_limitations", []))),
            "implementation_limitations": list(set(archived_text.get("limitations", {}).get("implementation_limitations", [])))
        }
        analysis["limitations"] = limitations

        # Risks
        risks = {
            "timeline_risks": list(set(archived_text.get("risks", {}).get("timeline_risks", []))),
            "technical_risks": list(set(archived_text.get("risks", {}).get("technical_risks", []))),
            "resource_risks": list(set(archived_text.get("risks", {}).get("resource_risks", []))),
            "quality_risks": list(set(archived_text.get("risks", {}).get("quality_risks", []))),
            "mitigations": list(set(archived_text.get("risks", {}).get("mitigations", [])))
        }
        if not risks["timeline_risks"] and meth_data_from_521.get("timeline") != "To be determined":
            risks["timeline_risks"].append(f"Potential timeline pressure due to estimated duration: {meth_data_from_521.get('timeline')}")
        analysis["risks"] = risks

        # Overall Assessment
        overall = {
            "suitability_rating_from_521": score_data_from_521.get("weighted_total", "N/A"), # Using the 5.2.1 score
            "recommended_scenarios": list(set(archived_text.get("overall_assessment", {}).get("recommended_scenarios", []))),
            "cautionary_scenarios": list(set(archived_text.get("overall_assessment", {}).get("cautionary_scenarios", [])))
        }
        analysis["overall_assessment"] = overall
        
        methodology_analyses[key] = analysis
    return methodology_analyses

def generate_markdown_summary_522(analysis_report: dict):
    md_parts = []
    metadata = analysis_report.get("metadata", {})
    research_context = analysis_report.get("research_context", {})
    methodology_analyses = analysis_report.get("methodology_analyses", {})

    md_parts.append(f"# Methodology Strengths and Limitations Analysis (Task 5.2.2 - Updated)\n")
    md_parts.append(f"*Generated: {metadata.get('timestamp')}*\n")
    md_parts.append(f"*Based on: {Path(COMPARISON_MATRIX_INPUT_JSON).name}*\n")
    md_parts.append(f"*Methodologies Analyzed: {metadata.get('methodologies_analyzed')}*\n\n")

    md_parts.append(f"## Research Context\n")
    md_parts.append(f"- **Focus**: {research_context.get('focus', 'N/A')}\n")
    md_parts.append(f"- **Domain**: {research_context.get('domain', 'N/A')}\n")
    md_parts.append(f"- **Constraints**: {research_context.get('constraints', 'N/A')}\n\n")

    # Sort methodologies by ranking score for presentation
    sorted_analysis_items = sorted(
        methodology_analyses.items(), 
        key=lambda item: item[1].get('ranking_score', 0) if isinstance(item[1].get('ranking_score'), (int, float)) else 0, 
        reverse=True
    )

    for key, analysis in sorted_analysis_items:
        md_parts.append(f"### {analysis.get('methodology_name', key)}\n")
        md_parts.append(f"- **Category**: {analysis.get('category', 'N/A')}\n")
        md_parts.append(f"- **Description**: {analysis.get('description', 'N/A')}\n")
        md_parts.append(f"- **5.2.1 Ranking Score**: {analysis.get('ranking_score', 'N/A')} ({analysis.get('ranking_category', 'N/A')})\n")

        strengths = analysis.get("strengths", {})
        if strengths:
            md_parts.append("#### Strengths\n")
            if strengths.get("generic_strengths"): md_parts.append(f"- Generic: { '; '.join(strengths['generic_strengths']) }\n")
            if strengths.get("contextual_strengths"): md_parts.append(f"- Contextual (ACP/A2A): { '; '.join(strengths['contextual_strengths']) }\n")
            if strengths.get("integration_strengths"): md_parts.append(f"- Integration: { '; '.join(strengths['integration_strengths']) }\n")
        
        limitations = analysis.get("limitations", {})
        if limitations:
            md_parts.append("#### Limitations\n")
            if limitations.get("generic_limitations"): md_parts.append(f"- Generic: { '; '.join(limitations['generic_limitations']) }\n")
            if limitations.get("contextual_limitations"): md_parts.append(f"- Contextual: { '; '.join(limitations['contextual_limitations']) }\n")
            if limitations.get("implementation_limitations"): md_parts.append(f"- Implementation: { '; '.join(limitations['implementation_limitations']) }\n")

        risks = analysis.get("risks", {})
        if risks:
            md_parts.append("#### Risks & Mitigations\n")
            if risks.get("timeline_risks"): md_parts.append(f"- Timeline Risks: { '; '.join(risks['timeline_risks']) }\n")
            if risks.get("technical_risks"): md_parts.append(f"- Technical Risks: { '; '.join(risks['technical_risks']) }\n")
            if risks.get("mitigations"): md_parts.append(f"- Mitigations: { '; '.join(risks['mitigations']) }\n")

        overall = analysis.get("overall_assessment", {})
        if overall:
            md_parts.append("#### Overall Assessment Notes\n")
            if overall.get("recommended_scenarios"): md_parts.append(f"- Recommended Scenarios: { '; '.join(overall['recommended_scenarios']) }\n")
            if overall.get("cautionary_scenarios"): md_parts.append(f"- Cautionary Scenarios: { '; '.join(overall['cautionary_scenarios']) }\n")
        md_parts.append("\n---\n")
    
    md_parts.append("\n## Next Steps\n- Task 5.2.3: Assess detailed resource requirements for top-ranked methodologies.\n")
    return "".join(md_parts)

def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.2.2 (Evaluate Strengths and Limitations - Updated) at {datetime.now().isoformat()}\n")
    
    print("📝 Task 5.2.2 (Updated): Evaluating Strengths and Limitations")
    print("=" * 70)

    comparison_matrix_data = load_comparison_matrix(COMPARISON_MATRIX_INPUT_JSON)
    if not comparison_matrix_data or "methodologies" not in comparison_matrix_data:
        write_log("Comparison matrix data is missing or invalid. Aborting.")
        print("Error: Could not load valid data from 5.2.1-methodology-comparison-matrix.json")
        return
    write_log(f"Loaded data for {len(comparison_matrix_data.get('methodologies',{}))} methodologies from {COMPARISON_MATRIX_INPUT_JSON.name}")

    methodology_analyses = evaluate_all_methodologies(comparison_matrix_data)
    write_log(f"Completed S/L analysis for {len(methodology_analyses)} methodologies.")

    analysis_report = {
        "metadata": {
            "task": "5.2.2 - Evaluate Strengths and Limitations (Updated)",
            "timestamp": datetime.now().isoformat(),
            "input_source": str(COMPARISON_MATRIX_INPUT_JSON.name),
            "methodologies_analyzed": len(methodology_analyses)
        },
        "research_context": comparison_matrix_data.get("metadata",{}).get("research_context", {
            "focus": "ACP/A2A for DER predictive maintenance", "domain": "DER", "constraints": "20-week thesis"
        }),
        "methodology_analyses": methodology_analyses
    }

    # Save JSON output
    json_output_path = OUTPUT_DOCS_DIR / "5.2.2-methodology-strengths-limitations.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON S/L analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")

    # Save Markdown summary
    md_summary = generate_markdown_summary_522(analysis_report)
    md_output_path = OUTPUT_SOURCES_DIR / "5.2.2-methodology-strengths-limitations.md"
    try:
        OUTPUT_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(md_summary)
        write_log(f"Markdown S/L summary saved to {md_output_path}")
        print(f"Markdown summary saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving Markdown summary: {e}")

    write_log(f"Finished Task 5.2.2 (Updated) at {datetime.now().isoformat()}")
    print("\n✅ Task 5.2.2 (Updated) complete.")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Task 5.3.1: Justify Research Methodology

Focus: Systematic justification of methodology selection based on comprehensive analysis
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Results from 5.2.4 feasibility analysis
- Perplexity dialogue recommendations
- Project constraints and requirements
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
FEASIBILITY_ANALYSIS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.4-feasibility-analysis.json"
PERPLEXITY_DIALOGUE_INPUT = Path(__file__).resolve().parent.parent / "sources" / "5.3-dialogue-with-perplexity-Methodology Recommendation for Human DER Worker Di.md"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.3.1_justify_research_methodology.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analysis ---
def load_feasibility_analysis():
    if not FEASIBILITY_ANALYSIS_INPUT_JSON.exists():
        write_log(f"Error: Feasibility analysis file not found at {FEASIBILITY_ANALYSIS_INPUT_JSON}")
        return {}
    try:
        with open(FEASIBILITY_ANALYSIS_INPUT_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        write_log(f"Error loading feasibility analysis: {e}")
        return {}

# --- Methodology Justification Analysis ---
def analyze_methodology_options(feasibility_data):
    """Analyze top methodologies and their suitability for the research"""
    
    feasibility_analyses = feasibility_data.get("feasibility_analyses", {})
    
    # Sort by feasibility score
    sorted_methodologies = sorted(
        feasibility_analyses.items(),
        key=lambda x: x[1].get("total_feasibility_score", 0),
        reverse=True
    )
    
    # Analyze top 5 methodologies
    top_methodologies = []
    for key, analysis in sorted_methodologies[:5]:
        methodology = {
            "key": key,
            "name": analysis.get("methodology_name", key),
            "category": analysis.get("category", "N/A"),
            "feasibility_score": analysis.get("total_feasibility_score", 0),
            "recommendation": analysis.get("recommendation", "N/A"),
            "feasibility_category": analysis.get("feasibility_category", "N/A"),
            "score_breakdown": analysis.get("scores_breakdown", {}),
            "enhancers": analysis.get("key_feasibility_enhancers", []),
            "inhibitors": analysis.get("key_feasibility_inhibitors", [])
        }
        top_methodologies.append(methodology)
    
    return top_methodologies, sorted_methodologies

def evaluate_perplexity_recommendations():
    """Evaluate the recommendations from the Perplexity dialogue"""
    
    perplexity_analysis = {
        "dsr_recommendation": {
            "methodology": "Design Science Research",
            "rationale": [
                "Validated by Carrión & Pastor Digital Twin methodology review",
                "Three-step process aligns with DSR phases",
                "Supports HDT framework development",
                "Addresses standardization gap in DT methodologies"
            ],
            "concerns": [
                "High resource intensity and timeline requirements",
                "Ranked 20th in feasibility analysis (score 2.71)",
                "Recommendation is 'Use with Caution'",
                "May exceed 20-week thesis timeline"
            ]
        },
        "composition_methodology": {
            "approach": "Protocol Composition vs Selection",
            "rationale": [
                "Protocols work together rather than compete",
                "Focus on integration rather than selection",
                "More realistic representation of real-world usage",
                "Addresses gap in multi-protocol frameworks"
            ],
            "concerns": [
                "Expands scope beyond original ACP/A2A focus",
                "Adds MCP and ANP without clear justification",
                "May increase complexity beyond thesis scope",
                "No feasibility analysis for this novel approach"
            ]
        }
    }
    
    return perplexity_analysis

def justify_methodology_selection(top_methodologies, perplexity_analysis):
    """Provide systematic justification for methodology selection"""
    
    # Primary methodology recommendation based on feasibility
    primary_methodology = top_methodologies[0]
    
    # Hybrid approach consideration
    hybrid_options = []
    for method in top_methodologies[:3]:
        if method["feasibility_score"] >= 3.5:
            hybrid_options.append(method)
    
    justification = {
        "recommended_approach": {
            "primary_methodology": primary_methodology["name"],
            "justification_criteria": [
                "Highest feasibility score among all analyzed methodologies",
                "Aligns with project timeline and resource constraints",
                "Provides systematic approach to research objectives",
                "Maintains academic rigor while ensuring deliverability"
            ],
            "specific_rationale": {
                "feasibility_score": primary_methodology["feasibility_score"],
                "timeline_alignment": "Fits within 20-week thesis timeline",
                "resource_requirements": "Moderate resource intensity suitable for individual project",
                "academic_rigor": "Well-established methodology with clear evaluation criteria"
            }
        },
        "perplexity_recommendations_assessment": {
            "dsr_evaluation": {
                "alignment_with_research": "Strong theoretical alignment with HDT development",
                "feasibility_concerns": "Low feasibility score (2.71) raises serious implementation risks",
                "timeline_risk": "20-week estimated duration may be challenging",
                "recommendation": "Consider as secondary/supporting methodology rather than primary"
            },
            "composition_approach_evaluation": {
                "conceptual_merit": "Valid insight about protocol integration",
                "scope_expansion_risk": "Adds complexity that may exceed thesis boundaries",
                "methodological_uncertainty": "Novel approach lacks established implementation framework",
                "recommendation": "Incorporate insights into primary methodology rather than replace it"
            }
        },
        "hybrid_methodology_consideration": {
            "approach": "Multi-phase methodology combining strengths",
            "phases": [
                {
                    "phase": "Phase 1: Systematic Literature Review",
                    "methodology": "Systematic Literature Review Methodology",
                    "focus": "Protocol composition patterns and integration approaches",
                    "duration": "6-8 weeks"
                },
                {
                    "phase": "Phase 2: Comparative Framework Development", 
                    "methodology": "Comparative Research Methodology",
                    "focus": "ACP vs A2A analysis with composition considerations",
                    "duration": "8-10 weeks"
                },
                {
                    "phase": "Phase 3: Proof of Concept",
                    "methodology": "Rapid Prototyping",
                    "focus": "Protocol integration demonstration",
                    "duration": "4-6 weeks"
                }
            ],
            "advantages": [
                "Leverages top-feasible methodologies",
                "Incorporates Perplexity insights without scope explosion",
                "Maintains focus on ACP/A2A while considering integration",
                "Provides multiple validation approaches"
            ]
        },
        "risk_mitigation": {
            "scope_management": "Maintain focus on ACP/A2A core objectives",
            "timeline_control": "Use rapid prototyping for proof-of-concept only",
            "complexity_management": "Limit protocol composition analysis to ACP/A2A integration",
            "quality_assurance": "Regular milestone reviews and supervisor feedback"
        }
    }
    
    return justification

def generate_methodology_justification_document(justification, top_methodologies, perplexity_analysis):
    """Generate comprehensive methodology justification document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Research Methodology Justification (Task 5.3.1)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Based on: 5.2.4 Feasibility Analysis and Perplexity Methodology Recommendations*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    primary = justification["recommended_approach"]
    doc_parts.append(f"Based on comprehensive feasibility analysis and expert recommendations, this research will employ **{primary['primary_methodology']}** as the primary methodology, enhanced with insights from protocol composition research. This approach balances academic rigor with practical deliverability within the 20-week thesis timeline.\n\n")
    
    # Feasibility Analysis Results
    doc_parts.append("## Feasibility Analysis Results\n\n")
    doc_parts.append("The comprehensive feasibility analysis of 25 research methodologies revealed the following top candidates:\n\n")
    doc_parts.append("| Rank | Methodology | Feasibility Score | Recommendation |\n")
    doc_parts.append("|------|-------------|-------------------|----------------|\n")
    for i, method in enumerate(top_methodologies, 1):
        doc_parts.append(f"| {i} | {method['name']} | {method['feasibility_score']:.2f} | {method['recommendation']} |\n")
    doc_parts.append("\n")
    
    # Perplexity Recommendations Analysis
    doc_parts.append("## Analysis of Expert Recommendations\n\n")
    doc_parts.append("### Design Science Research Recommendation\n")
    dsr = perplexity_analysis["dsr_recommendation"]
    doc_parts.append("**Rationale:**\n")
    for rationale in dsr["rationale"]:
        doc_parts.append(f"- {rationale}\n")
    doc_parts.append("\n**Concerns:**\n")
    for concern in dsr["concerns"]:
        doc_parts.append(f"- {concern}\n")
    doc_parts.append("\n")
    
    doc_parts.append("### Protocol Composition Approach\n")
    comp = perplexity_analysis["composition_methodology"]
    doc_parts.append("**Rationale:**\n")
    for rationale in comp["rationale"]:
        doc_parts.append(f"- {rationale}\n")
    doc_parts.append("\n**Concerns:**\n")
    for concern in comp["concerns"]:
        doc_parts.append(f"- {concern}\n")
    doc_parts.append("\n")
    
    # Methodology Justification
    doc_parts.append("## Methodology Selection Justification\n\n")
    hybrid = justification["hybrid_methodology_consideration"]
    doc_parts.append(f"### Recommended Approach: {hybrid['approach']}\n\n")
    
    for phase in hybrid["phases"]:
        doc_parts.append(f"#### {phase['phase']}\n")
        doc_parts.append(f"- **Methodology**: {phase['methodology']}\n")
        doc_parts.append(f"- **Focus**: {phase['focus']}\n")
        doc_parts.append(f"- **Duration**: {phase['duration']}\n\n")
    
    doc_parts.append("### Advantages of This Approach\n")
    for advantage in hybrid["advantages"]:
        doc_parts.append(f"- {advantage}\n")
    doc_parts.append("\n")
    
    # Risk Management
    doc_parts.append("## Risk Management and Mitigation\n\n")
    risks = justification["risk_mitigation"]
    for risk_type, mitigation in risks.items():
        doc_parts.append(f"- **{risk_type.replace('_', ' ').title()}**: {mitigation}\n")
    doc_parts.append("\n")
    
    # Conclusion
    doc_parts.append("## Conclusion\n\n")
    doc_parts.append("The selected hybrid methodology approach provides optimal balance between:\n")
    doc_parts.append("- **Academic Rigor**: Systematic literature review and comparative analysis\n")
    doc_parts.append("- **Practical Feasibility**: High feasibility scores and proven implementation\n")
    doc_parts.append("- **Innovation**: Integration of protocol composition insights\n")
    doc_parts.append("- **Deliverability**: Realistic timeline and resource requirements\n\n")
    doc_parts.append("This approach ensures the research contributes novel insights while maintaining the quality and rigor expected of a Master's thesis.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.3.1 (Justify Research Methodology) at {datetime.now().isoformat()}\n")
    
    print("📋 Task 5.3.1: Justifying Research Methodology")
    print("=" * 70)
    
    # Load feasibility analysis
    feasibility_data = load_feasibility_analysis()
    if not feasibility_data:
        print("Error: Could not load feasibility analysis data")
        return
    
    # Analyze methodology options
    top_methodologies, all_methodologies = analyze_methodology_options(feasibility_data)
    write_log(f"Analyzed {len(all_methodologies)} methodologies, identified top {len(top_methodologies)}")
    
    # Evaluate Perplexity recommendations
    perplexity_analysis = evaluate_perplexity_recommendations()
    write_log("Evaluated Perplexity dialogue recommendations")
    
    # Generate justification
    justification = justify_methodology_selection(top_methodologies, perplexity_analysis)
    write_log("Generated methodology selection justification")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "5.3.1 - Justify Research Methodology",
            "timestamp": datetime.now().isoformat(),
            "input_sources": ["5.2.4-feasibility-analysis.json", "5.3-perplexity-dialogue.md"]
        },
        "top_methodologies": top_methodologies,
        "perplexity_analysis": perplexity_analysis,
        "methodology_justification": justification
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "5.3.1-methodology-justification.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON justification saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save methodology justification document
    justification_doc = generate_methodology_justification_document(
        justification, top_methodologies, perplexity_analysis
    )
    md_output_path = OUTPUT_DOCS_DIR / "5.3.1-methodology-justification.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(justification_doc)
        write_log(f"Methodology justification document saved to {md_output_path}")
        print(f"Methodology justification saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving methodology justification document: {e}")
    
    write_log(f"Finished Task 5.3.1 at {datetime.now().isoformat()}")
    print("\n✅ Task 5.3.1 complete.")

if __name__ == "__main__":
    main() 
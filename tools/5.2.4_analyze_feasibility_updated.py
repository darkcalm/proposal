#!/usr/bin/env python3
"""
Task 5.2.4: Analyze Feasibility (Updated)

Focus: Comprehensive feasibility analysis for identified methodologies.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
         for DER predictive maintenance coordination

Based on:
- Results from updated 5.2.1, 5.2.2, and 5.2.3 JSON outputs.
- Feasibility calculation logic adapted from archived 5.2.4 script.
"""

import json
from datetime import datetime
from pathlib import Path
import os # Retained for os.path.join if used by archive logic, prefer Path
import re # Added for parsing timeline strings

# --- Configuration ---
COMPARISON_MATRIX_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.1-methodology-comparison-matrix.json"
STRENGTHS_LIMITATIONS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.2-methodology-strengths-limitations.json"
RESOURCE_REQUIREMENTS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.3-resource-requirements-assessment.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.2.4_analyze_feasibility_updated.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analyses ---
def load_previous_analyses_updated():
    comparison_matrix = {}
    strengths_analysis_data = {}
    resource_assessment_data = {}
    files_loaded = True

    for file_path, data_dict_ref_name in [
        (COMPARISON_MATRIX_INPUT_JSON, "comparison_matrix"),
        (STRENGTHS_LIMITATIONS_INPUT_JSON, "strengths_analysis_data"),
        (RESOURCE_REQUIREMENTS_INPUT_JSON, "resource_assessment_data")
    ]:
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    if data_dict_ref_name == "comparison_matrix": comparison_matrix = json.load(f)
                    elif data_dict_ref_name == "strengths_analysis_data": strengths_analysis_data = json.load(f)
                    elif data_dict_ref_name == "resource_assessment_data": resource_assessment_data = json.load(f)
                write_log(f"Loaded data from {file_path.name}")
            except Exception as e:
                write_log(f"Error loading {file_path.name}: {e}")
                files_loaded = False
        else:
            write_log(f"Error: {file_path.name} not found.")
            files_loaded = False
            
    if not files_loaded:
        write_log("One or more input files were missing or failed to load. Feasibility analysis may be incomplete.")
        # Decide if to proceed with partial data or abort - for now, allow partial
        
    return comparison_matrix, strengths_analysis_data, resource_assessment_data


# --- Feasibility Analysis (Adapted from Archive) ---
def analyze_feasibility_updated(comparison_matrix, strengths_data, resource_data):
    research_context_default = {
        "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
        "domain": "Distributed Energy Resources (DER) predictive maintenance",
        "timeframe": "20-week Master's thesis",
        "constraints": ["Individual project", "Academic environment", "Limited budget", "Fixed timeline"]
    }
    research_context = comparison_matrix.get("research_context", comparison_matrix.get("metadata",{}).get("research_context", research_context_default))

    feasibility_analyses = {}
    
    # Methodologies to analyze are those present in the comparison_matrix
    # (which should be the superset from 5.2.1)
    methodologies_from_521 = comparison_matrix.get("methodologies", {})
    methodology_scores_from_521 = comparison_matrix.get("methodology_scores", {})

    if not methodologies_from_521:
        write_log("No methodologies found in 5.2.1 data. Cannot perform feasibility analysis.")
        return {}, research_context

    for method_key, meth_521_data in methodologies_from_521.items():
        meth_strength_data = strengths_data.get("methodology_analyses", {}).get(method_key, {})
        meth_resource_data = resource_data.get("resource_assessments", {}).get(method_key, {})
        meth_521_score_data = methodology_scores_from_521.get(method_key, {})

        # 1. Suitability Score (from 5.2.1 weighted total score)
        # This score is already on a good scale (e.g. 0-5 or similar if weights sum to 1 or 5)
        suitability_score_raw = meth_521_score_data.get("weighted_total", 0)
        # Ensure it's normalized to a 0-5 scale if not already.
        # Assuming the weighted_total from 5.2.1 is already effectively a 0-5 or 1-5 suitability indication.
        # For this example, if max score is 5, it is fine. Otherwise, normalization needed.
        suitability_score_component = float(suitability_score_raw) # Directly use it if it represents overall suitability

        # 2. Resource Intensity Score (from 5.2.3, 1-5 where 5 is VERY HIGH intensity)
        # We need to invert this for feasibility: 5 = low intensity (good), 1 = high intensity (bad)
        resource_intensity_val = meth_resource_data.get("resource_intensity", {}).get("intensity_score", 3) # Default to moderate
        resource_feasibility_score_component = max(1, 6 - resource_intensity_val) # Invert: 1->5, 2->4, 3->3, 4->2, 5->1

        # 3. Risk Score (from 5.2.2 - needs heuristic or more structured risk data from 5.2.2)
        # Using a heuristic based on number of identified risks (example)
        num_timeline_risks = len(meth_strength_data.get("risks", {}).get("timeline_risks", []))
        num_technical_risks = len(meth_strength_data.get("risks", {}).get("technical_risks", []))
        total_risks = num_timeline_risks + num_technical_risks
        if total_risks == 0: risk_score_component = 5    # Low risk
        elif total_risks <= 2: risk_score_component = 4  # Moderately Low risk
        elif total_risks <= 4: risk_score_component = 3  # Moderate risk
        elif total_risks <= 6: risk_score_component = 2  # Moderately High risk
        else: risk_score_component = 1                      # High risk

        # 4. Timeline Alignment (from 5.2.3 or 5.2.1)
        timeline_str_from_521 = meth_521_data.get("timeline", "To be determined")
        timeline_str_from_523 = meth_resource_data.get("time_resources", {}).get("total_project_duration", timeline_str_from_521)
        # Try to parse weeks (improved parsing for ranges)
        timeline_alignment_score_component = 3 # Default moderate
        try:
            if "weeks" in timeline_str_from_523:
                # Extract all numbers from the string
                duration_parts = [int(s) for s in re.findall(r'\d+', timeline_str_from_523)]
                if duration_parts:
                    # For ranges, use the maximum duration
                    max_duration = max(duration_parts)
                    # Adjusted scoring based on 5.2.3 time estimates
                    if max_duration <= 16: timeline_alignment_score_component = 5    # Excellent (14-16 weeks like SLR)
                    elif max_duration <= 18: timeline_alignment_score_component = 4.5  # Very Good (16-18 weeks like Rapid Prototyping)
                    elif max_duration <= 20: timeline_alignment_score_component = 4    # Good (18-20 weeks like Case Study)
                    elif max_duration <= 22: timeline_alignment_score_component = 3.5  # Moderately Good (20-22 weeks like Digital Twin)
                    elif max_duration <= 24: timeline_alignment_score_component = 3    # Moderate (22-24 weeks like Living Lab)
                    elif max_duration <= 26: timeline_alignment_score_component = 2    # Challenging (24-26 weeks like Sequential)
                    else: timeline_alignment_score_component = 1                       # Poor (beyond 26 weeks)
            elif meth_521_data.get("feasibility_20_weeks","").lower() == "excellent": timeline_alignment_score_component = 5
            elif meth_521_data.get("feasibility_20_weeks","").lower() == "good": timeline_alignment_score_component = 4
            elif meth_521_data.get("feasibility_20_weeks","").lower() == "moderate": timeline_alignment_score_component = 3
            elif meth_521_data.get("feasibility_20_weeks","").lower() == "challenging": timeline_alignment_score_component = 2
            elif meth_521_data.get("feasibility_20_weeks","").lower() == "poor": timeline_alignment_score_component = 1
        except Exception as e:
            write_log(f"Could not parse timeline {timeline_str_from_523} for {method_key}: {e}")
            # Keep default moderate score of 3

        # Weighted Total Feasibility Score (example weights)
        # Weights from archived 5.2.4: Suitability 30%, Resource Feasibility 30%, Risk 20%, Timeline 20%
        total_feasibility_score = (
            suitability_score_component * 0.30 +
            resource_feasibility_score_component * 0.30 +
            risk_score_component * 0.20 +
            timeline_alignment_score_component * 0.20
        )
        total_feasibility_score = round(max(0, min(5, total_feasibility_score)), 2)

        # Calculate Feasibility Score Without Timeline Alignment
        score_contrib_without_timeline = (
            suitability_score_component * 0.30 +
            resource_feasibility_score_component * 0.30 +
            risk_score_component * 0.20
        )
        # Sum of weights for components other than timeline = 0.30 + 0.30 + 0.20 = 0.80
        # Normalize this score to be on a 0-5 scale like the total_feasibility_score
        # If sum_of_weights_without_timeline is zero (though not in this config), handle division by zero.
        sum_of_weights_without_timeline = 0.80
        if sum_of_weights_without_timeline > 0:
            feasibility_score_without_timeline_normalized = round(score_contrib_without_timeline / sum_of_weights_without_timeline, 2)
        else:
            feasibility_score_without_timeline_normalized = 0.0 # Should not happen with current weights

        if total_feasibility_score >= 4.0: feasibility_category = "Highly Feasible"
        elif total_feasibility_score >= 3.5: feasibility_category = "Feasible"
        elif total_feasibility_score >= 3.0: feasibility_category = "Feasible with Conditions"
        elif total_feasibility_score >= 2.0: feasibility_category = "Moderately Feasible (Challenging)"
        else: feasibility_category = "Low Feasibility / Not Recommended"

        recommendation = "Not Recommended"
        if total_feasibility_score >= 4.2: recommendation = "Strongly Recommended"
        elif total_feasibility_score >= 3.8: recommendation = "Highly Recommended"
        elif total_feasibility_score >= 3.3: recommendation = "Recommended"
        elif total_feasibility_score >= 2.8: recommendation = "Consider with Conditions"
        elif total_feasibility_score >= 2.0: recommendation = "Use with Caution"

        feasibility_analyses[method_key] = {
            "methodology_name": meth_521_data.get("name", method_key),
            "category": meth_521_data.get("category", "N/A"),
            "scores_breakdown": {
                "suitability_input_score": suitability_score_raw,
                "suitability_contrib": round(suitability_score_component * 0.30, 2),
                "resource_intensity_input": resource_intensity_val,
                "resource_feasibility_contrib": round(resource_feasibility_score_component * 0.30, 2),
                "risk_input_total_identified": total_risks,
                "risk_mitigation_contrib": round(risk_score_component * 0.20, 2),
                "timeline_input_str": timeline_str_from_523,
                "timeline_alignment_contrib": round(timeline_alignment_score_component * 0.20, 2),
            },
            "total_feasibility_score": total_feasibility_score,
            "feasibility_score_without_timeline_normalized": feasibility_score_without_timeline_normalized,
            "feasibility_category": feasibility_category,
            "recommendation": recommendation,
            "key_feasibility_enhancers": meth_strength_data.get("strengths",{}).get("contextual_strengths", [])[:2], # Example
            "key_feasibility_inhibitors": meth_resource_data.get("feasibility_constraints",{}).get("critical_constraints", [])[:2], # Example
        }
    return feasibility_analyses, research_context

def generate_markdown_summary_524(analysis_report: dict):
    md_parts = []
    metadata = analysis_report.get("metadata", {})
    research_context = analysis_report.get("research_context", {})
    feasibility_analyses = analysis_report.get("feasibility_analyses", {})

    md_parts.append(f"# Methodology Feasibility Analysis (Task 5.2.4 - Updated)\n")
    md_parts.append(f"*Generated: {metadata.get('timestamp')}*\n")
    md_parts.append(f"*Based on inputs from: { ', '.join(metadata.get('input_sources',[])) }*\n")
    md_parts.append(f"*Methodologies Analyzed: {metadata.get('methodologies_analyzed')}*\n\n")

    md_parts.append(f"## Research Context\n- Focus: {research_context.get('focus', 'N/A')}\n- Constraints: { ', '.join(research_context.get('constraints', [])) }\n\n")
    
    md_parts.append("## Feasibility Ranking Summary\n")
    md_parts.append("| Methodology | Category | Feasibility Score | Recommendation |\n")
    md_parts.append("|-------------|----------|-------------------|----------------|\n")

    sorted_analyses = sorted(
        feasibility_analyses.items(),
        key=lambda item: item[1]["total_feasibility_score"],
        reverse=True
    )
    for key, analysis in sorted_analyses:
        md_parts.append(f"| {analysis['methodology_name']} | {analysis['category']} | {analysis['total_feasibility_score']:.2f} | **{analysis['recommendation']}** |\n")
    md_parts.append("\n")

    md_parts.append("## Detailed Feasibility Assessments (Top 5)\n")
    for i, (key, analysis) in enumerate(sorted_analyses[:5]):
        scores_br = analysis["scores_breakdown"]
        md_parts.append(f"### {i+1}. {analysis['methodology_name']}\n")
        md_parts.append(f"- **Total Feasibility Score**: {analysis['total_feasibility_score']:.2f} ({analysis['feasibility_category']})\n")
        md_parts.append(f"- **Feasibility Score Without Timeline Alignment**: {analysis['feasibility_score_without_timeline_normalized']:.2f}\n")
        md_parts.append(f"- **Recommendation**: {analysis['recommendation']}\n")
        md_parts.append("- Score Contributions:\n")
        md_parts.append(f"  - Suitability (from 5.2.1 score {scores_br['suitability_input_score']}): {scores_br['suitability_contrib']}\n")
        md_parts.append(f"  - Resource Feasibility (intensity {scores_br['resource_intensity_input']}): {scores_br['resource_feasibility_contrib']}\n")
        md_parts.append(f"  - Risk Mitigation (identified risks {scores_br['risk_input_total_identified']}): {scores_br['risk_mitigation_contrib']}\n")
        md_parts.append(f"  - Timeline Alignment (evaluating '{scores_br['timeline_input_str']}'): {scores_br['timeline_alignment_contrib']}\n")
        if analysis["key_feasibility_enhancers"]: md_parts.append(f"- Key Enhancers: { '; '.join(analysis['key_feasibility_enhancers']) }\n")
        if analysis["key_feasibility_inhibitors"]: md_parts.append(f"- Key Inhibitors: { '; '.join(analysis['key_feasibility_inhibitors']) }\n")
        md_parts.append("---\n")

    md_parts.append("\n## Next Steps\n- Task 5.3.1: Select primary methodology based on this comprehensive feasibility analysis.\n")
    return "".join(md_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.2.4 (Analyze Feasibility - Updated) at {datetime.now().isoformat()}\n")

    print("🎯 Task 5.2.4 (Updated): Analyzing Methodology Feasibility")
    print("=" * 70)

    comparison_matrix, strengths_data, resource_data = load_previous_analyses_updated()

    if not comparison_matrix or "methodologies" not in comparison_matrix:
        write_log("Aborting: Comparison matrix data from 5.2.1 is missing or invalid.")
        print("Error: Could not load valid data from 5.2.1-methodology-comparison-matrix.json. Aborting.")
        return

    feasibility_analysis = analyze_feasibility_updated(comparison_matrix, strengths_data, resource_data)
    write_log(f"Completed feasibility analysis for {len(feasibility_analysis)} methodologies.")

    analysis_report = {
        "metadata": {
            "task": "5.2.4 - Analyze Feasibility (Updated)",
            "timestamp": datetime.now().isoformat(),
            "input_sources": [
                str(COMPARISON_MATRIX_INPUT_JSON.name),
                str(STRENGTHS_LIMITATIONS_INPUT_JSON.name),
                str(RESOURCE_REQUIREMENTS_INPUT_JSON.name)
            ],
            "methodologies_analyzed": len(feasibility_analysis)
        },
        "research_context": comparison_matrix.get("metadata",{}).get("research_context", {
            "focus": "ACP/A2A for DER predictive maintenance", "domain": "DER", "constraints": "20-week thesis"
        }),
        "feasibility_analysis": feasibility_analysis
    }

    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "5.2.4-feasibility-analysis.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON feasibility analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")

    write_log(f"Finished Task 5.2.4 (Updated) at {datetime.now().isoformat()}")
    print("\n✅ Task 5.2.4 (Updated) complete.")

if __name__ == "__main__":
    main() 
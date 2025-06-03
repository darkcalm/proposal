#!/usr/bin/env python3
"""
Task 5.2.4: Analyze Feasibility

Focus: Comprehensive feasibility analysis for top-ranked methodologies
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
         for DER predictive maintenance coordination

Based on:
- Results from Task 5.2.1 methodology comparison matrix
- Results from Task 5.2.2 strengths and limitations analysis
- Results from Task 5.2.3 resource requirements assessment
- Research context and constraints (20-week Master's thesis)
"""

import json
import os
from datetime import datetime

def load_previous_analyses():
    """Load previous analysis results from Tasks 5.2.1, 5.2.2, and 5.2.3"""
    base_path = "../docs/"
    matrix_file = os.path.join(base_path, "5.2.1-methodology-comparison-matrix.json")
    strengths_file = os.path.join(base_path, "5.2.2-methodology-strengths-limitations.json")
    resources_file = os.path.join(base_path, "5.2.3-resource-requirements-assessment.json")

    if not all(os.path.exists(f) for f in [matrix_file, strengths_file, resources_file]):
        raise FileNotFoundError("One or more required input files are missing.")

    with open(matrix_file, 'r') as f:
        comparison_matrix = json.load(f)
    with open(strengths_file, 'r') as f:
        strengths_analysis = json.load(f)
    with open(resources_file, 'r') as f:
        resource_assessment = json.load(f)

    return comparison_matrix, strengths_analysis, resource_assessment

def analyze_feasibility():
    """Analyze feasibility for the top-ranked methodologies."""
    comparison_matrix, strengths_analysis, resource_assessment = load_previous_analyses()

    research_context = {
        "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
        "domain": "Distributed Energy Resources (DER) predictive maintenance",
        "timeframe": "20-week Master's thesis",
        "constraints": ["Individual project", "Academic environment", "Limited budget", "Fixed timeline"]
    }

    feasibility_analyses = {}

    # Consider top 6 methodologies as per previous scripts
    top_method_keys = list(strengths_analysis["methodology_analyses"].keys())

    for method_key in top_method_keys:
        method_matrix_data = comparison_matrix["methodologies"].get(method_key, {})
        method_strengths_data = strengths_analysis["methodology_analyses"].get(method_key, {})
        method_resources_data = resource_assessment["resource_assessments"].get(method_key, {})

        if not all([method_matrix_data, method_strengths_data, method_resources_data]):
            print(f"Warning: Missing data for methodology key {method_key}. Skipping.")
            continue

        # --- Feasibility Scoring ---
        # Max possible score: 5 (suitability) + 5 (10 - resource intensity) + 5 (5 - avg risk score) + 5 (timeline alignment) = 20
        # Adjust scales to be roughly comparable

        # 1. Suitability Score (from 5.2.2, already 0-5 scale)
        suitability_score = method_strengths_data.get("overall_assessment", {}).get("suitability_rating", 0)

        # 2. Resource Intensity Score (from 5.2.3, 1-5 scale, invert so high score is good)
        # Lower resource intensity is better for feasibility
        resource_intensity = method_resources_data.get("resource_intensity", {}).get("intensity_score", 5) # Default to high if missing
        resource_feasibility_score = max(0, 5 - (resource_intensity -1)) # Scale to 0-4, then adjust to make 5 best

        # 3. Risk Score (from 5.2.2, qualitative, needs quantification)
        # Average risk level (1=Low, 2=Moderate, 3=High - based on mitigation count/severity perception)
        risks_data = method_strengths_data.get("risks", {})
        num_timeline_risks = len(risks_data.get("timeline_risks", []))
        num_technical_risks = len(risks_data.get("technical_risks", []))
        # Simple risk score: lower is better.
        # Max 5 for low risk, min 1 for high risk.
        avg_risk_level = (num_timeline_risks + num_technical_risks) / 4 # Heuristic: >4 high, 2-4 mod, <2 low
        if avg_risk_level <= 1: risk_score_component = 5    # Low risk
        elif avg_risk_level <= 2: risk_score_component = 3.5  # Moderate risk
        else: risk_score_component = 2                      # High risk


        # 4. Timeline Alignment (from 5.2.3, qualitative, needs quantification)
        # Considering 20-week Master's thesis
        timeline_data = method_resources_data.get("time_resources", {})
        project_duration_str = timeline_data.get("total_project_duration", "20 weeks")
        timeline_alignment_score = 5 # Assume good alignment initially

        if "weeks" in project_duration_str:
            try:
                # Extract max duration if a range, e.g., "16-20 weeks"
                duration_max = int(project_duration_str.split('-')[-1].split(' ')[0])
                if duration_max > 20: timeline_alignment_score = 2 # Over budget
                elif duration_max > 18: timeline_alignment_score = 3.5 # Tight
                elif duration_max <= 16: timeline_alignment_score = 5 # Well within
                else: timeline_alignment_score = 4 # Good fit
            except ValueError:
                 if "very tight" in project_duration_str.lower() or "tight" in project_duration_str.lower() : timeline_alignment_score = 2.5
                 elif "flexible" in project_duration_str.lower(): timeline_alignment_score = 4.5


        # Total Feasibility Score
        # Normalizing factors can be added if scales are too different
        total_feasibility_score = (
            suitability_score * 0.30 +
            resource_feasibility_score * 0.30 +
            risk_score_component * 0.20 +
            timeline_alignment_score * 0.20
        )
        total_feasibility_score = round(max(0, min(5, total_feasibility_score)), 2) # Ensure score is 0-5

        # Qualitative Feasibility Assessment
        if total_feasibility_score >= 4.0: feasibility_category = "Highly Feasible"
        elif total_feasibility_score >= 3.0: feasibility_category = "Feasible with Conditions"
        elif total_feasibility_score >= 2.0: feasibility_category = "Moderately Feasible"
        else: feasibility_category = "Low Feasibility"

        # Recommendation Level
        if total_feasibility_score >= 4.2: recommendation = "Highly Recommended"
        elif total_feasibility_score >= 3.5: recommendation = "Recommended"
        elif total_feasibility_score >= 2.5: recommendation = "Use with Caution"
        else: recommendation = "Not Recommended"


        # Feasibility Enhancers and Inhibitors
        enhancers = []
        inhibitors = []

        # Strengths as enhancers
        enhancers.extend(method_strengths_data.get("strengths",{}).get("contextual_strengths", [])[:2])
        if suitability_score >=4: enhancers.append("High overall suitability for research context.")

        # Resource optimization as enhancers
        enhancers.extend(method_resources_data.get("resource_optimization",{}).get("efficiency_improvements", [])[:1])
        if resource_feasibility_score >=4 : enhancers.append("Manageable resource intensity.")

        # Limitations as inhibitors
        inhibitors.extend(method_strengths_data.get("limitations",{}).get("contextual_limitations", [])[:2])
        if suitability_score < 3: inhibitors.append("Lower suitability for specific research goals.")

        # Critical constraints as inhibitors
        inhibitors.extend(method_resources_data.get("feasibility_constraints",{}).get("critical_constraints", [])[:2])
        if resource_feasibility_score < 3 : inhibitors.append("High resource intensity poses challenges.")

        # Risks as inhibitors
        if risk_score_component < 3: inhibitors.append("Notable timeline or technical risks.")
        inhibitors.extend(risks_data.get("timeline_risks",[])[:1])


        feasibility_analyses[method_key] = {
            "methodology_name": method_strengths_data.get("methodology_name", method_key),
            "category": method_strengths_data.get("category", "Unknown"),
            "scores": {
                "suitability_score_contrib": round(suitability_score * 0.30, 2),
                "resource_feasibility_score_contrib": round(resource_feasibility_score * 0.30, 2),
                "risk_score_component_contrib": round(risk_score_component * 0.20, 2),
                "timeline_alignment_score_contrib": round(timeline_alignment_score * 0.20, 2),
                "total_feasibility_score": total_feasibility_score
            },
            "feasibility_category": feasibility_category,
            "recommendation": recommendation,
            "key_feasibility_enhancers": list(set(enhancers)), # Remove duplicates
            "key_feasibility_inhibitors": list(set(inhibitors)),
            "detailed_scores": {
                 "suitability_raw": suitability_score,
                 "resource_intensity_raw": resource_intensity,
                 "resource_feasibility_calc": resource_feasibility_score,
                 "risk_level_heuristic": avg_risk_level,
                 "risk_score_calc": risk_score_component,
                 "timeline_duration_eval": project_duration_str,
                 "timeline_alignment_calc": timeline_alignment_score
            }
        }

    return feasibility_analyses, research_context

def generate_markdown_summary(feasibility_analyses, research_context_details):
    """Generate markdown summary of feasibility analysis."""
    output_path = "../docs/5.2.4-feasibility-analysis.md"
    timestamp = datetime.now().isoformat()

    # Sort by total_feasibility_score descending
    sorted_analyses = sorted(
        feasibility_analyses.items(),
        key=lambda item: item[1]["scores"]["total_feasibility_score"],
        reverse=True
    )

    md_content = f"""# Methodology Feasibility Analysis (Task 5.2.4)

*Generated: {timestamp}*

## Research Context

**Focus**: {research_context_details['focus']}
**Domain**: {research_context_details['domain']}
**Timeframe**: {research_context_details['timeframe']}
**Key Constraints**: {', '.join(research_context_details['constraints'])}
**Methodologies Analyzed**: {len(feasibility_analyses)}

## Executive Summary - Feasibility Rankings

| Rank | Methodology                 | Category             | Feasibility Score | Recommendation         |
|------|-----------------------------|----------------------|-------------------|------------------------|
"""
    for i, (method_key, analysis) in enumerate(sorted_analyses):
        md_content += f"| {i+1:<4} | {analysis['methodology_name']:<27} | {analysis['category']:<20} | {analysis['scores']['total_feasibility_score']:<17.2f} | **{analysis['recommendation']}**      |\n"

    md_content += """

## Detailed Feasibility Assessments
"""

    for method_key, analysis in sorted_analyses:
        md_content += f"""
### {analysis['methodology_name']}
**Category**: {analysis['category']}
**Total Feasibility Score**: {analysis['scores']['total_feasibility_score']:.2f} ({analysis['feasibility_category']})
**Overall Recommendation**: **{analysis['recommendation']}**

**Score Breakdown (Contributions):**
- Suitability: {analysis['scores']['suitability_score_contrib']:.2f} (raw: {analysis['detailed_scores']['suitability_raw']:.2f})
- Resource Feasibility: {analysis['scores']['resource_feasibility_score_contrib']:.2f} (raw intensity: {analysis['detailed_scores']['resource_intensity_raw']:.2f}, calc: {analysis['detailed_scores']['resource_feasibility_calc']:.2f})
- Risk Mitigation: {analysis['scores']['risk_score_component_contrib']:.2f} (heuristic risk level: {analysis['detailed_scores']['risk_level_heuristic']:.2f}, calc: {analysis['detailed_scores']['risk_score_calc']:.2f})
- Timeline Alignment: {analysis['scores']['timeline_alignment_score_contrib']:.2f} (eval: '{analysis['detailed_scores']['timeline_duration_eval']}', calc: {analysis['detailed_scores']['timeline_alignment_calc']:.2f})

**Key Feasibility Enhancers:**
"""
        for enhancer in analysis['key_feasibility_enhancers']:
            md_content += f"- {enhancer}\n"
        if not analysis['key_feasibility_enhancers']: 
            md_content += "- None explicitly identified beyond general strengths.\n"

        md_content += """
**Key Feasibility Inhibitors:**
"""
        for inhibitor in analysis['key_feasibility_inhibitors']:
            md_content += f"- {inhibitor}\n"
        if not analysis['key_feasibility_inhibitors']:
            md_content += "- None explicitly identified beyond general limitations/risks.\n"
        md_content += "\n---\n"

    md_content += """\n## Feasibility Considerations Summary

- **Highly Recommended Methodologies** are those with strong alignment across suitability, resource manageability, risk profile, and timeline.
- **Feasible with Conditions** methodologies may require specific strategies to mitigate identified inhibitors (e.g., securing specific resources, careful risk management).
- **Low Feasibility** or **Not Recommended** methodologies present significant challenges within the defined research context and constraints, often due to high resource needs, excessive risks, or poor timeline fit for a 20-week individual Master's thesis.

## Next Steps
- Task 5.3.1: Select primary methodology, considering this feasibility analysis. The user will be prompted for this selection.
"""

    with open(output_path, 'w') as f:
        f.write(md_content)
    print(f"✅ Markdown summary saved to: {output_path}")

def main():
    """Main execution function"""
    os.makedirs("../docs", exist_ok=True)
    print("🔍 Task 5.2.4: Analyzing Methodology Feasibility")
    print("=" * 70)

    try:
        print("📊 Analyzing feasibility based on previous task outputs...")
        feasibility_analyses, research_context = analyze_feasibility()

        analysis_report = {
            "metadata": {
                "task": "5.2.4 - Analyze Feasibility",
                "timestamp": datetime.now().isoformat(),
                "scope": "Top-ranked methodologies from Tasks 5.2.1, 5.2.2, and 5.2.3",
                "methodologies_analyzed": len(feasibility_analyses)
            },
            "research_context": research_context,
            "feasibility_analyses": feasibility_analyses
        }

        json_file = "../docs/5.2.4-feasibility-analysis.json"
        with open(json_file, 'w') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        print(f"✅ Detailed feasibility analysis saved to: {json_file}")

        generate_markdown_summary(feasibility_analyses, research_context)

        print(f"✅ Feasibility analysis complete for {len(feasibility_analyses)} methodologies.")
        print("🎯 Ready for Task 5.3.1: Select primary methodology (User Prompt)")

    except FileNotFoundError as e:
        print(f"❌ Error: Required input file not found. {e}")
        print("Please ensure Tasks 5.2.1, 5.2.2, and 5.2.3 have been run successfully.")
    except Exception as e:
        print(f"❌ Error in feasibility analysis: {e}")
        # import traceback
        # traceback.print_exc() # Uncomment for detailed debugging if needed
        raise

if __name__ == "__main__":
    main() 
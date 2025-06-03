#!/usr/bin/env python3
"""
Task 5.2.3: Assess Resource Requirements (Updated)

Focus: Detailed resource assessment for identified methodologies.
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Results from docs/5.2.1-methodology-comparison-matrix.json (Updated)
- Results from docs/5.2.2-methodology-strengths-limitations.json (Updated)
- Detailed assessment logic adapted from archived 5.2.3 script.
"""

import json
from datetime import datetime
from pathlib import Path
import os # Keep for existing os.path checks if any, though Path is primary

# --- Configuration ---
COMPARISON_MATRIX_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.2.1-methodology-comparison-matrix.json"
STRENGTHS_LIMITATIONS_INPUT_JSON = Path(__file__).resolve().parent.parent / "docs" / "5.2.2-methodology-strengths-limitations.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.2.3_assess_resource_requirements_updated.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analyses ---
def load_previous_analyses_updated():
    comparison_matrix = {}
    strengths_analysis_data = {}

    if COMPARISON_MATRIX_INPUT_JSON.exists():
        try:
            with open(COMPARISON_MATRIX_INPUT_JSON, 'r', encoding='utf-8') as f:
                comparison_matrix = json.load(f)
            write_log(f"Loaded comparison matrix from {COMPARISON_MATRIX_INPUT_JSON}")
        except Exception as e:
            write_log(f"Error loading {COMPARISON_MATRIX_INPUT_JSON}: {e}")
    else:
        write_log(f"Error: {COMPARISON_MATRIX_INPUT_JSON} not found.")

    if STRENGTHS_LIMITATIONS_INPUT_JSON.exists():
        try:
            with open(STRENGTHS_LIMITATIONS_INPUT_JSON, 'r', encoding='utf-8') as f:
                strengths_analysis_data = json.load(f)
            write_log(f"Loaded strengths/limitations analysis from {STRENGTHS_LIMITATIONS_INPUT_JSON}")
        except Exception as e:
            write_log(f"Error loading {STRENGTHS_LIMITATIONS_INPUT_JSON}: {e}")
    else:
        write_log(f"Error: {STRENGTHS_LIMITATIONS_INPUT_JSON} not found.")
        
    return comparison_matrix, strengths_analysis_data

# --- Detailed Resource Assessment Functions (Adapted from Archive) ---
# These functions contain the detailed, hardcoded knowledge for common methodologies.

research_context_global = {
    "timeframe": "20 weeks",
    "project_type": "Master's thesis",
    "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
    "domain": "Distributed Energy Resources (DER) predictive maintenance",
    "constraints": ["Individual project", "Academic environment", "Limited budget"]
}

def assess_human_resources(method_key, method_data):
    human_resources = {
        "researcher_expertise_required": [], "additional_expertise_needed": [],
        "collaboration_requirements": [], "supervision_needs": ["Regular supervisor check-ins"],
        "time_commitment_breakdown": {"general_research": "20%", "method_specific_work": "60%", "writing": "20%"},
        "skill_development_required": []
    }
    # Default populated from method_data if possible, then specific overrides
    if "DSR" in method_data.get("name","") or "design_science" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Artifact design and development skills", "DSR methodology expertise"],
            "additional_expertise_needed": ["Technical expert for artifact validation"],
            "time_commitment_breakdown": {"artifact_development": "50%", "evaluation_design": "20%", "validation_execution": "20%", "documentation": "10%"}
        })
    elif "digital_twin" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Mathematical modeling and simulation skills", "DER systems domain knowledge"],
            "time_commitment_breakdown": {"model_development": "50%", "simulation_execution": "25%", "validation_analysis": "15%", "documentation": "10%"}
        })
    elif "case_study" in method_key:
         human_resources.update({
            "researcher_expertise_required": ["Qualitative data collection (interviews, observation)", "Qualitative data analysis"],
            "additional_expertise_needed": ["Access to case study sites/participants"],
             "time_commitment_breakdown": {"case_selection_access": "15%", "data_collection": "40%", "data_analysis": "30%", "write_up": "15%"}
         })
    # Add more specific overrides based on method_key or method_data content
    return human_resources

def assess_technical_resources(method_key, method_data):
    technical_resources = {
        "software_requirements": ["Standard office suite", "Reference manager"],
        "hardware_requirements": ["Standard research workstation"],
        "infrastructure_needs": ["University library access", "Internet connectivity"],
        "data_requirements": ["Relevant literature"],
        "computational_requirements": ["Low for most, varies by specific tasks"],
        "licensing_costs": ["Mostly open-source or institutional licenses"]
    }
    if "DSR" in method_data.get("name","") or "design_science" in method_key:
        technical_resources["software_requirements"].extend(["Development environment (IDE, version control)", "Prototyping tools"])
    elif "digital_twin" in method_key:
        technical_resources["software_requirements"].extend(["Simulation software (e.g., MATLAB/Simulink, Python SimPy)", "Data analysis software"])
        technical_resources["hardware_requirements"].append("High-performance workstation recommended for complex simulations")
        technical_resources["computational_requirements"] = ["Potentially High - complex simulation models"]
        technical_resources["licensing_costs"].append(r"Potential for simulation software licenses (e.g., MATLAB academic ~$1000-3000 if not provided)")
    return technical_resources

def assess_financial_resources(method_key, method_data):
    financial_resources = {
        "direct_costs": {"software_licenses_optional": r"$0-500", "conference_travel_optional": r"$500-1500"},
        "indirect_costs": {"university_overheads": "Covered by tuition/stipend"},
        "total_estimated_budget": "Low (mostly relies on existing resources)",
        "funding_sources": ["Personal, departmental small grants"],
        "cost_mitigation_strategies": ["Utilize open-source software", "Leverage university resources"]
    }
    if "digital_twin" in method_key:
        financial_resources["direct_costs"]["simulation_software_if_needed"] = r"$1000-3000"
        financial_resources["total_estimated_budget"] = "Low to Moderate (if simulation software needed)"
    elif "case_study" in method_key:
        financial_resources["direct_costs"]["travel_for_interviews_optional"] = r"$100-500"
        financial_resources["direct_costs"]["transcription_services_optional"] = r"$200-800"
    return financial_resources

def assess_access_resources(method_key, method_data):
    access_resources = {
        "data_access_needs": ["Access to scientific databases and literature"],
        "stakeholder_access_requirements": ["Supervisor and peer feedback"],
        "system_access_needs": ["University IT infrastructure"],
        "institutional_approvals": ["Ethics approval if human subjects involved (e.g. surveys, interviews in case studies)"],
        "access_barriers": [], "access_facilitation_strategies": []
    }
    if "case_study" in method_key or "interview" in method_data.get("name","").lower():
        access_resources["stakeholder_access_requirements"].append("Access to interview participants or case study organizations")
        access_resources["access_barriers"].append("Gatekeeper permissions, participant availability")
        access_resources["access_facilitation_strategies"].extend(["Clear communication of research benefits", "Flexible scheduling"])
    return access_resources

def assess_time_resources(method_key, method_data):
    time_resources = {
        "total_project_duration": method_data.get("timeline", "20 weeks (standard thesis duration)"),
        "phase_breakdown": {"literature_review": "4-6 weeks", "method_application": "8-10 weeks", "analysis_writing": "4-6 weeks"},
        "critical_path_activities": ["Defining research scope", "Data collection/artifact development (method-dependent)"],
        "timeline_risks": ["Underestimation of specific phases", "Scope creep"],
        "schedule_optimization": ["Detailed planning", "Regular progress reviews"]
    }
    # Specific timeline details would come from the method_data (populated by 5.2.1 from KBs)
    if method_data.get("timeline") and method_data.get("timeline") != "To be determined":
        time_resources["total_project_duration"] = method_data["timeline"]
        # Potentially parse detailed phases if available in method_data
    return time_resources

def calculate_resource_intensity(method_key, method_data, all_resource_aspects:dict):
    # Simplified intensity calculation. Could be more nuanced.
    score = 3 # Default Moderate
    is_high_in_summary = "High" in method_data.get("resource_requirements_summary","")
    is_high_in_aspects = any(
        "High" in str(v) 
        for aspect in all_resource_aspects.values() 
        for v in aspect.values() if isinstance(v,list) and "High" in str(v)
    )

    if is_high_in_summary or is_high_in_aspects:
        score = 4 # Moderate to High
    if "Very High" in method_data.get("resource_requirements_summary",""):
        score = 5 # High
    if "Low" in method_data.get("resource_requirements_summary",""):
        score = 2 # Low to Moderate
    
    levels = {1:"Very Low", 2:"Low", 3:"Moderate", 4:"High", 5:"Very High"}
    intensity_score_for_reporting = score 
    if "digital_twin" in method_key: intensity_score_for_reporting = 4
    if "case_study" in method_key: intensity_score_for_reporting = 4
    if "sequential_explanatory" in method_key: intensity_score_for_reporting = 5
    
    return {
        "intensity_score": intensity_score_for_reporting, 
        "intensity_level": levels.get(intensity_score_for_reporting, "Moderate"),
        "summary_from_521": method_data.get("resource_requirements_summary","N/A")
    }

def identify_feasibility_constraints(method_key, method_data, all_resource_aspects:dict):
    constraints = {"critical_constraints": [], "moderate_constraints": []}
    if "digital_twin" in method_key:
        constraints["critical_constraints"].extend(["Access to DER system data/specifications for model", "Computational resources for simulation"])
    if "case_study" in method_key:
        constraints["critical_constraints"].append("Access to suitable case study sites and participants")
    
    feasibility_20_weeks_lower = method_data.get("feasibility_20_weeks", "").lower()
    if feasibility_20_weeks_lower == "challenging" or feasibility_20_weeks_lower == "poor":
        constraints["critical_constraints"].append(f"Timeline feasibility for 20 weeks noted as '{method_data.get('feasibility_20_weeks')}'")
    return constraints

def suggest_resource_optimization(method_key, method_data):
    optimization = {"cost_reduction": ["Prioritize open-source tools"], "time_optimization": ["Clear task breakdown and regular reviews"]}
    if "digital_twin" in method_key:
        optimization["cost_reduction"].append("Explore academic licenses for simulation software")
        optimization["time_optimization"].append("Iterative model development: start simple")
    return optimization

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.2.3 (Assess Resource Requirements - Updated) at {datetime.now().isoformat()}\n")

    print("💰 Task 5.2.3 (Updated): Assessing Resource Requirements")
    print("=" * 70)

    comparison_matrix, strengths_analysis_data = load_previous_analyses_updated()

    if not comparison_matrix or "methodologies" not in comparison_matrix:
        write_log("Aborting: Comparison matrix data from 5.2.1 is missing or invalid.")
        print("Error: Could not load valid data from 5.2.1-methodology-comparison-matrix.json. Aborting.")
        return
    
    # Use methodologies from the 5.2.1 comparison matrix as the primary list
    input_methodologies_from_521 = comparison_matrix.get("methodologies", {})
    methodology_scores_from_521 = comparison_matrix.get("methodology_scores", {})
    write_log(f"Loaded {len(input_methodologies_from_521)} methodologies from 5.2.1 data.")

    resource_assessments = {}
    for key, meth_521_data in input_methodologies_from_521.items():
        if not meth_521_data: # Skip if data is empty for some reason
            write_log(f"Skipping methodology key {key} due to empty data from 5.2.1 matrix.")
            continue
        
        # Combine all resource aspects for intensity calculation
        current_assessment = {
            "human_resources": assess_human_resources(key, meth_521_data),
            "technical_resources": assess_technical_resources(key, meth_521_data),
            "financial_resources": assess_financial_resources(key, meth_521_data),
            "access_resources": assess_access_resources(key, meth_521_data),
            "time_resources": assess_time_resources(key, meth_521_data),
        }
        current_assessment["resource_intensity"] = calculate_resource_intensity(key, meth_521_data, current_assessment)
        current_assessment["feasibility_constraints"] = identify_feasibility_constraints(key, meth_521_data, current_assessment)
        current_assessment["resource_optimization"] = suggest_resource_optimization(key, meth_521_data)
        
        # Add some metadata from 5.2.1 for context
        current_assessment["methodology_name"] = meth_521_data.get("name", key.replace("_"," ").title())
        current_assessment["category"] = meth_521_data.get("category", "N/A")
        current_assessment["ranking_score_from_521"] = methodology_scores_from_521.get(key, {}).get("weighted_total", "N/A")

        resource_assessments[key] = current_assessment
        write_log(f"Assessed resources for: {current_assessment['methodology_name']}")

    analysis_report = {
        "metadata": {
            "task": "5.2.3 - Assess Resource Requirements (Updated)",
            "timestamp": datetime.now().isoformat(),
            "input_sources": [str(COMPARISON_MATRIX_INPUT_JSON.name), str(STRENGTHS_LIMITATIONS_INPUT_JSON.name)],
            "methodologies_assessed": len(resource_assessments)
        },
        "research_context": research_context_global,
        "resource_assessments": resource_assessments
    }

    # Save JSON output
    json_output_path = OUTPUT_DOCS_DIR / "5.2.3-resource-requirements-assessment.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON resource assessment saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")

    # Generate Markdown summary
    md_parts = [f"# Resource Requirements Assessment (Task 5.2.3 - Updated)\n"]
    md_parts.append(f"*Generated: {analysis_report['metadata']['timestamp']}*\n")
    md_parts.append(f"*Based on methodologies from: {Path(COMPARISON_MATRIX_INPUT_JSON).name}*\n\n")
    md_parts.append(f"## Research Context\n- Focus: {research_context_global['focus']}\n- Domain: {research_context_global['domain']}\n- Constraints: { ', '.join(research_context_global['constraints']) }\n\n")

    # Sort by resource intensity for presentation (higher intensity first)
    sorted_assessments = sorted(
        resource_assessments.items(),
        key=lambda item: item[1]["resource_intensity"]["intensity_score"],
        reverse=True
    )

    for key, assessment in sorted_assessments:
        md_parts.append(f"### {assessment['methodology_name']}\n")
        md_parts.append(f"- **Category**: {assessment.get('category', 'N/A')}\n")
        md_parts.append(f"- **Resource Intensity**: {assessment['resource_intensity']['intensity_level']} (Score: {assessment['resource_intensity']['intensity_score']})\n")
        md_parts.append(f"- **Human Resources Summary**: Expertise in {assessment['human_resources']['researcher_expertise_required'][:1]}... Needs: {assessment['human_resources']['additional_expertise_needed'][:1]}... \n")
        md_parts.append(f"- **Technical Resources Summary**: Software like {assessment['technical_resources']['software_requirements'][:2]}... Hardware: {assessment['technical_resources']['hardware_requirements'][:1]}...\n")
        md_parts.append(f"- **Estimated Budget Indication**: {assessment['financial_resources']['total_estimated_budget']}\n")
        md_parts.append(f"- **Time Resources Summary**: Duration {assessment['time_resources']['total_project_duration']}\n")
        if assessment["feasibility_constraints"]["critical_constraints"]:
            md_parts.append(f"- **Critical Constraints**: { '; '.join(assessment['feasibility_constraints']['critical_constraints']) }\n")
        md_parts.append("---\n")

    md_parts.append("\n## Next Steps\n- Task 5.2.4: Analyze implementation feasibility based on these resource constraints.\n")
    md_summary = "".join(md_parts)
    md_output_path = OUTPUT_SOURCES_DIR / "5.2.3-resource-requirements-assessment.md"
    try:
        OUTPUT_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(md_summary)
        write_log(f"Markdown resource assessment summary saved to {md_output_path}")
        print(f"Markdown summary saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving Markdown summary: {e}")

    write_log(f"Finished Task 5.2.3 (Updated) at {datetime.now().isoformat()}")
    print("\n✅ Task 5.2.3 (Updated) complete.")

if __name__ == "__main__":
    main() 
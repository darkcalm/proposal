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
COMPARISON_MATRIX_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.1-methodology-comparison-matrix.json"
STRENGTHS_LIMITATIONS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.2-methodology-strengths-limitations.json"
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
    # Comprehensive overrides for all methodologies
    if "design_science_research" in method_key or "DSR" in method_data.get("name",""):
        human_resources.update({
            "researcher_expertise_required": ["Artifact design and development skills", "DSR methodology expertise", "Software architecture and development", "Systematic evaluation methodology"],
            "additional_expertise_needed": ["Technical expert for artifact validation", "Industry partners for realistic evaluation"],
            "time_commitment_breakdown": {"artifact_development": "50%", "evaluation_design": "20%", "validation_execution": "20%", "documentation": "10%"},
            "skill_development_required": ["Advanced programming skills", "System design patterns", "Evaluation framework design"]
        })
    elif "digital_twin" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Mathematical modeling and simulation skills", "DER systems domain knowledge", "Programming for simulation environments", "Statistical analysis and validation techniques"],
            "additional_expertise_needed": ["DER system experts", "Simulation software specialists"],
            "time_commitment_breakdown": {"model_development": "50%", "simulation_execution": "25%", "validation_analysis": "15%", "documentation": "10%"},
            "skill_development_required": ["Advanced simulation techniques", "DER system modeling", "Validation methodologies"]
        })
    elif "case_study" in method_key:
         human_resources.update({
            "researcher_expertise_required": ["Qualitative data collection (interviews, observation)", "Qualitative data analysis", "Case study methodology", "Interview techniques"],
            "additional_expertise_needed": ["Access to case study sites/participants", "Gatekeepers for organizational access"],
             "time_commitment_breakdown": {"case_selection_access": "15%", "data_collection": "40%", "data_analysis": "30%", "write_up": "15%"},
             "skill_development_required": ["Advanced interviewing skills", "Qualitative coding", "Case analysis techniques"]
         })
    elif "participatory_design" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Facilitation skills", "Stakeholder engagement", "Design thinking", "Group dynamics management"],
            "additional_expertise_needed": ["Diverse stakeholder representatives", "Co-design facilitators"],
            "time_commitment_breakdown": {"stakeholder_recruitment": "20%", "design_sessions": "40%", "synthesis": "25%", "documentation": "15%"},
            "skill_development_required": ["Workshop facilitation", "Conflict resolution", "Design synthesis"]
        })
    elif "experimental_research" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Experimental design methodology", "Statistical analysis and hypothesis testing", "Protocol performance measurement", "Controlled environment setup"],
            "additional_expertise_needed": ["Statistical consultant", "Experimental environment access"],
            "time_commitment_breakdown": {"experimental_design": "25%", "setup_and_execution": "40%", "analysis_and_validation": "25%", "documentation": "10%"},
            "skill_development_required": ["Advanced statistics", "Experimental control techniques", "Data analysis software"]
        })
    elif "simulation_modeling" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Simulation modeling", "Programming", "System analysis", "Model validation"],
            "additional_expertise_needed": ["Domain experts for model validation", "Computational resources"],
            "time_commitment_breakdown": {"model_design": "30%", "implementation": "35%", "validation": "20%", "analysis": "15%"},
            "skill_development_required": ["Simulation software proficiency", "Model validation techniques", "Performance analysis"]
        })
    elif "computational_social_science" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Computational analysis", "Social network analysis", "Big data processing", "Programming skills"],
            "additional_expertise_needed": ["Data access partnerships", "Computational infrastructure"],
            "time_commitment_breakdown": {"data_acquisition": "25%", "analysis_development": "40%", "interpretation": "25%", "documentation": "10%"},
            "skill_development_required": ["Advanced programming", "Network analysis tools", "Large-scale data processing"]
        })
    elif "ai_explainability" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["AI/ML expertise", "Explainability methods", "Human-computer interaction", "Evaluation techniques"],
            "additional_expertise_needed": ["Domain experts for explanation validation", "End users for testing"],
            "time_commitment_breakdown": {"system_development": "45%", "explanation_design": "25%", "validation": "20%", "documentation": "10%"},
            "skill_development_required": ["XAI frameworks", "User testing methods", "Explanation evaluation"]
        })
    elif "human_ai_collaboration" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Human-computer interaction", "AI system design", "User experience design", "Collaboration frameworks"],
            "additional_expertise_needed": ["End users for testing", "AI development team", "UX designers"],
            "time_commitment_breakdown": {"interaction_design": "35%", "implementation": "30%", "user_testing": "25%", "refinement": "10%"},
            "skill_development_required": ["Interaction design", "User testing", "Collaborative AI systems"]
        })
    elif "living_lab" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Multi-stakeholder management", "Innovation management", "Real-world experimentation", "Partnership development"],
            "additional_expertise_needed": ["Industry partners", "Community stakeholders", "Infrastructure providers"],
            "time_commitment_breakdown": {"partnership_development": "30%", "experimentation": "40%", "evaluation": "20%", "dissemination": "10%"},
            "skill_development_required": ["Partnership negotiation", "Real-world experimentation", "Stakeholder management"]
        })
    elif "systematic_literature_review" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Systematic review methodology", "Literature search techniques", "Critical appraisal", "Evidence synthesis"],
            "additional_expertise_needed": ["Librarian for search strategy", "Second reviewer for quality assessment"],
            "time_commitment_breakdown": {"search_and_screening": "40%", "quality_assessment": "25%", "data_extraction": "20%", "synthesis": "15%"},
            "skill_development_required": ["Database searching", "Critical appraisal tools", "Evidence synthesis methods"]
        })
    elif "comparative_research" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Comparative methodology", "Framework development", "Systematic evaluation", "Literature analysis"],
            "additional_expertise_needed": ["Domain experts for framework validation", "Access to comparison cases"],
            "time_commitment_breakdown": {"framework_development": "30%", "data_collection": "35%", "comparative_analysis": "25%", "synthesis": "10%"},
            "skill_development_required": ["Comparative analysis techniques", "Framework development", "Multi-criteria evaluation"]
        })
    elif "optimization_research" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Mathematical optimization", "Algorithm development", "Performance analysis", "Model formulation"],
            "additional_expertise_needed": ["Mathematics/operations research consultant", "Domain experts for constraint definition"],
            "time_commitment_breakdown": {"problem_formulation": "30%", "algorithm_development": "35%", "optimization": "25%", "validation": "10%"},
            "skill_development_required": ["Optimization algorithms", "Mathematical modeling", "Performance evaluation"]
        })
    elif "rapid_prototyping" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Software development", "Agile methodology", "Rapid iteration", "Stakeholder engagement"],
            "additional_expertise_needed": ["Stakeholders for feedback", "Technical mentors"],
            "time_commitment_breakdown": {"development": "60%", "stakeholder_engagement": "15%", "iteration": "15%", "documentation": "10%"},
            "skill_development_required": ["Rapid development techniques", "Agile practices", "Continuous integration"]
        })
    elif "agent_based_modeling" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Agent-based modeling", "Complex systems", "Programming", "Emergent behavior analysis"],
            "additional_expertise_needed": ["ABM specialists", "Domain experts for agent behavior"],
            "time_commitment_breakdown": {"agent_design": "30%", "model_implementation": "35%", "simulation": "20%", "analysis": "15%"},
            "skill_development_required": ["ABM platforms", "Complex systems analysis", "Emergent behavior interpretation"]
        })
    elif "action_research" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Action research methodology", "Organizational development", "Participatory methods", "Change management"],
            "additional_expertise_needed": ["Organizational partners", "Change champions", "Stakeholder representatives"],
            "time_commitment_breakdown": {"action_planning": "25%", "action_implementation": "40%", "reflection": "20%", "documentation": "15%"},
            "skill_development_required": ["Organizational intervention", "Participatory evaluation", "Change facilitation"]
        })
    elif "grounded_theory" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Grounded theory methodology", "Qualitative data collection", "Theoretical coding", "Constant comparison"],
            "additional_expertise_needed": ["Participants for theoretical sampling", "Grounded theory expert"],
            "time_commitment_breakdown": {"data_collection": "40%", "coding_analysis": "35%", "theory_development": "15%", "validation": "10%"},
            "skill_development_required": ["Theoretical coding", "Constant comparison", "Theory development"]
        })
    elif "ethnography" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Ethnographic methods", "Participant observation", "Cultural analysis", "Field work"],
            "additional_expertise_needed": ["Community access", "Cultural informants", "Safety support"],
            "time_commitment_breakdown": {"field_access": "15%", "fieldwork": "50%", "analysis": "25%", "writing": "10%"},
            "skill_development_required": ["Participant observation", "Cultural analysis", "Field note techniques"]
        })
    elif "delphi" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Delphi methodology", "Expert panel management", "Consensus analysis", "Survey design"],
            "additional_expertise_needed": ["Expert panel members", "Survey platform access"],
            "time_commitment_breakdown": {"expert_recruitment": "20%", "round_execution": "50%", "analysis": "20%", "synthesis": "10%"},
            "skill_development_required": ["Expert panel management", "Consensus measurement", "Iterative survey design"]
        })
    elif "mixed_methods" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Mixed methods design", "Quantitative methods", "Qualitative methods", "Integration techniques"],
            "additional_expertise_needed": ["Statistical consultant", "Qualitative expert", "Integration specialist"],
            "time_commitment_breakdown": {"quantitative_phase": "40%", "qualitative_phase": "35%", "integration": "15%", "synthesis": "10%"},
            "skill_development_required": ["Method integration", "Multi-paradigm thinking", "Complex analysis"]
        })
    elif "content_analysis" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Content analysis methodology", "Coding scheme development", "Text analysis", "Reliability assessment"],
            "additional_expertise_needed": ["Second coder for reliability", "Domain experts for code validation"],
            "time_commitment_breakdown": {"coding_scheme": "25%", "coding": "40%", "reliability_testing": "20%", "analysis": "15%"},
            "skill_development_required": ["Systematic coding", "Inter-rater reliability", "Text analysis software"]
        })
    elif "sequential_explanatory" in method_key:
        human_resources.update({
            "researcher_expertise_required": ["Sequential mixed methods", "Quantitative analysis", "Qualitative follow-up", "Integration skills"],
            "additional_expertise_needed": ["Phase 1 participants", "Phase 2 interview participants", "Mixed methods expert"],
            "time_commitment_breakdown": {"quantitative_phase": "45%", "qualitative_phase": "35%", "integration": "15%", "synthesis": "5%"},
            "skill_development_required": ["Sequential design", "Phase integration", "Explanatory analysis"]
        })
    
    return human_resources

def assess_technical_resources(method_key, method_data):
    technical_resources = {
        "software_requirements": ["Standard office suite", "Reference manager"],
        "hardware_requirements": ["Standard research workstation"],
        "infrastructure_needs": ["University library access", "Internet connectivity"],
        "data_requirements": ["Relevant literature"],
        "computational_requirements": ["Low for most, varies by specific tasks"],
        "licensing_costs": ["Mostly open-source or institutional licenses"],
        "specialized_tools": []
    }
    
    if "design_science_research" in method_key or "DSR" in method_data.get("name",""):
        technical_resources.update({
            "software_requirements": ["Development environment (IDE, version control)", "Prototyping tools (e.g., Figma, Adobe XD, or specific coding frameworks)", "Modeling tools (UML, BPMN)", "Data analysis software for evaluation"],
            "hardware_requirements": ["High-performance development workstation", "Testing devices/environments"],
            "computational_requirements": ["Moderate to high, depending on artifact complexity and evaluation methods"],
            "licensing_costs": ["Development tools ($100-1000)", "Design software ($200-600)", "Cloud services ($50-200)"],
            "specialized_tools": ["Artifact development frameworks", "Evaluation platforms", "Version control systems"]
        })
    elif "digital_twin" in method_key:
        technical_resources.update({
            "software_requirements": ["Simulation software (MATLAB/Simulink, Python SimPy, specialized DER simulators)", "Mathematical modeling tools", "Data analysis software", "Visualization tools"],
            "hardware_requirements": ["High-performance workstation for complex simulations", "Parallel processing capabilities", "Large memory capacity"],
            "computational_requirements": ["High - complex simulation models, long-running simulation jobs"],
            "licensing_costs": ["Simulation software ($1000-3000 if not institutional)", "Computational cloud resources ($200-800)"],
            "specialized_tools": ["DER system modeling software", "Simulation validation tools", "Performance monitoring systems"]
        })
    elif "case_study" in method_key:
        technical_resources.update({
            "software_requirements": ["Qualitative data analysis software (NVivo, ATLAS.ti)", "Interview recording software", "Transcription tools", "Document analysis tools"],
            "hardware_requirements": ["Recording equipment", "Secure data storage", "Mobile computing for field work"],
            "data_requirements": ["Case study access agreements", "Interview recordings", "Organizational documents"],
            "licensing_costs": ["QDA software ($0-500 with academic licenses)", "Transcription services ($200-800)"],
            "specialized_tools": ["Interview recording equipment", "Field note software", "Data anonymization tools"]
        })
    elif "participatory_design" in method_key:
        technical_resources.update({
            "software_requirements": ["Collaboration platforms", "Design thinking tools", "Workshop facilitation software", "Feedback collection systems"],
            "hardware_requirements": ["Presentation equipment", "Workshop materials", "Mobile devices for participants"],
            "infrastructure_needs": ["Workshop spaces", "Video conferencing capabilities", "Collaborative workspace"],
            "specialized_tools": ["Digital whiteboards", "Voting systems", "Collaborative design platforms"]
        })
    elif "experimental_research" in method_key:
        technical_resources.update({
            "software_requirements": ["Experiment control software", "Data logging and acquisition software", "Statistical analysis software", "Stimulus presentation software"],
            "hardware_requirements": ["Experimental equipment", "Data collection sensors", "Controlled environment setup"],
            "computational_requirements": ["Moderate to high for statistical analysis and large datasets"],
            "licensing_costs": ["Statistical software ($200-1000)", "Experimental software ($200-2000)", "Equipment rental ($200-5000+)"],
            "specialized_tools": ["Experimental control systems", "Data acquisition hardware", "Statistical analysis platforms"]
        })
    elif "simulation_modeling" in method_key:
        technical_resources.update({
            "software_requirements": ["Simulation platforms", "Modeling software", "Data analysis tools", "Visualization software"],
            "hardware_requirements": ["Computational workstation", "Sufficient RAM and processing power"],
            "computational_requirements": ["Moderate to high depending on model complexity"],
            "licensing_costs": ["Simulation software ($500-2000)", "Cloud computing ($100-500)"],
            "specialized_tools": ["Domain-specific simulation tools", "Model validation software", "Performance analysis tools"]
        })
    elif "computational_social_science" in method_key:
        technical_resources.update({
            "software_requirements": ["Programming environments (Python, R)", "Network analysis tools", "Big data processing frameworks", "Machine learning libraries"],
            "hardware_requirements": ["High-performance computing resources", "Large storage capacity", "GPU for complex analyses"],
            "computational_requirements": ["High - large dataset processing, complex algorithms"],
            "data_requirements": ["Large-scale social/communication datasets", "Network data", "Behavioral data"],
            "specialized_tools": ["Social network analysis software", "Big data platforms", "Computational clusters"]
        })
    elif "ai_explainability" in method_key:
        technical_resources.update({
            "software_requirements": ["AI/ML development frameworks", "Explainability libraries", "User interface development tools", "Evaluation platforms"],
            "hardware_requirements": ["AI development workstation", "GPU for model training", "User testing equipment"],
            "computational_requirements": ["High for AI model development and explanation generation"],
            "specialized_tools": ["XAI frameworks (LIME, SHAP)", "Model interpretation tools", "User testing platforms"]
        })
    elif "human_ai_collaboration" in method_key:
        technical_resources.update({
            "software_requirements": ["AI development platforms", "User interface frameworks", "Collaboration software", "User testing tools"],
            "hardware_requirements": ["Development workstation", "User testing lab", "Interaction devices"],
            "computational_requirements": ["Moderate to high for AI components and interaction systems"],
            "specialized_tools": ["Human-AI interaction frameworks", "User experience testing tools", "Collaborative AI platforms"]
        })
    elif "living_lab" in method_key:
        technical_resources.update({
            "software_requirements": ["Real-world monitoring systems", "Data collection platforms", "Collaboration tools", "Innovation management software"],
            "hardware_requirements": ["Sensing equipment", "Communication infrastructure", "Mobile computing"],
            "infrastructure_needs": ["Real-world deployment environment", "Partner organization systems", "Communication networks"],
            "specialized_tools": ["IoT sensors", "Real-time monitoring systems", "Stakeholder engagement platforms"]
        })
    elif "systematic_literature_review" in method_key:
        technical_resources.update({
            "software_requirements": ["Reference management (Zotero, Mendeley)", "Literature search tools", "Systematic review software", "Data extraction tools"],
            "data_requirements": ["Access to academic databases", "Full-text articles", "Grey literature"],
            "specialized_tools": ["Systematic review platforms (Covidence, Rayyan)", "Citation analysis tools", "Quality assessment frameworks"]
        })
    elif "comparative_research" in method_key:
        technical_resources.update({
            "software_requirements": ["Data analysis software", "Comparison frameworks", "Visualization tools", "Statistical packages"],
            "data_requirements": ["Comparable datasets", "Literature sources", "Evaluation criteria"],
            "specialized_tools": ["Multi-criteria decision analysis tools", "Benchmarking software", "Comparative analysis platforms"]
        })
    elif "optimization_research" in method_key:
        technical_resources.update({
            "software_requirements": ["Optimization software (GAMS, CPLEX)", "Mathematical modeling tools", "Algorithm development environments", "Performance analysis tools"],
            "hardware_requirements": ["High-performance computing", "Substantial RAM", "Fast processors"],
            "computational_requirements": ["High - complex optimization problems, iterative algorithms"],
            "specialized_tools": ["Optimization solvers", "Mathematical programming languages", "Performance profiling tools"]
        })
    elif "rapid_prototyping" in method_key:
        technical_resources.update({
            "software_requirements": ["Development environments", "Version control systems", "Continuous integration tools", "Prototype testing frameworks"],
            "hardware_requirements": ["Development workstation", "Testing devices", "Deployment infrastructure"],
            "specialized_tools": ["Rapid development frameworks", "Automated testing tools", "Continuous deployment systems"]
        })
    elif "agent_based_modeling" in method_key:
        technical_resources.update({
            "software_requirements": ["ABM platforms (NetLogo, MASON, AnyLogic)", "Programming environments", "Simulation analysis tools", "Visualization software"],
            "hardware_requirements": ["High-performance workstation", "Sufficient memory for large simulations"],
            "computational_requirements": ["High - complex agent simulations, emergent behavior analysis"],
            "specialized_tools": ["Agent-based modeling platforms", "Behavior analysis tools", "Complex systems visualization"]
        })
    elif "action_research" in method_key:
        technical_resources.update({
            "software_requirements": ["Collaboration platforms", "Data collection tools", "Reflection and documentation software", "Stakeholder engagement tools"],
            "infrastructure_needs": ["Organizational access", "Meeting facilities", "Communication systems"],
            "specialized_tools": ["Participatory evaluation tools", "Change management software", "Stakeholder feedback systems"]
        })
    elif "grounded_theory" in method_key:
        technical_resources.update({
            "software_requirements": ["Qualitative data analysis software", "Coding tools", "Theory development platforms", "Data management systems"],
            "data_requirements": ["Rich qualitative data", "Interview transcripts", "Observational notes"],
            "specialized_tools": ["Grounded theory software modules", "Coding frameworks", "Theoretical modeling tools"]
        })
    elif "ethnography" in method_key:
        technical_resources.update({
            "software_requirements": ["Field note software", "Audio/video recording tools", "Cultural analysis software", "Data management systems"],
            "hardware_requirements": ["Recording equipment", "Field computing devices", "Secure storage"],
            "specialized_tools": ["Ethnographic data collection tools", "Cultural mapping software", "Field observation platforms"]
        })
    elif "delphi" in method_key:
        technical_resources.update({
            "software_requirements": ["Survey platforms", "Expert panel management tools", "Consensus analysis software", "Round management systems"],
            "infrastructure_needs": ["Anonymous communication platform", "Expert recruitment systems"],
            "specialized_tools": ["Delphi study platforms", "Consensus measurement tools", "Expert panel software"]
        })
    elif "mixed_methods" in method_key:
        technical_resources.update({
            "software_requirements": ["Quantitative analysis software", "Qualitative analysis tools", "Integration platforms", "Multi-method frameworks"],
            "computational_requirements": ["Moderate to high for complex multi-method analyses"],
            "specialized_tools": ["Mixed methods analysis software", "Data integration tools", "Multi-paradigm platforms"]
        })
    elif "content_analysis" in method_key:
        technical_resources.update({
            "software_requirements": ["Text analysis software", "Coding platforms", "Reliability analysis tools", "Content management systems"],
            "data_requirements": ["Text corpora", "Communication logs", "Document collections"],
            "specialized_tools": ["Content analysis software", "Text mining tools", "Inter-rater reliability platforms"]
        })
    elif "sequential_explanatory" in method_key:
        technical_resources.update({
            "software_requirements": ["Statistical analysis software", "Qualitative analysis tools", "Integration software", "Sequential design platforms"],
            "computational_requirements": ["Moderate for quantitative phase, lower for qualitative phase"],
            "specialized_tools": ["Sequential mixed methods software", "Phase integration tools", "Explanatory analysis platforms"]
        })
    
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
        "total_project_duration": "20 weeks (standard thesis duration)",  # Default
        "phase_breakdown": {"literature_review": "4-6 weeks", "method_application": "8-10 weeks", "analysis_writing": "4-6 weeks"},
        "critical_path_activities": ["Defining research scope", "Data collection/artifact development (method-dependent)"],
        "timeline_risks": ["Underestimation of specific phases", "Scope creep"],
        "schedule_optimization": ["Detailed planning", "Regular progress reviews"]
    }

    # Methodology-specific time estimates
    if "sequential_explanatory" in method_key:
        time_resources["total_project_duration"] = "24-26 weeks (extended due to sequential phases)"
        time_resources["phase_breakdown"] = {
            "quantitative_phase": "10-12 weeks",
            "qualitative_phase": "8-10 weeks",
            "integration": "4 weeks",
            "writing": "2-4 weeks"
        }
    elif "case_study" in method_key:
        time_resources["total_project_duration"] = "18-20 weeks (intensive data collection and analysis)"
        time_resources["phase_breakdown"] = {
            "case_selection": "2-3 weeks",
            "data_collection": "8-10 weeks",
            "analysis": "6-8 weeks",
            "writing": "2-3 weeks"
        }
    elif "digital_twin" in method_key:
        time_resources["total_project_duration"] = "20-22 weeks (model development and validation intensive)"
        time_resources["phase_breakdown"] = {
            "model_design": "6-8 weeks",
            "implementation": "8-10 weeks",
            "validation": "4-6 weeks",
            "documentation": "2-4 weeks"
        }
    elif "optimization_research" in method_key:
        time_resources["total_project_duration"] = "16-20 weeks (iterative algorithm development and testing)"
        time_resources["phase_breakdown"] = {
            "problem_formulation": "4-6 weeks",
            "algorithm_development": "6-8 weeks",
            "testing": "4-6 weeks",
            "documentation": "2-4 weeks"
        }
    elif "agent_based_modeling" in method_key:
        time_resources["total_project_duration"] = "20-24 weeks (complex model development and validation)"
        time_resources["phase_breakdown"] = {
            "model_design": "6-8 weeks",
            "implementation": "8-10 weeks",
            "validation": "4-6 weeks",
            "analysis": "2-4 weeks"
        }
    elif "computational_social_science" in method_key:
        time_resources["total_project_duration"] = "18-22 weeks (data collection and computational analysis)"
        time_resources["phase_breakdown"] = {
            "data_collection": "6-8 weeks",
            "analysis": "8-10 weeks",
            "interpretation": "4-6 weeks"
        }
    elif "ai_explainability" in method_key:
        time_resources["total_project_duration"] = "18-22 weeks (model development and explanation framework)"
        time_resources["phase_breakdown"] = {
            "model_development": "8-10 weeks",
            "explanation_framework": "6-8 weeks",
            "validation": "4-6 weeks"
        }
    elif "design_science_research" in method_key or "DSR" in method_data.get("name",""):
        time_resources["total_project_duration"] = "20 weeks (artifact development and evaluation cycles)"
        time_resources["phase_breakdown"] = {
            "design": "6-8 weeks",
            "development": "8-10 weeks",
            "evaluation": "4-6 weeks"
        }
    elif "mixed_methods" in method_key:
        time_resources["total_project_duration"] = "20-22 weeks (parallel quantitative and qualitative phases)"
        time_resources["phase_breakdown"] = {
            "quantitative": "8-10 weeks",
            "qualitative": "8-10 weeks",
            "integration": "4-6 weeks"
        }
    elif "action_research" in method_key:
        time_resources["total_project_duration"] = "16-20 weeks (iterative action-reflection cycles)"
        time_resources["phase_breakdown"] = {
            "planning": "4-6 weeks",
            "action": "6-8 weeks",
            "reflection": "4-6 weeks",
            "iteration": "2-4 weeks"
        }
    elif "systematic_literature_review" in method_key:
        time_resources["total_project_duration"] = "14-16 weeks (structured review process)"
        time_resources["phase_breakdown"] = {
            "search_strategy": "2-3 weeks",
            "screening": "4-6 weeks",
            "analysis": "6-8 weeks",
            "synthesis": "2-3 weeks"
        }
    elif "simulation_modeling" in method_key:
        time_resources["total_project_duration"] = "18-20 weeks (model development and scenario testing)"
        time_resources["phase_breakdown"] = {
            "model_development": "8-10 weeks",
            "validation": "4-6 weeks",
            "scenario_testing": "4-6 weeks"
        }
    elif "experimental_research" in method_key:
        time_resources["total_project_duration"] = "16-20 weeks (setup, execution, and analysis)"
        time_resources["phase_breakdown"] = {
            "design": "4-6 weeks",
            "setup": "4-6 weeks",
            "execution": "4-6 weeks",
            "analysis": "4-6 weeks"
        }
    elif "comparative_research" in method_key:
        time_resources["total_project_duration"] = "14-18 weeks (framework development and comparison)"
        time_resources["phase_breakdown"] = {
            "framework_development": "4-6 weeks",
            "data_collection": "6-8 weeks",
            "comparison": "4-6 weeks"
        }
    elif "living_lab" in method_key:
        time_resources["total_project_duration"] = "22-24 weeks (setup and real-world testing cycles)"
        time_resources["phase_breakdown"] = {
            "setup": "6-8 weeks",
            "testing": "10-12 weeks",
            "evaluation": "4-6 weeks"
        }
    elif "participatory_design" in method_key:
        time_resources["total_project_duration"] = "18-20 weeks (stakeholder engagement and iterations)"
        time_resources["phase_breakdown"] = {
            "stakeholder_engagement": "4-6 weeks",
            "design": "8-10 weeks",
            "iteration": "4-6 weeks"
        }
    elif "grounded_theory" in method_key:
        time_resources["total_project_duration"] = "18-22 weeks (data collection to theory saturation)"
        time_resources["phase_breakdown"] = {
            "data_collection": "8-10 weeks",
            "analysis": "6-8 weeks",
            "theory_development": "4-6 weeks"
        }
    elif "delphi" in method_key:
        time_resources["total_project_duration"] = "16-20 weeks (multiple expert consultation rounds)"
        time_resources["phase_breakdown"] = {
            "panel_setup": "2-4 weeks",
            "rounds": "10-12 weeks",
            "analysis": "4-6 weeks"
        }
    elif "rapid_prototyping" in method_key:
        time_resources["total_project_duration"] = "16-18 weeks (rapid development cycles)"
        time_resources["phase_breakdown"] = {
            "initial_design": "2-4 weeks",
            "iterations": "10-12 weeks",
            "refinement": "2-4 weeks"
        }
    elif "ethnography" in method_key:
        time_resources["total_project_duration"] = "20-24 weeks (extended field observation period)"
        time_resources["phase_breakdown"] = {
            "preparation": "2-4 weeks",
            "fieldwork": "12-14 weeks",
            "analysis": "4-6 weeks"
        }
    elif "content_analysis" in method_key:
        time_resources["total_project_duration"] = "14-18 weeks (systematic content processing)"
        time_resources["phase_breakdown"] = {
            "preparation": "2-4 weeks",
            "coding": "8-10 weeks",
            "analysis": "4-6 weeks"
        }
    elif "human_ai_collaboration" in method_key:
        time_resources["total_project_duration"] = "18-22 weeks (system development and user testing)"
        time_resources["phase_breakdown"] = {
            "development": "8-10 weeks",
            "testing": "6-8 weeks",
            "refinement": "4-6 weeks"
        }

    # If timeline is specified in method_data, use that instead
    if method_data.get("timeline") and method_data.get("timeline") != "To be determined":
        time_resources["total_project_duration"] = method_data["timeline"]
    
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
    json_output_path = OUTPUT_SOURCES_DIR / "5.2.3-resource-requirements-assessment.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON resource assessment saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")

    write_log(f"Finished Task 5.2.3 (Updated) at {datetime.now().isoformat()}")
    print("\n✅ Task 5.2.3 (Updated) complete.")

if __name__ == "__main__":
    main() 
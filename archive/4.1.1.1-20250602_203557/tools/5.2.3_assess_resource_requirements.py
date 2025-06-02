#!/usr/bin/env python3
"""
Task 5.2.3: Assess Resource Requirements

Focus: Detailed resource assessment for top-ranked methodologies
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- Results from Task 5.2.2 strengths and limitations analysis
- Results from Task 5.2.1 methodology comparison matrix
- Research context and constraints from previous tasks
- Focus on practical resource planning for 20-week Master's thesis
"""

import json
import os
from datetime import datetime

def load_previous_analyses():
    """Load previous analysis results from Tasks 5.2.1 and 5.2.2"""
    
    with open("../docs/5.2.1-methodology-comparison-matrix.json", 'r') as f:
        comparison_matrix = json.load(f)
    
    with open("../docs/5.2.2-methodology-strengths-limitations.json", 'r') as f:
        strengths_analysis = json.load(f)
    
    return comparison_matrix, strengths_analysis

def assess_detailed_resource_requirements():
    """Detailed resource requirements assessment for top methodologies"""
    
    comparison_matrix, strengths_analysis = load_previous_analyses()
    
    research_context = {
        "timeframe": "20 weeks",
        "project_type": "Master's thesis",
        "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
        "domain": "Distributed Energy Resources (DER) predictive maintenance",
        "constraints": ["Individual project", "Academic environment", "Limited budget"]
    }
    
    resource_assessments = {}
    
    for method_key, method_analysis in strengths_analysis["methodology_analyses"].items():
        
        method_data = comparison_matrix["methodologies"][method_key]
        
        resource_assessment = {
            "methodology_name": method_analysis["methodology_name"],
            "category": method_analysis["category"],
            "ranking_score": method_analysis["ranking_score"],
            
            "human_resources": assess_human_resources(method_key, method_data, research_context),
            "technical_resources": assess_technical_resources(method_key, method_data, research_context),
            "financial_resources": assess_financial_resources(method_key, method_data, research_context),
            "access_resources": assess_access_resources(method_key, method_data, research_context),
            "time_resources": assess_time_resources(method_key, method_data, research_context),
            
            "resource_intensity": calculate_resource_intensity(method_key, method_data),
            "feasibility_constraints": identify_feasibility_constraints(method_key, method_data, research_context),
            "resource_optimization": suggest_resource_optimization(method_key, method_data, research_context)
        }
        
        resource_assessments[method_key] = resource_assessment
    
    return resource_assessments

def assess_human_resources(method_key, method_data, research_context):
    """Assess human resource requirements"""
    
    human_resources = {
        "researcher_expertise_required": [],
        "additional_expertise_needed": [],
        "collaboration_requirements": [],
        "supervision_needs": [],
        "time_commitment_breakdown": {},
        "skill_development_required": []
    }
    
    if method_key == "rapid_prototyping":
        human_resources.update({
            "researcher_expertise_required": [
                "Software development and programming skills",
                "Agile project management experience", 
                "Protocol design and networking knowledge",
                "Iterative development methodology understanding"
            ],
            "additional_expertise_needed": [
                "Industry stakeholder contacts for validation",
                "Expert reviewer for technical architecture",
                "Mentor guidance for scope management"
            ],
            "collaboration_requirements": [
                "Regular stakeholder feedback sessions (bi-weekly)",
                "Expert review meetings (monthly)",
                "Supervisor check-ins (weekly during development phases)"
            ],
            "time_commitment_breakdown": {
                "development_work": "60% of project time",
                "stakeholder_engagement": "15% of project time",
                "documentation": "20% of project time", 
                "evaluation": "5% of project time"
            },
            "skill_development_required": [
                "Advanced protocol implementation",
                "Agile documentation practices",
                "Stakeholder communication",
                "Rapid evaluation techniques"
            ]
        })
    
    elif method_key == "digital_twin":
        human_resources.update({
            "researcher_expertise_required": [
                "Mathematical modeling and simulation skills",
                "DER systems domain knowledge",
                "Programming for simulation environments",
                "Statistical analysis and validation techniques"
            ],
            "additional_expertise_needed": [
                "DER systems expert for model validation",
                "Simulation modeling specialist", 
                "Industry expert for real-world validation data"
            ],
            "collaboration_requirements": [
                "Expert consultation for model design (initial phases)",
                "Validation review sessions (mid-project)",
                "Technical review of simulation results"
            ],
            "time_commitment_breakdown": {
                "model_development": "50% of project time",
                "simulation_execution": "25% of project time",
                "validation_analysis": "15% of project time",
                "documentation": "10% of project time"
            },
            "skill_development_required": [
                "Advanced simulation software usage",
                "DER systems technical knowledge",
                "Statistical model validation",
                "Computational optimization techniques"
            ]
        })
    
    elif method_key == "comparative_research":
        human_resources.update({
            "researcher_expertise_required": [
                "Literature review and analysis skills",
                "Comparative methodology expertise",
                "Statistical analysis capabilities",
                "Protocol evaluation framework development"
            ],
            "additional_expertise_needed": [
                "Industry expert for practical insights",
                "Academic supervisor for methodology guidance"
            ],
            "collaboration_requirements": [
                "Expert interviews for validation",
                "Academic review of comparison framework",
                "Industry consultation for practical relevance"
            ],
            "time_commitment_breakdown": {
                "literature_analysis": "40% of project time",
                "framework_development": "30% of project time",
                "comparison_execution": "20% of project time",
                "documentation": "10% of project time"
            },
            "skill_development_required": [
                "Advanced comparative analysis techniques",
                "Protocol evaluation metrics",
                "Industry consultation skills"
            ]
        })
    
    elif method_key == "design_science_research":
        human_resources.update({
            "researcher_expertise_required": [
                "Artifact design and development skills",
                "DSR methodology expertise",
                "Software architecture and development",
                "Systematic evaluation methodology"
            ],
            "additional_expertise_needed": [
                "DSR methodology expert for guidance",
                "Technical expert for artifact validation",
                "Industry stakeholder for practical evaluation"
            ],
            "collaboration_requirements": [
                "DSR methodology consultation (early phases)",
                "Artifact design review sessions",
                "Evaluation framework validation",
                "Industry feedback collection"
            ],
            "time_commitment_breakdown": {
                "artifact_development": "50% of project time",
                "evaluation_design": "20% of project time",
                "validation_execution": "20% of project time",
                "documentation": "10% of project time"
            },
            "skill_development_required": [
                "DSR artifact development",
                "Systematic evaluation design",
                "Technical validation methods",
                "Industry stakeholder engagement"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        human_resources.update({
            "researcher_expertise_required": [
                "Quantitative research methodology",
                "Qualitative research methodology",
                "Mixed methods integration",
                "Statistical analysis",
                "Interview and observation techniques"
            ],
            "additional_expertise_needed": [
                "Mixed methods expert for methodology guidance",
                "Statistical analysis expert",
                "Industry stakeholders for both phases"
            ],
            "collaboration_requirements": [
                "Methodology expert consultations",
                "Stakeholder interviews and surveys",
                "Validation workshops with experts"
            ],
            "time_commitment_breakdown": {
                "quantitative_phase": "40% of project time",
                "qualitative_phase": "35% of project time",
                "integration_analysis": "15% of project time",
                "documentation": "10% of project time"
            },
            "skill_development_required": [
                "Advanced statistical analysis",
                "Qualitative data analysis",
                "Mixed methods integration",
                "Multi-stakeholder coordination"
            ]
        })
    
    elif method_key == "experimental_research":
        human_resources.update({
            "researcher_expertise_required": [
                "Experimental design methodology",
                "Statistical analysis and hypothesis testing",
                "Protocol performance measurement",
                "Controlled environment setup"
            ],
            "additional_expertise_needed": [
                "Statistics expert for design validation",
                "Protocol expert for realistic scenarios",
                "Technical expert for measurement setup"
            ],
            "collaboration_requirements": [
                "Statistical consultant for design review",
                "Technical expert for experimental setup",
                "Industry validation of experimental scenarios"
            ],
            "time_commitment_breakdown": {
                "experimental_design": "25% of project time",
                "setup_and_execution": "40% of project time",
                "analysis_and_validation": "25% of project time",
                "documentation": "10% of project time"
            },
            "skill_development_required": [
                "Advanced experimental design",
                "Statistical software proficiency",
                "Measurement and instrumentation",
                "Data analysis and interpretation"
            ]
        })
    
    return human_resources

def assess_technical_resources(method_key, method_data, research_context):
    """Assess technical resource requirements"""
    
    technical_resources = {
        "software_requirements": [],
        "hardware_requirements": [],
        "infrastructure_needs": [],
        "data_requirements": [],
        "computational_requirements": [],
        "licensing_costs": []
    }
    
    if method_key == "rapid_prototyping":
        technical_resources.update({
            "software_requirements": [
                "Development environment (IDE, version control)",
                "Protocol testing frameworks",
                "Agile project management tools",
                "Continuous integration tools"
            ],
            "hardware_requirements": [
                "Development workstation (standard laptop sufficient)",
                "Testing devices/simulators for protocol validation",
                "Network testing equipment (potentially simulated)"
            ],
            "infrastructure_needs": [
                "Internet connectivity for stakeholder collaboration",
                "Cloud services for CI/CD pipeline",
                "Version control hosting (Git repository)"
            ],
            "computational_requirements": [
                "Low to moderate - standard development machine",
                "Network simulation capabilities"
            ],
            "licensing_costs": [
                "Mostly open-source tools available",
                "Potential cloud service costs ($10-50/month)",
                "Professional development tools (optional, ~$100-500)"
            ]
        })
    
    elif method_key == "digital_twin":
        technical_resources.update({
            "software_requirements": [
                "Simulation software (MATLAB/Simulink, Python SimPy, or specialized DER simulators)",
                "Mathematical modeling tools",
                "Data analysis software (Python/R with scientific libraries)",
                "Visualization tools for results presentation"
            ],
            "hardware_requirements": [
                "High-performance workstation for complex simulations",
                "Adequate RAM (16GB+ recommended)",
                "Sufficient storage for simulation data"
            ],
            "infrastructure_needs": [
                "High-speed internet for data access",
                "Potential cloud computing resources for large-scale simulations",
                "Access to DER system data or specifications"
            ],
            "computational_requirements": [
                "High - complex simulation models",
                "Parallel processing capabilities beneficial",
                "Long-running simulation jobs"
            ],
            "licensing_costs": [
                "MATLAB/Simulink licenses (~$1000-3000 academic)",
                "Specialized simulation software licenses",
                "Cloud computing costs for large simulations ($100-500)"
            ]
        })
    
    elif method_key == "comparative_research":
        technical_resources.update({
            "software_requirements": [
                "Literature management software (Zotero, Mendeley)",
                "Statistical analysis software (R, Python, SPSS)",
                "Document analysis tools",
                "Data visualization software"
            ],
            "hardware_requirements": [
                "Standard research workstation",
                "Adequate storage for literature database"
            ],
            "infrastructure_needs": [
                "Library database access",
                "Internet connectivity for literature search",
                "Document storage and backup systems"
            ],
            "computational_requirements": [
                "Low to moderate - mainly data analysis",
                "Statistical processing capabilities"
            ],
            "licensing_costs": [
                "Most tools available as open-source",
                "Academic database access (usually provided by institution)",
                "Optional: Professional statistical software (~$100-300)"
            ]
        })
    
    elif method_key == "design_science_research":
        technical_resources.update({
            "software_requirements": [
                "Development environment (IDE, version control)",
                "Prototyping tools (e.g., Figma, Adobe XD, or specific coding frameworks)",
                "Modeling tools (if applicable, e.g., UML, BPMN)",
                "Data analysis software for evaluation (e.g., R, Python, SPSS)",
                "Documentation tools (e.g., Confluence, Word)"
            ],
            "hardware_requirements": [
                "Development workstation",
                "Specific hardware if artifact is physical or interacts with hardware (e.g., sensors, microcontrollers)",
                "Testing devices for evaluation"
            ],
            "infrastructure_needs": [
                "Testing environment (lab or simulated)",
                "Version control hosting (e.g., GitHub, GitLab)",
                "Collaboration platform"
            ],
            "data_requirements": [
                "Problem-specific data for design phase",
                "Data for artifact evaluation (quantitative or qualitative)",
                "Access to existing literature and design principles"
            ],
            "computational_requirements": [
                "Moderate, depending on artifact complexity and evaluation methods",
                "May increase if simulations or complex data analysis are involved in evaluation"
            ],
            "licensing_costs": [
                "Mostly open-source tools available for development",
                "Potential costs for specialized modeling or prototyping software (~$100-1000 academic)",
                "Costs for data analysis software if not provided by institution"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        technical_resources.update({
            "software_requirements": [
                "Survey administration tools (e.g., Qualtrics, SurveyMonkey, Google Forms)",
                "Statistical analysis software (e.g., SPSS, R, Python with stats libraries) for quantitative phase",
                "Qualitative Data Analysis Software (QDAS) (e.g., NVivo, MAXQDA, ATLAS.ti) for qualitative phase",
                "Interview recording and transcription tools/services",
                "Reference management software"
            ],
            "hardware_requirements": [
                "Standard research workstation",
                "Audio recording equipment for interviews/focus groups"
            ],
            "infrastructure_needs": [
                "Access to target population for surveys and interviews",
                "Secure data storage for sensitive qualitative data",
                "Platform for online survey distribution"
            ],
            "data_requirements": [
                "Quantitative data from surveys or experiments",
                "Qualitative data from interviews, focus groups, or observations",
                "Sampling frame for participant recruitment"
            ],
            "computational_requirements": [
                "Moderate for statistical analysis of quantitative data",
                "Low for qualitative data analysis (software aids organization more than computation)"
            ],
            "licensing_costs": [
                "Survey platform subscription (~$50-300, or institutional access)",
                "QDAS license (~$500-1500 academic, or institutional access)",
                "Statistical software if not open source or provided",
                "Transcription services (~$1-2 per audio minute, optional)"
            ]
        })
    
    elif method_key == "experimental_research":
        technical_resources.update({
            "software_requirements": [
                "Experiment control software (if applicable, e.g., E-Prime, PsychoPy, custom scripts)",
                "Data logging and acquisition software",
                "Statistical analysis software (e.g., R, SPSS, Python)",
                "Stimulus presentation software (if applicable)"
            ],
            "hardware_requirements": [
                "Standard or specialized computer for running experiments",
                "Measurement devices, sensors, actuators as per experimental design",
                "Controlled environment setup (e.g., soundproof room, specific lighting)"
            ],
            "infrastructure_needs": [
                "Laboratory space or controlled setting",
                "Specific network configurations if relevant",
                "Secure data storage for experimental results"
            ],
            "data_requirements": [
                "Precise data from experimental manipulations and measurements",
                "Control group data",
                "Calibration data for equipment"
            ],
            "computational_requirements": [
                "Moderate to high for statistical analysis, especially with large datasets or complex models",
                "Real-time processing if experiment requires it"
            ],
            "licensing_costs": [
                "Specialized experimental software licenses (~$200-2000)",
                "Statistical software if not open source or provided",
                "Potential costs for hardware drivers or development kits"
            ]
        })
    
    return technical_resources

def assess_financial_resources(method_key, method_data, research_context):
    """Assess financial resource requirements"""
    
    financial_resources = {
        "direct_costs": {},
        "indirect_costs": {},
        "total_estimated_budget": "",
        "budget_breakdown": {},
        "funding_sources": [],
        "cost_mitigation_strategies": []
    }
    
    if method_key == "rapid_prototyping":
        financial_resources.update({
            "direct_costs": {
                "software_licenses": "$100-500 (optional professional tools)",
                "cloud_services": "$50-200 (CI/CD and hosting)",
                "testing_equipment": "$0-300 (if physical hardware needed)",
                "stakeholder_engagement": "$100-300 (travel/communication costs)"
            },
            "total_estimated_budget": "$300-1,200",
            "cost_mitigation_strategies": [
                "Use open-source development tools",
                "Leverage cloud free tiers",
                "Virtual stakeholder meetings to reduce travel",
                "Academic licensing discounts"
            ]
        })
    
    elif method_key == "digital_twin":
        financial_resources.update({
            "direct_costs": {
                "simulation_software": "$1,000-3,000 (MATLAB/specialized tools)",
                "computational_resources": "$200-800 (cloud computing)",
                "data_acquisition": "$100-500 (DER system data access)",
                "validation_activities": "$200-400 (expert consultation)"
            },
            "total_estimated_budget": "$1,500-4,700",
            "cost_mitigation_strategies": [
                "Use institution's existing software licenses",
                "Start with open-source simulation tools",
                "Negotiate industry data access partnerships",
                "Optimize simulation models for efficiency"
            ]
        })
    
    elif method_key == "comparative_research":
        financial_resources.update({
            "direct_costs": {
                "literature_access": "$0-200 (additional database access)",
                "analysis_software": "$0-300 (statistical tools)",
                "expert_consultation": "$200-500 (industry expert interviews)",
                "documentation_tools": "$50-100 (professional writing tools)"
            },
            "total_estimated_budget": "$250-1,100",
            "cost_mitigation_strategies": [
                "Maximize use of institutional library access",
                "Use open-source analysis tools",
                "Academic expert consultation through university networks",
                "Free documentation and reference management tools"
            ]
        })
    
    elif method_key == "design_science_research":
        financial_resources.update({
            "direct_costs": {
                "software_licenses": "$100-1000 (specialized tools, if needed)",
                "hardware_components": "$50-500 (if physical artifact)",
                "cloud_services": "$50-200 (testing, deployment)",
                "participant_incentives_evaluation": "$100-400 (if applicable)",
                "publication_fees": "$0-500 (open access options)"
            },
            "total_estimated_budget": "$300-2,500 (highly variable based on artifact)",
            "cost_mitigation_strategies": [
                "Prioritize open-source software and platforms",
                "Utilize university lab resources and equipment",
                "Scope artifact complexity to available budget",
                "Seek academic discounts for software/hardware"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        financial_resources.update({
            "direct_costs": {
                "survey_platform": "$50-300 (or institutional)",
                "transcription_services": "$200-800 (for qualitative interviews)",
                "participant_incentives_quant": "$100-500 (surveys)",
                "participant_incentives_qual": "$100-500 (interviews)",
                "qda_software": "$0-1500 (open source, student licenses, or institutional)"
            },
            "total_estimated_budget": "$450-3,600 (transcription and incentives are major drivers)",
            "cost_mitigation_strategies": [
                "Use free survey tools for smaller samples",
                "Researcher performs transcriptions (time cost)",
                "Utilize institutional software licenses (QDAS, statistical)",
                "Non-monetary incentives for participants where appropriate"
            ]
        })
    
    elif method_key == "experimental_research":
        financial_resources.update({
            "direct_costs": {
                "specialized_equipment_rental_purchase": "$200-5000+ (highly variable)",
                "lab_materials_consumables": "$100-500",
                "participant_compensation": "$200-1000 (depending on number and duration)",
                "software_licenses_experimental": "$200-2000"
            },
            "total_estimated_budget": "$700-8,500+ (equipment is the major variable)",
            "cost_mitigation_strategies": [
                "Utilize existing university lab equipment and facilities",
                "Design experiments with lower-cost materials",
                "Simulate parts of the experiment if feasible",
                "Collaborate to share equipment costs",
                "Apply for small internal research grants"
            ]
        })
    
    return financial_resources

def assess_access_resources(method_key, method_data, research_context):
    """Assess access requirements (data, stakeholders, systems)"""
    
    access_resources = {
        "data_access_needs": [],
        "stakeholder_access_requirements": [],
        "system_access_needs": [],
        "institutional_approvals": [],
        "access_timeline": {},
        "access_barriers": [],
        "access_facilitation_strategies": []
    }
    
    if method_key == "rapid_prototyping":
        access_resources.update({
            "stakeholder_access_requirements": [
                "Industry professionals for feedback (3-5 contacts)",
                "Technical experts for architecture review",
                "Potential end-users for usability testing"
            ],
            "data_access_needs": [
                "Protocol specifications and documentation",
                "DER system operational data (potentially simulated)",
                "Existing implementation examples"
            ],
            "access_barriers": [
                "Industry stakeholder availability",
                "Proprietary protocol information access",
                "Coordination across multiple stakeholders"
            ],
            "access_facilitation_strategies": [
                "Early stakeholder recruitment through academic networks",
                "Use of publicly available protocol specifications",
                "Flexible meeting scheduling for stakeholder convenience"
            ]
        })
    
    elif method_key == "design_science_research":
        access_resources.update({
            "data_access_needs": [
                "Relevant literature and existing design knowledge",
                "Data from the problem domain to inform design",
                "Access to users or systems for evaluation"
            ],
            "stakeholder_access_requirements": [
                "Domain experts for initial problem understanding and design feedback",
                "Target users or representatives for iterative feedback and evaluation",
                "Technical experts for feasibility and implementation advice"
            ],
            "system_access_needs": [
                "Access to development and testing environments",
                "Access to existing systems if the artifact requires integration",
                "Tools and platforms for artifact development"
            ],
            "institutional_approvals": [
                "Ethics committee approval if evaluation involves human subjects",
                "Departmental approvals for resource use (e.g., labs)"
            ],
            "access_barriers": [
                "Difficulty in recruiting relevant stakeholders or users",
                "Proprietary data or systems needed for design/evaluation",
                "Time constraints of stakeholders for participation"
            ],
            "access_facilitation_strategies": [
                "Clearly articulate value proposition for stakeholders",
                "Leverage university contacts and networks",
                "Plan for remote participation where possible",
                "Offer appropriate incentives for participation"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        access_resources.update({
            "data_access_needs": [
                "Sampling frame for quantitative phase (e.g., list of potential survey respondents)",
                "Access to settings or individuals for qualitative data collection (observations, interviews)"
            ],
            "stakeholder_access_requirements": [
                "Participants for quantitative phase (surveys, experiments)",
                "Participants for qualitative phase (interviews, focus groups) - often a subset or purposively selected based on quant results",
                "Gatekeepers for access to specific populations or organizations"
            ],
            "system_access_needs": [
                "Survey distribution platforms",
                "Quiet, private spaces for interviews or focus groups"
            ],
            "institutional_approvals": [
                "Ethics committee approval for both quantitative and qualitative phases involving human subjects",
                "Permissions from organizations if conducting research on-site or with their members"
            ],
            "access_barriers": [
                "Low response rates for surveys",
                "Difficulty recruiting for in-depth qualitative phase",
                "Gaining trust and rapport with qualitative participants",
                "Gatekeeper reluctance"
            ],
            "access_facilitation_strategies": [
                "Pilot quantitative instruments",
                "Clear communication of research purpose and data handling",
                "Build rapport with gatekeepers and participants",
                "Offer anonymity/confidentiality assurances"
            ]
        })
    
    elif method_key == "experimental_research":
        access_resources.update({
            "data_access_needs": [
                "Source for recruiting a sufficient and appropriate sample of participants",
                "Access to any pre-existing data needed for stimulus creation or participant screening"
            ],
            "stakeholder_access_requirements": [
                "Human participants meeting specific criteria",
                "Technical staff for operating or maintaining specialized equipment/labs"
            ],
            "system_access_needs": [
                "Controlled laboratory environment or experimental setting",
                "Specific hardware or software setups",
                "Access to an online platform if the experiment is run remotely"
            ],
            "institutional_approvals": [
                "Ethics committee approval for experiments with human subjects",
                "Safety approvals if experiment involves potentially hazardous materials or equipment",
                "Lab access permissions"
            ],
            "access_barriers": [
                "Recruiting participants matching strict experimental criteria",
                "Availability of specialized lab spaces or equipment",
                "Participant attrition during multi-session experiments"
            ],
            "access_facilitation_strategies": [
                "Use university participant pools or established recruitment channels",
                "Book lab spaces/equipment well in advance",
                "Offer fair compensation for participant time and effort",
                "Thorough piloting of experimental procedures"
            ]
        })
    
    return access_resources

def assess_time_resources(method_key, method_data, research_context):
    """Assess detailed time allocation and scheduling"""
    
    time_resources = {
        "total_project_duration": method_data.get("timeline", "Unknown"),
        "phase_breakdown": {},
        "weekly_time_allocation": {},
        "critical_path_activities": [],
        "timeline_risks": [],
        "schedule_optimization": []
    }
    
    if method_key == "rapid_prototyping":
        time_resources.update({
            "total_project_duration": "8-20 weeks (flexible)",
            "phase_breakdown": {
                "initial_setup_and_planning": "2 weeks",
                "iteration_1_development": "3 weeks",
                "iteration_2_development": "3 weeks",
                "iteration_3_development": "3 weeks",
                "final_integration_and_evaluation": "2 weeks",
                "documentation_and_finalization": "2 weeks",
                "buffer_time": "5 weeks distributed"
            },
            "critical_path_activities": [
                "Stakeholder availability for feedback",
                "Technical architecture decisions",
                "Integration testing between iterations"
            ],
            "timeline_risks": [
                "Scope creep extending iteration duration",
                "Stakeholder feedback delays",
                "Technical challenges requiring additional development time"
            ]
        })
    
    elif method_key == "digital_twin":
        time_resources.update({
            "total_project_duration": "14-18 weeks",
            "phase_breakdown": {
                "model_design_and_setup": "4 weeks",
                "initial_model_development": "4 weeks",
                "model_validation_and_refinement": "3 weeks",
                "simulation_execution": "3 weeks",
                "results_analysis": "2 weeks",
                "documentation": "2 weeks",
                "buffer_time": "2 weeks"
            },
            "critical_path_activities": [
                "Model validation against real data",
                "Computational resource availability",
                "Complex simulation convergence"
            ],
            "timeline_risks": [
                "Model development complexity exceeding estimates",
                "Simulation runtime longer than expected",
                "Validation data access delays"
            ]
        })
    
    elif method_key == "design_science_research":
        time_resources.update({
            "total_project_duration": "16-20 weeks (iterative)",
            "phase_breakdown": {
                "problem_identification_and_motivation": "2-3 weeks",
                "define_objectives_for_solution": "1-2 weeks",
                "design_and_development_iteration_1": "4-6 weeks",
                "demonstration_evaluation_iteration_1": "2-3 weeks",
                "design_and_development_iteration_2 (if needed)": "3-4 weeks",
                "demonstration_evaluation_iteration_2 (if needed)": "1-2 weeks",
                "communication_and_final_documentation": "2-3 weeks",
                "buffer_time": "1-2 weeks"
            },
            "critical_path_activities": [
                "Artifact development cycles",
                "Securing access for and conducting evaluations",
                "Integrating feedback into subsequent design iterations"
            ],
            "timeline_risks": [
                "Underestimation of development effort for the artifact",
                "Delays in obtaining evaluation feedback",
                "Scope creep if design objectives are not well-defined",
                "Technical challenges during development"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        time_resources.update({
            "total_project_duration": "18-20 weeks (can be very tight)",
            "phase_breakdown": {
                "quantitative_design_and_instrument_development": "2-3 weeks",
                "quantitative_data_collection": "3-4 weeks",
                "quantitative_data_analysis_and_interpretation": "2-3 weeks",
                "qualitative_design_and_instrument_development": "1-2 weeks (informed by quant)",
                "qualitative_data_collection": "3-4 weeks",
                "qualitative_data_analysis_and_interpretation": "3-4 weeks",
                "integration_of_findings_and_documentation": "2-3 weeks",
                "buffer_time": "1 week (minimal)"
            },
            "critical_path_activities": [
                "Completion of quantitative phase before qualitative can be fully designed/initiated",
                "Participant recruitment for both phases",
                "Qualitative data analysis (can be very time-consuming, e.g., transcription, coding)"
            ],
            "timeline_risks": [
                "Insufficient time for in-depth qualitative analysis if quantitative phase overruns",
                "Delays in recruitment for either phase",
                "Complexity of integrating quantitative and qualitative findings",
                "High risk of timeline overrun in a 20-week individual project"
            ]
        })
    
    elif method_key == "experimental_research":
        time_resources.update({
            "total_project_duration": "16-20 weeks",
            "phase_breakdown": {
                "literature_review_and_hypothesis_formulation": "2-3 weeks",
                "experimental_design_and_materials_preparation": "3-4 weeks",
                "ethics_approval_and_pilot_testing": "2-3 weeks",
                "participant_recruitment": "1-2 weeks (can overlap)",
                "data_collection_experiment_execution": "3-5 weeks",
                "data_analysis_and_interpretation": "3-4 weeks",
                "documentation_and_write_up": "2-3 weeks",
                "buffer_time": "1-2 weeks"
            },
            "critical_path_activities": [
                "Obtaining ethics approval",
                "Setting up and calibrating experimental apparatus/environment",
                "Participant recruitment and scheduling",
                "Rigorous data analysis"
            ],
            "timeline_risks": [
                "Delays in ethics approval",
                "Technical issues with experimental setup or equipment",
                "Slow participant recruitment",
                "Unexpected complexities in data analysis"
            ]
        })
    
    return time_resources

def calculate_resource_intensity(method_key, method_data):
    """Calculate overall resource intensity score"""
    
    base_requirement = method_data.get("resource_requirements", "Unknown")
    
    intensity_mapping = {
        "Low": 1,
        "Low to Moderate": 2,
        "Moderate": 3,
        "Moderate to High": 4,
        "High": 5,
        "Very High": 5
    }
    
    intensity_score = 3  # Default moderate
    for level, score in intensity_mapping.items():
        if level in str(base_requirement):
            intensity_score = score
            break
    
    adjustment_factors = {
        "rapid_prototyping": -0.5,
        "digital_twin": +1.0,
        "comparative_research": -1.0,
        "design_science_research": +0.5,
        "sequential_explanatory": +1.5,
        "experimental_research": +0.0
    }
    
    final_score = intensity_score + adjustment_factors.get(method_key, 0)
    final_score = max(1, min(5, final_score))
    
    return {
        "intensity_score": round(final_score, 1),
        "intensity_level": get_intensity_level(final_score),
        "base_requirement": str(base_requirement)
    }

def get_intensity_level(score):
    """Convert numeric score to intensity level"""
    if score <= 1.5:
        return "Low"
    elif score <= 2.5:
        return "Low to Moderate"
    elif score <= 3.5:
        return "Moderate"
    elif score <= 4.5:
        return "Moderate to High"
    else:
        return "High"

def identify_feasibility_constraints(method_key, method_data, research_context):
    """Identify key feasibility constraints for each methodology"""
    
    constraints = {
        "critical_constraints": [],
        "moderate_constraints": [],
        "constraint_severity": "",
        "mitigation_urgency": ""
    }
    
    if method_key == "rapid_prototyping":
        constraints.update({
            "critical_constraints": [
                "Stakeholder availability throughout project timeline",
                "Scope management discipline required"
            ],
            "moderate_constraints": [
                "Development environment setup",
                "Continuous integration infrastructure"
            ],
            "constraint_severity": "Moderate",
            "mitigation_urgency": "Early planning required"
        })
    
    elif method_key == "digital_twin":
        constraints.update({
            "critical_constraints": [
                "Access to DER system data and specifications",
                "Computational resources for complex simulations",
                "Domain expertise for model validation"
            ],
            "moderate_constraints": [
                "Software licensing costs",
                "Extended development timeline"
            ],
            "constraint_severity": "High",
            "mitigation_urgency": "Immediate planning required"
        })
    
    elif method_key == "design_science_research":
        constraints.update({
            "critical_constraints": [
                "Complexity of integrating quantitative and qualitative findings",
                "High risk of timeline overrun in a 20-week individual project"
            ],
            "moderate_constraints": [
                "Complexity of the artifact",
                "Time constraints of stakeholders for participation"
            ],
            "constraint_severity": "High",
            "mitigation_urgency": "Immediate planning required"
        })
    
    elif method_key == "sequential_explanatory":
        constraints.update({
            "critical_constraints": [
                "Complexity of integrating quantitative and qualitative findings",
                "High risk of timeline overrun in a 20-week individual project"
            ],
            "moderate_constraints": [
                "Complexity of the research methodology",
                "Time constraints of stakeholders for participation"
            ],
            "constraint_severity": "High",
            "mitigation_urgency": "Immediate planning required"
        })
    
    elif method_key == "experimental_research":
        constraints.update({
            "critical_constraints": [
                "Complexity of the experimental methodology",
                "High risk of timeline overrun in a 20-week individual project"
            ],
            "moderate_constraints": [
                "Complexity of the experimental setup",
                "Time constraints of stakeholders for participation"
            ],
            "constraint_severity": "High",
            "mitigation_urgency": "Immediate planning required"
        })
    
    return constraints

def suggest_resource_optimization(method_key, method_data, research_context):
    """Suggest strategies for optimizing resource usage"""
    
    optimization = {
        "cost_reduction_strategies": [],
        "time_optimization_strategies": [],
        "resource_sharing_opportunities": [],
        "efficiency_improvements": []
    }
    
    if method_key == "rapid_prototyping":
        optimization.update({
            "cost_reduction_strategies": [
                "Use open-source development tools and frameworks",
                "Leverage cloud free tiers for CI/CD",
                "Virtual stakeholder meetings to reduce travel costs"
            ],
            "time_optimization_strategies": [
                "Parallel development of independent components",
                "Automated testing and deployment pipelines",
                "Pre-scheduled stakeholder feedback sessions"
            ],
            "efficiency_improvements": [
                "Template-based iteration structure",
                "Standardized evaluation criteria",
                "Continuous documentation practices"
            ]
        })
    
    elif method_key == "digital_twin":
        optimization.update({
            "cost_reduction_strategies": [
                "Use institution's existing software licenses",
                "Start with open-source simulation tools",
                "Negotiate industry data access partnerships",
                "Optimize simulation models for efficiency"
            ],
            "time_optimization_strategies": [
                "Parallel development of independent components",
                "Automated testing and deployment pipelines",
                "Pre-scheduled stakeholder feedback sessions"
            ],
            "efficiency_improvements": [
                "Template-based iteration structure",
                "Standardized evaluation criteria",
                "Continuous documentation practices"
            ]
        })
    
    elif method_key == "design_science_research":
        optimization.update({
            "cost_reduction_strategies": [
                "Prioritize open-source software and platforms",
                "Utilize university lab resources and equipment",
                "Scope artifact complexity to available budget",
                "Seek academic discounts for software/hardware"
            ],
            "time_optimization_strategies": [
                "Parallel development of independent components",
                "Automated testing and deployment pipelines",
                "Pre-scheduled stakeholder feedback sessions"
            ],
            "efficiency_improvements": [
                "Template-based iteration structure",
                "Standardized evaluation criteria",
                "Continuous documentation practices"
            ]
        })
    
    elif method_key == "sequential_explanatory":
        optimization.update({
            "cost_reduction_strategies": [
                "Use free survey tools for smaller samples",
                "Researcher performs transcriptions (time cost)",
                "Utilize institutional software licenses (QDAS, statistical)",
                "Non-monetary incentives for participants where appropriate"
            ],
            "time_optimization_strategies": [
                "Parallel development of independent components",
                "Automated testing and deployment pipelines",
                "Pre-scheduled stakeholder feedback sessions"
            ],
            "efficiency_improvements": [
                "Template-based iteration structure",
                "Standardized evaluation criteria",
                "Continuous documentation practices"
            ]
        })
    
    elif method_key == "experimental_research":
        optimization.update({
            "cost_reduction_strategies": [
                "Utilize existing university lab equipment and facilities",
                "Design experiments with lower-cost materials",
                "Simulate parts of the experiment if feasible",
                "Collaborate to share equipment costs",
                "Apply for small internal research grants"
            ],
            "time_optimization_strategies": [
                "Parallel development of independent components",
                "Automated testing and deployment pipelines",
                "Pre-scheduled stakeholder feedback sessions"
            ],
            "efficiency_improvements": [
                "Template-based iteration structure",
                "Standardized evaluation criteria",
                "Continuous documentation practices"
            ]
        })
    
    return optimization

def main():
    """Main execution function"""
    
    os.makedirs("../docs", exist_ok=True)
    
    print("🔍 Task 5.2.3: Assessing Resource Requirements")
    print("=" * 70)
    
    try:
        print("📊 Analyzing resource requirements for top-ranked methodologies...")
        resource_assessments = assess_detailed_resource_requirements()
        
        analysis_report = {
            "metadata": {
                "task": "5.2.3 - Assess Resource Requirements",
                "timestamp": datetime.now().isoformat(),
                "scope": "Top-ranked methodologies from Tasks 5.2.1 and 5.2.2",
                "methodologies_analyzed": len(resource_assessments)
            },
            "research_context": {
                "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
                "domain": "Distributed Energy Resources (DER) predictive maintenance",
                "constraints": "20-week Master's thesis, individual project, academic environment"
            },
            "resource_assessments": resource_assessments
        }
        
        json_file = "../docs/5.2.3-resource-requirements-assessment.json"
        with open(json_file, 'w') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Detailed assessment saved to: {json_file}")
        
        # Generate markdown summary
        generate_markdown_summary(analysis_report)
        
        print(f"✅ Analysis complete for {len(resource_assessments)} methodologies")
        print("🎯 Ready for Task 5.2.4: Analyze feasibility")
        
    except Exception as e:
        print(f"❌ Error in analysis: {e}")
        raise

def generate_markdown_summary(analysis_report):
    """Generate markdown summary of resource requirements analysis"""
    
    assessments = analysis_report["resource_assessments"]
    
    md_content = f"""# Resource Requirements Assessment (Task 5.2.3)

*Generated: {analysis_report['metadata']['timestamp']}*

## Research Context

**Focus**: {analysis_report['research_context']['focus']}
**Domain**: {analysis_report['research_context']['domain']}  
**Constraints**: {analysis_report['research_context']['constraints']}
**Methodologies Analyzed**: {analysis_report['metadata']['methodologies_analyzed']}

## Executive Summary

### Resource Intensity Ranking
{chr(10).join([f"{i+1}. **{assessment['methodology_name']}** - {assessment['resource_intensity']['intensity_level']} (Score: {assessment['resource_intensity']['intensity_score']})" for i, assessment in enumerate(assessments.values())])}

## Detailed Resource Analysis

"""
    
    for method_key, assessment in assessments.items():
        md_content += f"""### {assessment['methodology_name']}

**Resource Intensity**: {assessment['resource_intensity']['intensity_level']} (Score: {assessment['resource_intensity']['intensity_score']})
**Estimated Budget**: {assessment['financial_resources']['total_estimated_budget']}
**Project Duration**: {assessment['time_resources']['total_project_duration']}

#### Human Resources
**Required Expertise:**
{chr(10).join([f"- {item}" for item in assessment['human_resources']['researcher_expertise_required']])}

**Time Commitment:**
{chr(10).join([f"- {k}: {v}" for k, v in assessment['human_resources']['time_commitment_breakdown'].items()])}

#### Technical Resources
**Software Requirements:**
{chr(10).join([f"- {item}" for item in assessment['technical_resources']['software_requirements']])}

**Computational Requirements:**
{chr(10).join([f"- {item}" for item in assessment['technical_resources']['computational_requirements']])}

#### Financial Resources
**Direct Costs:**
{chr(10).join([f"- {k}: {v}" for k, v in assessment['financial_resources']['direct_costs'].items()])}

**Cost Mitigation Strategies:**
{chr(10).join([f"- {item}" for item in assessment['financial_resources']['cost_mitigation_strategies']])}

---

"""
    
    md_content += f"""## Key Findings

1. **Resource Intensity**: Ranges from Low (Comparative Research) to High (Digital Twin, Sequential Explanatory)
2. **Budget Requirements**: Vary from $250-1,100 to $1,500-4,700 depending on methodology
3. **Critical Success Factors**: Early stakeholder access, computational resource planning, expertise availability

## Next Steps

- Task 5.2.4: Analyze implementation feasibility based on resource constraints
- Task 5.3.1: Select primary methodology considering resource availability

---

*Task 5.2.3 completed - Comprehensive resource requirements assessment*
*Sources: Tasks 5.2.1-5.2.2 methodology analyses, resource planning frameworks*
"""
    
    md_file = "../docs/5.2.3-resource-requirements-assessment.md"
    with open(md_file, 'w') as f:
        f.write(md_content)
    
    print(f"✅ Summary saved to: {md_file}")

if __name__ == "__main__":
    main() 
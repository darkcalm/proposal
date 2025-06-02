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
from pathlib import Path

def load_previous_analyses():
    """Load previous analysis results from Tasks 5.2.1 and 5.2.2"""
    
    # Load comparison matrix
    matrix_file = "../docs/5.2.1-methodology-comparison-matrix.json"
    if not os.path.exists(matrix_file):
        raise FileNotFoundError(f"Comparison matrix not found: {matrix_file}")
    
    with open(matrix_file, 'r') as f:
        comparison_matrix = json.load(f)
    
    # Load strengths/limitations analysis
    strengths_file = "../docs/5.2.2-methodology-strengths-limitations.json"
    if not os.path.exists(strengths_file):
        raise FileNotFoundError(f"Strengths analysis not found: {strengths_file}")
    
    with open(strengths_file, 'r') as f:
        strengths_analysis = json.load(f)
    
    return comparison_matrix, strengths_analysis

def assess_detailed_resource_requirements():
    """
    Detailed resource requirements assessment for top methodologies
    
    Categories:
    - Human Resources (expertise, time commitment)
    - Technical Resources (software, hardware, infrastructure)
    - Financial Resources (costs, budget requirements)
    - Access Resources (data, stakeholders, systems)
    - Time Resources (detailed breakdown by phase)
    """
    
    # Load previous analyses
    comparison_matrix, strengths_analysis = load_previous_analyses()
    
    # Get methodologies to analyze (from strengths analysis)
    methodologies_to_analyze = strengths_analysis["methodology_analyses"]
    
    # Research context for resource planning
    research_context = {
        "timeframe": "20 weeks",
        "project_type": "Master's thesis",
        "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
        "domain": "Distributed Energy Resources (DER) predictive maintenance",
        "constraints": ["Individual project", "Academic environment", "Limited budget"]
    }
    
    resource_assessments = {}
    
    for method_key, method_analysis in methodologies_to_analyze.items():
        # Base methodology data from comparison matrix
        method_data = comparison_matrix["methodologies"][method_key]
        
        # Detailed resource assessment
        resource_assessment = {
            "methodology_name": method_analysis["methodology_name"],
            "category": method_analysis["category"],
            "ranking_score": method_analysis["ranking_score"],
            
            # Resource Categories
            "human_resources": assess_human_resources(method_key, method_data, research_context),
            "technical_resources": assess_technical_resources(method_key, method_data, research_context),
            "financial_resources": assess_financial_resources(method_key, method_data, research_context),
            "access_resources": assess_access_resources(method_key, method_data, research_context),
            "time_resources": assess_time_resources(method_key, method_data, research_context),
            
            # Resource Analysis
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
    
    # Methodology-specific human resource analysis
    if method_key == "rapid_prototyping":
        human_resources["researcher_expertise_required"] = [
            "Software development and programming skills",
            "Agile project management experience",
            "Protocol design and networking knowledge",
            "Iterative development methodology understanding"
        ]
        human_resources["additional_expertise_needed"] = [
            "Industry stakeholder contacts for validation",
            "Expert reviewer for technical architecture",
            "Mentor guidance for scope management"
        ]
        human_resources["collaboration_requirements"] = [
            "Regular stakeholder feedback sessions (bi-weekly)",
            "Expert review meetings (monthly)",
            "Supervisor check-ins (weekly during development phases)"
        ]
        human_resources["time_commitment_breakdown"] = {
            "development_work": "60% of project time",
            "stakeholder_engagement": "15% of project time", 
            "documentation": "20% of project time",
            "evaluation": "5% of project time"
        }
        human_resources["skill_development_required"] = [
            "Advanced protocol implementation",
            "Agile documentation practices",
            "Stakeholder communication",
            "Rapid evaluation techniques"
        ]
    
    elif method_key == "digital_twin":
        human_resources["researcher_expertise_required"] = [
            "Mathematical modeling and simulation skills",
            "DER systems domain knowledge",
            "Programming for simulation environments",
            "Statistical analysis and validation techniques"
        ]
        human_resources["additional_expertise_needed"] = [
            "DER systems expert for model validation",
            "Simulation modeling specialist",
            "Industry expert for real-world validation data"
        ]
        human_resources["collaboration_requirements"] = [
            "Expert consultation for model design (initial phases)",
            "Validation review sessions (mid-project)",
            "Technical review of simulation results"
        ]
        human_resources["time_commitment_breakdown"] = {
            "model_development": "50% of project time",
            "simulation_execution": "25% of project time",
            "validation_analysis": "15% of project time",
            "documentation": "10% of project time"
        }
        human_resources["skill_development_required"] = [
            "Advanced simulation software usage",
            "DER systems technical knowledge",
            "Statistical model validation",
            "Computational optimization techniques"
        ]
    
    elif method_key == "comparative_research":
        human_resources["researcher_expertise_required"] = [
            "Literature review and analysis skills",
            "Comparative methodology expertise",
            "Statistical analysis capabilities",
            "Protocol evaluation framework development"
        ]
        human_resources["additional_expertise_needed"] = [
            "Industry expert for practical insights",
            "Academic supervisor for methodology guidance"
        ]
        human_resources["collaboration_requirements"] = [
            "Expert interviews for validation",
            "Academic review of comparison framework",
            "Industry consultation for practical relevance"
        ]
        human_resources["time_commitment_breakdown"] = {
            "literature_analysis": "40% of project time",
            "framework_development": "30% of project time",
            "comparison_execution": "20% of project time",
            "documentation": "10% of project time"
        }
        human_resources["skill_development_required"] = [
            "Advanced comparative analysis techniques",
            "Protocol evaluation metrics",
            "Industry consultation skills"
        ]
    
    elif method_key == "design_science_research":
        human_resources["researcher_expertise_required"] = [
            "Artifact design and development skills",
            "DSR methodology expertise",
            "Software architecture and development",
            "Systematic evaluation methodology"
        ]
        human_resources["additional_expertise_needed"] = [
            "DSR methodology expert for guidance",
            "Technical expert for artifact validation",
            "Industry stakeholder for practical evaluation"
        ]
        human_resources["collaboration_requirements"] = [
            "DSR methodology consultation (early phases)",
            "Artifact design review sessions",
            "Evaluation framework validation",
            "Industry feedback collection"
        ]
        human_resources["time_commitment_breakdown"] = {
            "artifact_development": "50% of project time",
            "evaluation_design": "20% of project time",
            "validation_execution": "20% of project time",
            "documentation": "10% of project time"
        }
        human_resources["skill_development_required"] = [
            "DSR artifact development",
            "Systematic evaluation design",
            "Technical validation methods",
            "Industry stakeholder engagement"
        ]
    
    # Add similar assessments for other methodologies...
    
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
    
    # Methodology-specific technical resource analysis
    if method_key == "rapid_prototyping":
        technical_resources["software_requirements"] = [
            "Development environment (IDE, version control)",
            "Protocol testing frameworks",
            "Agile project management tools",
            "Continuous integration tools"
        ]
        technical_resources["hardware_requirements"] = [
            "Development workstation (standard laptop sufficient)",
            "Testing devices/simulators for protocol validation",
            "Network testing equipment (potentially simulated)"
        ]
        technical_resources["infrastructure_needs"] = [
            "Internet connectivity for stakeholder collaboration",
            "Cloud services for CI/CD pipeline",
            "Version control hosting (Git repository)"
        ]
        technical_resources["computational_requirements"] = [
            "Low to moderate - standard development machine",
            "Network simulation capabilities"
        ]
        technical_resources["licensing_costs"] = [
            "Mostly open-source tools available",
            "Potential cloud service costs ($10-50/month)",
            "Professional development tools (optional, ~$100-500)"
        ]
    
    elif method_key == "digital_twin":
        technical_resources["software_requirements"] = [
            "Simulation software (MATLAB/Simulink, Python SimPy, or specialized DER simulators)",
            "Mathematical modeling tools",
            "Data analysis software (Python/R with scientific libraries)",
            "Visualization tools for results presentation"
        ]
        technical_resources["hardware_requirements"] = [
            "High-performance workstation for complex simulations",
            "Adequate RAM (16GB+ recommended)",
            "Sufficient storage for simulation data"
        ]
        technical_resources["infrastructure_needs"] = [
            "High-speed internet for data access",
            "Potential cloud computing resources for large-scale simulations",
            "Access to DER system data or specifications"
        ]
        technical_resources["computational_requirements"] = [
            "High - complex simulation models",
            "Parallel processing capabilities beneficial",
            "Long-running simulation jobs"
        ]
        technical_resources["licensing_costs"] = [
            "MATLAB/Simulink licenses (~$1000-3000 academic)",
            "Specialized simulation software licenses",
            "Cloud computing costs for large simulations ($100-500)"
        ]
    
    elif method_key == "comparative_research":
        technical_resources["software_requirements"] = [
            "Literature management software (Zotero, Mendeley)",
            "Statistical analysis software (R, Python, SPSS)",
            "Document analysis tools",
            "Data visualization software"
        ]
        technical_resources["hardware_requirements"] = [
            "Standard research workstation",
            "Adequate storage for literature database"
        ]
        technical_resources["infrastructure_needs"] = [
            "Library database access",
            "Internet connectivity for literature search",
            "Document storage and backup systems"
        ]
        technical_resources["computational_requirements"] = [
            "Low to moderate - mainly data analysis",
            "Statistical processing capabilities"
        ]
        technical_resources["licensing_costs"] = [
            "Most tools available as open-source",
            "Academic database access (usually provided by institution)",
            "Optional: Professional statistical software (~$100-300)"
        ]
    
    return technical_resources

def assess_financial_resources(method_key, method_data, research_context):
    """Assess financial resource requirements"""
    
    financial_resources = {
        "direct_costs": {},
        "indirect_costs": {},
        "opportunity_costs": {},
        "total_estimated_budget": "",
        "budget_breakdown": {},
        "funding_sources": [],
        "cost_mitigation_strategies": []
    }
    
    # Methodology-specific financial analysis
    if method_key == "rapid_prototyping":
        financial_resources["direct_costs"] = {
            "software_licenses": "$100-500 (optional professional tools)",
            "cloud_services": "$50-200 (CI/CD and hosting)",
            "testing_equipment": "$0-300 (if physical hardware needed)",
            "stakeholder_engagement": "$100-300 (travel/communication costs)"
        }
        financial_resources["indirect_costs"] = {
            "increased_development_time": "Potential overtime/extended timeline",
            "documentation_tools": "$50-100",
            "backup_systems": "$20-50"
        }
        financial_resources["total_estimated_budget"] = "$300-1,200"
        financial_resources["funding_sources"] = [
            "Personal/student budget",
            "Academic department support",
            "Open-source alternatives to reduce costs"
        ]
        financial_resources["cost_mitigation_strategies"] = [
            "Use open-source development tools",
            "Leverage cloud free tiers",
            "Virtual stakeholder meetings to reduce travel",
            "Academic licensing discounts"
        ]
    
    elif method_key == "digital_twin":
        financial_resources["direct_costs"] = {
            "simulation_software": "$1,000-3,000 (MATLAB/specialized tools)",
            "computational_resources": "$200-800 (cloud computing)",
            "data_acquisition": "$100-500 (DER system data access)",
            "validation_activities": "$200-400 (expert consultation)"
        }
        financial_resources["indirect_costs"] = {
            "extended_computation_time": "Additional cloud costs if simulations exceed estimates",
            "model_validation": "Expert consultation fees"
        }
        financial_resources["total_estimated_budget"] = "$1,500-4,700"
        financial_resources["funding_sources"] = [
            "Academic institution software licenses",
            "Research grants or department funding",
            "Industry partnership for data access"
        ]
        financial_resources["cost_mitigation_strategies"] = [
            "Use institution's existing software licenses",
            "Start with open-source simulation tools",
            "Negotiate industry data access partnerships",
            "Optimize simulation models for efficiency"
        ]
    
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
    
    # Methodology-specific access analysis
    if method_key == "rapid_prototyping":
        access_resources["stakeholder_access_requirements"] = [
            "Industry professionals for feedback (3-5 contacts)",
            "Technical experts for architecture review",
            "Potential end-users for usability testing"
        ]
        access_resources["data_access_needs"] = [
            "Protocol specifications and documentation",
            "DER system operational data (potentially simulated)",
            "Existing implementation examples"
        ]
        access_resources["access_timeline"] = {
            "stakeholder_recruitment": "Weeks 1-2",
            "data_access_establishment": "Weeks 1-3",
            "ongoing_stakeholder_engagement": "Throughout project"
        }
        access_resources["access_barriers"] = [
            "Industry stakeholder availability",
            "Proprietary protocol information access",
            "Coordination across multiple stakeholders"
        ]
        access_resources["access_facilitation_strategies"] = [
            "Early stakeholder recruitment through academic networks",
            "Use of publicly available protocol specifications",
            "Flexible meeting scheduling for stakeholder convenience"
        ]
    
    elif method_key == "digital_twin":
        access_resources["data_access_needs"] = [
            "DER system technical specifications",
            "Historical operational data for validation",
            "Protocol performance benchmarks",
            "Grid integration requirements"
        ]
        access_resources["system_access_needs"] = [
            "High-performance computing resources",
            "Simulation software environments",
            "Validation datasets"
        ]
        access_resources["access_timeline"] = {
            "data_access_negotiation": "Weeks 1-4",
            "system_setup": "Weeks 2-3",
            "ongoing_computational_access": "Throughout project"
        }
        access_resources["access_barriers"] = [
            "Proprietary DER system data",
            "Limited public datasets",
            "Computational resource availability"
        ]
        access_resources["access_facilitation_strategies"] = [
            "Partner with industry for data access",
            "Use publicly available datasets where possible",
            "Synthetic data generation for missing information"
        ]
    
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
    
    # Methodology-specific time analysis
    if method_key == "rapid_prototyping":
        time_resources["phase_breakdown"] = {
            "initial_setup_and_planning": "2 weeks",
            "iteration_1_development": "3 weeks",
            "iteration_2_development": "3 weeks", 
            "iteration_3_development": "3 weeks",
            "final_integration_and_evaluation": "2 weeks",
            "documentation_and_finalization": "2 weeks",
            "buffer_time": "5 weeks distributed"
        }
        time_resources["weekly_time_allocation"] = {
            "development_activities": "15-20 hours/week",
            "stakeholder_communication": "2-3 hours/week",
            "documentation": "3-5 hours/week",
            "evaluation_and_testing": "5-8 hours/week"
        }
        time_resources["critical_path_activities"] = [
            "Stakeholder availability for feedback",
            "Technical architecture decisions",
            "Integration testing between iterations"
        ]
        time_resources["timeline_risks"] = [
            "Scope creep extending iteration duration",
            "Stakeholder feedback delays",
            "Technical challenges requiring additional development time"
        ]
    
    elif method_key == "digital_twin":
        time_resources["phase_breakdown"] = {
            "model_design_and_setup": "4 weeks",
            "initial_model_development": "4 weeks",
            "model_validation_and_refinement": "3 weeks",
            "simulation_execution": "3 weeks",
            "results_analysis": "2 weeks",
            "documentation": "2 weeks",
            "buffer_time": "2 weeks"
        }
        time_resources["weekly_time_allocation"] = {
            "model_development": "12-15 hours/week",
            "simulation_execution": "8-12 hours/week",
            "analysis_and_validation": "6-10 hours/week",
            "documentation": "3-5 hours/week"
        }
        time_resources["critical_path_activities"] = [
            "Model validation against real data",
            "Computational resource availability",
            "Complex simulation convergence"
        ]
        time_resources["timeline_risks"] = [
            "Model development complexity exceeding estimates",
            "Simulation runtime longer than expected",
            "Validation data access delays"
        ]
    
    return time_resources

def calculate_resource_intensity(method_key, method_data):
    """Calculate overall resource intensity score"""
    
    # Base resource requirement score from methodology data
    base_requirement = method_data.get("resource_requirements", "Unknown")
    
    intensity_mapping = {
        "Low": 1,
        "Low to Moderate": 2,
        "Moderate": 3,
        "Moderate to High": 4,
        "High": 5,
        "Very High": 5
    }
    
    # Extract intensity from text description
    intensity_score = 3  # Default moderate
    for level, score in intensity_mapping.items():
        if level in base_requirement:
            intensity_score = score
            break
    
    # Methodology-specific adjustments
    adjustment_factors = {
        "rapid_prototyping": -0.5,  # Generally more efficient
        "digital_twin": +1.0,       # High computational requirements
        "comparative_research": -1.0,  # Lower resource needs
        "design_science_research": +0.5,  # Moderate to high requirements
        "sequential_explanatory": +1.5,   # Very high due to complexity
        "experimental_research": +0.0     # Baseline moderate
    }
    
    final_score = intensity_score + adjustment_factors.get(method_key, 0)
    final_score = max(1, min(5, final_score))  # Clamp to 1-5 range
    
    return {
        "intensity_score": round(final_score, 1),
        "intensity_level": get_intensity_level(final_score),
        "base_requirement": base_requirement
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
    
    # Common constraint patterns
    if method_key == "rapid_prototyping":
        constraints["critical_constraints"] = [
            "Stakeholder availability throughout project timeline",
            "Scope management discipline required"
        ]
        constraints["moderate_constraints"] = [
            "Development environment setup",
            "Continuous integration infrastructure"
        ]
        constraints["constraint_severity"] = "Moderate"
        constraints["mitigation_urgency"] = "Early planning required"
    
    elif method_key == "digital_twin":
        constraints["critical_constraints"] = [
            "Access to DER system data and specifications",
            "Computational resources for complex simulations",
            "Domain expertise for model validation"
        ]
        constraints["moderate_constraints"] = [
            "Software licensing costs",
            "Extended development timeline"
        ]
        constraints["constraint_severity"] = "High"
        constraints["mitigation_urgency"] = "Immediate planning required"
    
    return constraints

def suggest_resource_optimization(method_key, method_data, research_context):
    """Suggest strategies for optimizing resource usage"""
    
    optimization = {
        "cost_reduction_strategies": [],
        "time_optimization_strategies": [],
        "resource_sharing_opportunities": [],
        "efficiency_improvements": []
    }
    
    # Methodology-specific optimization
    if method_key == "rapid_prototyping":
        optimization["cost_reduction_strategies"] = [
            "Use open-source development tools and frameworks",
            "Leverage cloud free tiers for CI/CD",
            "Virtual stakeholder meetings to reduce travel costs"
        ]
        optimization["time_optimization_strategies"] = [
            "Parallel development of independent components",
            "Automated testing and deployment pipelines",
            "Pre-scheduled stakeholder feedback sessions"
        ]
        optimization["efficiency_improvements"] = [
            "Template-based iteration structure",
            "Standardized evaluation criteria",
            "Continuous documentation practices"
        ]
    
    elif method_key == "digital_twin":
        optimization["cost_reduction_strategies"] = [
            "Start with open-source simulation tools",
            "Use academic institution licenses",
            "Optimize models for computational efficiency"
        ]
        optimization["time_optimization_strategies"] = [
            "Incremental model complexity",
            "Parallel simulation execution",
            "Early validation with simplified models"
        ]
        optimization["efficiency_improvements"] = [
            "Modular model architecture",
            "Automated simulation workflows",
            "Efficient data management systems"
        ]
    
    return optimization

def main():
    """Main execution function"""
    
    # Create output directories
    os.makedirs("../docs", exist_ok=True)
    
    print("🔍 Task 5.2.3: Assessing Resource Requirements")
    print("=" * 70)
    
    try:
        # Perform detailed resource assessment
        print("📊 Analyzing resource requirements for top-ranked methodologies...")
        resource_assessments = assess_detailed_resource_requirements()
        
        # Create comprehensive resource analysis report
        analysis_report = {
            "metadata": {
                "task": "5.2.3 - Assess Resource Requirements",
                "timestamp": datetime.now().isoformat(),
                "scope": "Top-ranked methodologies from Tasks 5.2.1 and 5.2.2",
                "methodologies_analyzed": len(resource_assessments),
                "resource_categories": [
                    "Human Resources",
                    "Technical Resources",
                    "Financial Resources",
                    "Access Resources",
                    "Time Resources"
                ]
            },
            "research_context": {
                "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
                "domain": "Distributed Energy Resources (DER) predictive maintenance",
                "constraints": "20-week Master's thesis, individual project, academic environment"
            },
            "resource_assessments": resource_assessments,
            "comparative_analysis": generate_comparative_resource_analysis(resource_assessments),
            "recommendations": generate_resource_recommendations(resource_assessments)
        }
        
        # Save detailed JSON output
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

def generate_comparative_resource_analysis(resource_assessments):
    """Generate comparative analysis across methodologies"""
    
    comparative_analysis = {
        "resource_intensity_ranking": [],
        "cost_comparison": {},
        "time_comparison": {},
        "feasibility_ranking": []
    }
    
    # Resource intensity ranking
    intensity_scores = [(method_key, assessment["resource_intensity"]["intensity_score"]) 
                       for method_key, assessment in resource_assessments.items()]
    intensity_scores.sort(key=lambda x: x[1])
    
    comparative_analysis["resource_intensity_ranking"] = [
        {
            "methodology": resource_assessments[method_key]["methodology_name"],
            "intensity_score": score,
            "intensity_level": resource_assessments[method_key]["resource_intensity"]["intensity_level"]
        }
        for method_key, score in intensity_scores
    ]
    
    # Extract budget estimates for comparison
    comparative_analysis["cost_comparison"] = {
        resource_assessments[method_key]["methodology_name"]: assessment["financial_resources"]["total_estimated_budget"]
        for method_key, assessment in resource_assessments.items()
    }
    
    # Extract time estimates
    comparative_analysis["time_comparison"] = {
        resource_assessments[method_key]["methodology_name"]: assessment["time_resources"]["total_project_duration"]
        for method_key, assessment in resource_assessments.items()
    }
    
    return comparative_analysis

def generate_resource_recommendations(resource_assessments):
    """Generate recommendations based on resource analysis"""
    
    # Find methodology with best resource profile
    best_resource_profile = min(resource_assessments.items(), 
                               key=lambda x: x[1]["resource_intensity"]["intensity_score"])
    
    recommendations = {
        "most_resource_efficient": {
            "methodology": best_resource_profile[1]["methodology_name"],
            "rationale": f"Lowest resource intensity score ({best_resource_profile[1]['resource_intensity']['intensity_score']})"
        },
        "resource_optimization_priorities": [
            "Secure access resources early in project planning",
            "Leverage institutional resources and partnerships", 
            "Use open-source alternatives where possible",
            "Plan for resource sharing and collaboration opportunities"
        ],
        "critical_success_factors": [
            "Early stakeholder engagement and access negotiation",
            "Realistic budget planning and contingency allocation",
            "Technical infrastructure setup in initial phases",
            "Timeline management with adequate buffer allocation"
        ]
    }
    
    return recommendations

def generate_markdown_summary(analysis_report):
    """Generate markdown summary of resource requirements analysis"""
    
    assessments = analysis_report["resource_assessments"]
    comparative = analysis_report["comparative_analysis"]
    recommendations = analysis_report["recommendations"]
    
    md_content = f"""# Resource Requirements Assessment (Task 5.2.3)

*Generated: {analysis_report['metadata']['timestamp']}*

## Research Context

**Focus**: {analysis_report['research_context']['focus']}
**Domain**: {analysis_report['research_context']['domain']}  
**Constraints**: {analysis_report['research_context']['constraints']}
**Methodologies Analyzed**: {analysis_report['metadata']['methodologies_analyzed']}

## Resource Categories Analyzed

{chr(10).join([f"- {category}" for category in analysis_report['metadata']['resource_categories']])}

## Executive Summary

### Most Resource Efficient
**{recommendations['most_resource_efficient']['methodology']}**
- {recommendations['most_resource_efficient']['rationale']}

### Resource Intensity Ranking
{chr(10).join([f"{i+1}. **{item['methodology']}** - {item['intensity_level']} (Score: {item['intensity_score']})" for i, item in enumerate(comparative['resource_intensity_ranking'])])}

## Detailed Resource Analysis

"""
    
    # Add detailed analysis for each methodology
    for method_key, assessment in assessments.items():
        md_content += f"""### {assessment['methodology_name']}

**Resource Intensity**: {assessment['resource_intensity']['intensity_level']} (Score: {assessment['resource_intensity']['intensity_score']})
**Estimated Budget**: {assessment['financial_resources']['total_estimated_budget']}
**Project Duration**: {assessment['time_resources']['total_project_duration']}

#### Human Resources
**Required Expertise:**
{chr(10).join([f"- {item}" for item in assessment['human_resources']['researcher_expertise_required']])}

**Additional Support Needed:**
{chr(10).join([f"- {item}" for item in assessment['human_resources']['additional_expertise_needed']])}

**Time Commitment:**
{chr(10).join([f"- {k}: {v}" for k, v in assessment['human_resources']['time_commitment_breakdown'].items()])}

#### Technical Resources
**Software Requirements:**
{chr(10).join([f"- {item}" for item in assessment['technical_resources']['software_requirements']])}

**Hardware Requirements:**
{chr(10).join([f"- {item}" for item in assessment['technical_resources']['hardware_requirements']])}

**Computational Requirements:**
{chr(10).join([f"- {item}" for item in assessment['technical_resources']['computational_requirements']])}

#### Financial Resources
**Direct Costs:**
{chr(10).join([f"- {k}: {v}" for k, v in assessment['financial_resources']['direct_costs'].items()])}

**Cost Mitigation Strategies:**
{chr(10).join([f"- {item}" for item in assessment['financial_resources']['cost_mitigation_strategies']])}

#### Access Resources
**Key Access Requirements:**
{chr(10).join([f"- {item}" for item in assessment['access_resources']['stakeholder_access_requirements'] + assessment['access_resources']['data_access_needs'][:3]])}

**Access Barriers:**
{chr(10).join([f"- {item}" for item in assessment['access_resources']['access_barriers']])}

#### Time Resources
**Phase Breakdown:**
{chr(10).join([f"- {k}: {v}" for k, v in assessment['time_resources']['phase_breakdown'].items()])}

**Timeline Risks:**
{chr(10).join([f"- {item}" for item in assessment['time_resources']['timeline_risks']])}

#### Feasibility Assessment
**Critical Constraints:**
{chr(10).join([f"- {item}" for item in assessment['feasibility_constraints']['critical_constraints']])}

**Constraint Severity**: {assessment['feasibility_constraints']['constraint_severity']}

---

"""
    
    md_content += f"""## Comparative Analysis

### Cost Comparison
{chr(10).join([f"- **{methodology}**: {budget}" for methodology, budget in comparative['cost_comparison'].items()])}

### Time Comparison  
{chr(10).join([f"- **{methodology}**: {duration}" for methodology, duration in comparative['time_comparison'].items()])}

## Recommendations

### Critical Success Factors
{chr(10).join([f"- {factor}" for factor in recommendations['critical_success_factors']])}

### Resource Optimization Priorities
{chr(10).join([f"- {priority}" for priority in recommendations['resource_optimization_priorities']])}

## Key Findings

1. **Most Resource Efficient**: {recommendations['most_resource_efficient']['methodology']}
2. **Highest Resource Intensity**: {comparative['resource_intensity_ranking'][-1]['methodology']} ({comparative['resource_intensity_ranking'][-1]['intensity_level']})
3. **Critical Planning Requirements**: Early access negotiation and stakeholder engagement
4. **Budget Range**: Varies from low-cost comparative research to high-investment digital twin approaches

## Next Steps

- Task 5.2.4: Analyze implementation feasibility based on resource constraints
- Task 5.3.1: Select primary methodology considering resource availability
- Detailed resource planning for selected methodology

---

*Task 5.2.3 completed - Comprehensive resource requirements assessment*
*Sources: Tasks 5.2.1-5.2.2 methodology analyses, resource planning frameworks*
"""
    
    # Save markdown file
    md_file = "../docs/5.2.3-resource-requirements-assessment.md"
    with open(md_file, 'w') as f:
        f.write(md_content)
    
    print(f"✅ Summary saved to: {md_file}")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Tool: Assess Resource Requirements (Task 5.2.3)

Purpose: Systematically assess resource requirements for all research methods
to support practical methodology selection and implementation planning.

Research Context:
- Focus: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
- Domain: Distributed Energy Resources (DER) predictive maintenance coordination
- Input: Previous evaluations from tasks 5.2.1-5.2.2 and method details from 5.1.x tasks
- Output: Comprehensive resource requirements assessment

This script analyzes human, technical, financial, and temporal resource needs
for each method within the 20-week thesis timeline constraints.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

def load_previous_evaluations():
    """Load previous evaluation data from tasks 5.2.1-5.2.2"""
    evaluation_data = {}
    
    files_to_load = {
        'comparison_matrix': 'docs/5.2.1-comparison-matrix.json',
        'strengths_limitations': 'docs/5.2.2-strengths-limitations.json'
    }
    
    for data_type, file_path in files_to_load.items():
        try:
            with open(file_path, 'r') as f:
                evaluation_data[data_type] = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Could not load {file_path}")
            evaluation_data[data_type] = None
    
    return evaluation_data

def load_method_details():
    """Load detailed method information from tasks 5.1.2-5.1.5"""
    method_details = {}
    
    json_files = {
        '5.1.2': 'docs/5.1.2-quantitative-methods.json',
        '5.1.3': 'docs/5.1.3-qualitative-methods.json',
        '5.1.4': 'docs/5.1.4-mixed-methods.json', 
        '5.1.5': 'docs/5.1.5-emerging-methods.json'
    }
    
    for task_num, file_path in json_files.items():
        try:
            with open(file_path, 'r') as f:
                task_data = json.load(f)
                if 'documented_methods' in task_data:
                    for method_key, method_info in task_data['documented_methods'].items():
                        method_details[method_key] = method_info
        except FileNotFoundError:
            print(f"Warning: Could not load {file_path}")
    
    return method_details

def define_resource_categories():
    """Define comprehensive resource assessment framework"""
    return {
        "human_resources": {
            "description": "Personnel and expertise requirements",
            "subcategories": {
                "researcher_time": {
                    "unit": "person-weeks",
                    "description": "Primary researcher time investment",
                    "factors": ["Learning curve", "Implementation time", "Analysis time", "Documentation time"]
                },
                "expert_consultation": {
                    "unit": "expert-hours", 
                    "description": "External expert input requirements",
                    "factors": ["Method validation", "Domain expertise", "Technical guidance", "Quality assurance"]
                },
                "collaboration_needs": {
                    "unit": "collaboration-weeks",
                    "description": "Required collaboration with other researchers/stakeholders",
                    "factors": ["Data access", "Validation", "Feedback", "Joint analysis"]
                },
                "skill_development": {
                    "unit": "learning-weeks",
                    "description": "Time needed to acquire necessary skills",
                    "factors": ["Technical skills", "Domain knowledge", "Tool proficiency", "Method expertise"]
                }
            }
        },
        "technical_resources": {
            "description": "Technology, tools, and infrastructure requirements",
            "subcategories": {
                "software_tools": {
                    "unit": "tool-licenses",
                    "description": "Required software applications and licenses",
                    "factors": ["Simulation platforms", "Analysis software", "Development tools", "Specialized applications"]
                },
                "hardware_requirements": {
                    "unit": "computing-power",
                    "description": "Computational and hardware needs",
                    "factors": ["Processing power", "Memory requirements", "Storage needs", "Specialized equipment"]
                },
                "data_infrastructure": {
                    "unit": "data-systems",
                    "description": "Data collection, storage, and management systems",
                    "factors": ["Data access", "Storage systems", "Processing pipelines", "Backup systems"]
                },
                "network_connectivity": {
                    "unit": "connectivity-level",
                    "description": "Internet and network access requirements",
                    "factors": ["Bandwidth needs", "Reliability requirements", "Security considerations", "Remote access"]
                }
            }
        },
        "financial_resources": {
            "description": "Monetary costs and budget requirements",
            "subcategories": {
                "software_licensing": {
                    "unit": "EUR",
                    "description": "Cost of software licenses and subscriptions",
                    "factors": ["Academic discounts", "Open source alternatives", "Duration needs", "Feature requirements"]
                },
                "hardware_costs": {
                    "unit": "EUR", 
                    "description": "Equipment purchase or rental costs",
                    "factors": ["Computing equipment", "Specialized hardware", "Rental vs purchase", "Depreciation"]
                },
                "expert_fees": {
                    "unit": "EUR",
                    "description": "Costs for external expert consultation",
                    "factors": ["Hourly rates", "Duration of engagement", "Level of expertise", "Travel costs"]
                },
                "operational_costs": {
                    "unit": "EUR",
                    "description": "Ongoing operational expenses",
                    "factors": ["Cloud computing", "Data storage", "Internet costs", "Miscellaneous expenses"]
                }
            }
        },
        "temporal_resources": {
            "description": "Time-related constraints and scheduling requirements",
            "subcategories": {
                "development_time": {
                    "unit": "weeks",
                    "description": "Time needed for method setup and development",
                    "factors": ["Initial setup", "Tool configuration", "Framework development", "Testing and validation"]
                },
                "execution_time": {
                    "unit": "weeks", 
                    "description": "Active time for method execution",
                    "factors": ["Data collection", "Analysis execution", "Simulation runtime", "Result generation"]
                },
                "analysis_time": {
                    "unit": "weeks",
                    "description": "Time for data analysis and interpretation",
                    "factors": ["Statistical analysis", "Result interpretation", "Validation checks", "Sensitivity analysis"]
                },
                "integration_time": {
                    "unit": "weeks",
                    "description": "Time needed for integration with other methods",
                    "factors": ["Method coordination", "Data integration", "Result synthesis", "Cross-validation"]
                }
            }
        }
    }

def assess_method_resources(method_key, method_info, evaluation_data, resource_framework):
    """Assess resource requirements for a specific method"""
    
    # Get method scores from comparison matrix
    method_scores = None
    if evaluation_data['comparison_matrix']:
        for method in evaluation_data['comparison_matrix']['comparison_matrix']:
            if method['method_key'] == method_key:
                method_scores = method
                break
    
    if not method_scores:
        return None
    
    assessment = {
        "method_key": method_key,
        "method_name": method_info.get('method_name', method_key),
        "category": method_info.get('category', 'Unknown'),
        "overall_score": method_scores.get('weighted_score', 0),
        "resource_requirements": {},
        "total_cost_estimate": {},
        "timeline_breakdown": {},
        "resource_intensity_analysis": {},
        "feasibility_assessment": ""
    }
    
    # Assess each resource category
    implementation_info = method_info.get('implementation_framework', {})
    practical_info = method_info.get('practical_implementation', {})
    
    # Human resources assessment
    assessment['resource_requirements']['human_resources'] = assess_human_resources(
        method_key, method_info, method_scores, resource_framework
    )
    
    # Technical resources assessment
    assessment['resource_requirements']['technical_resources'] = assess_technical_resources(
        method_key, method_info, method_scores, resource_framework
    )
    
    # Financial resources assessment
    assessment['resource_requirements']['financial_resources'] = assess_financial_resources(
        method_key, method_info, method_scores, resource_framework
    )
    
    # Temporal resources assessment
    assessment['resource_requirements']['temporal_resources'] = assess_temporal_resources(
        method_key, method_info, method_scores, resource_framework
    )
    
    # Generate overall assessments
    assessment['total_cost_estimate'] = calculate_total_costs(assessment['resource_requirements'])
    assessment['timeline_breakdown'] = generate_timeline_breakdown(assessment['resource_requirements'])
    assessment['resource_intensity_analysis'] = analyze_resource_intensity(assessment, method_scores)
    assessment['feasibility_assessment'] = generate_feasibility_assessment(assessment, method_scores)
    
    return assessment

def assess_human_resources(method_key, method_info, method_scores, framework):
    """Assess human resource requirements"""
    human_resources = {}
    
    # Researcher time based on complexity and scope
    feasibility_score = method_scores.get('feasibility', 0)
    if feasibility_score >= 4:
        researcher_weeks = 2.0  # High feasibility = low time
    elif feasibility_score >= 3:
        researcher_weeks = 4.0  # Moderate feasibility
    elif feasibility_score >= 2:
        researcher_weeks = 6.0  # Low feasibility = high time
    else:
        researcher_weeks = 8.0  # Very low feasibility
    
    human_resources['researcher_time'] = {
        "estimate": researcher_weeks,
        "unit": "person-weeks",
        "confidence": "medium",
        "factors": [
            f"Feasibility score: {feasibility_score}/5",
            "Learning curve considerations",
            "Implementation complexity",
            "Documentation requirements"
        ]
    }
    
    # Expert consultation needs
    expert_hours = 4.0  # Base requirement
    if method_scores.get('relevance', 0) <= 3:
        expert_hours += 2.0  # Need more validation for lower relevance
    if any('expert' in str(req).lower() for req in method_info.get('implementation_framework', {}).get('required_tools', [])):
        expert_hours += 3.0  # Method specifically requires expert input
    
    human_resources['expert_consultation'] = {
        "estimate": expert_hours,
        "unit": "expert-hours", 
        "confidence": "medium",
        "factors": [
            "Method validation needs",
            "Domain expertise requirements",
            "Quality assurance needs"
        ]
    }
    
    # Skill development time
    skill_requirements = method_info.get('implementation_framework', {}).get('skill_requirements', [])
    learning_curve = method_info.get('implementation_framework', {}).get('learning_curve', '')
    
    if 'high' in learning_curve.lower():
        skill_weeks = 2.0
    elif 'moderate' in learning_curve.lower():
        skill_weeks = 1.0
    else:
        skill_weeks = 0.5
    
    human_resources['skill_development'] = {
        "estimate": skill_weeks,
        "unit": "learning-weeks",
        "confidence": "medium",
        "factors": [
            f"Learning curve: {learning_curve}",
            f"Required skills: {len(skill_requirements)}",
            "Prior experience assumptions"
        ]
    }
    
    # Collaboration needs (minimal for thesis work)
    human_resources['collaboration_needs'] = {
        "estimate": 0.5,
        "unit": "collaboration-weeks",
        "confidence": "high",
        "factors": [
            "Supervisor consultations",
            "Peer review activities",
            "Academic community engagement"
        ]
    }
    
    return human_resources

def assess_technical_resources(method_key, method_info, method_scores, framework):
    """Assess technical resource requirements"""
    technical_resources = {}
    
    # Software tools
    required_tools = method_info.get('implementation_framework', {}).get('required_tools', [])
    tool_count = len([tool for tool in required_tools if tool])  # Count non-empty tools
    
    technical_resources['software_tools'] = {
        "estimate": tool_count,
        "unit": "tool-licenses",
        "confidence": "high",
        "details": required_tools[:5],  # Show first 5 tools
        "factors": [
            f"Total tools required: {tool_count}",
            "Academic licensing availability",
            "Open source alternatives"
        ]
    }
    
    # Hardware requirements based on method type
    if method_key in ['experimental_simulation', 'digital_twin_methodology']:
        compute_level = "high"
        compute_score = 4
    elif method_key in ['comparative_analysis', 'metrics_framework']:
        compute_level = "medium"
        compute_score = 2
    else:
        compute_level = "low"
        compute_score = 1
    
    technical_resources['hardware_requirements'] = {
        "estimate": compute_score,
        "unit": "computing-power-level",
        "confidence": "medium",
        "details": f"Computing level: {compute_level}",
        "factors": [
            "Simulation complexity",
            "Data processing needs",
            "Parallel computation requirements"
        ]
    }
    
    # Data infrastructure
    data_needs = 1  # Base requirement
    if 'data' in method_info.get('primary_purpose', '').lower():
        data_needs += 1
    if any('database' in str(tool).lower() for tool in required_tools):
        data_needs += 1
    
    technical_resources['data_infrastructure'] = {
        "estimate": data_needs,
        "unit": "data-systems",
        "confidence": "medium",
        "factors": [
            "Data collection requirements",
            "Storage and backup needs",
            "Processing pipeline complexity"
        ]
    }
    
    # Network connectivity (standard requirement)
    technical_resources['network_connectivity'] = {
        "estimate": 1,
        "unit": "standard-connectivity",
        "confidence": "high",
        "factors": [
            "Standard academic internet access",
            "Cloud service access needs",
            "Collaboration requirements"
        ]
    }
    
    return technical_resources

def assess_financial_resources(method_key, method_info, method_scores, framework):
    """Assess financial resource requirements"""
    financial_resources = {}
    
    # Software licensing costs
    required_tools = method_info.get('implementation_framework', {}).get('required_tools', [])
    
    # Estimate based on tool types
    software_cost = 0
    for tool in required_tools:
        if any(commercial in str(tool).lower() for commercial in ['powerworld', 'matlab', 'expert choice']):
            software_cost += 200  # Commercial academic license
        elif any(cloud in str(tool).lower() for cloud in ['cloud', 'aws', 'azure']):
            software_cost += 50   # Cloud services
        # Open source tools have no cost
    
    financial_resources['software_licensing'] = {
        "estimate": software_cost,
        "unit": "EUR",
        "confidence": "medium",
        "factors": [
            f"Commercial tools: {len([t for t in required_tools if 'commercial' in str(t).lower()])}",
            "Academic licensing discounts",
            "Open source alternatives available"
        ]
    }
    
    # Hardware costs (mostly covered by university)
    hardware_cost = 0
    if method_key in ['experimental_simulation', 'digital_twin_methodology']:
        hardware_cost = 100  # Cloud computing costs
    
    financial_resources['hardware_costs'] = {
        "estimate": hardware_cost,
        "unit": "EUR",
        "confidence": "medium",
        "factors": [
            "University infrastructure available",
            "Cloud computing supplements",
            "Specialized equipment needs"
        ]
    }
    
    # Expert fees (academic context - minimal)
    expert_cost = 0  # Assume academic supervision covers this
    
    financial_resources['expert_fees'] = {
        "estimate": expert_cost,
        "unit": "EUR",
        "confidence": "high",
        "factors": [
            "Academic supervision included",
            "Internal university expertise",
            "Conference/workshop costs"
        ]
    }
    
    # Operational costs
    operational_cost = 25  # Base operational needs
    
    financial_resources['operational_costs'] = {
        "estimate": operational_cost,
        "unit": "EUR",
        "confidence": "medium",
        "factors": [
            "Internet and communication costs",
            "Documentation and printing",
            "Miscellaneous project expenses"
        ]
    }
    
    return financial_resources

def assess_temporal_resources(method_key, method_info, method_scores, framework):
    """Assess temporal resource requirements"""
    temporal_resources = {}
    
    # Development time based on setup complexity
    setup_complexity = method_info.get('implementation_framework', {}).get('setup_complexity', '')
    if 'high' in setup_complexity.lower():
        dev_weeks = 3.0
    elif 'moderate' in setup_complexity.lower():
        dev_weeks = 2.0
    else:
        dev_weeks = 1.0
    
    temporal_resources['development_time'] = {
        "estimate": dev_weeks,
        "unit": "weeks",
        "confidence": "medium",
        "factors": [
            f"Setup complexity: {setup_complexity}",
            "Tool installation and configuration",
            "Framework development",
            "Initial testing"
        ]
    }
    
    # Execution time based on method type
    if method_key == 'experimental_simulation':
        exec_weeks = 4.0  # Simulation runs take time
    elif method_key in ['comparative_analysis', 'document_analysis']:
        exec_weeks = 2.0  # Analysis-focused methods
    elif method_key in ['case_study_analysis', 'expert_evaluation']:
        exec_weeks = 3.0  # Data collection methods
    else:
        exec_weeks = 2.0  # Default
    
    temporal_resources['execution_time'] = {
        "estimate": exec_weeks,
        "unit": "weeks",
        "confidence": "medium",
        "factors": [
            "Method-specific execution requirements",
            "Data collection time",
            "Processing and simulation time",
            "Quality assurance activities"
        ]
    }
    
    # Analysis time
    analysis_weeks = 1.5  # Standard analysis time
    if method_scores.get('potential_impact', 0) >= 4:
        analysis_weeks += 0.5  # More analysis for high-impact methods
    
    temporal_resources['analysis_time'] = {
        "estimate": analysis_weeks,
        "unit": "weeks",
        "confidence": "medium",
        "factors": [
            "Statistical analysis requirements",
            "Result interpretation complexity",
            "Validation and verification",
            "Documentation preparation"
        ]
    }
    
    # Integration time (for method combination)
    temporal_resources['integration_time'] = {
        "estimate": 0.5,
        "unit": "weeks",
        "confidence": "medium",
        "factors": [
            "Method coordination needs",
            "Data integration requirements",
            "Result synthesis activities",
            "Cross-validation processes"
        ]
    }
    
    return temporal_resources

def calculate_total_costs(resource_requirements):
    """Calculate total estimated costs across all categories"""
    total_costs = {
        "financial_total": 0,
        "time_total": 0,
        "cost_breakdown": {},
        "time_breakdown": {}
    }
    
    # Sum financial costs
    financial = resource_requirements.get('financial_resources', {})
    for cost_type, cost_info in financial.items():
        cost = cost_info.get('estimate', 0)
        total_costs['financial_total'] += cost
        total_costs['cost_breakdown'][cost_type] = cost
    
    # Sum time requirements
    human_time = resource_requirements.get('human_resources', {}).get('researcher_time', {}).get('estimate', 0)
    temporal = resource_requirements.get('temporal_resources', {})
    
    total_time = human_time
    for time_type, time_info in temporal.items():
        time_weeks = time_info.get('estimate', 0)
        total_time += time_weeks
        total_costs['time_breakdown'][time_type] = time_weeks
    
    total_costs['time_total'] = total_time
    
    return total_costs

def generate_timeline_breakdown(resource_requirements):
    """Generate detailed timeline breakdown"""
    timeline = {
        "total_duration": 0,
        "phases": [],
        "critical_path": [],
        "parallel_activities": []
    }
    
    temporal = resource_requirements.get('temporal_resources', {})
    
    # Sequential phases
    phases = [
        ("Development", temporal.get('development_time', {}).get('estimate', 0)),
        ("Execution", temporal.get('execution_time', {}).get('estimate', 0)),
        ("Analysis", temporal.get('analysis_time', {}).get('estimate', 0)),
        ("Integration", temporal.get('integration_time', {}).get('estimate', 0))
    ]
    
    cumulative_time = 0
    for phase_name, duration in phases:
        timeline['phases'].append({
            "phase": phase_name,
            "duration": duration,
            "start_week": cumulative_time,
            "end_week": cumulative_time + duration
        })
        cumulative_time += duration
    
    timeline['total_duration'] = cumulative_time
    
    # Identify critical path (longest sequence)
    timeline['critical_path'] = [phase['phase'] for phase in timeline['phases'] if phase['duration'] > 0]
    
    return timeline

def analyze_resource_intensity(assessment, method_scores):
    """Analyze overall resource intensity"""
    analysis = {
        "intensity_level": "",
        "resource_efficiency": 0,
        "bottlenecks": [],
        "optimization_opportunities": []
    }
    
    # Calculate resource intensity based on costs and time
    financial_total = assessment['total_cost_estimate']['financial_total']
    time_total = assessment['total_cost_estimate']['time_total']
    
    # Normalize and combine (simple approach)
    financial_norm = min(financial_total / 500, 1.0)  # Normalize to 0-1 scale
    time_norm = min(time_total / 20, 1.0)  # Normalize to 0-1 scale (20 weeks = full thesis)
    
    intensity = (financial_norm + time_norm) / 2
    
    if intensity < 0.3:
        analysis['intensity_level'] = "Low"
    elif intensity < 0.6:
        analysis['intensity_level'] = "Medium"
    else:
        analysis['intensity_level'] = "High"
    
    # Resource efficiency (benefit vs cost)
    overall_score = method_scores.get('weighted_score', 0)
    if time_total > 0:
        analysis['resource_efficiency'] = overall_score / time_total
    else:
        analysis['resource_efficiency'] = overall_score
    
    # Identify bottlenecks
    if time_total > 15:  # More than 75% of thesis time
        analysis['bottlenecks'].append("High time requirements")
    if financial_total > 300:
        analysis['bottlenecks'].append("High financial costs")
    
    # Optimization opportunities
    if financial_total > 200:
        analysis['optimization_opportunities'].append("Explore open source alternatives")
    if time_total > 12:
        analysis['optimization_opportunities'].append("Consider parallel execution with other methods")
    
    return analysis

def generate_feasibility_assessment(assessment, method_scores):
    """Generate overall feasibility assessment"""
    financial_total = assessment['total_cost_estimate']['financial_total']
    time_total = assessment['total_cost_estimate']['time_total']
    intensity_level = assessment['resource_intensity_analysis']['intensity_level']
    
    # Feasibility decision logic
    if time_total > 16:  # More than 80% of thesis time
        return "LOW FEASIBILITY - Exceeds reasonable time allocation for thesis project"
    elif financial_total > 500:  # High financial burden
        return "LOW FEASIBILITY - Financial requirements exceed typical thesis budget"
    elif intensity_level == "High" and method_scores.get('weighted_score', 0) < 3.5:
        return "LOW FEASIBILITY - High resource intensity not justified by method quality"
    elif time_total > 12 and intensity_level == "High":
        return "MODERATE FEASIBILITY - High resource requirements but manageable with careful planning"
    elif method_scores.get('weighted_score', 0) >= 4.0:
        return "HIGH FEASIBILITY - Strong method with reasonable resource requirements"
    else:
        return "MODERATE FEASIBILITY - Balanced resource requirements and method quality"

def assess_all_method_resources():
    """Main function to assess resource requirements for all methods"""
    print("=== Task 5.2.3: Assess Resource Requirements ===")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Load required data
    print("Loading evaluation data and method details...")
    evaluation_data = load_previous_evaluations()
    method_details = load_method_details()
    
    if not all(evaluation_data.values()) or not method_details:
        print("Error: Required data not available")
        return None
    
    print(f"✓ Loaded evaluation data from previous tasks")
    print(f"✓ Loaded detailed information for {len(method_details)} methods")
    
    # Define resource framework
    resource_framework = define_resource_categories()
    print(f"✓ Defined resource framework with {len(resource_framework)} categories")
    
    # Assess each method
    assessments = []
    for method in evaluation_data['comparison_matrix']['comparison_matrix']:
        method_key = method['method_key']
        if method_key in method_details:
            assessment = assess_method_resources(
                method_key, method_details[method_key], evaluation_data, resource_framework
            )
            if assessment:
                assessments.append(assessment)
    
    print(f"✓ Completed resource assessments for {len(assessments)} methods")
    
    # Generate summary analysis
    summary = generate_resource_summary(assessments)
    
    # Compile comprehensive output
    output = {
        "task": "5.2.3 - Assess Resource Requirements",
        "timestamp": datetime.now().isoformat(),
        "research_context": evaluation_data['comparison_matrix']['research_context'],
        "resource_framework": resource_framework,
        "method_assessments": assessments,
        "summary_analysis": summary,
        "implementation_recommendations": generate_implementation_recommendations(assessments)
    }
    
    # Save outputs
    os.makedirs("docs", exist_ok=True)
    
    # Save detailed JSON
    with open("docs/5.2.3-resource-requirements.json", "w") as f:
        json.dump(output, f, indent=2)
    
    # Generate markdown report
    markdown_content = generate_markdown_report(output)
    with open("docs/5.2.3-resource-requirements.md", "w") as f:
        f.write(markdown_content)
    
    print()
    print("=== Resource Assessment Results ===")
    print(f"Methods Assessed: {len(assessments)}")
    print(f"High Feasibility: {summary['feasibility_distribution']['high']}")
    print(f"Moderate Feasibility: {summary['feasibility_distribution']['moderate']}")
    print(f"Low Feasibility: {summary['feasibility_distribution']['low']}")
    
    return output

def generate_resource_summary(assessments):
    """Generate summary analysis of resource requirements"""
    summary = {
        "total_methods": len(assessments),
        "feasibility_distribution": {"high": 0, "moderate": 0, "low": 0},
        "cost_analysis": {"min": float('inf'), "max": 0, "average": 0},
        "time_analysis": {"min": float('inf'), "max": 0, "average": 0},
        "resource_efficiency": {"highest": None, "lowest": None},
        "optimization_priorities": []
    }
    
    total_cost = 0
    total_time = 0
    max_efficiency = 0
    min_efficiency = float('inf')
    
    for assessment in assessments:
        # Feasibility distribution
        feasibility = assessment['feasibility_assessment']
        if "HIGH FEASIBILITY" in feasibility:
            summary['feasibility_distribution']['high'] += 1
        elif "MODERATE FEASIBILITY" in feasibility:
            summary['feasibility_distribution']['moderate'] += 1
        else:
            summary['feasibility_distribution']['low'] += 1
        
        # Cost and time analysis
        cost = assessment['total_cost_estimate']['financial_total']
        time = assessment['total_cost_estimate']['time_total']
        
        summary['cost_analysis']['min'] = min(summary['cost_analysis']['min'], cost)
        summary['cost_analysis']['max'] = max(summary['cost_analysis']['max'], cost)
        summary['time_analysis']['min'] = min(summary['time_analysis']['min'], time)
        summary['time_analysis']['max'] = max(summary['time_analysis']['max'], time)
        
        total_cost += cost
        total_time += time
        
        # Resource efficiency tracking
        efficiency = assessment['resource_intensity_analysis']['resource_efficiency']
        if efficiency > max_efficiency:
            max_efficiency = efficiency
            summary['resource_efficiency']['highest'] = assessment['method_name']
        if efficiency < min_efficiency:
            min_efficiency = efficiency
            summary['resource_efficiency']['lowest'] = assessment['method_name']
    
    # Calculate averages
    if assessments:
        summary['cost_analysis']['average'] = total_cost / len(assessments)
        summary['time_analysis']['average'] = total_time / len(assessments)
    
    return summary

def generate_implementation_recommendations(assessments):
    """Generate implementation recommendations based on resource analysis"""
    recommendations = {
        "resource_optimization": [],
        "sequencing_strategy": [],
        "risk_mitigation": [],
        "budget_allocation": {}
    }
    
    # Find high-efficiency methods
    high_efficiency = [a for a in assessments if a['resource_intensity_analysis']['resource_efficiency'] > 0.3]
    high_efficiency.sort(key=lambda a: a['resource_intensity_analysis']['resource_efficiency'], reverse=True)
    
    if high_efficiency:
        recommendations['resource_optimization'].append(
            f"Prioritize high-efficiency methods: {', '.join([a['method_name'] for a in high_efficiency[:3]])}"
        )
    
    # Sequencing strategy
    low_resource = [a for a in assessments if a['total_cost_estimate']['time_total'] < 6]
    high_resource = [a for a in assessments if a['total_cost_estimate']['time_total'] >= 10]
    
    if low_resource:
        recommendations['sequencing_strategy'].append(
            f"Start with low-resource methods: {', '.join([a['method_name'] for a in low_resource[:2]])}"
        )
    
    if high_resource:
        recommendations['sequencing_strategy'].append(
            f"Plan high-resource methods carefully: {', '.join([a['method_name'] for a in high_resource[:2]])}"
        )
    
    return recommendations

def generate_markdown_report(output):
    """Generate markdown report for resource requirements analysis"""
    markdown = f"""# Resource Requirements Assessment (Task 5.2.3)

*Generated: {output['timestamp']}*

## Research Context

**Focus**: {output['research_context']['focus']}
**Domain**: {output['research_context']['domain']}
**Overarching Methodology**: {output['research_context']['overarching_methodology']}

## Assessment Overview

**Total Methods Assessed**: {output['summary_analysis']['total_methods']}
**High Feasibility**: {output['summary_analysis']['feasibility_distribution']['high']}
**Moderate Feasibility**: {output['summary_analysis']['feasibility_distribution']['moderate']}
**Low Feasibility**: {output['summary_analysis']['feasibility_distribution']['low']}

## Resource Summary

### Cost Analysis
- **Minimum Cost**: {output['summary_analysis']['cost_analysis']['min']:.0f} EUR
- **Maximum Cost**: {output['summary_analysis']['cost_analysis']['max']:.0f} EUR  
- **Average Cost**: {output['summary_analysis']['cost_analysis']['average']:.0f} EUR

### Time Analysis
- **Minimum Time**: {output['summary_analysis']['time_analysis']['min']:.1f} weeks
- **Maximum Time**: {output['summary_analysis']['time_analysis']['max']:.1f} weeks
- **Average Time**: {output['summary_analysis']['time_analysis']['average']:.1f} weeks

### Resource Efficiency
- **Most Efficient**: {output['summary_analysis']['resource_efficiency']['highest']}
- **Least Efficient**: {output['summary_analysis']['resource_efficiency']['lowest']}

## Method Resource Assessments

### High Feasibility Methods

"""
    
    for assessment in output['method_assessments']:
        if "HIGH FEASIBILITY" in assessment['feasibility_assessment']:
            markdown += f"""#### {assessment['method_name']}
**Category**: {assessment['category']} | **Score**: {assessment['overall_score']:.2f}

**Resource Summary**:
- **Total Cost**: {assessment['total_cost_estimate']['financial_total']:.0f} EUR
- **Total Time**: {assessment['total_cost_estimate']['time_total']:.1f} weeks
- **Resource Intensity**: {assessment['resource_intensity_analysis']['intensity_level']}

**Feasibility**: {assessment['feasibility_assessment']}

"""
    
    markdown += """### Moderate Feasibility Methods

"""
    
    for assessment in output['method_assessments']:
        if "MODERATE FEASIBILITY" in assessment['feasibility_assessment']:
            markdown += f"""#### {assessment['method_name']}
**Category**: {assessment['category']} | **Score**: {assessment['overall_score']:.2f}

**Resource Summary**:
- **Total Cost**: {assessment['total_cost_estimate']['financial_total']:.0f} EUR
- **Total Time**: {assessment['total_cost_estimate']['time_total']:.1f} weeks
- **Resource Intensity**: {assessment['resource_intensity_analysis']['intensity_level']}

**Feasibility**: {assessment['feasibility_assessment']}

"""
    
    markdown += """## Implementation Recommendations

### Resource Optimization
"""
    
    for rec in output['implementation_recommendations']['resource_optimization']:
        markdown += f"- {rec}\n"
    
    markdown += """
### Sequencing Strategy
"""
    
    for rec in output['implementation_recommendations']['sequencing_strategy']:
        markdown += f"- {rec}\n"
    
    markdown += """## Sources Used

- Comparison matrix from `docs/5.2.1-comparison-matrix.json`
- Strengths/limitations analysis from `docs/5.2.2-strengths-limitations.json`
- Method details from `docs/5.1.2-quantitative-methods.json`
- Method details from `docs/5.1.3-qualitative-methods.json`
- Method details from `docs/5.1.4-mixed-methods.json`
- Method details from `docs/5.1.5-emerging-methods.json`

---

*Task 5.2.3 completed - Resource requirements systematically assessed*
*Ready for feasibility analysis in Task 5.2.4*
"""
    
    return markdown

if __name__ == "__main__":
    assess_all_method_resources() 
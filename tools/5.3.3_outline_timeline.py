#!/usr/bin/env python3
"""
Task 5.3.3: Outline Rough Timeline

Focus: Detailed project timeline for hybrid methodology approach
Context: Agent Communication Protocol research with 20-week thesis constraint

Based on:
- Results from 5.3.1 methodology justification (hybrid approach)
- 5.3.2 limitations and mitigation strategies
- 5.2.3 resource requirements assessment
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

# --- Configuration ---
METHODOLOGY_JUSTIFICATION_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.1-methodology-justification.json"
LIMITATIONS_ANALYSIS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.2-methodology-limitations-analysis.json"
RESOURCE_ASSESSMENT_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.3-resource-requirements-assessment.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.3.3_outline_timeline.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analyses ---
def load_previous_analyses():
    methodology_justification = {}
    limitations_analysis = {}
    resource_assessment = {}
    
    files_to_load = [
        (METHODOLOGY_JUSTIFICATION_INPUT_JSON, "methodology_justification"),
        (LIMITATIONS_ANALYSIS_INPUT_JSON, "limitations_analysis"),
        (RESOURCE_ASSESSMENT_INPUT_JSON, "resource_assessment")
    ]
    
    for file_path, data_name in files_to_load:
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data_name == "methodology_justification":
                        methodology_justification = data
                    elif data_name == "limitations_analysis":
                        limitations_analysis = data
                    elif data_name == "resource_assessment":
                        resource_assessment = data
                write_log(f"Loaded data from {file_path.name}")
            except Exception as e:
                write_log(f"Error loading {file_path.name}: {e}")
        else:
            write_log(f"Warning: {file_path.name} not found")
    
    return methodology_justification, limitations_analysis, resource_assessment

# --- Timeline Development Functions ---
def extract_phase_structure(methodology_justification):
    """Extract the phase structure from methodology justification"""
    
    hybrid_phases = methodology_justification.get("methodology_justification", {}).get("hybrid_methodology_consideration", {}).get("phases", [])
    
    phases = []
    for phase in hybrid_phases:
        phase_info = {
            "name": phase.get("phase", "Unknown Phase"),
            "methodology": phase.get("methodology", "Unknown Methodology"),
            "focus": phase.get("focus", "Unknown Focus"),
            "duration_range": phase.get("duration", "Unknown Duration"),
            "min_weeks": 0,
            "max_weeks": 0
        }
        
        # Parse duration range
        duration_str = phase_info["duration_range"]
        if "weeks" in duration_str:
            import re
            weeks = re.findall(r'\d+', duration_str)
            if len(weeks) >= 2:
                phase_info["min_weeks"] = int(weeks[0])
                phase_info["max_weeks"] = int(weeks[1])
            elif len(weeks) == 1:
                phase_info["min_weeks"] = int(weeks[0])
                phase_info["max_weeks"] = int(weeks[0])
        
        phases.append(phase_info)
    
    return phases

def develop_detailed_phase_timelines(phases, limitations_analysis):
    """Develop detailed timelines for each phase with activities and milestones"""
    
    detailed_phases = []
    
    for i, phase in enumerate(phases):
        phase_details = {
            "phase_number": i + 1,
            "name": phase["name"],
            "methodology": phase["methodology"],
            "focus": phase["focus"],
            "duration_weeks": phase["max_weeks"],  # Use max for conservative planning
            "activities": [],
            "milestones": [],
            "dependencies": [],
            "risk_factors": [],
            "buffer_time": 0
        }
        
        # Define activities based on methodology
        if "Literature Review" in phase["methodology"]:
            phase_details["activities"] = [
                {"activity": "Search strategy refinement", "duration_weeks": 1, "week_start": 1},
                {"activity": "Database searches and screening", "duration_weeks": 2, "week_start": 2},
                {"activity": "Full-text review and data extraction", "duration_weeks": 2, "week_start": 4},
                {"activity": "Protocol composition pattern analysis", "duration_weeks": 1, "week_start": 6},
                {"activity": "Literature synthesis and gap identification", "duration_weeks": 2, "week_start": 7}
            ]
            phase_details["milestones"] = [
                {"milestone": "Search strategy approved", "week": 1},
                {"milestone": "Initial screening complete", "week": 3},
                {"milestone": "Full-text review complete", "week": 6},
                {"milestone": "Literature synthesis complete", "week": 8}
            ]
            
        elif "Comparative Research" in phase["methodology"]:
            phase_details["activities"] = [
                {"activity": "Framework design and validation", "duration_weeks": 2, "week_start": 1},
                {"activity": "ACP protocol analysis", "duration_weeks": 2, "week_start": 3},
                {"activity": "A2A protocol analysis", "duration_weeks": 2, "week_start": 5},
                {"activity": "Comparative evaluation", "duration_weeks": 2, "week_start": 7},
                {"activity": "Integration pattern assessment", "duration_weeks": 2, "week_start": 9}
            ]
            phase_details["milestones"] = [
                {"milestone": "Comparison framework validated", "week": 2},
                {"milestone": "ACP analysis complete", "week": 4},
                {"milestone": "A2A analysis complete", "week": 6},
                {"milestone": "Comparative evaluation complete", "week": 8},
                {"milestone": "Integration assessment complete", "week": 10}
            ]
            
        elif "Rapid Prototyping" in phase["methodology"]:
            phase_details["activities"] = [
                {"activity": "Prototype design and specification", "duration_weeks": 1, "week_start": 1},
                {"activity": "Core protocol integration development", "duration_weeks": 2, "week_start": 2},
                {"activity": "Testing and validation", "duration_weeks": 1, "week_start": 4},
                {"activity": "Documentation and evaluation", "duration_weeks": 1, "week_start": 5},
                {"activity": "Integration with previous findings", "duration_weeks": 1, "week_start": 6}
            ]
            phase_details["milestones"] = [
                {"milestone": "Prototype design approved", "week": 1},
                {"milestone": "Core integration developed", "week": 3},
                {"milestone": "Testing complete", "week": 4},
                {"milestone": "Prototype documentation complete", "week": 5},
                {"milestone": "Integration analysis complete", "week": 6}
            ]
        
        # Add dependencies
        if i > 0:
            phase_details["dependencies"] = [f"Completion of {phases[i-1]['name']}"]
        
        # Add risk factors from limitations analysis
        mitigation_strategies = limitations_analysis.get("mitigation_strategies", {})
        phase_specific_mitigations = mitigation_strategies.get("phase_specific_mitigations", {})
        
        if phase["name"] in phase_specific_mitigations:
            phase_details["risk_factors"] = [
                mitigation["strategy"] for mitigation in phase_specific_mitigations[phase["name"]]
            ]
        
        # Add buffer time (10% of phase duration, minimum 0.5 weeks)
        base_buffer = max(0.5, phase_details["duration_weeks"] * 0.1)
        phase_details["buffer_time"] = round(base_buffer, 1)
        
        detailed_phases.append(phase_details)
    
    return detailed_phases

def create_project_timeline(detailed_phases, limitations_analysis):
    """Create overall project timeline with critical path and risk management"""
    
    # Calculate total duration
    total_duration = sum(phase["duration_weeks"] + phase["buffer_time"] for phase in detailed_phases)
    
    # Project timeline structure
    project_timeline = {
        "total_duration_weeks": round(total_duration, 1),
        "phases": detailed_phases,
        "critical_path": [],
        "integration_points": [],
        "risk_management_schedule": [],
        "review_schedule": [],
        "deliverable_schedule": []
    }
    
    # Identify critical path
    current_week = 0
    for phase in detailed_phases:
        start_week = current_week + 1
        end_week = current_week + phase["duration_weeks"]
        
        project_timeline["critical_path"].append({
            "phase": phase["name"],
            "start_week": start_week,
            "end_week": end_week,
            "buffer_start": end_week + 1,
            "buffer_end": end_week + phase["buffer_time"]
        })
        
        current_week = end_week + phase["buffer_time"]
    
    # Define integration points
    project_timeline["integration_points"] = [
        {
            "point": "Phase 1-2 Integration",
            "week": detailed_phases[0]["duration_weeks"] + detailed_phases[0]["buffer_time"],
            "purpose": "Transfer literature findings to comparative framework",
            "activities": ["Knowledge transfer meeting", "Framework refinement", "Gap validation"]
        },
        {
            "point": "Phase 2-3 Integration", 
            "week": sum(phase["duration_weeks"] + phase["buffer_time"] for phase in detailed_phases[:2]),
            "purpose": "Transfer comparative insights to prototype design",
            "activities": ["Design requirements specification", "Architecture planning", "Validation criteria definition"]
        },
        {
            "point": "Final Integration",
            "week": total_duration - 1,
            "purpose": "Synthesize all findings into coherent conclusions",
            "activities": ["Cross-phase synthesis", "Conclusion development", "Final validation"]
        }
    ]
    
    # Risk management schedule from limitations analysis
    risk_monitoring = limitations_analysis.get("residual_risks", {}).get("risk_monitoring_plan", [])
    
    project_timeline["risk_management_schedule"] = []
    for risk_monitor in risk_monitoring:
        if risk_monitor["monitoring_frequency"] == "Weekly":
            project_timeline["risk_management_schedule"].append({
                "risk_category": risk_monitor["risk_category"],
                "frequency": "Weekly",
                "weeks": list(range(1, int(total_duration) + 1))
            })
        elif risk_monitor["monitoring_frequency"] == "Bi-weekly":
            project_timeline["risk_management_schedule"].append({
                "risk_category": risk_monitor["risk_category"],
                "frequency": "Bi-weekly", 
                "weeks": list(range(2, int(total_duration) + 1, 2))
            })
        elif "End of each phase" in risk_monitor["monitoring_frequency"]:
            phase_end_weeks = []
            current_week = 0
            for phase in detailed_phases:
                current_week += phase["duration_weeks"] + phase["buffer_time"]
                phase_end_weeks.append(int(current_week))
            project_timeline["risk_management_schedule"].append({
                "risk_category": risk_monitor["risk_category"],
                "frequency": "End of phase",
                "weeks": phase_end_weeks
            })
    
    # Review schedule
    project_timeline["review_schedule"] = [
        {"review_type": "Supervisor meeting", "frequency": "Weekly", "weeks": list(range(1, int(total_duration) + 1))},
        {"review_type": "Phase review", "frequency": "End of phase", "weeks": [
            int(detailed_phases[0]["duration_weeks"] + detailed_phases[0]["buffer_time"]),
            int(sum(phase["duration_weeks"] + phase["buffer_time"] for phase in detailed_phases[:2])),
            int(total_duration)
        ]},
        {"review_type": "Progress assessment", "frequency": "Monthly", "weeks": list(range(4, int(total_duration) + 1, 4))}
    ]
    
    # Deliverable schedule
    project_timeline["deliverable_schedule"] = [
        {
            "deliverable": "Literature Review Report",
            "week": int(detailed_phases[0]["duration_weeks"]),
            "phase": "Phase 1: Systematic Literature Review"
        },
        {
            "deliverable": "Comparative Analysis Report", 
            "week": int(sum(phase["duration_weeks"] for phase in detailed_phases[:2])),
            "phase": "Phase 2: Comparative Framework Development"
        },
        {
            "deliverable": "Prototype and Integration Report",
            "week": int(sum(phase["duration_weeks"] for phase in detailed_phases)),
            "phase": "Phase 3: Proof of Concept"
        },
        {
            "deliverable": "Final Thesis Document",
            "week": int(total_duration),
            "phase": "Project Completion"
        }
    ]
    
    return project_timeline

def assess_timeline_feasibility(project_timeline, limitations_analysis):
    """Assess timeline feasibility and provide recommendations"""
    
    total_weeks = project_timeline["total_duration_weeks"]
    target_weeks = 20  # Standard thesis duration
    
    feasibility_assessment = {
        "duration_analysis": {
            "planned_duration": total_weeks,
            "target_duration": target_weeks,
            "variance_weeks": total_weeks - target_weeks,
            "variance_percentage": ((total_weeks - target_weeks) / target_weeks) * 100
        },
        "feasibility_rating": "Feasible",
        "key_risks": [],
        "optimization_opportunities": [],
        "contingency_plans": []
    }
    
    # Determine feasibility rating
    if total_weeks <= target_weeks:
        feasibility_assessment["feasibility_rating"] = "Highly Feasible"
    elif total_weeks <= target_weeks * 1.1:
        feasibility_assessment["feasibility_rating"] = "Feasible"
    elif total_weeks <= target_weeks * 1.2:
        feasibility_assessment["feasibility_rating"] = "Challenging but Feasible"
    else:
        feasibility_assessment["feasibility_rating"] = "Requires Optimization"
    
    # Identify key risks from limitations analysis
    high_priority_risks = limitations_analysis.get("residual_risks", {}).get("high_priority_residual_risks", [])
    feasibility_assessment["key_risks"] = [risk["risk"] for risk in high_priority_risks]
    
    # Optimization opportunities
    if total_weeks > target_weeks:
        feasibility_assessment["optimization_opportunities"] = [
            "Parallel execution of independent activities",
            "Reduce buffer time from 10% to 5% for non-critical activities",
            "Streamline integration points with more efficient handoff procedures",
            "Consider accelerated literature review with focused scope"
        ]
    
    # Contingency plans
    feasibility_assessment["contingency_plans"] = [
        {
            "scenario": "Phase 1 overruns by 1-2 weeks",
            "action": "Reduce Phase 2 buffer time and parallelize some Phase 3 planning",
            "impact": "Minimal impact on overall quality"
        },
        {
            "scenario": "Technical challenges in Phase 3",
            "action": "Simplify prototype scope while maintaining integration demonstration",
            "impact": "Reduced prototype complexity but maintained research objectives"
        },
        {
            "scenario": "Integration complexity higher than expected",
            "action": "Focus on key integration points and defer comprehensive integration to final phase",
            "impact": "May require more intensive final synthesis work"
        }
    ]
    
    return feasibility_assessment

def generate_timeline_document(project_timeline, feasibility_assessment, detailed_phases):
    """Generate comprehensive timeline document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Research Project Timeline (Task 5.3.3)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Based on: Hybrid methodology approach with systematic risk management*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    doc_parts.append(f"This timeline outlines a **{project_timeline['total_duration_weeks']:.1f}-week** research project using a hybrid methodology approach. ")
    doc_parts.append(f"The timeline is assessed as **{feasibility_assessment['feasibility_rating']}** with structured risk management and integration points.\n\n")
    
    # Timeline Overview
    doc_parts.append("## Timeline Overview\n\n")
    doc_parts.append(f"- **Total Duration**: {project_timeline['total_duration_weeks']:.1f} weeks\n")
    doc_parts.append(f"- **Target Duration**: {feasibility_assessment['duration_analysis']['target_duration']} weeks\n")
    doc_parts.append(f"- **Variance**: {feasibility_assessment['duration_analysis']['variance_weeks']:+.1f} weeks ({feasibility_assessment['duration_analysis']['variance_percentage']:+.1f}%)\n")
    doc_parts.append(f"- **Feasibility Rating**: {feasibility_assessment['feasibility_rating']}\n\n")
    
    # Phase Details
    doc_parts.append("## Phase Timeline Details\n\n")
    
    for i, phase in enumerate(detailed_phases):
        critical_path_info = project_timeline["critical_path"][i]
        
        doc_parts.append(f"### {phase['name']}\n")
        doc_parts.append(f"**Methodology**: {phase['methodology']}\n")
        doc_parts.append(f"**Focus**: {phase['focus']}\n")
        doc_parts.append(f"**Duration**: {phase['duration_weeks']} weeks (Weeks {critical_path_info['start_week']}-{critical_path_info['end_week']})\n")
        doc_parts.append(f"**Buffer Time**: {phase['buffer_time']} weeks\n\n")
        
        if phase["dependencies"]:
            doc_parts.append("**Dependencies**:\n")
            for dep in phase["dependencies"]:
                doc_parts.append(f"- {dep}\n")
            doc_parts.append("\n")
        
        doc_parts.append("**Activities**:\n")
        for activity in phase["activities"]:
            end_week = activity["week_start"] + activity["duration_weeks"] - 1
            doc_parts.append(f"- **{activity['activity']}** (Weeks {activity['week_start']}-{end_week})\n")
        doc_parts.append("\n")
        
        doc_parts.append("**Milestones**:\n")
        for milestone in phase["milestones"]:
            doc_parts.append(f"- Week {milestone['week']}: {milestone['milestone']}\n")
        doc_parts.append("\n")
        
        doc_parts.append("---\n")
    
    # Integration Points
    doc_parts.append("## Integration Points\n\n")
    for integration in project_timeline["integration_points"]:
        doc_parts.append(f"### {integration['point']} (Week {integration['week']:.0f})\n")
        doc_parts.append(f"**Purpose**: {integration['purpose']}\n")
        doc_parts.append("**Activities**:\n")
        for activity in integration["activities"]:
            doc_parts.append(f"- {activity}\n")
        doc_parts.append("\n")
    
    # Risk Management Schedule
    doc_parts.append("## Risk Management Schedule\n\n")
    doc_parts.append("| Risk Category | Frequency | Monitoring Weeks |\n")
    doc_parts.append("|---------------|-----------|------------------|\n")
    for risk_schedule in project_timeline["risk_management_schedule"]:
        weeks_str = ", ".join(map(str, risk_schedule["weeks"][:8]))  # Show first 8 weeks
        if len(risk_schedule["weeks"]) > 8:
            weeks_str += "..."
        doc_parts.append(f"| {risk_schedule['risk_category']} | {risk_schedule['frequency']} | {weeks_str} |\n")
    doc_parts.append("\n")
    
    # Review Schedule
    doc_parts.append("## Review and Milestone Schedule\n\n")
    
    doc_parts.append("### Deliverables\n")
    for deliverable in project_timeline["deliverable_schedule"]:
        doc_parts.append(f"- **Week {deliverable['week']}**: {deliverable['deliverable']} ({deliverable['phase']})\n")
    doc_parts.append("\n")
    
    doc_parts.append("### Regular Reviews\n")
    for review in project_timeline["review_schedule"]:
        if review["frequency"] == "Weekly":
            doc_parts.append(f"- **{review['review_type']}**: Every week\n")
        elif review["frequency"] == "Monthly":
            doc_parts.append(f"- **{review['review_type']}**: Weeks {', '.join(map(str, review['weeks']))}\n")
        else:
            doc_parts.append(f"- **{review['review_type']}**: Weeks {', '.join(map(str, review['weeks']))}\n")
    doc_parts.append("\n")
    
    # Feasibility Assessment
    doc_parts.append("## Feasibility Assessment\n\n")
    
    if feasibility_assessment["key_risks"]:
        doc_parts.append("### Key Risks\n")
        for risk in feasibility_assessment["key_risks"]:
            doc_parts.append(f"- {risk}\n")
        doc_parts.append("\n")
    
    if feasibility_assessment["optimization_opportunities"]:
        doc_parts.append("### Optimization Opportunities\n")
        for opportunity in feasibility_assessment["optimization_opportunities"]:
            doc_parts.append(f"- {opportunity}\n")
        doc_parts.append("\n")
    
    doc_parts.append("### Contingency Plans\n")
    for plan in feasibility_assessment["contingency_plans"]:
        doc_parts.append(f"**{plan['scenario']}**\n")
        doc_parts.append(f"- Action: {plan['action']}\n")
        doc_parts.append(f"- Impact: {plan['impact']}\n\n")
    
    # Conclusion
    doc_parts.append("## Conclusion\n\n")
    doc_parts.append(f"The proposed timeline provides a structured approach to executing the hybrid methodology within a {project_timeline['total_duration_weeks']:.1f}-week timeframe. ")
    doc_parts.append("The timeline incorporates appropriate buffer time, regular integration points, and comprehensive risk management. ")
    doc_parts.append(f"With a feasibility rating of '{feasibility_assessment['feasibility_rating']}', this timeline provides a realistic path to successful project completion.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def create_optimized_timeline(detailed_phases, limitations_analysis, target_weeks=20):
    """Create an optimized timeline that fits within the target duration"""
    
    # Create optimized phases with reduced durations and overlaps
    optimized_phases = []
    
    for i, phase in enumerate(detailed_phases):
        optimized_phase = phase.copy()
        
        # Reduce durations using minimum estimates and optimization
        if "Literature Review" in phase["methodology"]:
            # Optimize literature review: 6 weeks instead of 8
            optimized_phase["duration_weeks"] = 6
            optimized_phase["activities"] = [
                {"activity": "Search strategy refinement", "duration_weeks": 0.5, "week_start": 1, "optimization": "Parallel with initial searches"},
                {"activity": "Database searches and screening", "duration_weeks": 2, "week_start": 1.5, "optimization": "Accelerated screening with AI tools"},
                {"activity": "Full-text review and data extraction", "duration_weeks": 2, "week_start": 3.5, "optimization": "Focused on high-impact papers"},
                {"activity": "Protocol composition pattern analysis", "duration_weeks": 1, "week_start": 5.5, "optimization": "Concurrent with synthesis"},
                {"activity": "Literature synthesis and gap identification", "duration_weeks": 1, "week_start": 5.5, "optimization": "Streamlined synthesis process"}
            ]
            optimized_phase["milestones"] = [
                {"milestone": "Search strategy approved", "week": 1},
                {"milestone": "Initial screening complete", "week": 3},
                {"milestone": "Full-text review complete", "week": 5},
                {"milestone": "Literature synthesis complete", "week": 6}
            ]
            
        elif "Comparative Research" in phase["methodology"]:
            # Optimize comparative research: 8 weeks instead of 10
            optimized_phase["duration_weeks"] = 8
            optimized_phase["activities"] = [
                {"activity": "Framework design and validation", "duration_weeks": 1.5, "week_start": 1, "optimization": "Leverage literature findings directly"},
                {"activity": "ACP protocol analysis", "duration_weeks": 2, "week_start": 2.5, "optimization": "Focused analysis using established framework"},
                {"activity": "A2A protocol analysis", "duration_weeks": 2, "week_start": 4.5, "optimization": "Parallel validation with ACP insights"},
                {"activity": "Comparative evaluation", "duration_weeks": 1.5, "week_start": 6.5, "optimization": "Concurrent with final analysis"},
                {"activity": "Integration pattern assessment", "duration_weeks": 1, "week_start": 7.5, "optimization": "Streamlined integration focus"}
            ]
            optimized_phase["milestones"] = [
                {"milestone": "Comparison framework validated", "week": 2},
                {"milestone": "ACP analysis complete", "week": 4},
                {"milestone": "A2A analysis complete", "week": 6},
                {"milestone": "Comparative evaluation complete", "week": 7},
                {"milestone": "Integration assessment complete", "week": 8}
            ]
            
        elif "Rapid Prototyping" in phase["methodology"]:
            # Optimize prototyping: 4 weeks instead of 6
            optimized_phase["duration_weeks"] = 4
            optimized_phase["activities"] = [
                {"activity": "Prototype design and specification", "duration_weeks": 0.5, "week_start": 1, "optimization": "Use comparative insights directly"},
                {"activity": "Core protocol integration development", "duration_weeks": 2, "week_start": 1.5, "optimization": "Focused on key integration points"},
                {"activity": "Testing and validation", "duration_weeks": 1, "week_start": 3.5, "optimization": "Simplified validation criteria"},
                {"activity": "Documentation and evaluation", "duration_weeks": 0.5, "week_start": 3.5, "optimization": "Concurrent with testing"},
                {"activity": "Integration with previous findings", "duration_weeks": 0.5, "week_start": 4, "optimization": "Continuous integration approach"}
            ]
            optimized_phase["milestones"] = [
                {"milestone": "Prototype design approved", "week": 1},
                {"milestone": "Core integration developed", "week": 3},
                {"milestone": "Testing complete", "week": 4},
                {"milestone": "Prototype documentation complete", "week": 4},
                {"milestone": "Integration analysis complete", "week": 4}
            ]
        
        # Reduce buffer time to 5% instead of 10%
        optimized_phase["buffer_time"] = round(max(0.25, optimized_phase["duration_weeks"] * 0.05), 2)
        
        # Add optimization notes
        optimized_phase["optimizations_applied"] = []
        if "Literature Review" in phase["methodology"]:
            optimized_phase["optimizations_applied"] = [
                "Parallel search and screening activities",
                "AI-assisted literature screening",
                "Focused scope on protocol composition patterns",
                "Concurrent analysis and synthesis"
            ]
        elif "Comparative Research" in phase["methodology"]:
            optimized_phase["optimizations_applied"] = [
                "Direct leverage of literature review framework",
                "Parallel protocol analysis phases",
                "Streamlined validation processes",
                "Integrated evaluation approach"
            ]
        elif "Rapid Prototyping" in phase["methodology"]:
            optimized_phase["optimizations_applied"] = [
                "Simplified prototype scope",
                "Concurrent design and development",
                "Focused validation on key integration points",
                "Continuous integration methodology"
            ]
        
        optimized_phases.append(optimized_phase)
    
    # Calculate total optimized duration
    total_optimized_duration = sum(phase["duration_weeks"] + phase["buffer_time"] for phase in optimized_phases)
    
    # Create optimized project timeline
    optimized_timeline = {
        "total_duration_weeks": round(total_optimized_duration, 1),
        "phases": optimized_phases,
        "critical_path": [],
        "integration_points": [],
        "parallel_activities": [],
        "risk_management_schedule": [],
        "optimization_summary": {}
    }
    
    # Identify critical path for optimized timeline
    current_week = 0
    for phase in optimized_phases:
        start_week = current_week + 1
        end_week = current_week + phase["duration_weeks"]
        
        optimized_timeline["critical_path"].append({
            "phase": phase["name"],
            "start_week": start_week,
            "end_week": end_week,
            "buffer_start": end_week + 0.1,
            "buffer_end": end_week + phase["buffer_time"]
        })
        
        current_week = end_week + phase["buffer_time"]
    
    # Define optimized integration points (overlapping where possible)
    optimized_timeline["integration_points"] = [
        {
            "point": "Phase 1-2 Integration",
            "week": optimized_phases[0]["duration_weeks"] - 0.5,  # Start before Phase 1 ends
            "purpose": "Early transfer of literature findings to comparative framework",
            "activities": ["Preliminary framework design", "Early gap identification", "Framework pre-validation"],
            "optimization": "Overlapped with Phase 1 completion"
        },
        {
            "point": "Phase 2-3 Integration", 
            "week": sum(phase["duration_weeks"] for phase in optimized_phases[:2]) - 0.5,  # Start before Phase 2 ends
            "purpose": "Early transfer of comparative insights to prototype design",
            "activities": ["Prototype architecture planning", "Technical requirements specification", "Early design validation"],
            "optimization": "Overlapped with Phase 2 completion"
        },
        {
            "point": "Continuous Integration",
            "week": "Throughout project",
            "purpose": "Ongoing synthesis and validation",
            "activities": ["Weekly integration reviews", "Continuous documentation", "Progressive validation"],
            "optimization": "Replaced final integration with continuous approach"
        }
    ]
    
    # Identify parallel activities
    optimized_timeline["parallel_activities"] = [
        {
            "activity_set": "Literature review optimization",
            "activities": ["Search strategy development", "Initial database searches"],
            "weeks": "1-1.5",
            "time_saved": "0.5 weeks"
        },
        {
            "activity_set": "Comparative analysis optimization", 
            "activities": ["Framework validation", "Protocol analysis preparation"],
            "weeks": "6.5-7",
            "time_saved": "0.5 weeks"
        },
        {
            "activity_set": "Prototyping optimization",
            "activities": ["Documentation", "Testing", "Evaluation"],
            "weeks": "3.5-4",
            "time_saved": "1 week"
        }
    ]
    
    # Optimization summary
    original_duration = sum(phase["duration_weeks"] + max(0.5, phase["duration_weeks"] * 0.1) for phase in detailed_phases)
    
    optimized_timeline["optimization_summary"] = {
        "original_duration": round(original_duration, 1),
        "optimized_duration": total_optimized_duration,
        "time_saved": round(original_duration - total_optimized_duration, 1),
        "target_duration": target_weeks,
        "target_achieved": total_optimized_duration <= target_weeks,
        "variance_from_target": round(total_optimized_duration - target_weeks, 1),
        "key_optimizations": [
            "Reduced Phase 1 from 8 to 6 weeks (25% reduction)",
            "Reduced Phase 2 from 10 to 8 weeks (20% reduction)", 
            "Reduced Phase 3 from 6 to 4 weeks (33% reduction)",
            "Reduced buffer time from 10% to 5%",
            "Introduced parallel and overlapping activities",
            "Streamlined integration points"
        ],
        "trade_offs": [
            "Reduced literature review scope requires more focused search strategy",
            "Accelerated comparative analysis may reduce depth in some areas",
            "Simplified prototype may have limited functionality",
            "Reduced buffer time increases risk of schedule pressure",
            "Parallel activities require more intensive coordination"
        ],
        "risk_mitigation": [
            "Regular supervisor meetings to ensure quality is maintained",
            "Early validation checkpoints to catch issues quickly",
            "Flexible scope adjustment mechanisms",
            "Continuous integration to prevent late-stage integration issues"
        ]
    }
    
    return optimized_timeline

def generate_optimization_comparison_document(original_timeline, optimized_timeline, feasibility_assessment):
    """Generate a document comparing original and optimized timelines"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("\n## Timeline Optimization Analysis\n\n")
    doc_parts.append("To address the 20-week constraint, the following optimization analysis demonstrates how the hybrid methodology can be compressed while maintaining research quality.\n\n")
    
    # Optimization Summary
    opt_summary = optimized_timeline["optimization_summary"]
    doc_parts.append("### Optimization Summary\n\n")
    doc_parts.append(f"- **Original Duration**: {opt_summary['original_duration']} weeks\n")
    doc_parts.append(f"- **Optimized Duration**: {opt_summary['optimized_duration']} weeks\n")
    doc_parts.append(f"- **Time Saved**: {opt_summary['time_saved']} weeks\n")
    doc_parts.append(f"- **Target Achievement**: {'✅ YES' if opt_summary['target_achieved'] else '❌ NO'}\n")
    doc_parts.append(f"- **Variance from Target**: {opt_summary['variance_from_target']:+.1f} weeks\n\n")
    
    # Timeline Comparison
    doc_parts.append("### Phase-by-Phase Comparison\n\n")
    doc_parts.append("| Phase | Original Duration | Optimized Duration | Time Saved | Key Optimizations |\n")
    doc_parts.append("|-------|-------------------|-------------------|------------|-------------------|\n")
    
    for i, (orig_phase, opt_phase) in enumerate(zip(original_timeline["phases"], optimized_timeline["phases"])):
        time_saved = (orig_phase["duration_weeks"] + orig_phase["buffer_time"]) - (opt_phase["duration_weeks"] + opt_phase["buffer_time"])
        key_opts = "; ".join(opt_phase["optimizations_applied"][:2])  # Show first 2
        doc_parts.append(f"| {opt_phase['name']} | {orig_phase['duration_weeks'] + orig_phase['buffer_time']:.1f}w | {opt_phase['duration_weeks'] + opt_phase['buffer_time']:.1f}w | {time_saved:.1f}w | {key_opts} |\n")
    doc_parts.append("\n")
    
    # Detailed Optimizations
    doc_parts.append("### Key Optimizations Applied\n\n")
    for optimization in opt_summary["key_optimizations"]:
        doc_parts.append(f"- **{optimization}**\n")
    doc_parts.append("\n")
    
    # Parallel Activities
    doc_parts.append("### Parallel Activities for Time Savings\n\n")
    for parallel in optimized_timeline["parallel_activities"]:
        doc_parts.append(f"**{parallel['activity_set']}** (Weeks {parallel['weeks']})\n")
        doc_parts.append(f"- Activities: {', '.join(parallel['activities'])}\n")
        doc_parts.append(f"- Time Saved: {parallel['time_saved']}\n\n")
    
    # Optimized Integration Points
    doc_parts.append("### Optimized Integration Strategy\n\n")
    for integration in optimized_timeline["integration_points"]:
        if integration["point"] != "Continuous Integration":
            doc_parts.append(f"**{integration['point']}** (Week {integration['week']})\n")
        else:
            doc_parts.append(f"**{integration['point']}**\n")
        doc_parts.append(f"- Purpose: {integration['purpose']}\n")
        doc_parts.append(f"- Optimization: {integration['optimization']}\n\n")
    
    # Trade-offs and Risks
    doc_parts.append("### Trade-offs and Risk Assessment\n\n")
    doc_parts.append("#### Trade-offs\n")
    for trade_off in opt_summary["trade_offs"]:
        doc_parts.append(f"- {trade_off}\n")
    doc_parts.append("\n")
    
    doc_parts.append("#### Risk Mitigation Strategies\n")
    for mitigation in opt_summary["risk_mitigation"]:
        doc_parts.append(f"- {mitigation}\n")
    doc_parts.append("\n")
    
    # Recommendation
    doc_parts.append("### Optimization Recommendation\n\n")
    if opt_summary["target_achieved"]:
        doc_parts.append(f"✅ **RECOMMENDED**: The optimized timeline achieves the 20-week target with {opt_summary['optimized_duration']} weeks total duration. ")
        doc_parts.append("While this requires more intensive project management and accepts some trade-offs in scope depth, it maintains the core research objectives and provides a feasible path to completion within the thesis constraint.\n\n")
    else:
        doc_parts.append(f"⚠️ **REQUIRES FURTHER OPTIMIZATION**: The optimized timeline ({opt_summary['optimized_duration']} weeks) still exceeds the 20-week target by {abs(opt_summary['variance_from_target']):.1f} weeks. ")
        doc_parts.append("Additional scope reductions or methodology simplifications may be necessary.\n\n")
    
    doc_parts.append("#### Implementation Guidelines\n")
    doc_parts.append("1. **Early Planning**: Begin Phase 2 framework design during Phase 1 completion\n")
    doc_parts.append("2. **Intensive Supervision**: Weekly supervisor meetings to maintain quality with accelerated pace\n")
    doc_parts.append("3. **Scope Management**: Clearly defined boundaries for each phase to prevent scope creep\n")
    doc_parts.append("4. **Continuous Integration**: Replace discrete integration phases with ongoing synthesis\n")
    doc_parts.append("5. **Risk Monitoring**: Enhanced monitoring due to reduced buffer time\n\n")
    
    return "".join(doc_parts)

def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.3.3 (Outline Timeline) at {datetime.now().isoformat()}\n")
    
    print("📅 Task 5.3.3: Outlining Project Timeline")
    print("=" * 70)
    
    # Load previous analyses
    methodology_justification, limitations_analysis, resource_assessment = load_previous_analyses()
    
    if not methodology_justification:
        print("Error: Could not load methodology justification data")
        return
    
    # Extract phase structure
    phases = extract_phase_structure(methodology_justification)
    write_log(f"Extracted {len(phases)} phases from methodology justification")
    
    # Develop detailed phase timelines
    detailed_phases = develop_detailed_phase_timelines(phases, limitations_analysis)
    write_log("Developed detailed phase timelines with activities and milestones")
    
    # Create project timeline
    project_timeline = create_project_timeline(detailed_phases, limitations_analysis)
    write_log(f"Created project timeline with {project_timeline['total_duration_weeks']:.1f} week duration")
    
    # Assess timeline feasibility
    feasibility_assessment = assess_timeline_feasibility(project_timeline, limitations_analysis)
    write_log(f"Assessed timeline feasibility: {feasibility_assessment['feasibility_rating']}")
    
    # Create optimized timeline
    optimized_timeline = create_optimized_timeline(detailed_phases, limitations_analysis, target_weeks=20)
    write_log(f"Created optimized timeline with {optimized_timeline['total_duration_weeks']:.1f} week duration")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "5.3.3 - Outline Timeline",
            "timestamp": datetime.now().isoformat(),
            "input_sources": ["5.3.1-methodology-justification.json", "5.3.2-methodology-limitations-analysis.json"]
        },
        "original_timeline": project_timeline,
        "optimized_timeline": optimized_timeline,
        "feasibility_assessment": feasibility_assessment,
        "detailed_phases": detailed_phases
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "5.3.3-project-timeline.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON timeline saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate timeline document with optimization
    timeline_doc = generate_timeline_document(
        project_timeline, feasibility_assessment, detailed_phases
    )
    
    # Add optimization analysis
    optimization_doc = generate_optimization_comparison_document(
        project_timeline, optimized_timeline, feasibility_assessment
    )
    
    complete_doc = timeline_doc + optimization_doc
    
    md_output_path = OUTPUT_DOCS_DIR / "5.3.3-project-timeline.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(complete_doc)
        write_log(f"Timeline document with optimization saved to {md_output_path}")
        print(f"Timeline document with optimization saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving timeline document: {e}")
    
    write_log(f"Finished Task 5.3.3 at {datetime.now().isoformat()}")
    print(f"\n✅ Task 5.3.3 complete with optimization analysis")
    print(f"Original timeline: {project_timeline['total_duration_weeks']:.1f} weeks")
    print(f"Optimized timeline: {optimized_timeline['total_duration_weeks']:.1f} weeks")
    print(f"Target achieved: {'YES' if optimized_timeline['optimization_summary']['target_achieved'] else 'NO'}")

if __name__ == "__main__":
    main() 
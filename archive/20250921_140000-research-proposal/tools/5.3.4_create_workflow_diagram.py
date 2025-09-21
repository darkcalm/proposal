#!/usr/bin/env python3
"""
Task 5.3.4: Create Workflow Diagram

Focus: Visual workflow representations for hybrid methodology approach
Context: Agent Communication Protocol research with optimized timeline

Based on:
- Results from 5.3.1 methodology justification (hybrid approach)
- 5.3.2 limitations and mitigation strategies
- 5.3.3 optimized timeline analysis
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
METHODOLOGY_JUSTIFICATION_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.1-methodology-justification.json"
LIMITATIONS_ANALYSIS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.2-methodology-limitations-analysis.json"
TIMELINE_ANALYSIS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.3-project-timeline.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.3.4_create_workflow_diagram.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analyses ---
def load_previous_analyses():
    methodology_justification = {}
    limitations_analysis = {}
    timeline_analysis = {}
    
    files_to_load = [
        (METHODOLOGY_JUSTIFICATION_INPUT_JSON, "methodology_justification"),
        (LIMITATIONS_ANALYSIS_INPUT_JSON, "limitations_analysis"),
        (TIMELINE_ANALYSIS_INPUT_JSON, "timeline_analysis")
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
                    elif data_name == "timeline_analysis":
                        timeline_analysis = data
                write_log(f"Loaded data from {file_path.name}")
            except Exception as e:
                write_log(f"Error loading {file_path.name}: {e}")
        else:
            write_log(f"Warning: {file_path.name} not found")
    
    return methodology_justification, limitations_analysis, timeline_analysis

# --- Workflow Generation Functions ---
def create_high_level_workflow(methodology_justification, timeline_analysis):
    """Create high-level workflow structure"""
    
    # Extract optimized timeline if available
    optimized_timeline = timeline_analysis.get("optimized_timeline", timeline_analysis.get("original_timeline", {}))
    phases = optimized_timeline.get("phases", [])
    
    workflow = {
        "workflow_type": "High-Level Hybrid Methodology Workflow",
        "phases": [],
        "decision_points": [],
        "integration_gates": [],
        "deliverables": [],
        "feedback_loops": []
    }
    
    # Create phase workflow nodes
    for i, phase in enumerate(phases):
        phase_node = {
            "phase_id": f"P{i+1}",
            "name": phase.get("name", f"Phase {i+1}"),
            "methodology": phase.get("methodology", "Unknown"),
            "duration": f"{phase.get('duration_weeks', 0)} weeks",
            "activities": phase.get("activities", []),
            "milestones": phase.get("milestones", []),
            "inputs": [],
            "outputs": [],
            "decision_points": []
        }
        
        # Define inputs and outputs
        if i == 0:
            phase_node["inputs"] = ["Research objectives", "Literature search strategy", "Initial scope definition"]
        else:
            prev_phase = phases[i-1]["name"]
            phase_node["inputs"] = [f"Outputs from {prev_phase}", "Phase transition validation"]
        
        # Define outputs based on methodology
        if "Literature Review" in phase["methodology"]:
            phase_node["outputs"] = [
                "Comprehensive literature synthesis",
                "Protocol composition patterns",
                "Research gaps identification",
                "Theoretical framework validation"
            ]
        elif "Comparative Research" in phase["methodology"]:
            phase_node["outputs"] = [
                "ACP protocol analysis",
                "A2A protocol analysis", 
                "Comparative evaluation framework",
                "Integration pattern assessment",
                "Protocol composition recommendations"
            ]
        elif "Rapid Prototyping" in phase["methodology"]:
            phase_node["outputs"] = [
                "Protocol integration prototype",
                "Testing and validation results",
                "Implementation documentation",
                "Proof of concept demonstration"
            ]
        
        # Add decision points
        phase_node["decision_points"] = [
            f"Quality gate: {phase['name']} completion criteria met",
            f"Timeline check: {phase['name']} on schedule",
            f"Scope validation: {phase['name']} objectives achieved"
        ]
        
        workflow["phases"].append(phase_node)
    
    # Define major decision points
    workflow["decision_points"] = [
        {
            "decision_id": "D1",
            "name": "Literature Review Scope Decision",
            "location": "End of Phase 1",
            "criteria": ["Sufficient literature coverage", "Clear research gaps identified", "Framework validated"],
            "outcomes": ["Proceed to Phase 2", "Expand literature scope", "Refine research questions"]
        },
        {
            "decision_id": "D2", 
            "name": "Comparative Framework Validation",
            "location": "End of Phase 2",
            "criteria": ["Framework robustness confirmed", "Protocol analysis complete", "Integration patterns clear"],
            "outcomes": ["Proceed to Phase 3", "Refine framework", "Additional protocol analysis"]
        },
        {
            "decision_id": "D3",
            "name": "Prototype Validation Decision",
            "location": "End of Phase 3",
            "criteria": ["Prototype demonstrates key concepts", "Integration feasibility confirmed", "Research objectives met"],
            "outcomes": ["Complete project", "Extend prototype", "Additional validation"]
        }
    ]
    
    # Define integration gates
    integration_points = optimized_timeline.get("integration_points", [])
    for i, integration in enumerate(integration_points):
        if integration.get("point") != "Continuous Integration":
            gate = {
                "gate_id": f"G{i+1}",
                "name": integration.get("point", f"Integration Gate {i+1}"),
                "timing": integration.get("week", "TBD"),
                "purpose": integration.get("purpose", "Phase integration"),
                "activities": integration.get("activities", []),
                "validation_criteria": [
                    "Knowledge transfer completed",
                    "Phase objectives validated", 
                    "Next phase requirements confirmed"
                ]
            }
            workflow["integration_gates"].append(gate)
    
    # Define deliverables
    deliverable_schedule = optimized_timeline.get("deliverable_schedule", [])
    for deliverable in deliverable_schedule:
        workflow["deliverables"].append({
            "deliverable": deliverable.get("deliverable", "Unknown"),
            "week": deliverable.get("week", "TBD"),
            "phase": deliverable.get("phase", "Unknown"),
            "type": "Major Deliverable"
        })
    
    # Define feedback loops
    workflow["feedback_loops"] = [
        {
            "loop_id": "F1",
            "name": "Continuous Quality Feedback",
            "frequency": "Weekly",
            "participants": ["Researcher", "Supervisor"],
            "purpose": "Quality assurance and progress validation"
        },
        {
            "loop_id": "F2",
            "name": "Phase Integration Feedback",
            "frequency": "End of each phase",
            "participants": ["Research team", "Subject matter experts"],
            "purpose": "Phase completion validation and next phase preparation"
        },
        {
            "loop_id": "F3",
            "name": "Risk Management Feedback",
            "frequency": "Bi-weekly",
            "participants": ["Researcher", "Project stakeholders"],
            "purpose": "Risk assessment and mitigation strategy adjustment"
        }
    ]
    
    return workflow

def create_detailed_activity_workflow(methodology_justification, timeline_analysis):
    """Create detailed activity-level workflow"""
    
    optimized_timeline = timeline_analysis.get("optimized_timeline", timeline_analysis.get("original_timeline", {}))
    phases = optimized_timeline.get("phases", [])
    
    detailed_workflow = {
        "workflow_type": "Detailed Activity Workflow",
        "activity_chains": [],
        "parallel_processes": [],
        "critical_path": [],
        "resource_flows": []
    }
    
    # Create activity chains for each phase
    for phase_num, phase in enumerate(phases):
        activities = phase.get("activities", [])
        milestones = phase.get("milestones", [])
        
        activity_chain = {
            "phase": phase.get("name", f"Phase {phase_num + 1}"),
            "chain_id": f"AC{phase_num + 1}",
            "activities": [],
            "dependencies": [],
            "critical_activities": []
        }
        
        # Process activities
        for act_num, activity in enumerate(activities):
            activity_node = {
                "activity_id": f"A{phase_num + 1}.{act_num + 1}",
                "name": activity.get("activity", f"Activity {act_num + 1}"),
                "duration": f"{activity.get('duration_weeks', 0)} weeks",
                "start_week": activity.get("week_start", "TBD"),
                "optimization": activity.get("optimization", "Standard process"),
                "inputs": [],
                "outputs": [],
                "resources": [],
                "quality_criteria": []
            }
            
            # Define activity-specific details
            if "search strategy" in activity["activity"].lower():
                activity_node["inputs"] = ["Research objectives", "Initial literature"]
                activity_node["outputs"] = ["Refined search strategy", "Database selection"]
                activity_node["resources"] = ["Academic databases", "Search tools"]
                activity_node["quality_criteria"] = ["Strategy completeness", "Database coverage"]
                
            elif "database searches" in activity["activity"].lower():
                activity_node["inputs"] = ["Search strategy", "Database access"]
                activity_node["outputs"] = ["Initial paper list", "Screening results"]
                activity_node["resources"] = ["Multiple databases", "Screening tools"]
                activity_node["quality_criteria"] = ["Search comprehensiveness", "Relevance filtering"]
                
            elif "framework design" in activity["activity"].lower():
                activity_node["inputs"] = ["Literature findings", "Research objectives"]
                activity_node["outputs"] = ["Comparison framework", "Evaluation criteria"]
                activity_node["resources"] = ["Analysis tools", "Framework templates"]
                activity_node["quality_criteria"] = ["Framework validity", "Criteria robustness"]
                
            elif "protocol analysis" in activity["activity"].lower():
                activity_node["inputs"] = ["Protocol specifications", "Analysis framework"]
                activity_node["outputs"] = ["Protocol evaluation", "Feature analysis"]
                activity_node["resources"] = ["Protocol documentation", "Analysis tools"]
                activity_node["quality_criteria"] = ["Analysis depth", "Accuracy validation"]
                
            elif "prototype" in activity["activity"].lower():
                activity_node["inputs"] = ["Design specifications", "Protocol insights"]
                activity_node["outputs"] = ["Working prototype", "Integration demonstration"]
                activity_node["resources"] = ["Development tools", "Testing environment"]
                activity_node["quality_criteria"] = ["Functionality validation", "Integration success"]
            
            activity_chain["activities"].append(activity_node)
        
        # Identify critical activities (longest duration or high dependency)
        if activities:
            max_duration = max(act.get("duration_weeks", 0) for act in activities)
            activity_chain["critical_activities"] = [
                act["activity"] for act in activities 
                if act.get("duration_weeks", 0) >= max_duration * 0.8
            ]
        
        detailed_workflow["activity_chains"].append(activity_chain)
    
    # Identify parallel processes from optimizations
    parallel_activities = optimized_timeline.get("parallel_activities", [])
    for parallel in parallel_activities:
        parallel_process = {
            "process_id": f"PP{len(detailed_workflow['parallel_processes']) + 1}",
            "name": parallel.get("activity_set", "Parallel Process"),
            "activities": parallel.get("activities", []),
            "timing": parallel.get("weeks", "TBD"),
            "time_savings": parallel.get("time_saved", "Unknown"),
            "coordination_requirements": [
                "Regular sync meetings",
                "Shared documentation",
                "Progress coordination"
            ]
        }
        detailed_workflow["parallel_processes"].append(parallel_process)
    
    # Define critical path
    critical_path = optimized_timeline.get("critical_path", [])
    for cp_item in critical_path:
        detailed_workflow["critical_path"].append({
            "phase": cp_item.get("phase", "Unknown"),
            "start_week": cp_item.get("start_week", "TBD"),
            "end_week": cp_item.get("end_week", "TBD"),
            "buffer_time": cp_item.get("buffer_end", 0) - cp_item.get("end_week", 0),
            "criticality": "High"
        })
    
    # Define resource flows
    detailed_workflow["resource_flows"] = [
        {
            "resource_type": "Knowledge Assets",
            "flow": "Literature Review → Comparative Framework → Prototype Design",
            "transformation": "Raw literature → Structured analysis → Implementation guidance"
        },
        {
            "resource_type": "Validation Evidence",
            "flow": "Each phase → Integration gates → Final validation",
            "transformation": "Phase-specific validation → Cumulative evidence → Project validation"
        },
        {
            "resource_type": "Technical Artifacts",
            "flow": "Analysis frameworks → Protocol comparisons → Integration prototype",
            "transformation": "Analytical tools → Comparison results → Working demonstration"
        }
    ]
    
    return detailed_workflow

def create_risk_management_workflow(limitations_analysis, timeline_analysis):
    """Create risk management and mitigation workflow"""
    
    risk_workflow = {
        "workflow_type": "Risk Management Workflow",
        "risk_monitoring_process": [],
        "mitigation_workflows": [],
        "escalation_procedures": [],
        "contingency_workflows": []
    }
    
    # Risk monitoring process
    risk_monitoring = limitations_analysis.get("residual_risks", {}).get("risk_monitoring_plan", [])
    for risk in risk_monitoring:
        monitoring_process = {
            "risk_category": risk.get("risk_category", "Unknown"),
            "monitoring_frequency": risk.get("monitoring_frequency", "Unknown"),
            "monitoring_method": risk.get("monitoring_method", "Unknown"),
            "escalation_trigger": risk.get("escalation_trigger", "Unknown"),
            "workflow_steps": [
                "Assess risk indicators",
                "Document current status",
                "Compare against thresholds",
                "Determine escalation need",
                "Implement response actions"
            ]
        }
        risk_workflow["risk_monitoring_process"].append(monitoring_process)
    
    # Mitigation workflows
    mitigation_strategies = limitations_analysis.get("mitigation_strategies", {})
    
    # Phase-specific mitigations
    phase_mitigations = mitigation_strategies.get("phase_specific_mitigations", {})
    for phase, mitigations in phase_mitigations.items():
        for mitigation in mitigations:
            mitigation_workflow = {
                "phase": phase,
                "strategy": mitigation.get("strategy", "Unknown"),
                "implementation": mitigation.get("implementation", "Unknown"),
                "timeline": mitigation.get("timeline", "Unknown"),
                "workflow_steps": [
                    "Identify risk occurrence",
                    "Assess impact and urgency",
                    "Implement mitigation strategy",
                    "Monitor effectiveness",
                    "Adjust as needed"
                ]
            }
            risk_workflow["mitigation_workflows"].append(mitigation_workflow)
    
    # Escalation procedures
    risk_workflow["escalation_procedures"] = [
        {
            "escalation_level": "Level 1 - Routine Issues",
            "triggers": ["Minor schedule delays", "Quality concerns"],
            "response_team": ["Researcher", "Supervisor"],
            "response_time": "Within 24 hours",
            "workflow": [
                "Researcher identifies issue",
                "Consult with supervisor",
                "Implement immediate response",
                "Document resolution"
            ]
        },
        {
            "escalation_level": "Level 2 - Significant Issues",
            "triggers": ["Major timeline impact", "Scope changes"],
            "response_team": ["Researcher", "Supervisor", "Program coordinator"],
            "response_time": "Within 48 hours",
            "workflow": [
                "Formal issue documentation",
                "Stakeholder consultation",
                "Develop response plan",
                "Implement with monitoring",
                "Formal resolution report"
            ]
        },
        {
            "escalation_level": "Level 3 - Critical Issues",
            "triggers": ["Project viability threat", "Fundamental methodology issues"],
            "response_team": ["Full academic committee"],
            "response_time": "Within 72 hours",
            "workflow": [
                "Emergency committee convening",
                "Comprehensive issue assessment",
                "Alternative strategy development",
                "Formal approval process",
                "Implementation with close monitoring"
            ]
        }
    ]
    
    # Contingency workflows
    optimized_timeline = timeline_analysis.get("optimized_timeline", {})
    contingency_plans = optimized_timeline.get("optimization_summary", {}).get("risk_mitigation", [])
    
    for i, contingency in enumerate(contingency_plans):
        contingency_workflow = {
            "contingency_id": f"C{i+1}",
            "mitigation_strategy": contingency,
            "trigger_conditions": ["Risk threshold exceeded", "Mitigation strategy insufficient"],
            "workflow_steps": [
                "Activate contingency protocol",
                "Assess current project state",
                "Implement contingency measures",
                "Adjust project parameters",
                "Communicate changes to stakeholders",
                "Monitor contingency effectiveness"
            ]
        }
        risk_workflow["contingency_workflows"].append(contingency_workflow)
    
    return risk_workflow

def generate_mermaid_diagrams(high_level_workflow, detailed_workflow, risk_workflow):
    """Generate Mermaid diagram syntax for visual representation"""
    
    mermaid_diagrams = {}
    
    # High-level workflow diagram
    mermaid_high_level = []
    mermaid_high_level.append("graph TD")
    
    # Add phase nodes
    for i, phase in enumerate(high_level_workflow["phases"]):
        phase_id = phase["phase_id"]
        phase_name = phase["name"].replace(" ", "_")
        mermaid_high_level.append(f"    {phase_id}[\"{phase['name']}<br/>{phase['methodology']}<br/>{phase['duration']}\"]")
    
    # Add connections between phases
    for i in range(len(high_level_workflow["phases"]) - 1):
        current_phase = high_level_workflow["phases"][i]["phase_id"]
        next_phase = high_level_workflow["phases"][i + 1]["phase_id"]
        mermaid_high_level.append(f"    {current_phase} --> {next_phase}")
    
    # Add decision points
    for decision in high_level_workflow["decision_points"]:
        decision_id = decision["decision_id"]
        decision_name = decision["name"].replace(" ", "_")
        mermaid_high_level.append(f"    {decision_id}{{{decision['name']}}}")
    
    # Add integration gates
    for gate in high_level_workflow["integration_gates"]:
        gate_id = gate["gate_id"]
        mermaid_high_level.append(f"    {gate_id}[(\"{gate['name']}\")]")
    
    # Add deliverables
    for i, deliverable in enumerate(high_level_workflow["deliverables"]):
        deliv_id = f"DEL{i+1}"
        mermaid_high_level.append(f"    {deliv_id}[[\"{deliverable['deliverable']}\"]")
    
    mermaid_diagrams["high_level_workflow"] = "\n".join(mermaid_high_level)
    
    # Detailed activity workflow diagram  
    mermaid_detailed = []
    mermaid_detailed.append("graph LR")
    
    for chain in detailed_workflow["activity_chains"]:
        chain_id = chain["chain_id"]
        mermaid_detailed.append(f"    subgraph {chain_id} [\"{chain['phase']}\"]")
        
        for i, activity in enumerate(chain["activities"]):
            activity_id = activity["activity_id"]
            activity_name = activity["name"].replace(" ", "_")[:20]  # Truncate for readability
            mermaid_detailed.append(f"        {activity_id}[\"{activity_name}<br/>{activity['duration']}\"]")
            
            if i > 0:
                prev_activity = chain["activities"][i-1]["activity_id"]
                mermaid_detailed.append(f"        {prev_activity} --> {activity_id}")
        
        mermaid_detailed.append("    end")
    
    mermaid_diagrams["detailed_workflow"] = "\n".join(mermaid_detailed)
    
    # Risk management workflow diagram
    mermaid_risk = []
    mermaid_risk.append("graph TD")
    mermaid_risk.append("    START([Project Start]) --> MONITOR[Risk Monitoring]")
    mermaid_risk.append("    MONITOR --> ASSESS{Risk Assessment}")
    mermaid_risk.append("    ASSESS -->|Low Risk| CONTINUE[Continue Normal Process]")
    mermaid_risk.append("    ASSESS -->|Medium Risk| MITIGATE[Implement Mitigation]")
    mermaid_risk.append("    ASSESS -->|High Risk| ESCALATE[Escalate to Committee]")
    mermaid_risk.append("    MITIGATE --> MONITOR")
    mermaid_risk.append("    ESCALATE --> CONTINGENCY[Activate Contingency]")
    mermaid_risk.append("    CONTINGENCY --> MONITOR")
    mermaid_risk.append("    CONTINUE --> MONITOR")
    
    mermaid_diagrams["risk_management"] = "\n".join(mermaid_risk)
    
    return mermaid_diagrams

def generate_workflow_document(high_level_workflow, detailed_workflow, risk_workflow, mermaid_diagrams):
    """Generate comprehensive workflow documentation"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Research Methodology Workflow Diagrams (Task 5.3.4)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Based on: Hybrid methodology approach with optimized timeline and risk management*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    doc_parts.append("This document provides comprehensive workflow diagrams for the hybrid methodology approach, including high-level process flows, detailed activity workflows, and risk management procedures. The workflows are designed to support the optimized 18.95-week timeline while maintaining research quality and managing identified risks.\n\n")
    
    # High-Level Workflow
    doc_parts.append("## High-Level Methodology Workflow\n\n")
    doc_parts.append("### Process Overview\n\n")
    
    for i, phase in enumerate(high_level_workflow["phases"]):
        doc_parts.append(f"#### {phase['name']}\n")
        doc_parts.append(f"- **Methodology**: {phase['methodology']}\n")
        doc_parts.append(f"- **Duration**: {phase['duration']}\n")
        
        if phase["inputs"]:
            doc_parts.append("- **Key Inputs**: " + ", ".join(phase["inputs"]) + "\n")
        if phase["outputs"]:
            doc_parts.append("- **Key Outputs**: " + ", ".join(phase["outputs"]) + "\n")
        
        doc_parts.append("\n")
    
    # Decision Points
    doc_parts.append("### Critical Decision Points\n\n")
    for decision in high_level_workflow["decision_points"]:
        doc_parts.append(f"#### {decision['name']}\n")
        doc_parts.append(f"- **Location**: {decision['location']}\n")
        doc_parts.append(f"- **Criteria**: {', '.join(decision['criteria'])}\n")
        doc_parts.append(f"- **Possible Outcomes**: {', '.join(decision['outcomes'])}\n\n")
    
    # Integration Gates
    doc_parts.append("### Integration Gates\n\n")
    for gate in high_level_workflow["integration_gates"]:
        doc_parts.append(f"#### {gate['name']}\n")
        doc_parts.append(f"- **Timing**: Week {gate['timing']}\n")
        doc_parts.append(f"- **Purpose**: {gate['purpose']}\n")
        doc_parts.append(f"- **Activities**: {', '.join(gate['activities'])}\n\n")
    
    # High-Level Workflow Diagram
    doc_parts.append("### Visual Workflow (Mermaid Syntax)\n\n")
    doc_parts.append("```mermaid\n")
    doc_parts.append(mermaid_diagrams["high_level_workflow"])
    doc_parts.append("\n```\n\n")
    
    # Detailed Activity Workflow
    doc_parts.append("## Detailed Activity Workflow\n\n")
    
    for chain in detailed_workflow["activity_chains"]:
        doc_parts.append(f"### {chain['phase']}\n\n")
        
        doc_parts.append("| Activity | Duration | Optimization | Inputs | Outputs |\n")
        doc_parts.append("|----------|----------|--------------|--------|---------|\n")
        
        for activity in chain["activities"]:
            inputs_str = ", ".join(activity["inputs"][:2]) if activity["inputs"] else "Standard"
            outputs_str = ", ".join(activity["outputs"][:2]) if activity["outputs"] else "Standard"
            doc_parts.append(f"| {activity['name']} | {activity['duration']} | {activity['optimization']} | {inputs_str} | {outputs_str} |\n")
        
        doc_parts.append("\n")
        
        if chain["critical_activities"]:
            doc_parts.append(f"**Critical Activities**: {', '.join(chain['critical_activities'])}\n\n")
    
    # Parallel Processes
    if detailed_workflow["parallel_processes"]:
        doc_parts.append("### Parallel Processes\n\n")
        for parallel in detailed_workflow["parallel_processes"]:
            doc_parts.append(f"#### {parallel['name']}\n")
            doc_parts.append(f"- **Timing**: Weeks {parallel['timing']}\n")
            doc_parts.append(f"- **Activities**: {', '.join(parallel['activities'])}\n")
            doc_parts.append(f"- **Time Savings**: {parallel['time_savings']}\n")
            doc_parts.append(f"- **Coordination**: {', '.join(parallel['coordination_requirements'])}\n\n")
    
    # Detailed Workflow Diagram
    doc_parts.append("### Detailed Activity Flow (Mermaid Syntax)\n\n")
    doc_parts.append("```mermaid\n")
    doc_parts.append(mermaid_diagrams["detailed_workflow"])
    doc_parts.append("\n```\n\n")
    
    # Risk Management Workflow
    doc_parts.append("## Risk Management Workflow\n\n")
    
    # Risk Monitoring Process
    doc_parts.append("### Risk Monitoring Process\n\n")
    doc_parts.append("| Risk Category | Frequency | Method | Escalation Trigger |\n")
    doc_parts.append("|---------------|-----------|--------|-------------------|\n")
    
    for risk in risk_workflow["risk_monitoring_process"]:
        doc_parts.append(f"| {risk['risk_category']} | {risk['monitoring_frequency']} | {risk['monitoring_method']} | {risk['escalation_trigger']} |\n")
    
    doc_parts.append("\n")
    
    # Escalation Procedures
    doc_parts.append("### Escalation Procedures\n\n")
    for escalation in risk_workflow["escalation_procedures"]:
        doc_parts.append(f"#### {escalation['escalation_level']}\n")
        doc_parts.append(f"- **Triggers**: {', '.join(escalation['triggers'])}\n")
        doc_parts.append(f"- **Response Team**: {', '.join(escalation['response_team'])}\n")
        doc_parts.append(f"- **Response Time**: {escalation['response_time']}\n")
        doc_parts.append("- **Workflow Steps**:\n")
        for step in escalation['workflow']:
            doc_parts.append(f"  1. {step}\n")
        doc_parts.append("\n")
    
    # Risk Management Diagram
    doc_parts.append("### Risk Management Flow (Mermaid Syntax)\n\n")
    doc_parts.append("```mermaid\n")
    doc_parts.append(mermaid_diagrams["risk_management"])
    doc_parts.append("\n```\n\n")
    
    # Implementation Guidelines
    doc_parts.append("## Implementation Guidelines\n\n")
    doc_parts.append("### Workflow Execution Principles\n\n")
    doc_parts.append("1. **Sequential Phase Execution**: Complete each phase before proceeding to the next\n")
    doc_parts.append("2. **Gate-Based Validation**: Validate completion criteria at each integration gate\n")
    doc_parts.append("3. **Continuous Risk Monitoring**: Implement ongoing risk assessment throughout\n")
    doc_parts.append("4. **Parallel Activity Coordination**: Manage parallel processes with regular synchronization\n")
    doc_parts.append("5. **Quality Assurance Integration**: Embed quality checks within each workflow step\n\n")
    
    doc_parts.append("### Success Factors\n\n")
    doc_parts.append("- **Clear Role Definition**: Each workflow step has defined responsibilities\n")
    doc_parts.append("- **Regular Communication**: Weekly supervisor meetings and phase reviews\n")
    doc_parts.append("- **Documentation Standards**: Consistent documentation throughout all phases\n")
    doc_parts.append("- **Adaptive Management**: Flexibility to adjust workflows based on emerging needs\n")
    doc_parts.append("- **Stakeholder Engagement**: Regular communication with all project stakeholders\n\n")
    
    # Conclusion
    doc_parts.append("## Conclusion\n\n")
    doc_parts.append("The workflow diagrams provide a comprehensive roadmap for executing the hybrid methodology approach within the optimized timeline. The integration of high-level process flows, detailed activity management, and systematic risk management ensures both research quality and project deliverability. These workflows serve as living documents that should be adapted as the project progresses and new insights emerge.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.3.4 (Create Workflow Diagram) at {datetime.now().isoformat()}\n")
    
    print("🔄 Task 5.3.4: Creating Workflow Diagrams")
    print("=" * 70)
    
    # Load previous analyses
    methodology_justification, limitations_analysis, timeline_analysis = load_previous_analyses()
    
    if not methodology_justification:
        print("Error: Could not load methodology justification data")
        return
    
    # Create high-level workflow
    high_level_workflow = create_high_level_workflow(methodology_justification, timeline_analysis)
    write_log(f"Created high-level workflow with {len(high_level_workflow['phases'])} phases")
    
    # Create detailed activity workflow
    detailed_workflow = create_detailed_activity_workflow(methodology_justification, timeline_analysis)
    write_log(f"Created detailed workflow with {len(detailed_workflow['activity_chains'])} activity chains")
    
    # Create risk management workflow
    risk_workflow = create_risk_management_workflow(limitations_analysis, timeline_analysis)
    write_log(f"Created risk management workflow with {len(risk_workflow['escalation_procedures'])} escalation levels")
    
    # Generate Mermaid diagrams
    mermaid_diagrams = generate_mermaid_diagrams(high_level_workflow, detailed_workflow, risk_workflow)
    write_log(f"Generated {len(mermaid_diagrams)} Mermaid diagrams")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "5.3.4 - Create Workflow Diagram",
            "timestamp": datetime.now().isoformat(),
            "input_sources": ["5.3.1-methodology-justification.json", "5.3.2-methodology-limitations-analysis.json", "5.3.3-project-timeline.json"]
        },
        "high_level_workflow": high_level_workflow,
        "detailed_workflow": detailed_workflow,
        "risk_workflow": risk_workflow,
        "mermaid_diagrams": mermaid_diagrams
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "5.3.4-workflow-diagrams.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON workflow analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save workflow document
    workflow_doc = generate_workflow_document(
        high_level_workflow, detailed_workflow, risk_workflow, mermaid_diagrams
    )
    
    md_output_path = OUTPUT_DOCS_DIR / "5.3.4-workflow-diagrams.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(workflow_doc)
        write_log(f"Workflow diagrams document saved to {md_output_path}")
        print(f"Workflow diagrams document saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving workflow document: {e}")
    
    write_log(f"Finished Task 5.3.4 at {datetime.now().isoformat()}")
    print(f"\n✅ Task 5.3.4 complete with comprehensive workflow diagrams")
    print(f"Generated workflows: High-level, Detailed activities, Risk management")
    print(f"Visual diagrams: {len(mermaid_diagrams)} Mermaid syntax diagrams")

if __name__ == "__main__":
    main() 
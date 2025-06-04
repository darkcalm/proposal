#!/usr/bin/env python3
"""
Task 5.3.2: Address Limitations

Focus: Systematic identification and mitigation of limitations in selected methodology
Context: Hybrid methodology approach for Agent Communication Protocol research

Based on:
- Results from 5.3.1 methodology justification
- 5.2.2 methodology strengths and limitations analysis
- 5.2.3 resource requirements assessment
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
METHODOLOGY_JUSTIFICATION_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.3.1-methodology-justification.json"
STRENGTHS_LIMITATIONS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.2-methodology-strengths-limitations.json"
RESOURCE_ASSESSMENT_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "5.2.3-resource-requirements-assessment.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "5.3.2_address_limitations.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analyses ---
def load_previous_analyses():
    methodology_justification = {}
    strengths_limitations = {}
    resource_assessment = {}
    
    files_to_load = [
        (METHODOLOGY_JUSTIFICATION_INPUT_JSON, "methodology_justification"),
        (STRENGTHS_LIMITATIONS_INPUT_JSON, "strengths_limitations"),
        (RESOURCE_ASSESSMENT_INPUT_JSON, "resource_assessment")
    ]
    
    for file_path, data_name in files_to_load:
        if file_path.exists():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if data_name == "methodology_justification":
                        methodology_justification = data
                    elif data_name == "strengths_limitations":
                        strengths_limitations = data
                    elif data_name == "resource_assessment":
                        resource_assessment = data
                write_log(f"Loaded data from {file_path.name}")
            except Exception as e:
                write_log(f"Error loading {file_path.name}: {e}")
        else:
            write_log(f"Warning: {file_path.name} not found")
    
    return methodology_justification, strengths_limitations, resource_assessment

# --- Limitation Analysis Functions ---
def identify_methodology_specific_limitations(methodology_justification, strengths_limitations):
    """Identify limitations specific to each methodology in the hybrid approach"""
    
    hybrid_phases = methodology_justification.get("methodology_justification", {}).get("hybrid_methodology_consideration", {}).get("phases", [])
    methodology_analyses = strengths_limitations.get("methodology_analyses", {})
    
    phase_limitations = {}
    
    for phase in hybrid_phases:
        phase_name = phase.get("phase", "Unknown Phase")
        methodology_name = phase.get("methodology", "Unknown Methodology")
        
        # Map methodology names to keys
        methodology_key_mapping = {
            "Systematic Literature Review Methodology": "systematic_literature_review",
            "Comparative Research Methodology": "comparative_research", 
            "Rapid Prototyping": "rapid_prototyping"
        }
        
        methodology_key = methodology_key_mapping.get(methodology_name, methodology_name.lower().replace(" ", "_"))
        methodology_analysis = methodology_analyses.get(methodology_key, {})
        
        limitations = methodology_analysis.get("limitations", {})
        risks = methodology_analysis.get("risks", {})
        
        phase_limitations[phase_name] = {
            "methodology": methodology_name,
            "duration": phase.get("duration", "Unknown"),
            "focus": phase.get("focus", "Unknown"),
            "generic_limitations": limitations.get("generic_limitations", []),
            "contextual_limitations": limitations.get("contextual_limitations", []),
            "implementation_limitations": limitations.get("implementation_limitations", []),
            "timeline_risks": risks.get("timeline_risks", []),
            "technical_risks": risks.get("technical_risks", []),
            "mitigations": risks.get("mitigations", [])
        }
    
    return phase_limitations

def identify_hybrid_approach_limitations(methodology_justification):
    """Identify limitations specific to the hybrid approach itself"""
    
    hybrid_limitations = {
        "coordination_complexity": {
            "limitation": "Increased complexity in coordinating multiple methodologies",
            "impact": "May lead to inconsistent application and integration challenges",
            "severity": "Medium"
        },
        "phase_transition_risks": {
            "limitation": "Risk of inadequate knowledge transfer between phases",
            "impact": "Findings from earlier phases may not effectively inform later phases",
            "severity": "Medium"
        },
        "scope_management_challenges": {
            "limitation": "Difficulty maintaining consistent scope across different methodological approaches",
            "impact": "Potential for scope creep or inconsistent depth of analysis",
            "severity": "Medium"
        },
        "resource_distribution": {
            "limitation": "Uneven resource allocation across phases may compromise quality",
            "impact": "Some phases may receive insufficient attention or resources",
            "severity": "Medium"
        },
        "integration_complexity": {
            "limitation": "Challenge in synthesizing findings from different methodological paradigms",
            "impact": "Difficulty in creating coherent conclusions from diverse evidence types",
            "severity": "High"
        },
        "validation_consistency": {
            "limitation": "Different validation approaches across phases may create inconsistencies",
            "impact": "Challenges in maintaining uniform quality standards",
            "severity": "Medium"
        }
    }
    
    return hybrid_limitations

def assess_contextual_limitations(methodology_justification):
    """Assess limitations specific to the research context"""
    
    contextual_limitations = {
        "protocol_evolution_speed": {
            "limitation": "Rapid evolution of agent communication protocols",
            "impact": "Literature may become outdated during research timeline",
            "context": "ACP/A2A protocols are emerging and rapidly evolving",
            "severity": "High"
        },
        "limited_real_world_data": {
            "limitation": "Limited availability of real-world DER implementation data",
            "impact": "Comparative analysis may rely on theoretical frameworks rather than empirical evidence",
            "context": "DER predictive maintenance protocols are still emerging",
            "severity": "High"
        },
        "industry_access_constraints": {
            "limitation": "Limited access to industry implementations and stakeholders",
            "impact": "Prototyping phase may lack realistic validation opportunities",
            "context": "Individual academic project with limited industry connections",
            "severity": "Medium"
        },
        "technical_expertise_requirements": {
            "limitation": "High technical expertise required across multiple protocol domains",
            "impact": "Risk of superficial analysis in complex technical areas",
            "context": "Single researcher addressing multiple complex protocols",
            "severity": "Medium"
        },
        "regulatory_landscape_uncertainty": {
            "limitation": "Unclear regulatory requirements for agent protocols in energy sector",
            "impact": "Difficulty in assessing practical implementation feasibility",
            "context": "Emerging regulatory landscape for AI agents in critical infrastructure",
            "severity": "Medium"
        }
    }
    
    return contextual_limitations

def develop_limitation_mitigation_strategies(phase_limitations, hybrid_limitations, contextual_limitations):
    """Develop specific mitigation strategies for identified limitations"""
    
    mitigation_strategies = {
        "phase_specific_mitigations": {},
        "hybrid_approach_mitigations": {},
        "contextual_mitigations": {},
        "overarching_strategies": []
    }
    
    # Phase-specific mitigations
    for phase_name, limitations in phase_limitations.items():
        mitigations = []
        
        # Address generic limitations
        if limitations.get("generic_limitations"):
            mitigations.append({
                "strategy": "Leverage established best practices",
                "implementation": f"Follow established {limitations['methodology']} guidelines and standards",
                "timeline": "Throughout phase"
            })
        
        # Address timeline risks
        if limitations.get("timeline_risks"):
            mitigations.append({
                "strategy": "Proactive timeline management",
                "implementation": "Build buffer time and establish clear milestones with weekly progress reviews",
                "timeline": "Phase planning and execution"
            })
        
        # Address technical risks
        if limitations.get("technical_risks"):
            mitigations.append({
                "strategy": "Expert consultation and validation",
                "implementation": "Regular supervisor feedback and peer review of technical aspects",
                "timeline": "Ongoing throughout phase"
            })
        
        mitigation_strategies["phase_specific_mitigations"][phase_name] = mitigations
    
    # Hybrid approach mitigations
    for limitation_key, limitation_data in hybrid_limitations.items():
        strategy = ""
        implementation = ""
        
        if limitation_key == "coordination_complexity":
            strategy = "Structured integration framework"
            implementation = "Develop clear handoff procedures and integration checkpoints between phases"
        elif limitation_key == "phase_transition_risks":
            strategy = "Knowledge transfer protocols"
            implementation = "Create detailed phase summary documents and transition meetings"
        elif limitation_key == "integration_complexity":
            strategy = "Systematic synthesis approach"
            implementation = "Use structured frameworks for integrating different types of evidence"
        else:
            strategy = "Systematic management approach"
            implementation = "Develop specific procedures for this limitation"
        
        mitigation_strategies["hybrid_approach_mitigations"][limitation_key] = {
            "strategy": strategy,
            "implementation": implementation,
            "priority": limitation_data["severity"]
        }
    
    # Contextual mitigations
    for limitation_key, limitation_data in contextual_limitations.items():
        strategy = ""
        implementation = ""
        
        if limitation_key == "protocol_evolution_speed":
            strategy = "Continuous monitoring and adaptation"
            implementation = "Establish protocol monitoring system and plan for iterative updates"
        elif limitation_key == "limited_real_world_data":
            strategy = "Multi-source validation approach"
            implementation = "Combine theoretical analysis with simulation and expert validation"
        elif limitation_key == "industry_access_constraints":
            strategy = "Alternative validation methods"
            implementation = "Use publicly available case studies and expert interviews"
        else:
            strategy = "Proactive risk management"
            implementation = "Develop specific mitigation for this contextual factor"
        
        mitigation_strategies["contextual_mitigations"][limitation_key] = {
            "strategy": strategy,
            "implementation": implementation,
            "priority": limitation_data["severity"]
        }
    
    # Overarching strategies
    mitigation_strategies["overarching_strategies"] = [
        {
            "strategy": "Quality assurance framework",
            "implementation": "Establish regular review cycles with supervisor and implement peer review processes",
            "scope": "All phases"
        },
        {
            "strategy": "Adaptive project management",
            "implementation": "Use agile principles to adapt to emerging challenges and opportunities",
            "scope": "Project-wide"
        },
        {
            "strategy": "Documentation and transparency",
            "implementation": "Maintain detailed documentation of decisions, limitations, and adaptations",
            "scope": "All phases"
        },
        {
            "strategy": "Stakeholder engagement",
            "implementation": "Regular communication with supervisor and subject matter experts",
            "scope": "Project-wide"
        }
    ]
    
    return mitigation_strategies

def assess_residual_risks(phase_limitations, hybrid_limitations, contextual_limitations, mitigation_strategies):
    """Assess risks that remain after mitigation strategies"""
    
    residual_risks = {
        "high_priority_residual_risks": [],
        "medium_priority_residual_risks": [],
        "acceptable_residual_risks": [],
        "risk_monitoring_plan": []
    }
    
    # Assess residual risks from contextual limitations
    high_risk_contexts = [
        {
            "risk": "Rapid protocol evolution outpacing research timeline",
            "likelihood": "Medium",
            "impact": "High", 
            "mitigation_effectiveness": "Moderate",
            "residual_impact": "Protocol findings may require updates near project completion"
        },
        {
            "risk": "Limited real-world validation opportunities",
            "likelihood": "High",
            "impact": "Medium",
            "mitigation_effectiveness": "Moderate",
            "residual_impact": "Conclusions may have limited practical validation"
        }
    ]
    
    medium_risk_contexts = [
        {
            "risk": "Integration complexity across methodological paradigms",
            "likelihood": "Medium",
            "impact": "Medium",
            "mitigation_effectiveness": "Good",
            "residual_impact": "Some integration challenges may persist despite structured approach"
        },
        {
            "risk": "Technical depth limitations due to breadth requirements",
            "likelihood": "Medium",
            "impact": "Medium",
            "mitigation_effectiveness": "Moderate",
            "residual_impact": "Some technical areas may receive less detailed analysis"
        }
    ]
    
    acceptable_risks = [
        {
            "risk": "Phase coordination overhead",
            "likelihood": "Low",
            "impact": "Low",
            "mitigation_effectiveness": "Good",
            "residual_impact": "Minor efficiency impacts with good management"
        }
    ]
    
    residual_risks["high_priority_residual_risks"] = high_risk_contexts
    residual_risks["medium_priority_residual_risks"] = medium_risk_contexts
    residual_risks["acceptable_residual_risks"] = acceptable_risks
    
    # Risk monitoring plan
    residual_risks["risk_monitoring_plan"] = [
        {
            "risk_category": "Protocol Evolution",
            "monitoring_frequency": "Bi-weekly",
            "monitoring_method": "Literature alerts and protocol specification monitoring",
            "escalation_trigger": "Major protocol updates affecting research scope"
        },
        {
            "risk_category": "Integration Quality", 
            "monitoring_frequency": "End of each phase",
            "monitoring_method": "Integration review and supervisor feedback",
            "escalation_trigger": "Difficulty synthesizing findings across phases"
        },
        {
            "risk_category": "Timeline Adherence",
            "monitoring_frequency": "Weekly",
            "monitoring_method": "Progress tracking against milestones",
            "escalation_trigger": "Two consecutive weeks behind schedule"
        }
    ]
    
    return residual_risks

def generate_limitations_document(phase_limitations, hybrid_limitations, contextual_limitations, mitigation_strategies, residual_risks):
    """Generate comprehensive limitations and mitigation document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Methodology Limitations and Mitigation Strategies (Task 5.3.2)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Based on: Selected hybrid methodology approach and comprehensive risk analysis*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    doc_parts.append("This document systematically identifies and addresses the limitations of the selected hybrid methodology approach, providing specific mitigation strategies and residual risk management plans. The analysis covers phase-specific limitations, hybrid approach challenges, and contextual constraints.\n\n")
    
    # Phase-Specific Limitations
    doc_parts.append("## Phase-Specific Limitations\n\n")
    for phase_name, limitations in phase_limitations.items():
        doc_parts.append(f"### {phase_name}\n")
        doc_parts.append(f"**Methodology**: {limitations['methodology']}\n")
        doc_parts.append(f"**Duration**: {limitations['duration']}\n")
        doc_parts.append(f"**Focus**: {limitations['focus']}\n\n")
        
        if limitations['generic_limitations']:
            doc_parts.append("**Generic Limitations:**\n")
            for limitation in limitations['generic_limitations']:
                doc_parts.append(f"- {limitation}\n")
            doc_parts.append("\n")
        
        if limitations['contextual_limitations']:
            doc_parts.append("**Contextual Limitations:**\n")
            for limitation in limitations['contextual_limitations']:
                doc_parts.append(f"- {limitation}\n")
            doc_parts.append("\n")
        
        if limitations['implementation_limitations']:
            doc_parts.append("**Implementation Limitations:**\n")
            for limitation in limitations['implementation_limitations']:
                doc_parts.append(f"- {limitation}\n")
            doc_parts.append("\n")
        
        # Include mitigations for this phase
        phase_mitigations = mitigation_strategies["phase_specific_mitigations"].get(phase_name, [])
        if phase_mitigations:
            doc_parts.append("**Mitigation Strategies:**\n")
            for mitigation in phase_mitigations:
                doc_parts.append(f"- **{mitigation['strategy']}**: {mitigation['implementation']}\n")
            doc_parts.append("\n")
        
        doc_parts.append("---\n")
    
    # Hybrid Approach Limitations
    doc_parts.append("## Hybrid Approach Limitations\n\n")
    for limitation_key, limitation_data in hybrid_limitations.items():
        doc_parts.append(f"### {limitation_key.replace('_', ' ').title()}\n")
        doc_parts.append(f"**Limitation**: {limitation_data['limitation']}\n")
        doc_parts.append(f"**Impact**: {limitation_data['impact']}\n")
        doc_parts.append(f"**Severity**: {limitation_data['severity']}\n")
        
        # Include mitigation
        mitigation = mitigation_strategies["hybrid_approach_mitigations"].get(limitation_key, {})
        if mitigation:
            doc_parts.append(f"**Mitigation**: {mitigation['strategy']} - {mitigation['implementation']}\n")
        doc_parts.append("\n")
    
    # Contextual Limitations
    doc_parts.append("## Contextual Limitations\n\n")
    for limitation_key, limitation_data in contextual_limitations.items():
        doc_parts.append(f"### {limitation_key.replace('_', ' ').title()}\n")
        doc_parts.append(f"**Limitation**: {limitation_data['limitation']}\n")
        doc_parts.append(f"**Impact**: {limitation_data['impact']}\n")
        doc_parts.append(f"**Context**: {limitation_data['context']}\n")
        doc_parts.append(f"**Severity**: {limitation_data['severity']}\n")
        
        # Include mitigation
        mitigation = mitigation_strategies["contextual_mitigations"].get(limitation_key, {})
        if mitigation:
            doc_parts.append(f"**Mitigation**: {mitigation['strategy']} - {mitigation['implementation']}\n")
        doc_parts.append("\n")
    
    # Overarching Mitigation Strategies
    doc_parts.append("## Overarching Mitigation Strategies\n\n")
    for strategy in mitigation_strategies["overarching_strategies"]:
        doc_parts.append(f"### {strategy['strategy']}\n")
        doc_parts.append(f"- **Implementation**: {strategy['implementation']}\n")
        doc_parts.append(f"- **Scope**: {strategy['scope']}\n\n")
    
    # Residual Risk Assessment
    doc_parts.append("## Residual Risk Assessment\n\n")
    
    if residual_risks["high_priority_residual_risks"]:
        doc_parts.append("### High Priority Residual Risks\n")
        for risk in residual_risks["high_priority_residual_risks"]:
            doc_parts.append(f"- **Risk**: {risk['risk']}\n")
            doc_parts.append(f"  - Likelihood: {risk['likelihood']}, Impact: {risk['impact']}\n")
            doc_parts.append(f"  - Residual Impact: {risk['residual_impact']}\n\n")
    
    if residual_risks["medium_priority_residual_risks"]:
        doc_parts.append("### Medium Priority Residual Risks\n")
        for risk in residual_risks["medium_priority_residual_risks"]:
            doc_parts.append(f"- **Risk**: {risk['risk']}\n")
            doc_parts.append(f"  - Likelihood: {risk['likelihood']}, Impact: {risk['impact']}\n")
            doc_parts.append(f"  - Residual Impact: {risk['residual_impact']}\n\n")
    
    # Risk Monitoring Plan
    doc_parts.append("### Risk Monitoring Plan\n\n")
    doc_parts.append("| Risk Category | Frequency | Method | Escalation Trigger |\n")
    doc_parts.append("|---------------|-----------|--------|-------------------|\n")
    for monitor in residual_risks["risk_monitoring_plan"]:
        doc_parts.append(f"| {monitor['risk_category']} | {monitor['monitoring_frequency']} | {monitor['monitoring_method']} | {monitor['escalation_trigger']} |\n")
    doc_parts.append("\n")
    
    # Conclusion
    doc_parts.append("## Conclusion\n\n")
    doc_parts.append("While the selected hybrid methodology approach has inherent limitations, the systematic identification and mitigation strategies outlined above provide a robust framework for managing these challenges. The residual risks are manageable with appropriate monitoring and adaptive project management. This comprehensive approach to limitation management enhances the overall reliability and validity of the research outcomes.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 5.3.2 (Address Limitations) at {datetime.now().isoformat()}\n")
    
    print("⚠️  Task 5.3.2: Addressing Methodology Limitations")
    print("=" * 70)
    
    # Load previous analyses
    methodology_justification, strengths_limitations, resource_assessment = load_previous_analyses()
    
    if not methodology_justification:
        print("Error: Could not load methodology justification data")
        return
    
    # Identify limitations
    phase_limitations = identify_methodology_specific_limitations(methodology_justification, strengths_limitations)
    write_log(f"Identified limitations for {len(phase_limitations)} phases")
    
    hybrid_limitations = identify_hybrid_approach_limitations(methodology_justification)
    write_log(f"Identified {len(hybrid_limitations)} hybrid approach limitations")
    
    contextual_limitations = assess_contextual_limitations(methodology_justification)
    write_log(f"Identified {len(contextual_limitations)} contextual limitations")
    
    # Develop mitigation strategies
    mitigation_strategies = develop_limitation_mitigation_strategies(
        phase_limitations, hybrid_limitations, contextual_limitations
    )
    write_log("Developed comprehensive mitigation strategies")
    
    # Assess residual risks
    residual_risks = assess_residual_risks(
        phase_limitations, hybrid_limitations, contextual_limitations, mitigation_strategies
    )
    write_log("Completed residual risk assessment")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "5.3.2 - Address Limitations",
            "timestamp": datetime.now().isoformat(),
            "input_sources": ["5.3.1-methodology-justification.json", "5.2.2-methodology-strengths-limitations.json"]
        },
        "phase_limitations": phase_limitations,
        "hybrid_limitations": hybrid_limitations,
        "contextual_limitations": contextual_limitations,
        "mitigation_strategies": mitigation_strategies,
        "residual_risks": residual_risks
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "5.3.2-methodology-limitations-analysis.json"
    try:
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save limitations document
    limitations_doc = generate_limitations_document(
        phase_limitations, hybrid_limitations, contextual_limitations, 
        mitigation_strategies, residual_risks
    )
    md_output_path = OUTPUT_DOCS_DIR / "5.3.2-methodology-limitations.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(limitations_doc)
        write_log(f"Limitations document saved to {md_output_path}")
        print(f"Limitations analysis saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving limitations document: {e}")
    
    write_log(f"Finished Task 5.3.2 at {datetime.now().isoformat()}")
    print("\n✅ Task 5.3.2 complete.")

if __name__ == "__main__":
    main() 
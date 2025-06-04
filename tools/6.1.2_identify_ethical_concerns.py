#!/usr/bin/env python3
"""
Task 6.1.2: Identify Ethical Concerns

Focus: Systematic identification of specific ethical concerns in ACP/A2A research
Context: Building on ethics guidelines review to identify concrete ethical issues

Based on:
- Results from 6.1.1 ethics guidelines review
- Research focus on Agent Communication Protocols for DER predictive maintenance
- Specific research methodology and activities identified in earlier tasks
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
ETHICS_GUIDELINES_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "6.1.1-ethics-guidelines-review.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "6.1.2_identify_ethical_concerns.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analysis ---
def load_ethics_guidelines_review():
    if not ETHICS_GUIDELINES_INPUT_JSON.exists():
        write_log(f"Error: Ethics guidelines review file not found at {ETHICS_GUIDELINES_INPUT_JSON}")
        return {}
    try:
        with open(ETHICS_GUIDELINES_INPUT_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        write_log(f"Error loading ethics guidelines review: {e}")
        return {}

# --- Ethical Concern Identification Functions ---
def identify_research_phase_specific_concerns(ethics_review):
    """Identify ethical concerns specific to each research phase"""
    
    phase_concerns = {
        "literature_review_phase": {
            "phase_name": "Systematic Literature Review Phase",
            "duration": "6 weeks",
            "activities": [
                "Database searches and screening",
                "Full-text review and data extraction", 
                "Protocol composition pattern analysis",
                "Literature synthesis and gap identification"
            ],
            "ethical_concerns": []
        },
        "comparative_analysis_phase": {
            "phase_name": "Comparative Framework Development Phase",
            "duration": "8 weeks", 
            "activities": [
                "Framework design and validation",
                "ACP protocol analysis",
                "A2A protocol analysis",
                "Comparative evaluation",
                "Integration pattern assessment"
            ],
            "ethical_concerns": []
        },
        "prototype_development_phase": {
            "phase_name": "Proof of Concept Phase",
            "duration": "4 weeks",
            "activities": [
                "Prototype design and specification",
                "Core protocol integration development",
                "Testing and validation",
                "Documentation and evaluation"
            ],
            "ethical_concerns": []
        }
    }
    
    # Literature Review Phase Concerns
    phase_concerns["literature_review_phase"]["ethical_concerns"] = [
        {
            "concern_id": "LR-001",
            "concern": "Selection bias in literature inclusion",
            "description": "Risk of unconsciously selecting literature that supports predetermined conclusions about ACP vs A2A protocols",
            "severity": "Medium",
            "likelihood": "Medium",
            "affected_stakeholders": ["Academic community", "Technology developers", "Future researchers"],
            "potential_impact": "Skewed understanding of protocol capabilities and limitations",
            "ethics_frameworks": ["IEEE Code of Ethics", "Research integrity principles"],
            "manifestations": [
                "Preferential selection of papers favoring one protocol",
                "Exclusion of contradictory evidence without justification",
                "Over-representation of certain research groups or methodologies"
            ]
        },
        {
            "concern_id": "LR-002", 
            "concern": "Intellectual property and citation ethics",
            "description": "Proper attribution and respect for intellectual property in comprehensive literature analysis",
            "severity": "High",
            "likelihood": "Medium",
            "affected_stakeholders": ["Original researchers", "Academic institutions", "Publishers"],
            "potential_impact": "Academic misconduct, legal issues, damage to research integrity",
            "ethics_frameworks": ["Academic integrity standards", "Copyright law"],
            "manifestations": [
                "Inadequate citation of source materials",
                "Paraphrasing without proper attribution",
                "Use of proprietary information without permission"
            ]
        },
        {
            "concern_id": "LR-003",
            "concern": "Cultural and linguistic bias in literature selection",
            "description": "Potential bias toward English-language and Western research sources",
            "severity": "Medium",
            "likelihood": "High",
            "affected_stakeholders": ["Global research community", "Non-Western developers", "Diverse user populations"],
            "potential_impact": "Limited perspective on global protocol implementations and cultural considerations",
            "ethics_frameworks": ["Diversity and inclusion principles", "Global research equity"],
            "manifestations": [
                "Exclusion of non-English literature",
                "Under-representation of developing country research",
                "Missing cultural context in protocol evaluation"
            ]
        }
    ]
    
    # Comparative Analysis Phase Concerns
    phase_concerns["comparative_analysis_phase"]["ethical_concerns"] = [
        {
            "concern_id": "CA-001",
            "concern": "Fairness in protocol comparison methodology",
            "description": "Ensuring unbiased and fair comparison framework that doesn't favor one protocol over another",
            "severity": "High",
            "likelihood": "Medium",
            "affected_stakeholders": ["Protocol developers", "Technology users", "Industry stakeholders"],
            "potential_impact": "Unfair commercial advantage, misguided technology adoption decisions",
            "ethics_frameworks": ["IEEE Code of Ethics", "Fair evaluation principles"],
            "manifestations": [
                "Evaluation criteria that inherently favor one protocol",
                "Unequal testing conditions or scenarios",
                "Selective presentation of comparison results"
            ]
        },
        {
            "concern_id": "CA-002",
            "concern": "Transparency in evaluation criteria and methods",
            "description": "Obligation to clearly document and justify all evaluation criteria and analytical methods",
            "severity": "High",
            "likelihood": "Low",
            "affected_stakeholders": ["Research community", "Technology developers", "Policy makers"],
            "potential_impact": "Inability to validate research, reduced trust in findings",
            "ethics_frameworks": ["EU Ethics Guidelines for Trustworthy AI", "Transparency principles"],
            "manifestations": [
                "Undisclosed evaluation criteria",
                "Hidden assumptions in analysis",
                "Lack of methodology documentation"
            ]
        },
        {
            "concern_id": "CA-003",
            "concern": "Conflict of interest with protocol developers",
            "description": "Potential conflicts if researchers have relationships with protocol development organizations",
            "severity": "High",
            "likelihood": "Low",
            "affected_stakeholders": ["Research integrity", "Academic institutions", "Public trust"],
            "potential_impact": "Compromised research objectivity, loss of scientific credibility",
            "ethics_frameworks": ["IEEE Code of Ethics", "Academic conflict of interest policies"],
            "manifestations": [
                "Undisclosed financial relationships",
                "Previous employment with protocol developers",
                "Funding from biased sources"
            ]
        },
        {
            "concern_id": "CA-004",
            "concern": "Privacy implications in protocol evaluation",
            "description": "Protecting privacy when analyzing protocols that handle personal or sensitive data",
            "severity": "High",
            "likelihood": "Medium",
            "affected_stakeholders": ["DER users", "Energy consumers", "Privacy advocates"],
            "potential_impact": "Privacy violations, regulatory non-compliance, user harm",
            "ethics_frameworks": ["GDPR", "Smart Grid Ethics Framework"],
            "manifestations": [
                "Exposure of personal energy consumption patterns",
                "Inadequate data protection measures",
                "Lack of privacy impact assessment"
            ]
        }
    ]
    
    # Prototype Development Phase Concerns
    phase_concerns["prototype_development_phase"]["ethical_concerns"] = [
        {
            "concern_id": "PD-001",
            "concern": "Safety and reliability of prototype systems",
            "description": "Ensuring prototype development doesn't create safety risks or unreliable systems",
            "severity": "High",
            "likelihood": "Medium",
            "affected_stakeholders": ["Energy system operators", "End users", "Public safety"],
            "potential_impact": "System failures, safety incidents, infrastructure damage",
            "ethics_frameworks": ["IEEE Standards for Ethical Design", "Safety engineering principles"],
            "manifestations": [
                "Inadequate error handling in prototypes",
                "Unsafe testing procedures",
                "Deployment without proper safety validation"
            ]
        },
        {
            "concern_id": "PD-002",
            "concern": "Environmental impact of prototype development",
            "description": "Considering environmental costs of development and testing activities",
            "severity": "Medium",
            "likelihood": "High",
            "affected_stakeholders": ["Environment", "Future generations", "Local communities"],
            "potential_impact": "Unnecessary environmental damage, carbon footprint increase",
            "ethics_frameworks": ["UN Sustainable Development Goals", "Precautionary Principle"],
            "manifestations": [
                "Wasteful use of computing resources",
                "Unnecessary hardware procurement",
                "Energy-intensive testing procedures"
            ]
        },
        {
            "concern_id": "PD-003",
            "concern": "Accessibility and inclusivity in prototype design",
            "description": "Ensuring prototype design considers diverse user needs and capabilities",
            "severity": "Medium",
            "likelihood": "Medium",
            "affected_stakeholders": ["Disabled users", "Elderly users", "Low-income communities"],
            "potential_impact": "Digital exclusion, unequal access to benefits",
            "ethics_frameworks": ["Accessibility standards", "Digital inclusion principles"],
            "manifestations": [
                "Interface design barriers",
                "Language or literacy requirements",
                "Technology access requirements"
            ]
        },
        {
            "concern_id": "PD-004",
            "concern": "Data security in prototype implementation",
            "description": "Protecting data security during prototype development and testing",
            "severity": "High",
            "likelihood": "Medium",
            "affected_stakeholders": ["Data subjects", "System operators", "Cybersecurity"],
            "potential_impact": "Data breaches, system vulnerabilities, privacy violations",
            "ethics_frameworks": ["GDPR", "Cybersecurity frameworks"],
            "manifestations": [
                "Inadequate encryption protocols",
                "Insecure data storage practices",
                "Weak authentication mechanisms"
            ]
        }
    ]
    
    return phase_concerns

def identify_stakeholder_specific_concerns(ethics_review):
    """Identify ethical concerns specific to different stakeholder groups"""
    
    research_context = ethics_review.get("research_context", {})
    stakeholders = research_context.get("stakeholders", [])
    
    stakeholder_concerns = {}
    
    # Define concerns for each stakeholder group
    stakeholder_groups = {
        "energy_consumers": {
            "group_name": "Energy Consumers and DER Owners",
            "description": "Individuals and organizations that own or operate distributed energy resources",
            "primary_interests": ["Cost savings", "Privacy protection", "System reliability", "Ease of use"],
            "concerns": [
                {
                    "concern_id": "EC-001",
                    "concern": "Privacy of energy consumption data",
                    "description": "Risk of exposing personal energy usage patterns and behaviors",
                    "severity": "High",
                    "ethics_frameworks": ["GDPR", "Consumer privacy rights"],
                    "specific_risks": [
                        "Inference of daily routines from energy patterns",
                        "Exposure of occupancy patterns", 
                        "Commercial exploitation of usage data"
                    ]
                },
                {
                    "concern_id": "EC-002",
                    "concern": "Informed consent for data sharing",
                    "description": "Ensuring consumers understand and consent to data collection and use",
                    "severity": "High",
                    "ethics_frameworks": ["Helsinki Declaration", "Consumer protection law"],
                    "specific_risks": [
                        "Complex technical language in consent forms",
                        "Unclear scope of data sharing",
                        "Difficulty withdrawing consent"
                    ]
                },
                {
                    "concern_id": "EC-003",
                    "concern": "Equitable access to protocol benefits",
                    "description": "Ensuring all consumers can benefit regardless of technical sophistication or resources",
                    "severity": "Medium",
                    "ethics_frameworks": ["Energy justice principles", "Digital inclusion"],
                    "specific_risks": [
                        "Technology barriers for elderly users",
                        "Cost barriers for low-income households",
                        "Geographic digital divides"
                    ]
                }
            ]
        },
        "der_operators": {
            "group_name": "DER Operators and Energy Service Providers",
            "description": "Organizations that manage DER systems and provide energy services",
            "primary_interests": ["Operational efficiency", "Competitive advantage", "Regulatory compliance", "Customer satisfaction"],
            "concerns": [
                {
                    "concern_id": "DO-001",
                    "concern": "Commercial fairness and competition",
                    "description": "Ensuring protocol research doesn't unfairly advantage certain market players",
                    "severity": "Medium",
                    "ethics_frameworks": ["Fair competition principles", "Antitrust considerations"],
                    "specific_risks": [
                        "Research bias toward incumbent technologies",
                        "Intellectual property conflicts",
                        "Market manipulation through selective disclosure"
                    ]
                },
                {
                    "concern_id": "DO-002",
                    "concern": "Operational liability and responsibility",
                    "description": "Clarifying responsibility when automated protocols make decisions",
                    "severity": "High",
                    "ethics_frameworks": ["Accountability principles", "Professional liability"],
                    "specific_risks": [
                        "Unclear liability for autonomous agent decisions",
                        "Insurance and legal coverage gaps",
                        "Regulatory compliance uncertainties"
                    ]
                }
            ]
        },
        "grid_operators": {
            "group_name": "Grid Operators and System Managers",
            "description": "Utilities and organizations responsible for electrical grid stability and operation",
            "primary_interests": ["Grid stability", "System reliability", "Regulatory compliance", "Public safety"],
            "concerns": [
                {
                    "concern_id": "GO-001",
                    "concern": "Grid stability and safety risks",
                    "description": "Potential risks to grid stability from protocol implementation",
                    "severity": "High",
                    "ethics_frameworks": ["Public safety principles", "Critical infrastructure protection"],
                    "specific_risks": [
                        "Cascading failures from protocol errors",
                        "Cybersecurity vulnerabilities",
                        "Emergency response complications"
                    ]
                },
                {
                    "concern_id": "GO-002",
                    "concern": "Regulatory and legal compliance",
                    "description": "Ensuring protocols comply with existing and emerging regulations",
                    "severity": "High",
                    "ethics_frameworks": ["Regulatory compliance", "Legal responsibility"],
                    "specific_risks": [
                        "Conflicts with existing grid codes",
                        "Liability for protocol-caused incidents",
                        "Regulatory approval delays"
                    ]
                }
            ]
        },
        "technology_developers": {
            "group_name": "Technology Developers and Researchers",
            "description": "Organizations and individuals developing protocol technologies",
            "primary_interests": ["Innovation advancement", "Intellectual property protection", "Market adoption", "Technical excellence"],
            "concerns": [
                {
                    "concern_id": "TD-001",
                    "concern": "Intellectual property rights and open science",
                    "description": "Balancing IP protection with open scientific research",
                    "severity": "Medium",
                    "ethics_frameworks": ["Open science principles", "IP law"],
                    "specific_risks": [
                        "Conflicts between openness and commercialization",
                        "Patent blocking of research",
                        "Trade secret vs transparency tensions"
                    ]
                },
                {
                    "concern_id": "TD-002",
                    "concern": "Responsible innovation and deployment",
                    "description": "Ensuring technologies are developed and deployed responsibly",
                    "severity": "High",
                    "ethics_frameworks": ["Responsible innovation", "Technology assessment"],
                    "specific_risks": [
                        "Premature deployment without adequate testing",
                        "Inadequate consideration of social impacts",
                        "Lock-in of suboptimal technologies"
                    ]
                }
            ]
        },
        "researchers": {
            "group_name": "Academic and Research Community",
            "description": "Academic researchers and institutions studying energy systems and protocols",
            "primary_interests": ["Scientific validity", "Research integrity", "Knowledge advancement", "Academic freedom"],
            "concerns": [
                {
                    "concern_id": "R-001",
                    "concern": "Research integrity and bias",
                    "description": "Maintaining objectivity and avoiding conflicts of interest",
                    "severity": "High",
                    "ethics_frameworks": ["Research integrity standards", "Academic ethics"],
                    "specific_risks": [
                        "Funding source bias",
                        "Publication pressure",
                        "Confirmation bias in analysis"
                    ]
                },
                {
                    "concern_id": "R-002",
                    "concern": "Open access and knowledge sharing",
                    "description": "Balancing open science with competitive and IP concerns",
                    "severity": "Medium",
                    "ethics_frameworks": ["Open science principles", "Academic freedom"],
                    "specific_risks": [
                        "Paywall barriers to research access",
                        "Selective disclosure of results",
                        "Geographic barriers to knowledge access"
                    ]
                }
            ]
        }
    }
    
    return stakeholder_groups

def assess_concern_interactions_and_priorities(phase_concerns, stakeholder_concerns):
    """Assess how ethical concerns interact and prioritize them"""
    
    # Create comprehensive concern database
    all_concerns = {}
    
    # Add phase-specific concerns
    for phase_key, phase in phase_concerns.items():
        for concern in phase["ethical_concerns"]:
            concern_id = concern["concern_id"]
            concern["source_type"] = "research_phase"
            concern["source"] = phase["phase_name"]
            all_concerns[concern_id] = concern
    
    # Add stakeholder-specific concerns
    for stakeholder_key, stakeholder in stakeholder_concerns.items():
        for concern in stakeholder["concerns"]:
            concern_id = concern["concern_id"]
            concern["source_type"] = "stakeholder_group"
            concern["source"] = stakeholder["group_name"]
            concern["affected_stakeholders"] = [stakeholder["group_name"]]
            all_concerns[concern_id] = concern
    
    # Assess concern interactions
    concern_interactions = []
    
    # Privacy-related interactions
    privacy_concerns = [cid for cid, concern in all_concerns.items() if "privacy" in concern["concern"].lower()]
    if len(privacy_concerns) > 1:
        concern_interactions.append({
            "interaction_id": "INT-001",
            "interaction_type": "Reinforcing",
            "description": "Multiple privacy concerns create compounding risks",
            "involved_concerns": privacy_concerns,
            "interaction_effect": "Amplified risk of privacy violations across research phases and stakeholder groups",
            "mitigation_priority": "High"
        })
    
    # Safety and reliability interactions
    safety_concerns = [cid for cid, concern in all_concerns.items() if any(word in concern["concern"].lower() for word in ["safety", "reliability", "stability"])]
    if len(safety_concerns) > 1:
        concern_interactions.append({
            "interaction_id": "INT-002",
            "interaction_type": "Cascading",
            "description": "Safety issues in one area can cascade to others",
            "involved_concerns": safety_concerns,
            "interaction_effect": "Safety problems in prototype development could affect grid operations and public safety",
            "mitigation_priority": "High"
        })
    
    # Fairness and bias interactions
    fairness_concerns = [cid for cid, concern in all_concerns.items() if any(word in concern["concern"].lower() for word in ["fair", "bias", "equit"])]
    if len(fairness_concerns) > 1:
        concern_interactions.append({
            "interaction_id": "INT-003",
            "interaction_type": "Compounding",
            "description": "Bias at multiple levels compounds unfairness",
            "involved_concerns": fairness_concerns,
            "interaction_effect": "Research bias combined with deployment inequities creates systemic unfairness",
            "mitigation_priority": "Medium"
        })
    
    # Prioritization analysis
    concern_priorities = {}
    
    for concern_id, concern in all_concerns.items():
        # Calculate priority score based on severity, likelihood, and stakeholder impact
        severity_score = {"High": 3, "Medium": 2, "Low": 1}.get(concern.get("severity", "Medium"), 2)
        likelihood_score = {"High": 3, "Medium": 2, "Low": 1}.get(concern.get("likelihood", "Medium"), 2)
        
        # Count affected stakeholders
        stakeholder_count = len(concern.get("affected_stakeholders", []))
        stakeholder_score = min(3, stakeholder_count)  # Cap at 3
        
        # Calculate composite priority score
        priority_score = (severity_score * 0.4) + (likelihood_score * 0.3) + (stakeholder_score * 0.3)
        
        priority_level = "High" if priority_score >= 2.5 else "Medium" if priority_score >= 2.0 else "Low"
        
        concern_priorities[concern_id] = {
            "concern": concern,
            "priority_score": round(priority_score, 2),
            "priority_level": priority_level,
            "severity_score": severity_score,
            "likelihood_score": likelihood_score,
            "stakeholder_score": stakeholder_score
        }
    
    return all_concerns, concern_interactions, concern_priorities

def create_mitigation_framework(concern_priorities, concern_interactions):
    """Create framework for addressing identified ethical concerns"""
    
    mitigation_framework = {
        "framework_overview": {
            "purpose": "Systematic approach to addressing ethical concerns in ACP/A2A research",
            "scope": "All research phases and stakeholder impacts",
            "implementation_approach": "Prevention-focused with continuous monitoring"
        },
        "mitigation_strategies": {},
        "implementation_timeline": {},
        "monitoring_procedures": {}
    }
    
    # Group concerns by priority for mitigation planning
    high_priority_concerns = {cid: data for cid, data in concern_priorities.items() if data["priority_level"] == "High"}
    medium_priority_concerns = {cid: data for cid, data in concern_priorities.items() if data["priority_level"] == "Medium"}
    
    # Develop mitigation strategies for high-priority concerns
    for concern_id, concern_data in high_priority_concerns.items():
        concern = concern_data["concern"]
        
        mitigation_strategy = {
            "concern_id": concern_id,
            "concern_description": concern["concern"],
            "mitigation_approach": "Preventive and responsive measures",
            "specific_actions": [],
            "responsible_parties": [],
            "implementation_phase": "Immediate",
            "monitoring_indicators": [],
            "escalation_procedures": []
        }
        
        # Generate specific actions based on concern type
        if "privacy" in concern["concern"].lower():
            mitigation_strategy["specific_actions"] = [
                "Conduct Data Protection Impact Assessment (DPIA)",
                "Implement data minimization principles",
                "Establish clear data governance procedures",
                "Create transparent privacy policies",
                "Implement technical privacy safeguards"
            ]
            mitigation_strategy["responsible_parties"] = ["Principal Investigator", "Data Protection Officer", "Ethics Committee"]
            mitigation_strategy["monitoring_indicators"] = ["DPIA completion", "Privacy policy clarity", "Data minimization compliance"]
            
        elif "fairness" in concern["concern"].lower() or "bias" in concern["concern"].lower():
            mitigation_strategy["specific_actions"] = [
                "Develop explicit bias assessment criteria",
                "Implement diverse review panels",
                "Create transparent evaluation methodology",
                "Establish fairness metrics and thresholds",
                "Document all methodological decisions"
            ]
            mitigation_strategy["responsible_parties"] = ["Research Team", "External Reviewers", "Ethics Committee"]
            mitigation_strategy["monitoring_indicators"] = ["Bias assessment completion", "Review panel diversity", "Methodology transparency"]
            
        elif "safety" in concern["concern"].lower() or "reliability" in concern["concern"].lower():
            mitigation_strategy["specific_actions"] = [
                "Conduct comprehensive risk assessment",
                "Implement safety-by-design principles",
                "Establish testing and validation protocols",
                "Create emergency response procedures",
                "Implement continuous safety monitoring"
            ]
            mitigation_strategy["responsible_parties"] = ["Technical Team", "Safety Officer", "System Operators"]
            mitigation_strategy["monitoring_indicators"] = ["Risk assessment completion", "Safety protocol implementation", "Incident reporting"]
            
        else:
            # Generic mitigation approach
            mitigation_strategy["specific_actions"] = [
                "Establish clear ethical guidelines",
                "Implement regular review procedures",
                "Create stakeholder feedback mechanisms",
                "Document decision-making processes",
                "Provide ethics training for team members"
            ]
            mitigation_strategy["responsible_parties"] = ["Research Team", "Ethics Committee", "Stakeholder Representatives"]
            mitigation_strategy["monitoring_indicators"] = ["Guideline compliance", "Review completion", "Stakeholder feedback"]
        
        mitigation_strategy["escalation_procedures"] = [
            "Level 1: Team-level review and response",
            "Level 2: Ethics committee consultation",
            "Level 3: External expert review",
            "Level 4: Research suspension if necessary"
        ]
        
        mitigation_framework["mitigation_strategies"][concern_id] = mitigation_strategy
    
    # Create implementation timeline
    mitigation_framework["implementation_timeline"] = {
        "immediate_actions": {
            "timeframe": "Within 1 week",
            "actions": [
                "Establish ethics committee contacts",
                "Review and sign ethics commitments",
                "Create ethics documentation templates",
                "Begin high-priority DPIAs and risk assessments"
            ]
        },
        "short_term_actions": {
            "timeframe": "Within 1 month",
            "actions": [
                "Complete all high-priority mitigation implementations",
                "Establish monitoring and review procedures",
                "Conduct team ethics training",
                "Create stakeholder communication channels"
            ]
        },
        "ongoing_actions": {
            "timeframe": "Throughout research project",
            "actions": [
                "Regular ethics review meetings",
                "Continuous concern monitoring",
                "Stakeholder feedback collection",
                "Documentation and reporting"
            ]
        }
    }
    
    # Create monitoring procedures
    mitigation_framework["monitoring_procedures"] = {
        "daily_monitoring": [
            "Review data handling practices",
            "Check privacy safeguard implementation",
            "Monitor system safety indicators"
        ],
        "weekly_monitoring": [
            "Team ethics review meeting",
            "Stakeholder feedback review",
            "Incident and concern logging"
        ],
        "monthly_monitoring": [
            "Comprehensive ethics compliance review",
            "Mitigation effectiveness assessment",
            "External stakeholder consultation"
        ],
        "phase_transition_monitoring": [
            "Ethics impact assessment for next phase",
            "Concern priority re-evaluation",
            "Mitigation strategy updates"
        ]
    }
    
    return mitigation_framework

def generate_ethical_concerns_document(phase_concerns, stakeholder_concerns, all_concerns, concern_interactions, concern_priorities, mitigation_framework):
    """Generate comprehensive ethical concerns analysis document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Ethical Concerns Identification (Task 6.1.2)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Context: Systematic identification of ethical concerns in ACP vs A2A research*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    total_concerns = len(all_concerns)
    high_priority_count = len([c for c in concern_priorities.values() if c["priority_level"] == "High"])
    medium_priority_count = len([c for c in concern_priorities.values() if c["priority_level"] == "Medium"])
    
    doc_parts.append(f"This analysis identifies **{total_concerns} specific ethical concerns** across all research phases and stakeholder groups. ")
    doc_parts.append(f"Of these, **{high_priority_count} are classified as high priority** and **{medium_priority_count} as medium priority**, ")
    doc_parts.append("requiring immediate attention and systematic mitigation strategies.\n\n")
    
    # Research Phase Concerns
    doc_parts.append("## Research Phase-Specific Concerns\n\n")
    
    for phase_key, phase in phase_concerns.items():
        doc_parts.append(f"### {phase['phase_name']}\n")
        doc_parts.append(f"**Duration**: {phase['duration']}\n")
        doc_parts.append("**Key Activities**: " + ", ".join(phase['activities']) + "\n\n")
        
        doc_parts.append("| Concern ID | Concern | Severity | Likelihood | Key Impact |\n")
        doc_parts.append("|------------|---------|----------|------------|------------|\n")
        
        for concern in phase['ethical_concerns']:
            impact_summary = concern['potential_impact'][:50] + "..." if len(concern['potential_impact']) > 50 else concern['potential_impact']
            doc_parts.append(f"| {concern['concern_id']} | {concern['concern']} | {concern['severity']} | {concern['likelihood']} | {impact_summary} |\n")
        
        doc_parts.append("\n")
        
        # Detailed concern descriptions
        for concern in phase['ethical_concerns']:
            doc_parts.append(f"#### {concern['concern_id']}: {concern['concern']}\n")
            doc_parts.append(f"**Description**: {concern['description']}\n")
            doc_parts.append(f"**Affected Stakeholders**: {', '.join(concern['affected_stakeholders'])}\n")
            doc_parts.append("**Potential Manifestations**:\n")
            for manifestation in concern['manifestations']:
                doc_parts.append(f"- {manifestation}\n")
            doc_parts.append("\n")
        
        doc_parts.append("---\n")
    
    # Stakeholder-Specific Concerns
    doc_parts.append("## Stakeholder-Specific Concerns\n\n")
    
    for stakeholder_key, stakeholder in stakeholder_concerns.items():
        doc_parts.append(f"### {stakeholder['group_name']}\n")
        doc_parts.append(f"**Description**: {stakeholder['description']}\n")
        doc_parts.append("**Primary Interests**: " + ", ".join(stakeholder['primary_interests']) + "\n\n")
        
        for concern in stakeholder['concerns']:
            doc_parts.append(f"#### {concern['concern_id']}: {concern['concern']}\n")
            doc_parts.append(f"**Description**: {concern['description']}\n")
            doc_parts.append(f"**Severity**: {concern['severity']}\n")
            doc_parts.append("**Specific Risks**:\n")
            for risk in concern['specific_risks']:
                doc_parts.append(f"- {risk}\n")
            doc_parts.append("\n")
        
        doc_parts.append("---\n")
    
    # Concern Interactions
    doc_parts.append("## Concern Interactions and Dependencies\n\n")
    
    if concern_interactions:
        for interaction in concern_interactions:
            doc_parts.append(f"### {interaction['interaction_id']}: {interaction['interaction_type']} Interaction\n")
            doc_parts.append(f"**Description**: {interaction['description']}\n")
            doc_parts.append(f"**Involved Concerns**: {', '.join(interaction['involved_concerns'])}\n")
            doc_parts.append(f"**Effect**: {interaction['interaction_effect']}\n")
            doc_parts.append(f"**Mitigation Priority**: {interaction['mitigation_priority']}\n\n")
    else:
        doc_parts.append("No significant concern interactions identified at this time.\n\n")
    
    # Priority Analysis
    doc_parts.append("## Concern Priority Analysis\n\n")
    
    # High priority concerns
    high_priority_concerns = {cid: data for cid, data in concern_priorities.items() if data["priority_level"] == "High"}
    if high_priority_concerns:
        doc_parts.append("### High Priority Concerns\n")
        doc_parts.append("These concerns require immediate attention and comprehensive mitigation strategies:\n\n")
        
        # Sort by priority score
        sorted_high = sorted(high_priority_concerns.items(), key=lambda x: x[1]["priority_score"], reverse=True)
        
        for concern_id, concern_data in sorted_high:
            concern = concern_data["concern"]
            doc_parts.append(f"**{concern_id}: {concern['concern']}** (Priority Score: {concern_data['priority_score']}/3.0)\n")
            doc_parts.append(f"- Source: {concern['source']}\n")
            doc_parts.append(f"- Impact: {concern.get('potential_impact', concern.get('description', 'N/A'))}\n\n")
    
    # Medium priority concerns summary
    medium_priority_concerns = {cid: data for cid, data in concern_priorities.items() if data["priority_level"] == "Medium"}
    if medium_priority_concerns:
        doc_parts.append("### Medium Priority Concerns\n")
        doc_parts.append(f"**{len(medium_priority_concerns)} concerns** classified as medium priority require systematic monitoring and planned mitigation:\n")
        for concern_id, concern_data in medium_priority_concerns.items():
            doc_parts.append(f"- {concern_id}: {concern_data['concern']['concern']}\n")
        doc_parts.append("\n")
    
    # Mitigation Framework Overview
    doc_parts.append("## Mitigation Framework Overview\n\n")
    doc_parts.append("### Implementation Timeline\n")
    
    for timeline_key, timeline in mitigation_framework["implementation_timeline"].items():
        doc_parts.append(f"**{timeline_key.replace('_', ' ').title()}** ({timeline['timeframe']}):\n")
        for action in timeline['actions']:
            doc_parts.append(f"- {action}\n")
        doc_parts.append("\n")
    
    doc_parts.append("### High-Priority Mitigation Strategies\n")
    doc_parts.append("Detailed mitigation strategies for high-priority concerns:\n\n")
    
    for concern_id, strategy in mitigation_framework["mitigation_strategies"].items():
        if concern_id in high_priority_concerns:
            doc_parts.append(f"#### {concern_id}: {strategy['concern_description']}\n")
            doc_parts.append("**Specific Actions**:\n")
            for action in strategy['specific_actions']:
                doc_parts.append(f"- {action}\n")
            doc_parts.append(f"**Responsible Parties**: {', '.join(strategy['responsible_parties'])}\n")
            doc_parts.append(f"**Implementation Phase**: {strategy['implementation_phase']}\n\n")
    
    # Monitoring and Review
    doc_parts.append("## Monitoring and Review Procedures\n\n")
    
    for monitoring_key, procedures in mitigation_framework["monitoring_procedures"].items():
        doc_parts.append(f"### {monitoring_key.replace('_', ' ').title()}\n")
        for procedure in procedures:
            doc_parts.append(f"- {procedure}\n")
        doc_parts.append("\n")
    
    # Conclusion and Next Steps
    doc_parts.append("## Conclusion and Next Steps\n\n")
    doc_parts.append("This comprehensive analysis identifies significant ethical concerns across all aspects of the ACP vs A2A research project. ")
    doc_parts.append(f"The identification of {high_priority_count} high-priority concerns requires immediate implementation of mitigation strategies ")
    doc_parts.append("before proceeding with detailed research activities.\n\n")
    
    doc_parts.append("**Immediate Actions Required**:\n")
    doc_parts.append("1. Review and approve mitigation strategies for all high-priority concerns\n")
    doc_parts.append("2. Establish ethics committee contacts and consultation procedures\n")
    doc_parts.append("3. Begin implementation of immediate mitigation actions\n")
    doc_parts.append("4. Proceed to Task 6.1.3 (Address Data Privacy) for detailed privacy analysis\n\n")
    
    doc_parts.append("**Next Steps**: The identified concerns and mitigation framework will guide implementation of specific ethics measures in subsequent tasks, particularly data privacy protection (6.1.3) and consent requirements (6.1.4).\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 6.1.2 (Identify Ethical Concerns) at {datetime.now().isoformat()}\n")
    
    print("🔍 Task 6.1.2: Identifying Ethical Concerns")
    print("=" * 70)
    
    # Load ethics guidelines review
    ethics_review = load_ethics_guidelines_review()
    if not ethics_review:
        print("Error: Could not load ethics guidelines review data")
        return
    
    # Identify research phase-specific concerns
    phase_concerns = identify_research_phase_specific_concerns(ethics_review)
    write_log(f"Identified concerns across {len(phase_concerns)} research phases")
    
    # Identify stakeholder-specific concerns
    stakeholder_concerns = identify_stakeholder_specific_concerns(ethics_review)
    write_log(f"Identified concerns for {len(stakeholder_concerns)} stakeholder groups")
    
    # Assess concern interactions and priorities
    all_concerns, concern_interactions, concern_priorities = assess_concern_interactions_and_priorities(
        phase_concerns, stakeholder_concerns
    )
    write_log(f"Analyzed {len(all_concerns)} total concerns with {len(concern_interactions)} interactions")
    
    # Create mitigation framework
    mitigation_framework = create_mitigation_framework(concern_priorities, concern_interactions)
    high_priority_mitigations = len([c for c in concern_priorities.values() if c["priority_level"] == "High"])
    write_log(f"Created mitigation framework with {high_priority_mitigations} high-priority strategies")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "6.1.2 - Identify Ethical Concerns",
            "timestamp": datetime.now().isoformat(),
            "context": "ACP vs A2A research ethical concerns analysis",
            "input_sources": ["6.1.1-ethics-guidelines-review.json"]
        },
        "phase_concerns": phase_concerns,
        "stakeholder_concerns": stakeholder_concerns,
        "all_concerns": all_concerns,
        "concern_interactions": concern_interactions,
        "concern_priorities": concern_priorities,
        "mitigation_framework": mitigation_framework
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "6.1.2-ethical-concerns-analysis.json"
    try:
        OUTPUT_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save ethical concerns document
    concerns_doc = generate_ethical_concerns_document(
        phase_concerns, stakeholder_concerns, all_concerns, 
        concern_interactions, concern_priorities, mitigation_framework
    )
    
    md_output_path = OUTPUT_DOCS_DIR / "6.1.2-ethical-concerns-analysis.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(concerns_doc)
        write_log(f"Ethical concerns document saved to {md_output_path}")
        print(f"Ethical concerns analysis saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving concerns document: {e}")
    
    # Summary of findings
    high_priority_count = len([c for c in concern_priorities.values() if c["priority_level"] == "High"])
    medium_priority_count = len([c for c in concern_priorities.values() if c["priority_level"] == "Medium"])
    
    write_log(f"Finished Task 6.1.2 at {datetime.now().isoformat()}")
    print(f"\n✅ Task 6.1.2 complete")
    print(f"📊 Total ethical concerns identified: {len(all_concerns)}")
    print(f"🔥 High priority concerns: {high_priority_count}")
    print(f"⚠️ Medium priority concerns: {medium_priority_count}")
    print(f"🔗 Concern interactions: {len(concern_interactions)}")
    print(f"🛡️ Mitigation strategies developed: {len(mitigation_framework['mitigation_strategies'])}")

if __name__ == "__main__":
    main() 
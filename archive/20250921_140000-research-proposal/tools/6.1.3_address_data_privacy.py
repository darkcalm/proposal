#!/usr/bin/env python3
"""
Task 6.1.3: Address Data Privacy

Focus: Comprehensive data privacy analysis and protection framework for ACP/A2A research
Context: Building on identified privacy concerns to create robust data protection measures

Based on:
- Results from 6.1.1 ethics guidelines review (GDPR, Smart Grid Ethics, etc.)
- Results from 6.1.2 ethical concerns identification (privacy identified as highest priority)
- Research focus on Agent Communication Protocols involving energy data
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
ETHICAL_CONCERNS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "6.1.2-ethical-concerns-analysis.json"
ETHICS_GUIDELINES_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "6.1.1-ethics-guidelines-review.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "6.1.3_address_data_privacy.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analysis ---
def load_previous_analysis():
    """Load results from previous ethics tasks"""
    analysis_data = {}
    
    # Load ethical concerns analysis
    if ETHICAL_CONCERNS_INPUT_JSON.exists():
        try:
            with open(ETHICAL_CONCERNS_INPUT_JSON, 'r', encoding='utf-8') as f:
                analysis_data['ethical_concerns'] = json.load(f)
        except Exception as e:
            write_log(f"Error loading ethical concerns analysis: {e}")
    
    # Load ethics guidelines review
    if ETHICS_GUIDELINES_INPUT_JSON.exists():
        try:
            with open(ETHICS_GUIDELINES_INPUT_JSON, 'r', encoding='utf-8') as f:
                analysis_data['ethics_guidelines'] = json.load(f)
        except Exception as e:
            write_log(f"Error loading ethics guidelines review: {e}")
    
    return analysis_data

# --- Data Privacy Analysis Functions ---
def identify_data_types_and_flows(previous_analysis):
    """Identify specific data types and flows in ACP/A2A research"""
    
    data_taxonomy = {
        "personal_data": {
            "category": "Personal Data (GDPR Art. 4)",
            "description": "Data relating to identified or identifiable natural persons",
            "data_types": [
                {
                    "type": "Energy consumption patterns",
                    "description": "Individual household or building energy usage over time",
                    "sensitivity": "High",
                    "identifiability": "High - can reveal occupancy patterns, lifestyle habits",
                    "sources": ["Smart meters", "DER monitoring systems", "Building management systems"],
                    "processing_purposes": [
                        "Protocol performance evaluation",
                        "Predictive maintenance algorithm training",
                        "Communication pattern analysis"
                    ],
                    "gdpr_lawful_basis": ["Consent", "Legitimate interests (with balancing test)"],
                    "retention_requirements": "Limited to research completion + validation period"
                },
                {
                    "type": "Device operation data",
                    "description": "DER operational parameters and status information",
                    "sensitivity": "Medium",
                    "identifiability": "Medium - can be linked to specific installations",
                    "sources": ["Solar inverters", "Battery systems", "EV chargers", "Heat pumps"],
                    "processing_purposes": [
                        "Device behavior analysis",
                        "Fault detection research",
                        "Protocol optimization"
                    ],
                    "gdpr_lawful_basis": ["Consent", "Legitimate interests"],
                    "retention_requirements": "Research duration + 2 years for validation"
                },
                {
                    "type": "Location and property data",
                    "description": "Geographic location, property characteristics, installation details",
                    "sensitivity": "High",
                    "identifiability": "Very High - directly identifies premises",
                    "sources": ["Installation databases", "Grid connection records", "Property registries"],
                    "processing_purposes": [
                        "Geographic analysis of protocol performance",
                        "Context-aware optimization research"
                    ],
                    "gdpr_lawful_basis": ["Explicit consent required"],
                    "retention_requirements": "Minimized aggregation, limited retention"
                }
            ]
        },
        "quasi_personal_data": {
            "category": "Quasi-Personal Data",
            "description": "Data that could identify individuals when combined with other information",
            "data_types": [
                {
                    "type": "Communication metadata",
                    "description": "Agent-to-agent communication logs, timing, frequency",
                    "sensitivity": "Medium",
                    "identifiability": "Medium - patterns could identify specific systems",
                    "sources": ["Communication protocols", "Network logs", "Agent systems"],
                    "processing_purposes": [
                        "Communication efficiency analysis",
                        "Protocol comparison research",
                        "Network performance evaluation"
                    ],
                    "privacy_risks": [
                        "Inference of operational patterns",
                        "Device fingerprinting",
                        "Behavioral profiling"
                    ]
                },
                {
                    "type": "Aggregated energy data",
                    "description": "Neighborhood or district-level energy statistics",
                    "sensitivity": "Low-Medium",
                    "identifiability": "Low - but small groups may be identifiable",
                    "sources": ["Grid monitoring", "Aggregated smart meter data"],
                    "processing_purposes": [
                        "System-level impact analysis",
                        "Grid stability research",
                        "Collective behavior studies"
                    ],
                    "privacy_risks": [
                        "Re-identification through correlation",
                        "Inference attacks on small groups"
                    ]
                }
            ]
        },
        "technical_data": {
            "category": "Technical and System Data",
            "description": "Non-personal technical information about systems and protocols",
            "data_types": [
                {
                    "type": "Protocol performance metrics",
                    "description": "Technical performance indicators, response times, reliability metrics",
                    "sensitivity": "Low",
                    "identifiability": "None - anonymized technical data",
                    "sources": ["Protocol implementations", "Testing frameworks", "Simulation results"],
                    "processing_purposes": [
                        "Performance comparison",
                        "Technical optimization",
                        "Academic publication"
                    ],
                    "privacy_risks": ["Minimal - no personal identifiers"]
                },
                {
                    "type": "System configuration data",
                    "description": "DER system specifications, capabilities, settings",
                    "sensitivity": "Low",
                    "identifiability": "None when properly anonymized",
                    "sources": ["Device specifications", "Configuration files", "Technical documentation"],
                    "processing_purposes": [
                        "Compatibility analysis",
                        "Technical requirements research",
                        "Standard development"
                    ],
                    "privacy_risks": ["Minimal when anonymized"]
                }
            ]
        }
    }
    
    # Map data flows across research phases
    data_flows = {
        "literature_review_phase": {
            "phase": "Literature Review and Analysis",
            "data_interactions": [
                {
                    "flow_id": "LR-F001",
                    "description": "Access to published datasets and case studies",
                    "data_types": ["Published energy data", "Anonymized case studies"],
                    "privacy_risk": "Low - already published/anonymized",
                    "controls_required": ["Citation compliance", "Terms of use adherence"]
                }
            ]
        },
        "comparative_analysis_phase": {
            "phase": "Comparative Framework Development",
            "data_interactions": [
                {
                    "flow_id": "CA-F001",
                    "description": "Collection of real-world performance data for protocol comparison",
                    "data_types": ["Energy consumption patterns", "Communication metadata", "Device operation data"],
                    "privacy_risk": "High - access to potentially personal data",
                    "controls_required": ["DPIA", "Data minimization", "Anonymization", "Consent management"]
                },
                {
                    "flow_id": "CA-F002",
                    "description": "Data sharing with external validators or reviewers",
                    "data_types": ["Anonymized performance metrics", "Aggregated results"],
                    "privacy_risk": "Medium - risk of re-identification",
                    "controls_required": ["Data sharing agreements", "Additional anonymization", "Access controls"]
                }
            ]
        },
        "prototype_development_phase": {
            "phase": "Prototype Development and Testing",
            "data_interactions": [
                {
                    "flow_id": "PD-F001",
                    "description": "Live data collection for prototype testing",
                    "data_types": ["Real-time energy data", "Communication logs", "System status"],
                    "privacy_risk": "Very High - live personal data processing",
                    "controls_required": ["Real-time anonymization", "Secure processing", "Limited retention", "Participant consent"]
                },
                {
                    "flow_id": "PD-F002",
                    "description": "Prototype data storage and analysis",
                    "data_types": ["Test results", "Performance logs", "Error reports"],
                    "privacy_risk": "Medium - derived from personal data",
                    "controls_required": ["Encrypted storage", "Access controls", "Audit trails", "Secure deletion"]
                }
            ]
        }
    }
    
    return data_taxonomy, data_flows

def conduct_data_protection_impact_assessment(data_taxonomy, data_flows, previous_analysis):
    """Conduct comprehensive DPIA following GDPR requirements"""
    
    dpia = {
        "dpia_metadata": {
            "assessment_date": datetime.now().isoformat(),
            "assessor": "Research Team",
            "scope": "ACP vs A2A Protocol Research Project",
            "legal_basis": "GDPR Article 35 - high risk processing",
            "review_date": "To be updated at each research phase"
        },
        "processing_overview": {
            "controller": "University Research Institution",
            "joint_controllers": ["To be determined based on collaboration agreements"],
            "processors": ["Cloud computing providers", "Data analysis platforms", "Storage services"],
            "data_subjects": [
                "DER system owners",
                "Energy consumers", 
                "Building occupants",
                "System operators"
            ],
            "processing_purposes": [
                "Academic research on communication protocols",
                "Performance comparison and evaluation",
                "Technical innovation and development",
                "Publication and knowledge dissemination"
            ]
        },
        "necessity_and_proportionality": {
            "necessity_assessment": {
                "research_necessity": "High - data essential for meaningful protocol comparison",
                "data_minimization_applied": "Yes - only data necessary for research objectives",
                "purpose_limitation": "Yes - data used only for stated research purposes",
                "storage_limitation": "Yes - data retained only for research and validation periods"
            },
            "proportionality_assessment": {
                "benefits_vs_risks": "High research and societal benefits justify privacy risks with adequate safeguards",
                "less_intrusive_alternatives": "Explored - synthetic data insufficient for realistic protocol evaluation",
                "stakeholder_interests": "Balanced through comprehensive safeguards and stakeholder consultation"
            }
        },
        "risk_assessment": {},
        "safeguards_and_measures": {},
        "consultation_outcomes": {}
    }
    
    # Detailed risk assessment for each data type
    for category_key, category in data_taxonomy.items():
        category_risks = []
        
        for data_type in category["data_types"]:
            risk_analysis = {
                "data_type": data_type["type"],
                "sensitivity_level": data_type["sensitivity"],
                "identified_risks": [],
                "impact_assessment": {},
                "likelihood_assessment": {},
                "overall_risk_level": ""
            }
            
            # Identify specific risks based on data type and processing
            if data_type["sensitivity"] in ["High", "Very High"]:
                risk_analysis["identified_risks"] = [
                    {
                        "risk": "Unauthorized access to personal energy data",
                        "impact": "High - privacy violation, potential for profiling",
                        "likelihood": "Medium - with standard security measures",
                        "affected_rights": ["Privacy", "Data protection", "Non-discrimination"]
                    },
                    {
                        "risk": "Re-identification through data correlation",
                        "impact": "High - could identify individuals despite anonymization attempts",
                        "likelihood": "Medium - sophisticated attackers or data correlations",
                        "affected_rights": ["Privacy", "Anonymity"]
                    },
                    {
                        "risk": "Inference of sensitive personal information",
                        "impact": "Medium-High - lifestyle, health, financial status inference",
                        "likelihood": "High - energy patterns reveal personal information",
                        "affected_rights": ["Privacy", "Non-discrimination", "Human dignity"]
                    }
                ]
            elif data_type["sensitivity"] == "Medium":
                risk_analysis["identified_risks"] = [
                    {
                        "risk": "Device fingerprinting and tracking",
                        "impact": "Medium - could enable system identification",
                        "likelihood": "Medium - through technical characteristics",
                        "affected_rights": ["Privacy", "Anonymity"]
                    },
                    {
                        "risk": "Commercial exploitation of usage patterns",
                        "impact": "Medium - unfair commercial advantage",
                        "likelihood": "Low - with proper access controls",
                        "affected_rights": ["Fair treatment", "Economic interests"]
                    }
                ]
            else:
                risk_analysis["identified_risks"] = [
                    {
                        "risk": "Aggregation and correlation risks",
                        "impact": "Low-Medium - potential for unexpected correlations",
                        "likelihood": "Low - minimal personal information",
                        "affected_rights": ["Privacy (limited)"]
                    }
                ]
            
            # Calculate overall risk level
            max_impact = max([r["impact"] for r in risk_analysis["identified_risks"]], default="Low")
            max_likelihood = max([r["likelihood"] for r in risk_analysis["identified_risks"]], default="Low")
            
            # Risk matrix calculation
            impact_score = {"Low": 1, "Low-Medium": 1.5, "Medium": 2, "Medium-High": 2.5, "High": 3, "Very High": 4}.get(max_impact.split(" - ")[0], 2)
            likelihood_score = {"Low": 1, "Medium": 2, "High": 3}.get(max_likelihood.split(" - ")[0], 2)
            risk_score = impact_score * likelihood_score
            
            if risk_score >= 6:
                risk_analysis["overall_risk_level"] = "High"
            elif risk_score >= 4:
                risk_analysis["overall_risk_level"] = "Medium"
            else:
                risk_analysis["overall_risk_level"] = "Low"
            
            category_risks.append(risk_analysis)
        
        dpia["risk_assessment"][category_key] = {
            "category": category["category"],
            "risk_analyses": category_risks
        }
    
    return dpia

def design_privacy_safeguards_framework(dpia, data_taxonomy, data_flows):
    """Design comprehensive privacy safeguards framework"""
    
    safeguards_framework = {
        "framework_overview": {
            "approach": "Privacy by Design and by Default",
            "principles": [
                "Data minimization",
                "Purpose limitation", 
                "Transparency",
                "Security",
                "Accountability",
                "Rights protection"
            ],
            "implementation_layers": [
                "Technical safeguards",
                "Organizational measures",
                "Legal protections",
                "Procedural controls"
            ]
        },
        "technical_safeguards": {},
        "organizational_measures": {},
        "legal_protections": {},
        "procedural_controls": {}
    }
    
    # Technical Safeguards
    safeguards_framework["technical_safeguards"] = {
        "data_anonymization": {
            "technique": "Multi-layered anonymization approach",
            "methods": [
                {
                    "method": "Direct identifier removal",
                    "description": "Remove names, addresses, account numbers, device IDs",
                    "applicable_data": "All personal data types",
                    "effectiveness": "High for direct identification"
                },
                {
                    "method": "Temporal aggregation",
                    "description": "Aggregate high-resolution temporal data to reduce identifiability",
                    "applicable_data": "Energy consumption patterns, communication logs",
                    "effectiveness": "Medium-High - reduces pattern recognition"
                },
                {
                    "method": "Spatial aggregation",
                    "description": "Aggregate location-specific data to larger geographic areas",
                    "applicable_data": "Location and property data",
                    "effectiveness": "High when aggregation areas are sufficiently large"
                },
                {
                    "method": "Differential privacy",
                    "description": "Add statistical noise to prevent individual identification",
                    "applicable_data": "Aggregated energy data, performance metrics",
                    "effectiveness": "Very High with proper parameter selection"
                },
                {
                    "method": "K-anonymity clustering",
                    "description": "Ensure each record is indistinguishable from k-1 others",
                    "applicable_data": "Device operation data, system configurations",
                    "effectiveness": "High when k is sufficiently large"
                }
            ],
            "implementation_requirements": [
                "Anonymization algorithm validation",
                "Re-identification risk assessment",
                "Regular effectiveness reviews",
                "Expert consultation on techniques"
            ]
        },
        "encryption_and_security": {
            "data_at_rest": {
                "encryption_standard": "AES-256",
                "key_management": "Hardware security modules (HSM) or cloud KMS",
                "access_controls": "Role-based access with multi-factor authentication",
                "backup_security": "Encrypted backups with separate key management"
            },
            "data_in_transit": {
                "encryption_protocol": "TLS 1.3 minimum",
                "certificate_management": "Automated certificate lifecycle management",
                "network_security": "VPN or dedicated secure channels for sensitive data"
            },
            "data_in_processing": {
                "secure_enclaves": "Use of trusted execution environments where available",
                "memory_protection": "Secure memory allocation and cleanup",
                "audit_logging": "Comprehensive access and processing logs"
            }
        },
        "access_controls": {
            "authentication": "Multi-factor authentication for all data access",
            "authorization": "Principle of least privilege with role-based access",
            "session_management": "Automatic session timeouts and secure session handling",
            "audit_trails": "Comprehensive logging of all data access and modifications"
        }
    }
    
    # Organizational Measures
    safeguards_framework["organizational_measures"] = {
        "governance_structure": {
            "data_protection_officer": {
                "role": "Designated DPO for research project",
                "responsibilities": [
                    "Privacy compliance oversight",
                    "DPIA validation and updates",
                    "Data subject rights management",
                    "Incident response coordination"
                ],
                "qualifications": "GDPR certification and technical expertise"
            },
            "ethics_committee": {
                "role": "Research ethics oversight",
                "responsibilities": [
                    "Ethics approval for data processing",
                    "Ongoing ethics compliance monitoring",
                    "Stakeholder concern resolution"
                ],
                "composition": "Independent experts including privacy advocates"
            }
        },
        "staff_training": {
            "privacy_training": {
                "frequency": "Initial training + annual updates",
                "content": ["GDPR requirements", "Technical safeguards", "Incident procedures"],
                "assessment": "Training completion certification required"
            },
            "technical_training": {
                "focus": "Privacy-preserving techniques and secure development",
                "providers": "Internal experts and external privacy specialists"
            }
        },
        "vendor_management": {
            "data_processing_agreements": "GDPR-compliant DPAs with all processors",
            "vendor_assessment": "Privacy and security assessment of all service providers",
            "monitoring": "Regular compliance monitoring and audits"
        }
    }
    
    # Legal Protections
    safeguards_framework["legal_protections"] = {
        "lawful_basis": {
            "primary_basis": "Legitimate interests (Article 6(1)(f))",
            "balancing_test": "Research benefits outweigh privacy risks with adequate safeguards",
            "consent_fallback": "Explicit consent for high-risk processing",
            "documentation": "Legal basis assessment documented and reviewable"
        },
        "data_subject_rights": {
            "information_provision": {
                "privacy_notice": "Clear, comprehensive privacy notice in plain language",
                "transparency": "Full disclosure of processing purposes and safeguards",
                "contact_information": "Clear contact details for privacy queries"
            },
            "access_rights": {
                "data_access": "Procedures for data subject access requests",
                "portability": "Data export in machine-readable format where applicable",
                "response_time": "30-day response time for requests"
            },
            "control_rights": {
                "rectification": "Procedures for data correction",
                "erasure": "Right to be forgotten implementation",
                "restriction": "Processing restriction capabilities",
                "objection": "Opt-out mechanisms for legitimate interests processing"
            }
        },
        "international_transfers": {
            "adequacy_decisions": "Preference for EU adequacy decision countries",
            "standard_contractual_clauses": "EU SCCs for third country transfers",
            "additional_safeguards": "Encryption and access controls for international transfers"
        }
    }
    
    # Procedural Controls
    safeguards_framework["procedural_controls"] = {
        "data_lifecycle_management": {
            "collection_procedures": [
                "Pre-collection DPIA review",
                "Data minimization checklist",
                "Purpose specification documentation",
                "Consent collection (where required)"
            ],
            "processing_procedures": [
                "Regular processing audits",
                "Purpose limitation monitoring",
                "Anonymization quality checks",
                "Access log reviews"
            ],
            "retention_procedures": [
                "Automated retention period enforcement",
                "Regular data review and deletion",
                "Secure deletion verification",
                "Retention schedule documentation"
            ]
        },
        "incident_response": {
            "incident_detection": "Automated monitoring and manual reporting procedures",
            "assessment_criteria": "Risk-based incident classification",
            "notification_requirements": "72-hour regulatory notification for high-risk breaches",
            "remediation_procedures": "Incident containment, investigation, and resolution"
        },
        "monitoring_and_review": {
            "regular_audits": "Quarterly privacy compliance audits",
            "effectiveness_reviews": "Annual safeguards effectiveness assessment",
            "stakeholder_feedback": "Regular consultation with data subjects and advocates",
            "continuous_improvement": "Privacy safeguards update procedures"
        }
    }
    
    return safeguards_framework

def create_implementation_roadmap(safeguards_framework, data_flows):
    """Create detailed implementation roadmap for privacy safeguards"""
    
    implementation_roadmap = {
        "roadmap_overview": {
            "approach": "Phased implementation aligned with research phases",
            "timeline": "18-week research project timeline",
            "milestone_driven": "Implementation tied to research phase gates"
        },
        "phase_implementations": {}
    }
    
    # Pre-Research Phase (Weeks -2 to 0)
    implementation_roadmap["phase_implementations"]["pre_research"] = {
        "phase": "Pre-Research Preparation",
        "timeline": "2 weeks before research commencement",
        "critical_path": True,
        "deliverables": [
            {
                "deliverable": "Complete DPIA",
                "deadline": "Week -2",
                "responsibility": "DPO + Research Team",
                "dependencies": ["Ethics committee approval"],
                "acceptance_criteria": [
                    "All high-risk processing identified",
                    "Safeguards mapped to risks",
                    "Legal basis documented",
                    "Stakeholder consultation completed"
                ]
            },
            {
                "deliverable": "Privacy Safeguards Implementation",
                "deadline": "Week -1",
                "responsibility": "Technical Team + DPO",
                "dependencies": ["DPIA completion", "Technical infrastructure"],
                "acceptance_criteria": [
                    "Encryption systems operational",
                    "Access controls configured",
                    "Anonymization tools validated",
                    "Audit logging enabled"
                ]
            },
            {
                "deliverable": "Staff Training Completion",
                "deadline": "Week -1",
                "responsibility": "Project Manager",
                "dependencies": ["Training materials preparation"],
                "acceptance_criteria": [
                    "All team members trained",
                    "Training certification obtained",
                    "Privacy procedures documented"
                ]
            }
        ]
    }
    
    # Literature Review Phase (Weeks 1-6)
    implementation_roadmap["phase_implementations"]["literature_review"] = {
        "phase": "Literature Review Phase",
        "timeline": "Weeks 1-6",
        "privacy_risk_level": "Low",
        "key_activities": [
            {
                "activity": "Published data analysis",
                "privacy_controls": [
                    "Citation compliance verification",
                    "Terms of use adherence",
                    "No additional personal data collection"
                ],
                "monitoring": "Weekly compliance checks"
            }
        ],
        "deliverables": [
            {
                "deliverable": "Phase Privacy Report",
                "deadline": "Week 6",
                "content": [
                    "Data sources used and compliance status",
                    "No personal data collection confirmation",
                    "Next phase privacy preparations"
                ]
            }
        ]
    }
    
    # Comparative Analysis Phase (Weeks 7-14)
    implementation_roadmap["phase_implementations"]["comparative_analysis"] = {
        "phase": "Comparative Analysis Phase",
        "timeline": "Weeks 7-14",
        "privacy_risk_level": "High",
        "key_activities": [
            {
                "activity": "Real-world data collection",
                "privacy_controls": [
                    "Consent collection (if required)",
                    "Immediate anonymization",
                    "Data minimization enforcement",
                    "Secure processing environment"
                ],
                "monitoring": "Daily access logs, weekly anonymization quality checks"
            },
            {
                "activity": "External data sharing",
                "privacy_controls": [
                    "Data sharing agreements",
                    "Additional anonymization",
                    "Access controls and audit trails"
                ],
                "monitoring": "Real-time sharing logs, monthly access reviews"
            }
        ],
        "deliverables": [
            {
                "deliverable": "Mid-project DPIA Update",
                "deadline": "Week 10",
                "content": [
                    "Actual vs planned data processing",
                    "Risk reassessment",
                    "Safeguards effectiveness review"
                ]
            }
        ]
    }
    
    # Prototype Development Phase (Weeks 15-18)
    implementation_roadmap["phase_implementations"]["prototype_development"] = {
        "phase": "Prototype Development Phase",
        "timeline": "Weeks 15-18",
        "privacy_risk_level": "Very High",
        "key_activities": [
            {
                "activity": "Live data testing",
                "privacy_controls": [
                    "Real-time anonymization",
                    "Minimal data retention",
                    "Secure testing environment",
                    "Participant agreement"
                ],
                "monitoring": "Continuous monitoring, daily security checks"
            },
            {
                "activity": "Prototype data storage",
                "privacy_controls": [
                    "Encrypted storage",
                    "Limited access",
                    "Automated deletion",
                    "Audit trails"
                ],
                "monitoring": "Real-time access monitoring, automated retention enforcement"
            }
        ],
        "deliverables": [
            {
                "deliverable": "Final Privacy Compliance Report",
                "deadline": "Week 18",
                "content": [
                    "Complete privacy compliance assessment",
                    "Data deletion confirmation",
                    "Lessons learned and recommendations"
                ]
            }
        ]
    }
    
    # Post-Research Phase (Weeks 19+)
    implementation_roadmap["phase_implementations"]["post_research"] = {
        "phase": "Post-Research Data Management",
        "timeline": "Ongoing after research completion",
        "key_activities": [
            {
                "activity": "Data retention management",
                "privacy_controls": [
                    "Scheduled data reviews",
                    "Automated deletion procedures",
                    "Audit trail maintenance"
                ],
                "monitoring": "Monthly retention reviews, annual compliance audits"
            }
        ]
    }
    
    return implementation_roadmap

def generate_data_privacy_document(dpia, safeguards_framework, implementation_roadmap, data_taxonomy, data_flows):
    """Generate comprehensive data privacy analysis document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Data Privacy Analysis and Protection Framework (Task 6.1.3)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Context: Comprehensive data privacy framework for ACP vs A2A research*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    doc_parts.append("This document provides a comprehensive data privacy analysis and protection framework for the Agent Communication Protocol research project. ")
    doc_parts.append("Following GDPR requirements and best practices, it includes a detailed Data Protection Impact Assessment (DPIA), ")
    doc_parts.append("multi-layered technical and organizational safeguards, and a phased implementation roadmap aligned with research activities.\n\n")
    
    # Data Classification and Risk Assessment
    doc_parts.append("## Data Classification and Processing Overview\n\n")
    
    for category_key, category in data_taxonomy.items():
        doc_parts.append(f"### {category['category']}\n")
        doc_parts.append(f"**Description**: {category['description']}\n\n")
        
        doc_parts.append("| Data Type | Sensitivity | Identifiability | Primary Sources |\n")
        doc_parts.append("|-----------|-------------|-----------------|----------------|\n")
        
        for data_type in category['data_types']:
            sources_brief = ", ".join(data_type.get('sources', ['N/A'])[:3])
            doc_parts.append(f"| {data_type['type']} | {data_type['sensitivity']} | {data_type['identifiability'][:50]}... | {sources_brief} |\n")
        
        doc_parts.append("\n")
    
    # DPIA Summary
    doc_parts.append("## Data Protection Impact Assessment (DPIA)\n\n")
    doc_parts.append("### Processing Overview\n")
    doc_parts.append(f"**Data Controller**: {dpia['processing_overview']['controller']}\n")
    doc_parts.append("**Data Subjects**: " + ", ".join(dpia['processing_overview']['data_subjects']) + "\n")
    doc_parts.append("**Processing Purposes**: " + ", ".join(dpia['processing_overview']['processing_purposes']) + "\n\n")
    
    doc_parts.append("### High-Risk Processing Identification\n")
    doc_parts.append("The following processing activities have been identified as high-risk under GDPR Article 35:\n\n")
    
    high_risk_count = 0
    for category_key, risk_category in dpia['risk_assessment'].items():
        for risk_analysis in risk_category['risk_analyses']:
            if risk_analysis['overall_risk_level'] == 'High':
                high_risk_count += 1
                doc_parts.append(f"**{risk_analysis['data_type']}** (Risk Level: {risk_analysis['overall_risk_level']})\n")
                for risk in risk_analysis['identified_risks']:
                    doc_parts.append(f"- {risk['risk']}: {risk['impact']}\n")
                doc_parts.append("\n")
    
    if high_risk_count == 0:
        doc_parts.append("*No processing activities classified as high-risk with proposed safeguards*\n\n")
    
    # Privacy Safeguards Framework
    doc_parts.append("## Privacy Safeguards Framework\n\n")
    doc_parts.append("### Technical Safeguards\n\n")
    
    # Anonymization techniques
    doc_parts.append("#### Data Anonymization Strategy\n")
    doc_parts.append("Multi-layered anonymization approach with the following techniques:\n\n")
    
    for method in safeguards_framework['technical_safeguards']['data_anonymization']['methods']:
        doc_parts.append(f"**{method['method']}**\n")
        doc_parts.append(f"- Description: {method['description']}\n")
        doc_parts.append(f"- Applicable to: {method['applicable_data']}\n")
        doc_parts.append(f"- Effectiveness: {method['effectiveness']}\n\n")
    
    # Security measures
    doc_parts.append("#### Security and Encryption\n")
    security_measures = safeguards_framework['technical_safeguards']['encryption_and_security']
    
    doc_parts.append("**Data at Rest**:\n")
    doc_parts.append(f"- Encryption: {security_measures['data_at_rest']['encryption_standard']}\n")
    doc_parts.append(f"- Key Management: {security_measures['data_at_rest']['key_management']}\n")
    doc_parts.append(f"- Access Controls: {security_measures['data_at_rest']['access_controls']}\n\n")
    
    doc_parts.append("**Data in Transit**:\n")
    doc_parts.append(f"- Protocol: {security_measures['data_in_transit']['encryption_protocol']}\n")
    doc_parts.append(f"- Network Security: {security_measures['data_in_transit']['network_security']}\n\n")
    
    # Organizational measures
    doc_parts.append("### Organizational Measures\n\n")
    
    doc_parts.append("#### Governance Structure\n")
    governance = safeguards_framework['organizational_measures']['governance_structure']
    
    doc_parts.append(f"**Data Protection Officer**: {governance['data_protection_officer']['role']}\n")
    doc_parts.append("Responsibilities:\n")
    for resp in governance['data_protection_officer']['responsibilities']:
        doc_parts.append(f"- {resp}\n")
    doc_parts.append("\n")
    
    doc_parts.append(f"**Ethics Committee**: {governance['ethics_committee']['role']}\n")
    doc_parts.append("Responsibilities:\n")
    for resp in governance['ethics_committee']['responsibilities']:
        doc_parts.append(f"- {resp}\n")
    doc_parts.append("\n")
    
    # Data Subject Rights
    doc_parts.append("### Data Subject Rights Implementation\n\n")
    rights = safeguards_framework['legal_protections']['data_subject_rights']
    
    doc_parts.append("#### Information and Access Rights\n")
    doc_parts.append(f"- **Privacy Notice**: {rights['information_provision']['privacy_notice']}\n")
    doc_parts.append(f"- **Data Access**: {rights['access_rights']['data_access']}\n")
    doc_parts.append(f"- **Response Time**: {rights['access_rights']['response_time']}\n\n")
    
    doc_parts.append("#### Control Rights\n")
    for right, implementation in rights['control_rights'].items():
        doc_parts.append(f"- **{right.title()}**: {implementation}\n")
    doc_parts.append("\n")
    
    # Implementation Roadmap
    doc_parts.append("## Implementation Roadmap\n\n")
    
    for phase_key, phase in implementation_roadmap['phase_implementations'].items():
        doc_parts.append(f"### {phase['phase']}\n")
        doc_parts.append(f"**Timeline**: {phase['timeline']}\n")
        if 'privacy_risk_level' in phase:
            doc_parts.append(f"**Privacy Risk Level**: {phase['privacy_risk_level']}\n")
        doc_parts.append("\n")
        
        if 'deliverables' in phase:
            doc_parts.append("**Key Deliverables**:\n")
            for deliverable in phase['deliverables']:
                doc_parts.append(f"- {deliverable['deliverable']} (Due: {deliverable['deadline']})\n")
            doc_parts.append("\n")
        
        if 'key_activities' in phase:
            doc_parts.append("**Privacy-Critical Activities**:\n")
            for activity in phase['key_activities']:
                doc_parts.append(f"- {activity['activity']}\n")
                doc_parts.append(f"  - Controls: {', '.join(activity['privacy_controls'])}\n")
            doc_parts.append("\n")
        
        doc_parts.append("---\n")
    
    # Compliance Monitoring
    doc_parts.append("## Compliance Monitoring and Review\n\n")
    
    monitoring = safeguards_framework['procedural_controls']['monitoring_and_review']
    
    doc_parts.append("### Regular Monitoring Activities\n")
    for activity, description in monitoring.items():
        doc_parts.append(f"**{activity.replace('_', ' ').title()}**: {description}\n")
    doc_parts.append("\n")
    
    # Incident Response
    doc_parts.append("### Incident Response Procedures\n")
    incident_response = safeguards_framework['procedural_controls']['incident_response']
    
    doc_parts.append(f"**Detection**: {incident_response['incident_detection']}\n")
    doc_parts.append(f"**Assessment**: {incident_response['assessment_criteria']}\n")
    doc_parts.append(f"**Notification**: {incident_response['notification_requirements']}\n")
    doc_parts.append(f"**Remediation**: {incident_response['remediation_procedures']}\n\n")
    
    # Conclusion and Next Steps
    doc_parts.append("## Conclusion and Next Steps\n\n")
    doc_parts.append("This comprehensive data privacy framework provides robust protection for all personal data processing ")
    doc_parts.append("in the ACP vs A2A research project. The multi-layered approach combines technical, organizational, ")
    doc_parts.append("and procedural safeguards to ensure GDPR compliance and protect data subject rights.\n\n")
    
    doc_parts.append("**Immediate Actions Required**:\n")
    doc_parts.append("1. Review and approve the DPIA and safeguards framework\n")
    doc_parts.append("2. Implement pre-research technical safeguards\n")
    doc_parts.append("3. Complete staff privacy training\n")
    doc_parts.append("4. Establish DPO and ethics committee contacts\n\n")
    
    doc_parts.append("**Next Steps**: Proceed to Task 6.1.4 (Consider Consent Requirements) to develop detailed consent management procedures for data collection activities.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 6.1.3 (Address Data Privacy) at {datetime.now().isoformat()}\n")
    
    print("🔒 Task 6.1.3: Addressing Data Privacy")
    print("=" * 70)
    
    # Load previous analysis
    previous_analysis = load_previous_analysis()
    if not previous_analysis:
        print("Warning: Could not load complete previous analysis data")
    
    # Identify data types and flows
    data_taxonomy, data_flows = identify_data_types_and_flows(previous_analysis)
    write_log(f"Identified {sum(len(cat['data_types']) for cat in data_taxonomy.values())} data types across {len(data_taxonomy)} categories")
    
    # Conduct DPIA
    dpia = conduct_data_protection_impact_assessment(data_taxonomy, data_flows, previous_analysis)
    write_log("Completed comprehensive Data Protection Impact Assessment")
    
    # Design safeguards framework
    safeguards_framework = design_privacy_safeguards_framework(dpia, data_taxonomy, data_flows)
    write_log("Designed comprehensive privacy safeguards framework")
    
    # Create implementation roadmap
    implementation_roadmap = create_implementation_roadmap(safeguards_framework, data_flows)
    write_log(f"Created implementation roadmap across {len(implementation_roadmap['phase_implementations'])} phases")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "6.1.3 - Address Data Privacy",
            "timestamp": datetime.now().isoformat(),
            "context": "Comprehensive data privacy framework for ACP vs A2A research",
            "input_sources": [
                "6.1.1-ethics-guidelines-review.json",
                "6.1.2-ethical-concerns-analysis.json"
            ]
        },
        "data_taxonomy": data_taxonomy,
        "data_flows": data_flows,
        "dpia": dpia,
        "safeguards_framework": safeguards_framework,
        "implementation_roadmap": implementation_roadmap
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "6.1.3-data-privacy-framework.json"
    try:
        OUTPUT_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save data privacy document
    privacy_doc = generate_data_privacy_document(
        dpia, safeguards_framework, implementation_roadmap, data_taxonomy, data_flows
    )
    
    md_output_path = OUTPUT_DOCS_DIR / "6.1.3-data-privacy-framework.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(privacy_doc)
        write_log(f"Data privacy document saved to {md_output_path}")
        print(f"Data privacy framework saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving privacy document: {e}")
    
    # Summary of findings
    high_risk_processing = sum(
        1 for cat in dpia['risk_assessment'].values()
        for analysis in cat['risk_analyses']
        if analysis['overall_risk_level'] == 'High'
    )
    
    total_data_types = sum(len(cat['data_types']) for cat in data_taxonomy.values())
    
    write_log(f"Finished Task 6.1.3 at {datetime.now().isoformat()}")
    print(f"\n✅ Task 6.1.3 complete")
    print(f"📊 Data types analyzed: {total_data_types}")
    print(f"🔥 High-risk processing activities: {high_risk_processing}")
    print(f"🛡️ Technical safeguards designed: {len(safeguards_framework['technical_safeguards'])}")
    print(f"📋 Implementation phases: {len(implementation_roadmap['phase_implementations'])}")
    print(f"⚖️ DPIA completed with comprehensive risk assessment")

if __name__ == "__main__":
    main() 
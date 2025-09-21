#!/usr/bin/env python3
"""
Task 6.1.4: Consider Consent Requirements

Focus: Detailed analysis of consent requirements for ACP/A2A research data collection
Context: Building on comprehensive data privacy framework to create consent management system

Based on:
- Results from 6.1.3 data privacy framework (DPIA and safeguards)
- Results from 6.1.2 ethical concerns (consent identified as high priority)
- GDPR and research ethics requirements for informed consent
"""

import json
from datetime import datetime
from pathlib import Path

# --- Configuration ---
DATA_PRIVACY_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "6.1.3-data-privacy-framework.json"
ETHICAL_CONCERNS_INPUT_JSON = Path(__file__).resolve().parent.parent / "sources" / "6.1.2-ethical-concerns-analysis.json"
OUTPUT_DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
OUTPUT_SOURCES_DIR = Path(__file__).resolve().parent.parent / "sources"
LOG_FILE = Path(__file__).resolve().parent / "6.1.4_consider_consent_requirements.log"

# --- Logging ---
def write_log(message):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"{datetime.now().isoformat()} - {message}\n")

# --- Load Previous Analysis ---
def load_previous_analysis():
    """Load results from previous ethics and privacy tasks"""
    analysis_data = {}
    
    if DATA_PRIVACY_INPUT_JSON.exists():
        try:
            with open(DATA_PRIVACY_INPUT_JSON, 'r', encoding='utf-8') as f:
                analysis_data['data_privacy'] = json.load(f)
        except Exception as e:
            write_log(f"Error loading data privacy framework: {e}")
    
    if ETHICAL_CONCERNS_INPUT_JSON.exists():
        try:
            with open(ETHICAL_CONCERNS_INPUT_JSON, 'r', encoding='utf-8') as f:
                analysis_data['ethical_concerns'] = json.load(f)
        except Exception as e:
            write_log(f"Error loading ethical concerns analysis: {e}")
    
    return analysis_data

# --- Consent Analysis Functions ---
def analyze_consent_requirements(previous_analysis):
    """Analyze specific consent requirements for different data types and research phases"""
    
    consent_analysis = {
        "gdpr_consent_assessment": {},
        "research_ethics_consent": {},
        "consent_by_data_type": {},
        "consent_by_research_phase": {},
        "special_consent_considerations": {}
    }
    
    # Extract data types from privacy framework
    data_taxonomy = previous_analysis.get('data_privacy', {}).get('data_taxonomy', {})
    
    # GDPR Consent Assessment
    consent_analysis["gdpr_consent_assessment"] = {
        "consent_definition": "GDPR Article 4(11): freely given, specific, informed and unambiguous indication of agreement",
        "consent_criteria": {
            "freely_given": {
                "requirement": "No coercion, conditioning, or significant imbalance",
                "research_application": "Participation in research must be voluntary without academic or economic pressure",
                "implementation": "Clear statement that participation is optional, no academic consequences"
            },
            "specific": {
                "requirement": "Consent for specific processing purposes",
                "research_application": "Separate consent for each research activity and data type",
                "implementation": "Granular consent options for different data collection activities"
            },
            "informed": {
                "requirement": "Clear information about processing before consent",
                "research_application": "Comprehensive information about research purposes, data use, and rights",
                "implementation": "Detailed consent information sheet with plain language explanations"
            },
            "unambiguous": {
                "requirement": "Clear affirmative action indicating agreement",
                "research_application": "Active opt-in mechanisms, no pre-ticked boxes",
                "implementation": "Explicit consent checkboxes and digital signatures"
            }
        },
        "withdrawal_requirements": {
            "ease_of_withdrawal": "Withdrawal must be as easy as giving consent",
            "ongoing_effect": "Withdrawal affects future processing, not lawful past processing",
            "implementation": "One-click withdrawal mechanisms, clear withdrawal procedures"
        }
    }
    
    # Research Ethics Consent
    consent_analysis["research_ethics_consent"] = {
        "informed_consent_elements": {
            "research_purpose": "Clear explanation of research objectives and significance",
            "procedures": "Detailed description of what participation involves",
            "risks_and_benefits": "Comprehensive risk-benefit analysis",
            "confidentiality": "Data protection and anonymization procedures",
            "voluntary_participation": "Right to refuse or withdraw without penalty",
            "contact_information": "Researcher and ethics committee contact details"
        },
        "special_populations": {
            "vulnerable_groups": "Additional protections for elderly, disabled, or economically disadvantaged participants",
            "capacity_assessment": "Procedures to assess decision-making capacity",
            "proxy_consent": "Conditions under which proxy consent may be acceptable"
        }
    }
    
    # Consent by Data Type
    for category_key, category in data_taxonomy.items():
        category_consent = {
            "category": category.get("category", ""),
            "consent_requirements": []
        }
        
        for data_type in category.get("data_types", []):
            consent_requirement = {
                "data_type": data_type.get("type", ""),
                "sensitivity": data_type.get("sensitivity", ""),
                "consent_type": "",
                "consent_specificity": "",
                "special_requirements": []
            }
            
            # Determine consent type based on sensitivity and identifiability
            sensitivity = data_type.get("sensitivity", "Low")
            identifiability = data_type.get("identifiability", "None")
            
            if sensitivity in ["High", "Very High"] or "High" in identifiability:
                consent_requirement["consent_type"] = "Explicit consent required"
                consent_requirement["consent_specificity"] = "Specific consent for each processing purpose"
                consent_requirement["special_requirements"] = [
                    "Enhanced information provision",
                    "Clear explanation of privacy risks",
                    "Granular consent options",
                    "Easy withdrawal mechanisms"
                ]
            elif sensitivity == "Medium":
                consent_requirement["consent_type"] = "Informed consent recommended"
                consent_requirement["consent_specificity"] = "General consent with specific information"
                consent_requirement["special_requirements"] = [
                    "Clear purpose explanation",
                    "Data protection measures described",
                    "Withdrawal options provided"
                ]
            else:
                consent_requirement["consent_type"] = "Information notice sufficient"
                consent_requirement["consent_specificity"] = "General information about processing"
                consent_requirement["special_requirements"] = [
                    "Basic processing information",
                    "Contact details for queries"
                ]
            
            category_consent["consent_requirements"].append(consent_requirement)
        
        consent_analysis["consent_by_data_type"][category_key] = category_consent
    
    return consent_analysis

def design_consent_management_system(consent_analysis, previous_analysis):
    """Design comprehensive consent management system"""
    
    consent_system = {
        "system_overview": {
            "purpose": "Comprehensive consent management for ACP/A2A research",
            "scope": "All research phases requiring data collection",
            "compliance": "GDPR, research ethics, institutional requirements"
        },
        "consent_collection_framework": {},
        "consent_documentation": {},
        "consent_management_procedures": {},
        "technology_implementation": {}
    }
    
    # Consent Collection Framework
    consent_system["consent_collection_framework"] = {
        "multi_tier_consent": {
            "tier_1_basic": {
                "scope": "General research participation",
                "data_covered": "Non-personal technical data, anonymized performance metrics",
                "consent_mechanism": "Online consent form with basic information",
                "withdrawal_method": "Email request to research team"
            },
            "tier_2_standard": {
                "scope": "Device operation data and communication metadata",
                "data_covered": "Quasi-personal data with medium privacy risk",
                "consent_mechanism": "Enhanced consent form with detailed privacy information",
                "withdrawal_method": "Online withdrawal portal with immediate effect"
            },
            "tier_3_sensitive": {
                "scope": "Energy consumption patterns and location data",
                "data_covered": "Personal data with high privacy risk",
                "consent_mechanism": "Explicit consent with granular options",
                "withdrawal_method": "Multiple withdrawal channels with confirmation"
            }
        },
        "phase_specific_consent": {
            "literature_review_phase": {
                "consent_needed": "No new consent - using published data only",
                "information_required": "Notification of research purpose and publication intent"
            },
            "comparative_analysis_phase": {
                "consent_needed": "Tier 2-3 consent for real-world data collection",
                "information_required": "Detailed consent form with protocol comparison explanation"
            },
            "prototype_development_phase": {
                "consent_needed": "Tier 3 explicit consent for live data testing",
                "information_required": "Enhanced consent with prototype testing specifics"
            }
        }
    }
    
    # Consent Documentation
    consent_system["consent_documentation"] = {
        "consent_forms": {
            "basic_consent_form": {
                "target_audience": "General research participants",
                "content_sections": [
                    "Research purpose and significance",
                    "What participation involves",
                    "Data types collected",
                    "Data protection measures",
                    "Participant rights",
                    "Contact information"
                ],
                "length": "1-2 pages",
                "language_level": "8th grade reading level"
            },
            "enhanced_consent_form": {
                "target_audience": "Participants providing sensitive data",
                "content_sections": [
                    "Detailed research explanation",
                    "Comprehensive data inventory",
                    "Privacy risks and protections",
                    "Rights and withdrawal procedures",
                    "Data sharing and retention",
                    "Legal basis and compliance"
                ],
                "length": "3-4 pages",
                "language_level": "Clear, accessible language with technical appendix"
            }
        },
        "information_sheets": {
            "privacy_notice": "Comprehensive GDPR-compliant privacy notice",
            "participant_rights": "Detailed explanation of data subject rights",
            "data_protection_summary": "Plain language explanation of technical safeguards"
        },
        "consent_records": {
            "digital_signatures": "Secure digital signature collection and storage",
            "consent_timestamps": "Detailed logging of consent actions and timestamps",
            "version_control": "Tracking of consent form versions and participant responses"
        }
    }
    
    return consent_system

def create_consent_implementation_plan(consent_system, workflow_context):
    """Create detailed implementation plan for consent management"""
    
    implementation_plan = {
        "implementation_phases": {},
        "technology_requirements": {},
        "compliance_monitoring": {},
        "quality_assurance": {}
    }
    
    # Implementation Phases
    implementation_plan["implementation_phases"] = {
        "phase_1_preparation": {
            "timeline": "Weeks -2 to 0 (Pre-research)",
            "activities": [
                "Develop consent forms and information materials",
                "Set up consent management technology platform",
                "Conduct consent process testing",
                "Train team on consent procedures",
                "Obtain ethics committee approval for consent processes"
            ],
            "deliverables": [
                "Approved consent forms",
                "Functional consent management system",
                "Team training completion certificates",
                "Ethics committee consent approval"
            ]
        },
        "phase_2_literature_review": {
            "timeline": "Weeks 1-6",
            "activities": [
                "Implement information notices for published data use",
                "Monitor compliance with data use terms",
                "Prepare consent materials for next phase"
            ],
            "deliverables": [
                "Published data use compliance report",
                "Consent materials for comparative analysis phase"
            ]
        },
        "phase_3_comparative_analysis": {
            "timeline": "Weeks 7-14",
            "activities": [
                "Deploy Tier 2-3 consent collection",
                "Monitor consent collection and withdrawal rates",
                "Manage ongoing consent compliance",
                "Conduct mid-phase consent audit"
            ],
            "deliverables": [
                "Consent collection reports",
                "Compliance monitoring dashboard",
                "Mid-phase consent audit report"
            ]
        },
        "phase_4_prototype_development": {
            "timeline": "Weeks 15-18",
            "activities": [
                "Deploy enhanced consent for prototype testing",
                "Provide additional consent information for testing",
                "Monitor real-time consent status",
                "Conduct final consent compliance review"
            ],
            "deliverables": [
                "Prototype testing consent documentation",
                "Real-time consent monitoring reports",
                "Final consent compliance assessment"
            ]
        }
    }
    
    # Technology Requirements
    implementation_plan["technology_requirements"] = {
        "consent_platform": {
            "core_features": [
                "Multi-tier consent collection",
                "Digital signature capture",
                "Consent withdrawal processing",
                "Audit trail maintenance",
                "Compliance reporting"
            ],
            "security_requirements": [
                "End-to-end encryption",
                "Secure data storage",
                "Access controls",
                "Backup and recovery"
            ],
            "integration_needs": [
                "Data collection systems",
                "Privacy management tools",
                "Research databases",
                "Reporting platforms"
            ]
        }
    }
    
    return implementation_plan

def generate_consent_requirements_document(consent_analysis, consent_system, implementation_plan):
    """Generate comprehensive consent requirements document"""
    
    doc_parts = []
    
    # Header
    doc_parts.append("# Consent Requirements Analysis (Task 6.1.4)\n")
    doc_parts.append(f"*Generated: {datetime.now().isoformat()}*\n")
    doc_parts.append("*Context: Comprehensive consent management framework for ACP vs A2A research*\n\n")
    
    # Executive Summary
    doc_parts.append("## Executive Summary\n\n")
    doc_parts.append("This document provides a comprehensive analysis of consent requirements for the Agent Communication Protocol research project. ")
    doc_parts.append("Building on the data privacy framework, it establishes a multi-tier consent management system that ensures GDPR compliance ")
    doc_parts.append("and research ethics standards while facilitating efficient data collection across all research phases.\n\n")
    
    # GDPR Consent Requirements
    doc_parts.append("## GDPR Consent Requirements\n\n")
    gdpr_consent = consent_analysis["gdpr_consent_assessment"]
    
    doc_parts.append("### Consent Criteria\n")
    for criterion, details in gdpr_consent["consent_criteria"].items():
        doc_parts.append(f"**{criterion.replace('_', ' ').title()}**\n")
        doc_parts.append(f"- Requirement: {details['requirement']}\n")
        doc_parts.append(f"- Research Application: {details['research_application']}\n")
        doc_parts.append(f"- Implementation: {details['implementation']}\n\n")
    
    # Consent by Data Type
    doc_parts.append("## Consent Requirements by Data Type\n\n")
    
    for category_key, category_data in consent_analysis["consent_by_data_type"].items():
        doc_parts.append(f"### {category_data['category']}\n\n")
        
        for req in category_data["consent_requirements"]:
            doc_parts.append(f"**{req['data_type']}**\n")
            doc_parts.append(f"- Sensitivity: {req['sensitivity']}\n")
            doc_parts.append(f"- Consent Type: {req['consent_type']}\n")
            doc_parts.append(f"- Specificity: {req['consent_specificity']}\n")
            if req['special_requirements']:
                doc_parts.append("- Special Requirements:\n")
                for special_req in req['special_requirements']:
                    doc_parts.append(f"  - {special_req}\n")
            doc_parts.append("\n")
    
    # Multi-Tier Consent Framework
    doc_parts.append("## Multi-Tier Consent Framework\n\n")
    
    multi_tier = consent_system["consent_collection_framework"]["multi_tier_consent"]
    for tier_key, tier_data in multi_tier.items():
        doc_parts.append(f"### {tier_key.replace('_', ' ').title()}\n")
        doc_parts.append(f"**Scope**: {tier_data['scope']}\n")
        doc_parts.append(f"**Data Covered**: {tier_data['data_covered']}\n")
        doc_parts.append(f"**Consent Mechanism**: {tier_data['consent_mechanism']}\n")
        doc_parts.append(f"**Withdrawal Method**: {tier_data['withdrawal_method']}\n\n")
    
    # Phase-Specific Consent
    doc_parts.append("## Phase-Specific Consent Requirements\n\n")
    
    phase_consent = consent_system["consent_collection_framework"]["phase_specific_consent"]
    for phase_key, phase_data in phase_consent.items():
        doc_parts.append(f"### {phase_key.replace('_', ' ').title()}\n")
        doc_parts.append(f"**Consent Needed**: {phase_data['consent_needed']}\n")
        doc_parts.append(f"**Information Required**: {phase_data['information_required']}\n\n")
    
    # Implementation Timeline
    doc_parts.append("## Implementation Timeline\n\n")
    
    for phase_key, phase_data in implementation_plan["implementation_phases"].items():
        doc_parts.append(f"### {phase_key.replace('_', ' ').title()}\n")
        doc_parts.append(f"**Timeline**: {phase_data['timeline']}\n")
        doc_parts.append("**Key Activities**:\n")
        for activity in phase_data['activities']:
            doc_parts.append(f"- {activity}\n")
        doc_parts.append("**Deliverables**:\n")
        for deliverable in phase_data['deliverables']:
            doc_parts.append(f"- {deliverable}\n")
        doc_parts.append("\n")
    
    # Conclusion
    doc_parts.append("## Conclusion and Next Steps\n\n")
    doc_parts.append("This comprehensive consent requirements framework ensures full compliance with GDPR and research ethics standards ")
    doc_parts.append("while enabling efficient data collection for the ACP vs A2A research project. The multi-tier approach provides ")
    doc_parts.append("appropriate consent mechanisms for different data types and research phases.\n\n")
    
    doc_parts.append("**Next Steps**: Proceed to Task 6.1.5 (Document Approval Needs) to identify required institutional and regulatory approvals.\n")
    
    return "".join(doc_parts)

# --- Main Execution ---
def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(f"Starting Task 6.1.4 (Consider Consent Requirements) at {datetime.now().isoformat()}\n")
    
    print("📋 Task 6.1.4: Considering Consent Requirements")
    print("=" * 70)
    
    # Load previous analysis
    previous_analysis = load_previous_analysis()
    if not previous_analysis:
        print("Warning: Could not load complete previous analysis data")
    
    # Analyze consent requirements
    consent_analysis = analyze_consent_requirements(previous_analysis)
    write_log("Completed consent requirements analysis")
    
    # Design consent management system
    consent_system = design_consent_management_system(consent_analysis, previous_analysis)
    write_log("Designed consent management system")
    
    # Create implementation plan
    workflow_context = {}  # Could be loaded from workflow diagrams if needed
    implementation_plan = create_consent_implementation_plan(consent_system, workflow_context)
    write_log("Created consent implementation plan")
    
    # Create comprehensive analysis report
    analysis_report = {
        "metadata": {
            "task": "6.1.4 - Consider Consent Requirements",
            "timestamp": datetime.now().isoformat(),
            "context": "Comprehensive consent management framework for ACP vs A2A research",
            "input_sources": [
                "6.1.3-data-privacy-framework.json",
                "6.1.2-ethical-concerns-analysis.json"
            ]
        },
        "consent_analysis": consent_analysis,
        "consent_system": consent_system,
        "implementation_plan": implementation_plan
    }
    
    # Save JSON output
    json_output_path = OUTPUT_SOURCES_DIR / "6.1.4-consent-requirements-framework.json"
    try:
        OUTPUT_SOURCES_DIR.mkdir(parents=True, exist_ok=True)
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, indent=2, ensure_ascii=False)
        write_log(f"JSON analysis saved to {json_output_path}")
        print(f"JSON output saved to: {json_output_path}")
    except Exception as e:
        write_log(f"Error saving JSON output: {e}")
    
    # Generate and save consent requirements document
    consent_doc = generate_consent_requirements_document(
        consent_analysis, consent_system, implementation_plan
    )
    
    md_output_path = OUTPUT_DOCS_DIR / "6.1.4-consent-requirements-framework.md"
    try:
        OUTPUT_DOCS_DIR.mkdir(parents=True, exist_ok=True)
        with open(md_output_path, 'w', encoding='utf-8') as f:
            f.write(consent_doc)
        write_log(f"Consent requirements document saved to {md_output_path}")
        print(f"Consent requirements framework saved to: {md_output_path}")
    except Exception as e:
        write_log(f"Error saving consent document: {e}")
    
    # Summary of findings
    data_types_analyzed = sum(
        len(cat["consent_requirements"]) 
        for cat in consent_analysis["consent_by_data_type"].values()
    )
    
    consent_tiers = len(consent_system["consent_collection_framework"]["multi_tier_consent"])
    implementation_phases = len(implementation_plan["implementation_phases"])
    
    write_log(f"Finished Task 6.1.4 at {datetime.now().isoformat()}")
    print(f"\n✅ Task 6.1.4 complete")
    print(f"📊 Data types analyzed for consent: {data_types_analyzed}")
    print(f"🔒 Consent tiers designed: {consent_tiers}")
    print(f"📋 Implementation phases: {implementation_phases}")
    print(f"⚖️ GDPR and research ethics compliance framework established")

if __name__ == "__main__":
    main() 
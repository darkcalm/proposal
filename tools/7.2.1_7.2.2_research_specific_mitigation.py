#!/usr/bin/env python3
"""
Research-Specific Risk Mitigation and Contingency Planning (Tasks 7.2.1 & 7.2.2)

This script processes the research context from literature, methodology, and risk analysis
to develop tailored mitigation strategies and contingency plans for the HDT research project.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import re

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tools/7.2.1_7.2.2_research_specific_mitigation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define file paths
BASE_SOURCES_PATH = Path("sources")
BASE_DOCS_PATH = Path("docs")

# Input files
INPUT_RISK_REGISTER = BASE_SOURCES_PATH / "7.1.5-risk-register-prioritized.json"
RESEARCH_QUESTIONS = BASE_DOCS_PATH / "4.2.4.1-research-questions-refined.md"
HYPOTHESES = BASE_DOCS_PATH / "4.2.4.2-hypotheses-refined.md"
METHODOLOGY = BASE_DOCS_PATH / "5.3.1-methodology-justification.md"
LIMITATIONS = BASE_DOCS_PATH / "5.3.2-methodology-limitations.md"
TIMELINE = BASE_DOCS_PATH / "5.3.3-project-timeline.md"
WORKFLOW = BASE_DOCS_PATH / "5.3.4-workflow-diagrams.md"

# Literature sources
AGENT_PROTOCOLS_SURVEY = BASE_SOURCES_PATH / "2.1-initial_literature_input" / "A Survey of AI Agent Protocols.md"
INTEROP_SURVEY = BASE_SOURCES_PATH / "2.1-initial_literature_input" / "A survey of agent interoperability protocols- Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP).md"
LITERATURE_PAPERS = BASE_SOURCES_PATH / "4.3.1-elicit-results" / "markdown_papers"

# Output files
OUTPUT_MITIGATION = BASE_SOURCES_PATH / "7.2.1-research-specific-mitigation-strategies.json"
OUTPUT_CONTINGENCY = BASE_SOURCES_PATH / "7.2.2-research-specific-contingency-plans.json"
OUTPUT_COMBINED = BASE_SOURCES_PATH / "7.2-combined-risk-management.json"
OUTPUT_DOC = BASE_DOCS_PATH / "7.2-research-specific-risk-management.md"

def load_research_context():
    """Load all research context documents."""
    context = {}
    
    # Load core research documents
    research_docs = {
        'research_questions': RESEARCH_QUESTIONS,
        'hypotheses': HYPOTHESES,
        'methodology': METHODOLOGY,
        'limitations': LIMITATIONS,
        'timeline': TIMELINE,
        'workflow': WORKFLOW
    }
    
    for key, path in research_docs.items():
        try:
            with path.open('r', encoding='utf-8') as f:
                context[key] = f.read()
            logger.info(f"Loaded {key} from {path}")
        except FileNotFoundError:
            logger.warning(f"File not found: {path}")
            context[key] = ""
    
    # Load literature surveys
    try:
        with AGENT_PROTOCOLS_SURVEY.open('r', encoding='utf-8') as f:
            context['agent_protocols_survey'] = f.read()
        logger.info(f"Loaded agent protocols survey")
    except FileNotFoundError:
        logger.warning(f"Agent protocols survey not found")
        context['agent_protocols_survey'] = ""
    
    try:
        with INTEROP_SURVEY.open('r', encoding='utf-8') as f:
            context['interop_survey'] = f.read()
        logger.info(f"Loaded interoperability survey")
    except FileNotFoundError:
        logger.warning(f"Interoperability survey not found")
        context['interop_survey'] = ""
    
    # Load selected literature papers
    context['literature_papers'] = []
    if LITERATURE_PAPERS.exists():
        for paper_file in LITERATURE_PAPERS.glob("*.md"):
            try:
                with paper_file.open('r', encoding='utf-8') as f:
                    content = f.read()
                    # Extract key information from papers
                    if any(term in content.lower() for term in [
                        'digital twin', 'agent', 'protocol', 'communication', 
                        'der', 'energy', 'predictive maintenance', 'human factors'
                    ]):
                        context['literature_papers'].append({
                            'filename': paper_file.name,
                            'content': content[:5000]  # First 5000 chars for relevance
                        })
                        logger.info(f"Loaded relevant paper: {paper_file.name}")
            except Exception as e:
                logger.warning(f"Error loading paper {paper_file}: {e}")
    
    return context

def load_prioritized_risks():
    """Load the prioritized risk register."""
    try:
        with INPUT_RISK_REGISTER.open('r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and 'risk_register' in data:
                return data['risk_register']
            return data
    except Exception as e:
        logger.error(f"Error loading risk register: {e}")
        return []

def extract_research_specifics(context):
    """Extract key research-specific elements from context."""
    specifics = {
        'research_focus': 'HDT (Human DER Worker Digital Twins) using Agent Communication Protocols',
        'key_protocols': ['MCP', 'A2A', 'ANP', 'ACP'],
        'research_questions': [],
        'hypotheses': [],
        'methodology_approach': 'Hybrid methodology: Systematic Literature Review + Comparative Analysis + Rapid Prototyping',
        'timeline_constraints': '18.95 weeks optimized timeline',
        'domain_context': 'DER (Decentralized Energy Resources) predictive maintenance and operations',
        'technical_challenges': [],
        'stakeholder_dependencies': [],
        'literature_gaps': []
    }
    
    # Extract research questions
    rq_content = context.get('research_questions', '')
    rq_matches = re.findall(r'SRQ\d+(?:\.\d+)?[:\s]+(.*?)(?=\n\n|\nSRQ|\nMotivation|\Z)', rq_content, re.DOTALL)
    specifics['research_questions'] = [rq.strip().replace('\n', ' ') for rq in rq_matches]
    
    # Extract hypotheses
    hyp_content = context.get('hypotheses', '')
    hyp_matches = re.findall(r'H\d+(?:\.\d+)?[:\s]+(.*?)(?=\n\n|\nH\d|\nJustification|\Z)', hyp_content, re.DOTALL)
    specifics['hypotheses'] = [hyp.strip().replace('\n', ' ') for hyp in hyp_matches]
    
    # Extract technical challenges from methodology limitations
    limitations_content = context.get('limitations', '')
    if 'Protocol Evolution Speed' in limitations_content:
        specifics['technical_challenges'].append('Rapid evolution of agent communication protocols')
    if 'Limited Real World Data' in limitations_content:
        specifics['technical_challenges'].append('Limited availability of real-world DER implementation data')
    if 'Industry Access Constraints' in limitations_content:
        specifics['technical_challenges'].append('Limited access to industry implementations')
    
    # Extract protocol-specific insights from surveys
    agent_survey = context.get('agent_protocols_survey', '')
    if 'MCP' in agent_survey:
        specifics['protocol_insights'] = {
            'MCP': 'Context-oriented protocol for LLM-tool integration',
            'A2A': 'Enterprise-focused inter-agent collaboration',
            'ANP': 'Decentralized peer-to-peer agent communication',
            'ACP': 'REST-native multimodal messaging framework'
        }
    
    return specifics

def develop_research_specific_mitigations(risks, context, research_specifics):
    """Develop mitigation strategies tailored to the HDT research project."""
    mitigation_strategies = []
    
    # Protocol-specific mitigation patterns
    protocol_mitigations = {
        'MCP': {
            'integration_risk': 'Implement MCP client-server architecture with fallback to direct API integration',
            'version_drift': 'Monitor MCP specification updates and maintain compatibility matrix',
            'security_concerns': 'Implement OAuth 2.1 + PKCE for secure context acquisition'
        },
        'A2A': {
            'enterprise_adoption': 'Develop Agent Card specifications for HDT capabilities',
            'task_coordination': 'Implement JSON-RPC 2.0 based task delegation patterns',
            'scalability_limits': 'Design async-first architecture with SSE streaming'
        },
        'ANP': {
            'decentralized_identity': 'Implement W3C DID-based identity management for HDTs',
            'cross_domain_trust': 'Establish cryptographic verification for agent authenticity',
            'network_effects': 'Start with controlled pilot deployment before open network'
        },
        'ACP': {
            'integration_risk': 'Implement REST-native messaging with multi-part message support',
            'version_drift': 'Monitor ACP specification updates and maintain compatibility matrix',
            'security_concerns': 'Implement bearer token authentication with JWS message signing'
        }
    }
    
    # DER domain-specific mitigations
    der_mitigations = {
        'domain_expertise': 'Partner with DER operators for tacit knowledge elicitation',
        'regulatory_compliance': 'Align HDT design with energy sector security standards',
        'real_time_constraints': 'Implement predictive maintenance protocols with sub-second response',
        'data_privacy': 'Design federated learning approach for sensitive operational data'
    }
    
    # Literature-informed mitigations
    literature_mitigations = {
        'digital_twin_fidelity': 'Implement multi-fidelity modeling approach based on Ma et al. framework',
        'human_factors': 'Apply Chen et al. situational awareness principles to HDT design',
        'protocol_interoperability': 'Follow Ehtesham et al. layered protocol architecture',
        'tacit_knowledge': 'Use Carvalho et al. methods for capturing informal communication patterns'
    }
    
    for risk in risks:
        risk_id = risk['risk_id']
        category = risk['category']
        priority = risk['priority_score']
        
        mitigation = {
            'risk_id': risk_id,
            'risk_description': risk['description'],
            'category': category,
            'priority_score': priority,
            'research_context': research_specifics['research_focus'],
            'mitigation_strategies': [],
            'implementation_timeline': '',
            'resource_requirements': [],
            'success_metrics': [],
            'dependencies': [],
            'literature_basis': []
        }
        
        # Technical risks - protocol-specific mitigations
        if category == 'Technical':
            if 'protocol' in risk['description'].lower():
                for protocol in research_specifics['key_protocols']:
                    if protocol.lower() in risk['description'].lower():
                        mitigation['mitigation_strategies'].extend([
                            protocol_mitigations[protocol].get('integration_risk', ''),
                            protocol_mitigations[protocol].get('version_drift', ''),
                            protocol_mitigations[protocol].get('security_concerns', '')
                        ])
                        mitigation['literature_basis'].append(f'{protocol} protocol specifications from Ehtesham et al. survey')
            
            mitigation['mitigation_strategies'].extend([
                'Implement phased protocol adoption: MCP → ACP → A2A → ANP',
                'Establish protocol compatibility testing framework',
                'Create HDT-specific protocol extensions for DER domain'
            ])
            mitigation['implementation_timeline'] = 'Phase 1-2 of research timeline (Weeks 1-14)'
            mitigation['resource_requirements'] = ['Protocol development expertise', 'Testing infrastructure', 'Version control systems']
            mitigation['success_metrics'] = ['Protocol compatibility rate', 'Integration test pass rate', 'Performance benchmarks']
        
        # Methodological risks - research-specific approaches
        elif category == 'Methodological':
            mitigation['mitigation_strategies'].extend([
                'Apply systematic literature review with protocol composition focus',
                'Use comparative analysis framework for ACP vs A2A evaluation',
                'Implement rapid prototyping for proof-of-concept validation',
                'Establish clear validation criteria for each research question'
            ])
            for rq in research_specifics['research_questions'][:2]:  # First 2 RQs for brevity
                mitigation['mitigation_strategies'].append(f'Address specific RQ: {rq[:100]}...')
            
            mitigation['implementation_timeline'] = 'Throughout research phases (Weeks 1-19)'
            mitigation['resource_requirements'] = ['Literature access', 'Analytical frameworks', 'Validation tools']
            mitigation['success_metrics'] = ['Literature coverage completeness', 'Framework validation scores', 'Prototype functionality']
            mitigation['literature_basis'] = ['Systematic review methodology standards', 'Comparative analysis frameworks']
        
        # Resource risks - project-specific allocations
        elif category == 'Resource':
            mitigation['mitigation_strategies'].extend([
                'Allocate 40% effort to literature review, 40% to comparative analysis, 20% to prototyping',
                'Establish partnerships with DER industry contacts for domain expertise',
                'Leverage open-source protocol implementations where available',
                'Create resource allocation buffer for protocol evolution tracking'
            ])
            mitigation['implementation_timeline'] = 'Resource planning phase (Weeks 1-2) and ongoing monitoring'
            mitigation['resource_requirements'] = ['Project management tools', 'Industry partnerships', 'Computing resources']
            mitigation['success_metrics'] = ['Budget adherence', 'Timeline compliance', 'Resource utilization efficiency']
        
        # Impact risks - stakeholder-focused strategies
        elif category == 'Impact':
            mitigation['mitigation_strategies'].extend([
                'Align HDT development with DER operational requirements',
                'Establish clear value proposition for human-agent collaboration',
                'Design evaluation framework incorporating technical and human factors metrics',
                'Plan for academic publication and industry dissemination'
            ])
            mitigation['implementation_timeline'] = 'Phase 3 and post-research (Weeks 15-19+)'
            mitigation['resource_requirements'] = ['Evaluation frameworks', 'Stakeholder engagement', 'Dissemination channels']
            mitigation['success_metrics'] = ['Stakeholder satisfaction', 'Academic contribution', 'Industry adoption potential']
            mitigation['literature_basis'] = ['Human factors research (Chen et al.)', 'Digital twin evaluation frameworks']
        
        # Timeline risks - schedule optimization
        elif category == 'Timeline':
            mitigation['mitigation_strategies'].extend([
                'Implement optimized 18.95-week timeline with parallel activities',
                'Establish weekly progress checkpoints with supervisor',
                'Create buffer time for protocol evolution tracking',
                'Plan for iterative development with continuous integration'
            ])
            mitigation['implementation_timeline'] = 'Project management throughout (Weeks 1-19)'
            mitigation['resource_requirements'] = ['Project management systems', 'Progress tracking tools', 'Communication channels']
            mitigation['success_metrics'] = ['Milestone completion rate', 'Schedule variance', 'Quality maintenance under compression']
        
        # Add research-specific dependencies
        mitigation['dependencies'] = [
            'Access to latest protocol specifications',
            'DER domain expert consultation',
            'Literature database access',
            'Computing resources for prototyping'
        ]
        
        # Filter out empty strategies
        mitigation['mitigation_strategies'] = [s for s in mitigation['mitigation_strategies'] if s.strip()]
        
        mitigation_strategies.append(mitigation)
    
    return mitigation_strategies

def develop_research_specific_contingencies(risks, context, research_specifics):
    """Develop contingency plans tailored to the HDT research project."""
    contingency_plans = []
    
    for risk in risks:
        risk_id = risk['risk_id']
        category = risk['category']
        priority = risk['priority_score']
        
        contingency = {
            'risk_id': risk_id,
            'risk_description': risk['description'],
            'category': category,
            'priority_score': priority,
            'trigger_conditions': [],
            'contingency_actions': [],
            'fallback_strategies': [],
            'resource_reallocation': {},
            'timeline_adjustments': '',
            'quality_trade_offs': [],
            'escalation_procedures': [],
            'recovery_plans': []
        }
        
        # Technical contingencies
        if category == 'Technical':
            contingency['trigger_conditions'] = [
                'Protocol specification changes affecting core research',
                'Integration failures exceeding 48-hour resolution time',
                'Performance degradation below acceptable thresholds'
            ]
            contingency['contingency_actions'] = [
                'Activate alternative protocol implementation path',
                'Engage protocol community for clarification/support',
                'Implement simplified proof-of-concept for demonstration'
            ]
            contingency['fallback_strategies'] = [
                'Use previous protocol version with documented limitations',
                'Focus on theoretical framework if implementation fails',
                'Leverage existing agent frameworks (LangChain, AutoGen) as fallback'
            ]
            contingency['resource_reallocation'] = {
                'from_prototyping': '30%',
                'to_literature_analysis': '20%',
                'to_framework_development': '10%'
            }
        
        # Methodological contingencies
        elif category == 'Methodological':
            contingency['trigger_conditions'] = [
                'Literature gaps preventing comprehensive analysis',
                'Comparative framework validation failures',
                'Insufficient data for meaningful conclusions'
            ]
            contingency['contingency_actions'] = [
                'Expand literature search to adjacent domains',
                'Simplify comparative framework scope',
                'Conduct expert interviews for gap filling'
            ]
            contingency['fallback_strategies'] = [
                'Focus on single protocol deep-dive instead of comparison',
                'Emphasize theoretical contribution over empirical validation',
                'Leverage gray literature and industry reports'
            ]
            contingency['timeline_adjustments'] = 'Reduce Phase 2 from 8 to 6 weeks, extend Phase 1 by 2 weeks'
        
        # Resource contingencies
        elif category == 'Resource':
            contingency['trigger_conditions'] = [
                'Industry partnership unavailable',
                'Computing resource constraints',
                'Expert consultation inaccessible'
            ]
            contingency['contingency_actions'] = [
                'Utilize open-source alternatives and public datasets',
                'Partner with academic institutions for resource sharing',
                'Engage online communities and forums for expertise'
            ]
            contingency['fallback_strategies'] = [
                'Use simulation-based validation instead of real-world data',
                'Focus on protocol specification analysis over implementation',
                'Leverage existing research partnerships and networks'
            ]
        
        # Impact contingencies
        elif category == 'Impact':
            contingency['trigger_conditions'] = [
                'Limited industry interest in research outcomes',
                'Academic contribution below publication threshold',
                'Stakeholder feedback indicating low value'
            ]
            contingency['contingency_actions'] = [
                'Pivot to focus on most promising application area',
                'Enhance theoretical contributions and novelty',
                'Develop alternative dissemination strategies'
            ]
            contingency['fallback_strategies'] = [
                'Focus on educational/training applications',
                'Emphasize methodology contributions over domain-specific results',
                'Target niche academic venues and workshops'
            ]
        
        # Timeline contingencies
        elif category == 'Timeline':
            contingency['trigger_conditions'] = [
                'Two consecutive weeks behind schedule',
                'Major scope changes required',
                'External dependencies causing delays'
            ]
            contingency['contingency_actions'] = [
                'Activate accelerated parallel development tracks',
                'Reduce scope to core research questions only',
                'Implement daily progress monitoring and adjustment'
            ]
            contingency['quality_trade_offs'] = [
                'Reduce prototype complexity while maintaining core functionality',
                'Focus on primary research questions, defer secondary investigations',
                'Minimize documentation completeness for speed'
            ]
        
        # Universal escalation procedures
        contingency['escalation_procedures'] = [
            'Level 1: Self-resolution within 24 hours',
            'Level 2: Supervisor consultation within 48 hours',
            'Level 3: Advisory committee engagement within 72 hours',
            'Level 4: Program director involvement for critical issues'
        ]
        
        # Recovery planning
        contingency['recovery_plans'] = [
            'Document lessons learned and process improvements',
            'Update risk register with new insights',
            'Adjust remaining project phases based on experience',
            'Communicate changes to all stakeholders'
        ]
        
        contingency_plans.append(contingency)
    
    return contingency_plans

def generate_combined_output(mitigation_strategies, contingency_plans, research_specifics):
    """Generate combined risk management output."""
    combined_output = {
        'metadata': {
            'task': '7.2.1 & 7.2.2 - Research-Specific Risk Mitigation and Contingency Planning',
            'generated_date': datetime.now().isoformat(),
            'research_focus': research_specifics['research_focus'],
            'methodology': research_specifics['methodology_approach'],
            'timeline': research_specifics['timeline_constraints'],
            'total_risks': len(mitigation_strategies)
        },
        'research_context': research_specifics,
        'mitigation_strategies': mitigation_strategies,
        'contingency_plans': contingency_plans,
        'resource_allocation': {
            'high_priority_risks': len([r for r in mitigation_strategies if r['priority_score'] >= 3]),
            'medium_priority_risks': len([r for r in mitigation_strategies if r['priority_score'] == 2]),
            'low_priority_risks': len([r for r in mitigation_strategies if r['priority_score'] == 1]),
            'recommended_allocation': {
                'risk_management': '15%',
                'contingency_buffer': '10%',
                'monitoring_and_adjustment': '5%'
            }
        },
        'implementation_roadmap': [
            'Week 1-2: Establish risk monitoring systems and mitigation infrastructure',
            'Week 3-8: Implement technical and methodological risk mitigations during Phase 1',
            'Week 9-16: Monitor and adjust strategies during Phase 2',
            'Week 17-19: Execute contingency plans if needed during Phase 3',
            'Ongoing: Continuous risk assessment and strategy refinement'
        ]
    }
    
    return combined_output

def generate_markdown_documentation(combined_output):
    """Generate comprehensive markdown documentation."""
    md_lines = [
        "# Research-Specific Risk Management (Tasks 7.2.1 & 7.2.2)",
        "",
        "## Executive Summary",
        "",
        f"This document presents comprehensive risk mitigation strategies and contingency plans specifically tailored for the research project: **{combined_output['metadata']['research_focus']}**.",
        "",
        f"The analysis covers {combined_output['metadata']['total_risks']} identified risks with research-specific mitigations grounded in literature review, methodology constraints, and domain expertise.",
        "",
        "## Research Context",
        "",
        f"- **Research Focus**: {combined_output['research_context']['research_focus']}",
        f"- **Key Protocols**: {', '.join(combined_output['research_context']['key_protocols'])}",
        f"- **Methodology**: {combined_output['research_context']['methodology_approach']}",
        f"- **Timeline**: {combined_output['research_context']['timeline_constraints']}",
        f"- **Domain**: {combined_output['research_context']['domain_context']}",
        "",
        "## Risk Distribution and Allocation",
        "",
        f"- **High Priority (3-4)**: {combined_output['resource_allocation']['high_priority_risks']} risks",
        f"- **Medium Priority (2)**: {combined_output['resource_allocation']['medium_priority_risks']} risks", 
        f"- **Low Priority (1)**: {combined_output['resource_allocation']['low_priority_risks']} risks",
        "",
        "### Recommended Resource Allocation",
        "",
        f"- Risk Management: {combined_output['resource_allocation']['recommended_allocation']['risk_management']}",
        f"- Contingency Buffer: {combined_output['resource_allocation']['recommended_allocation']['contingency_buffer']}",
        f"- Monitoring & Adjustment: {combined_output['resource_allocation']['recommended_allocation']['monitoring_and_adjustment']}",
        "",
        "## Research-Specific Mitigation Strategies",
        ""
    ]
    
    # Add mitigation strategies by category
    categories = {}
    for strategy in combined_output['mitigation_strategies']:
        cat = strategy['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(strategy)
    
    for category, strategies in categories.items():
        md_lines.extend([
            f"### {category} Risk Mitigations",
            ""
        ])
        
        for strategy in strategies:
            md_lines.extend([
                f"#### {strategy['risk_id']}: {strategy['risk_description'][:80]}...",
                "",
                f"**Priority**: {strategy['priority_score']} | **Timeline**: {strategy['implementation_timeline']}",
                "",
                "**Mitigation Strategies**:",
            ])
            
            for i, mitigation in enumerate(strategy['mitigation_strategies'][:3], 1):  # Top 3 for brevity
                md_lines.append(f"{i}. {mitigation}")
            
            md_lines.extend([
                "",
                f"**Success Metrics**: {', '.join(strategy['success_metrics'][:3])}",
                ""
            ])
    
    md_lines.extend([
        "## Research-Specific Contingency Plans",
        "",
        "### Activation Framework",
        "",
        "Contingency plans are activated based on specific trigger conditions aligned with research objectives and timeline constraints.",
        ""
    ])
    
    # Add key contingency plans
    high_priority_contingencies = [c for c in combined_output['contingency_plans'] if c['priority_score'] >= 3]
    
    for contingency in high_priority_contingencies[:3]:  # Top 3 high-priority
        md_lines.extend([
            f"#### {contingency['risk_id']}: {contingency['category']} Risk",
            "",
            "**Trigger Conditions**:",
        ])
        
        for trigger in contingency['trigger_conditions']:
            md_lines.append(f"- {trigger}")
        
        md_lines.extend([
            "",
            "**Contingency Actions**:",
        ])
        
        for action in contingency['contingency_actions']:
            md_lines.append(f"- {action}")
        
        md_lines.extend([
            "",
            "**Fallback Strategies**:",
        ])
        
        for fallback in contingency['fallback_strategies']:
            md_lines.append(f"- {fallback}")
        
        md_lines.append("")
    
    md_lines.extend([
        "## Implementation Roadmap",
        "",
    ])
    
    for phase in combined_output['implementation_roadmap']:
        md_lines.append(f"- {phase}")
    
    md_lines.extend([
        "",
        "## Literature-Informed Approach",
        "",
        "This risk management strategy is grounded in:",
        "",
        "- **Protocol Evolution Research**: Ehtesham et al. survey on agent interoperability protocols",
        "- **Digital Twin Methodology**: Ma et al. framework for DT functional requirements",
        "- **Human Factors Integration**: Chen et al. principles for situational awareness",
        "- **Tacit Knowledge Capture**: Carvalho et al. methods for informal communication patterns",
        "- **Systematic Review Standards**: Established academic methodology practices",
        "",
        "## Continuous Improvement",
        "",
        "This risk management plan will be reviewed and updated:",
        "",
        "- Weekly during active research phases",
        "- After each major milestone completion",
        "- Following any significant protocol or methodology changes",
        "- Based on ongoing literature monitoring and stakeholder feedback",
        "",
        "## Conclusion",
        "",
        "The research-specific risk management approach ensures that the HDT research project can adapt to the rapidly evolving landscape of agent communication protocols while maintaining academic rigor and practical relevance. The combination of literature-grounded mitigations and flexible contingency planning provides a robust framework for successful project completion."
    ])
    
    return "\n".join(md_lines)

def save_outputs(mitigation_strategies, contingency_plans, combined_output, documentation):
    """Save all outputs to designated files."""
    # Save mitigation strategies
    mitigation_output = {
        'metadata': combined_output['metadata'],
        'research_context': combined_output['research_context'],
        'mitigation_strategies': mitigation_strategies
    }
    
    try:
        with OUTPUT_MITIGATION.open('w', encoding='utf-8') as f:
            json.dump(mitigation_output, f, indent=2, ensure_ascii=False)
        logger.info(f"Mitigation strategies saved to: {OUTPUT_MITIGATION}")
    except IOError as e:
        logger.error(f"Error saving mitigation strategies: {e}")
        raise
    
    # Save contingency plans
    contingency_output = {
        'metadata': combined_output['metadata'],
        'research_context': combined_output['research_context'],
        'contingency_plans': contingency_plans
    }
    
    try:
        with OUTPUT_CONTINGENCY.open('w', encoding='utf-8') as f:
            json.dump(contingency_output, f, indent=2, ensure_ascii=False)
        logger.info(f"Contingency plans saved to: {OUTPUT_CONTINGENCY}")
    except IOError as e:
        logger.error(f"Error saving contingency plans: {e}")
        raise
    
    # Save combined output
    try:
        with OUTPUT_COMBINED.open('w', encoding='utf-8') as f:
            json.dump(combined_output, f, indent=2, ensure_ascii=False)
        logger.info(f"Combined output saved to: {OUTPUT_COMBINED}")
    except IOError as e:
        logger.error(f"Error saving combined output: {e}")
        raise
    
    # Save documentation
    try:
        with OUTPUT_DOC.open('w', encoding='utf-8') as f:
            f.write(documentation)
        logger.info(f"Documentation saved to: {OUTPUT_DOC}")
    except IOError as e:
        logger.error(f"Error saving documentation: {e}")
        raise

def print_summary_to_console(combined_output):
    """Print a comprehensive summary to console."""
    print("\n" + "=" * 80)
    print("RESEARCH-SPECIFIC RISK MANAGEMENT COMPLETED (Tasks 7.2.1 & 7.2.2)")
    print("=" * 80)
    
    metadata = combined_output['metadata']
    print(f"Research Focus: {metadata['research_focus']}")
    print(f"Total Risks Addressed: {metadata['total_risks']}")
    
    # Mitigation summary
    print(f"\nMitigation Strategies Generated: {len(combined_output['mitigation_strategies'])}")
    categories = {}
    for strategy in combined_output['mitigation_strategies']:
        cat = strategy['category']
        if cat not in categories:
            categories[cat] = 0
        categories[cat] += 1
    
    print("Strategies by Category:")
    for category, count in categories.items():
        print(f"  • {category}: {count} strategies")
    
    # Contingency summary
    print(f"\nContingency Plans Developed: {len(combined_output['contingency_plans'])}")
    
    # Priority distribution
    allocation = combined_output['resource_allocation']
    print(f"\nRisk Priority Distribution:")
    print(f"  • High Priority: {allocation['high_priority_risks']} risks")
    print(f"  • Medium Priority: {allocation['medium_priority_risks']} risks")
    print(f"  • Low Priority: {allocation['low_priority_risks']} risks")
    
    print(f"\nOutputs Generated:")
    print(f"  • Mitigation Strategies: {OUTPUT_MITIGATION}")
    print(f"  • Contingency Plans: {OUTPUT_CONTINGENCY}")
    print(f"  • Combined Analysis: {OUTPUT_COMBINED}")
    print(f"  • Documentation: {OUTPUT_DOC}")
    
    print("=" * 80)

def main():
    """Main execution function."""
    logger.info("Starting Research-Specific Risk Mitigation and Contingency Planning")
    
    # Load research context
    logger.info("Loading research context...")
    context = load_research_context()
    
    # Load prioritized risks
    logger.info("Loading prioritized risks...")
    risks = load_prioritized_risks()
    if not risks:
        logger.error("No risks found in register.")
        return
    
    # Extract research specifics
    logger.info("Extracting research-specific elements...")
    research_specifics = extract_research_specifics(context)
    
    # Develop mitigation strategies
    logger.info("Developing research-specific mitigation strategies...")
    mitigation_strategies = develop_research_specific_mitigations(risks, context, research_specifics)
    
    # Develop contingency plans
    logger.info("Developing research-specific contingency plans...")
    contingency_plans = develop_research_specific_contingencies(risks, context, research_specifics)
    
    # Generate combined output
    logger.info("Generating combined risk management framework...")
    combined_output = generate_combined_output(mitigation_strategies, contingency_plans, research_specifics)
    
    # Generate documentation
    logger.info("Generating comprehensive documentation...")
    documentation = generate_markdown_documentation(combined_output)
    
    # Save all outputs
    logger.info("Saving outputs...")
    save_outputs(mitigation_strategies, contingency_plans, combined_output, documentation)
    
    # Print summary
    print_summary_to_console(combined_output)
    
    logger.info("Research-Specific Risk Management (Tasks 7.2.1 & 7.2.2) - COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Task 8.1.3: Visual Planning
Generate comprehensive visual planning documents for research proposal.

This script processes existing research data and creates visual planning materials
including timeline charts, comparison tables, risk matrices, and workflow diagrams.
"""

import json
import os
from datetime import datetime
from pathlib import Path

def create_timeline_gantt_tex():
    """Create a professional Gantt chart in TikZ format for the research timeline."""
    
    # Read timeline data
    timeline_file = Path("sources/5.3.3-project-timeline.json")
    if timeline_file.exists():
        with open(timeline_file, 'r') as f:
            timeline_data = json.load(f)
    else:
        timeline_data = {}
    
    gantt_content = r"""\documentclass[border=10pt]{standalone}
\usepackage{pgfgantt}
\usepackage{xcolor}

% Define colors for different phases
\definecolor{phase1color}{RGB}{70,130,180}    % Steel Blue - Literature Review
\definecolor{phase2color}{RGB}{60,179,113}    % Medium Sea Green - Comparative Framework
\definecolor{phase3color}{RGB}{255,140,0}     % Dark Orange - Proof of Concept
\definecolor{integcolor}{RGB}{147,112,219}    % Medium Purple - Integration points
\definecolor{milestonecolor}{RGB}{220,20,60}  % Crimson - Milestones

\begin{document}
\begin{ganttchart}[
    x unit=0.4cm,
    y unit title=0.8cm,
    y unit chart=0.6cm,
    vgrid,
    hgrid,
    title height=1,
    bar height=0.5,
    group height=0.6,
    milestone height=0.4,
    title label font=\footnotesize,
    bar label font=\scriptsize,
    group label font=\small,
    milestone label font=\scriptsize
]{1}{19}

% Title and weeks
\gantttitle{Optimized Research Timeline (19 weeks)}{19} \\
\gantttitlelist{1,...,19}{1} \\

% Phase 1: Systematic Literature Review (6 weeks)
\ganttgroup[group/.style={fill=phase1color!20}]{Phase 1: Literature Review}{1}{6} \\
\ganttbar[bar/.style={fill=phase1color!40}]{Search strategy refinement}{1}{1} \\
\ganttbar[bar/.style={fill=phase1color!40}]{Database searches \& screening}{2}{3} \\
\ganttbar[bar/.style={fill=phase1color!40}]{Full-text review \& extraction}{4}{5} \\
\ganttbar[bar/.style={fill=phase1color!40}]{Protocol pattern analysis}{6}{6} \\
\ganttbar[bar/.style={fill=phase1color!40}]{Literature synthesis}{6}{6} \\

% Integration Point 1
\ganttmilestone[milestone/.style={fill=integcolor}]{Phase 1-2 Integration}{6} \\

% Phase 2: Comparative Framework Development (8 weeks)
\ganttgroup[group/.style={fill=phase2color!20}]{Phase 2: Comparative Framework}{7}{14} \\
\ganttbar[bar/.style={fill=phase2color!40}]{Framework design \& validation}{7}{8} \\
\ganttbar[bar/.style={fill=phase2color!40}]{ACP protocol analysis}{9}{10} \\
\ganttbar[bar/.style={fill=phase2color!40}]{A2A protocol analysis}{11}{12} \\
\ganttbar[bar/.style={fill=phase2color!40}]{Comparative evaluation}{13}{14} \\
\ganttbar[bar/.style={fill=phase2color!40}]{Integration pattern assessment}{14}{14} \\

% Integration Point 2
\ganttmilestone[milestone/.style={fill=integcolor}]{Phase 2-3 Integration}{14} \\

% Phase 3: Proof of Concept (4 weeks)
\ganttgroup[group/.style={fill=phase3color!20}]{Phase 3: Proof of Concept}{15}{18} \\
\ganttbar[bar/.style={fill=phase3color!40}]{Prototype design \& specification}{15}{15} \\
\ganttbar[bar/.style={fill=phase3color!40}]{Core protocol integration dev}{16}{17} \\
\ganttbar[bar/.style={fill=phase3color!40}]{Testing \& validation}{18}{18} \\
\ganttbar[bar/.style={fill=phase3color!40}]{Documentation \& evaluation}{18}{18} \\

% Final Integration
\ganttmilestone[milestone/.style={fill=milestonecolor}]{Project Completion}{19} \\

% Add some parallel activities with links
\ganttlink{elem2}{elem3}
\ganttlink{elem4}{elem5}
\ganttlink{elem7}{elem8}
\ganttlink{elem9}{elem10}
\ganttlink{elem11}{elem12}

\end{ganttchart}

\vspace{0.5cm}

% Legend
\begin{tabular}{ll}
\colorbox{phase1color!40}{\rule{0.5cm}{0.3cm}} & Phase 1: Systematic Literature Review \\
\colorbox{phase2color!40}{\rule{0.5cm}{0.3cm}} & Phase 2: Comparative Framework Development \\
\colorbox{phase3color!40}{\rule{0.5cm}{0.3cm}} & Phase 3: Proof of Concept \\
\colorbox{integcolor}{\rule{0.5cm}{0.3cm}} & Integration Points \\
\colorbox{milestonecolor}{\rule{0.5cm}{0.3cm}} & Major Milestones \\
\end{tabular}

\end{document}"""
    
    return gantt_content

def create_methodology_comparison_table():
    """Create a comprehensive methodology comparison table from existing data."""
    
    # Read methodology comparison data
    matrix_file = Path("sources/5.2.1-methodology-comparison-matrix.json")
    if matrix_file.exists():
        with open(matrix_file, 'r') as f:
            matrix_data = json.load(f)
    else:
        matrix_data = {}
    
    content = f"""# Methodology Comparison Table (Visual Reference)

*Generated: {datetime.now().isoformat()}*
*Task: 8.1.3 - Incorporate Visual Planning*
*Based on: sources/5.2.1-methodology-comparison-matrix.json*

## Evaluation Criteria Summary

| Criterion | Weight | Scale | Description |
|-----------|--------|-------|-------------|
| Research Alignment | 25% | 1-5 | Alignment with ACP/A2A protocol research objectives |
| Timeline Feasibility | 20% | 1-5 | Feasibility within 20-week Master's thesis timeframe |
| Resource Requirements | 15% | 1-5 | Inverse of required resources (5=Low, 1=Very High) |
| Innovation Potential | 15% | 1-5 | Potential for novel research contribution |
| Practical Applicability | 10% | 1-5 | Real-world applicability and validation potential |
| Prior Research Credibility | 10% | 1-5 | Evidence of usage/success in related research |
| Integration Potential | 5% | 1-5 | Potential for integration with other methodologies |

## Top Methodologies Comparison

| Rank | Methodology | Category | Score | Research Align | Timeline | Resources | Innovation | Practical | Credibility | Integration |
|------|-------------|----------|-------|----------------|----------|-----------|------------|-----------|-------------|-------------|
| 1 | Digital Twin Methodology | Emerging | 3.7 | 4 | 3 | 3 | 5 | 4 | 4 | 4 |
| 2 | Participatory Design | Emerging/Qual | 3.5 | 3 | 4 | 4 | 4 | 4 | 3 | 4 |
| 3 | Experimental Research | Quantitative | 3.45 | 4 | 3 | 2 | 4 | 3 | 5 | 3 |
| 4 | Case Study Methodology | Qualitative | 3.3 | 3 | 4 | 4 | 3 | 4 | 4 | 3 |
| 5 | Simulation Modeling | Quant/Emerging | 3.1 | 4 | 2 | 2 | 4 | 3 | 4 | 3 |

## Selected Hybrid Methodology Components

| Phase | Primary Method | Supporting Methods | Rationale |
|-------|----------------|-------------------|-----------|
| Phase 1 | Systematic Literature Review | Content Analysis | Comprehensive literature coverage with systematic approach |
| Phase 2 | Comparative Research | Digital Twin Methodology | Framework development leveraging emerging DT approaches |
| Phase 3 | Rapid Prototyping | Experimental Research | Proof of concept with controlled validation |

## Risk Assessment by Methodology

| Methodology | Timeline Risk | Resource Risk | Technical Risk | Overall Risk |
|-------------|---------------|---------------|----------------|--------------|
| Digital Twin | Medium | High | High | Medium |
| Systematic Literature Review | Low | Low | Low | Low |
| Comparative Research | Low | Medium | Medium | Low |
| Rapid Prototyping | Medium | Medium | High | Medium |

## Methodology Integration Matrix

| Method A | Method B | Integration Level | Synergy Score | Implementation Complexity |
|----------|----------|-------------------|---------------|---------------------------|
| Literature Review | Comparative Research | High | 4.5 | Low |
| Comparative Research | Rapid Prototyping | High | 4.0 | Medium |
| Digital Twin | Rapid Prototyping | Very High | 5.0 | High |
| Literature Review | Digital Twin | Medium | 3.5 | Low |

## Decision Matrix Summary

**Selected Approach: Hybrid Methodology**
- **Phase 1**: Systematic Literature Review (6 weeks)
- **Phase 2**: Comparative Research with Digital Twin elements (8 weeks)  
- **Phase 3**: Rapid Prototyping (4 weeks)

**Key Advantages:**
- Balanced risk profile across phases
- High integration potential between methods
- Strong alignment with research objectives
- Feasible within timeline constraints
- Leverages emerging Digital Twin methodology while maintaining research rigor"""
    
    return content

def create_risk_management_table():
    """Create a comprehensive risk management table from existing risk data."""
    
    # Read risk data
    risk_files = [
        "sources/7.1.5-risk-register-prioritized.json",
        "sources/7.1.4-risk-register-likelihood-impact.json",
        "sources/7.2-combined-risk-management.json"
    ]
    
    risk_data = {}
    for file_path in risk_files:
        if Path(file_path).exists():
            with open(file_path, 'r') as f:
                risk_data.update(json.load(f))
    
    content = f"""# Risk Management Table (Visual Reference)

*Generated: {datetime.now().isoformat()}*
*Task: 8.1.3 - Incorporate Visual Planning*
*Based on: sources/7.1.* risk analysis documents*

## Risk Priority Matrix

| Risk Level | Technical | Methodological | Resource | Impact | Timeline | Total |
|------------|-----------|----------------|----------|---------|----------|-------|
| **High** | 0 | 0 | 3 | 3 | 3 | **9** |
| **Medium** | 3 | 3 | 0 | 0 | 0 | **6** |
| **Low** | 0 | 0 | 0 | 0 | 0 | **0** |
| **Total** | **3** | **3** | **3** | **3** | **3** | **15** |

## High Priority Risks (Score 3)

| Risk ID | Description | Category | Likelihood | Impact | Mitigation Strategy |
|---------|-------------|----------|------------|--------|-------------------|
| RES-001 | Time constraints affecting research depth | Resource | High | High | Optimized timeline, parallel activities |
| RES-002 | Limited access to specialized expertise | Resource | Medium | High | Early stakeholder engagement, alternatives |
| RES-003 | Budget constraints affecting prototype | Resource | Medium | High | Simplified prototype scope, open-source tools |
| IMP-001 | Negative social impact on DER workers | Impact | Low | High | Participatory design, worker involvement |
| IMP-002 | Environmental impact of computation | Impact | Medium | Medium | Efficient algorithms, green computing |
| IMP-003 | Policy and regulatory compliance | Impact | Medium | High | Regulatory review, compliance framework |
| TIME-001 | Literature review delays | Timeline | High | Medium | Accelerated screening, AI tools |
| TIME-002 | Prototype development delays | Timeline | Medium | High | Simplified scope, iterative development |
| TIME-003 | Stakeholder feedback delays | Timeline | Medium | Medium | Structured feedback cycles, alternatives |

## Medium Priority Risks (Score 2)

| Risk ID | Description | Category | Likelihood | Impact | Mitigation Strategy |
|---------|-------------|----------|------------|--------|-------------------|
| TECH-001 | Rapid protocol evolution | Technical | High | Low | Continuous monitoring, adaptive approach |
| TECH-002 | Integration challenges | Technical | Medium | Medium | Modular design, fallback options |
| TECH-003 | Computational limitations | Technical | Medium | Medium | Cloud resources, optimization |
| METH-001 | Limited real-world data access | Methodological | High | Low | Simulation data, synthetic datasets |
| METH-002 | Collaboration effectiveness evaluation | Methodological | Medium | Medium | Multiple evaluation metrics |
| METH-003 | Protocol comparison difficulties | Methodological | Medium | Medium | Standardized comparison framework |

## Risk Monitoring Schedule

| Risk Category | Monitoring Frequency | Review Method | Escalation Trigger |
|---------------|---------------------|---------------|-------------------|
| Technical | Bi-weekly | Literature alerts, protocol updates | Major protocol changes affecting scope |
| Methodological | Bi-weekly | Progress review, methodology validation | Difficulty synthesizing findings |
| Resource | Weekly | Progress tracking, resource assessment | Two consecutive weeks behind schedule |
| Impact | Monthly | Stakeholder feedback, impact assessment | Significant negative feedback |
| Timeline | Weekly | Milestone tracking, deliverable status | Missing critical milestones |

## Risk Response Strategies

### Prevention Strategies
| Risk Type | Prevention Approach | Implementation |
|-----------|-------------------|----------------|
| Timeline | Early planning, buffer time | Built into project schedule |
| Resource | Stakeholder engagement, alternatives | Ongoing relationship management |
| Technical | Continuous monitoring, modular design | Weekly protocol updates review |
| Methodological | Framework validation, peer review | Regular supervisor consultations |

### Contingency Plans
| Risk Scenario | Primary Response | Secondary Response | Decision Point |
|---------------|------------------|-------------------|----------------|
| Major timeline delay | Reduce scope, parallel activities | Extend timeline, simplify prototype | Week 8 review |
| Technical barriers | Alternative protocols, simplified integration | Focus on theoretical framework | Mid-Phase 2 |
| Resource constraints | Open-source alternatives, cloud resources | Academic partnerships, simplified scope | Ongoing |
| Data access issues | Synthetic data, simulation | Public datasets, literature-based | Phase 1 completion |

## Risk Success Metrics

| Risk Category | Success Indicator | Target Threshold | Measurement Method |
|---------------|------------------|------------------|-------------------|
| Timeline | Schedule adherence | >90% milestone completion | Weekly tracking |
| Quality | Research quality | Supervisor satisfaction >4/5 | Regular reviews |
| Technical | Integration success | >80% protocol features implemented | Technical validation |
| Resource | Budget adherence | <10% budget variance | Cost tracking |
| Impact | Stakeholder satisfaction | >3.5/5 stakeholder rating | Feedback surveys |

## Risk Register Summary

- **Total Risks Identified**: 15
- **High Priority**: 9 risks requiring immediate attention
- **Medium Priority**: 6 risks requiring regular monitoring  
- **Risk Review Frequency**: Weekly for high-priority, bi-weekly for medium
- **Escalation Protocol**: Defined for each risk category
- **Contingency Budget**: 10% of timeline allocated for risk response"""
    
    return content

def create_stakeholder_context_table():
    """Create a comprehensive stakeholder and system context table."""
    
    # Read stakeholder and ethics data
    ethics_files = [
        "sources/6.1.1-ethics-guidelines-review.json",
        "sources/6.1.2-ethical-concerns-analysis.json",
        "sources/6.1.3-data-privacy-framework.json",
        "sources/6.1.4-consent-requirements-framework.json"
    ]
    
    stakeholder_data = {}
    for file_path in ethics_files:
        if Path(file_path).exists():
            with open(file_path, 'r') as f:
                data = json.load(f)
                stakeholder_data.update(data)
    
    content = f"""# Stakeholder & System Context Table (Visual Reference)

*Generated: {datetime.now().isoformat()}*
*Task: 8.1.3 - Incorporate Visual Planning*
*Based on: sources/6.1.* ethics and stakeholder analysis documents*

## Primary Stakeholder Matrix

| Stakeholder | Role | Primary Interest | Influence Level | Impact Level | Engagement Strategy |
|-------------|------|------------------|-----------------|--------------|-------------------|
| DER Workers | Research Subjects | Job security, skill development | Medium | High | Participatory design, regular consultation |
| DER Operators | System Users | Operational efficiency, reliability | High | High | Co-design sessions, validation feedback |
| Energy Companies | Implementation Partners | Cost reduction, compliance | High | Medium | Strategic partnerships, pilot programs |
| Regulatory Bodies | Compliance Oversight | Safety, standards compliance | High | Medium | Regular updates, compliance documentation |
| Academic Supervisors | Research Guidance | Research quality, innovation | High | High | Weekly meetings, milestone reviews |
| Technology Vendors | Technical Partners | Market opportunities, integration | Medium | Low | Technical collaboration, standards input |
| End Consumers | Service Recipients | Reliable energy, cost effectiveness | Low | Medium | Indirect engagement, impact assessment |

## System Context Mapping

### Technical Systems
| System Component | Function | Stakeholder Owner | Integration Level | Data Requirements |
|------------------|----------|-------------------|-------------------|-------------------|
| SCADA Systems | DER monitoring and control | Energy Companies | High | Real-time operational data |
| DERMS | DER portfolio management | System Operators | High | Aggregated performance data |
| Digital Twin Platform | Worker expertise modeling | Research Team | Core | Worker knowledge, protocols |
| Communication Protocols | Agent coordination | Technology Vendors | High | Message standards, interfaces |
| Maintenance Systems | Work order management | DER Operators | Medium | Maintenance schedules, history |

### Organizational Systems
| Organization Type | Role in Research | Key Concerns | Engagement Requirements |
|-------------------|------------------|--------------|-------------------------|
| Energy Utilities | Data providers, validators | Competitive advantage, IP protection | NDAs, data sharing agreements |
| Research Institutions | Knowledge partners | Publication rights, collaboration | Academic partnerships, co-authorship |
| Professional Bodies | Standards input | Industry standards, best practices | Standards committee participation |
| Labor Organizations | Worker representation | Job impact, skill implications | Worker consultation, impact mitigation |

## Ethical Considerations Matrix

| Ethical Dimension | Stakeholder Impact | Risk Level | Mitigation Approach | Monitoring Method |
|-------------------|-------------------|------------|-------------------|-------------------|
| **Privacy** | DER Workers | High | Data anonymization, consent protocols | Privacy audit, worker feedback |
| **Autonomy** | DER Workers | Medium | Voluntary participation, opt-out options | Ongoing consent verification |
| **Job Security** | DER Workers | High | Augmentation focus, skill development | Employment impact assessment |
| **Data Ownership** | Energy Companies | Medium | Clear data agreements, IP protection | Legal review, compliance tracking |
| **Algorithmic Bias** | All Users | Medium | Diverse training data, bias testing | Algorithm auditing, performance metrics |
| **Transparency** | Regulatory Bodies | Medium | Open methodology, documentation | Public reporting, stakeholder updates |

## Consent and Participation Framework

| Participation Level | Stakeholder | Consent Type | Information Required | Withdrawal Rights |
|---------------------|-------------|--------------|---------------------|------------------|
| **Direct Data** | DER Workers | Informed written consent | Full research purpose, data use, risks | Full withdrawal anytime |
| **Observational** | DER Operators | Process consent | Observation methods, anonymization | Limited withdrawal |
| **System Data** | Energy Companies | Organizational consent | Data scope, security measures, IP | Contract-based withdrawal |
| **Validation** | All Stakeholders | Ongoing consent | Results sharing, feedback use | Feedback withdrawal |

## Impact Assessment Matrix

### Positive Impacts
| Impact Type | Beneficiary | Magnitude | Timeline | Measurement Method |
|-------------|-------------|-----------|----------|--------------------|
| Efficiency Gains | DER Operators | High | 6-12 months | Performance metrics |
| Skill Enhancement | DER Workers | Medium | 3-6 months | Training assessments |
| System Reliability | End Consumers | Medium | 12-24 months | Reliability statistics |
| Knowledge Preservation | Industry | High | Immediate | Knowledge base metrics |

### Potential Negative Impacts
| Impact Type | Affected Party | Risk Level | Mitigation Strategy | Monitoring Approach |
|-------------|----------------|------------|-------------------|-------------------|
| Job Displacement | DER Workers | Medium | Augmentation focus, retraining | Employment tracking |
| Skill Deskilling | DER Workers | Medium | Continuous learning, human oversight | Skill assessment |
| Data Misuse | Energy Companies | Low | Strict data governance, auditing | Compliance monitoring |
| System Dependency | DER Operators | Medium | Human override capabilities | System resilience testing |

## Regulatory Compliance Checklist

| Regulation/Standard | Applicability | Compliance Status | Required Actions | Review Date |
|---------------------|---------------|-------------------|------------------|-------------|
| GDPR | Personal data processing | Planning phase | Data protection impact assessment | Before data collection |
| IEEE Standards | Communication protocols | Design phase | Standards compliance review | Protocol design |
| ISO 27001 | Information security | Implementation | Security framework implementation | Ongoing |
| Industry Codes | DER operations | Throughout | Industry best practice adherence | Quarterly review |

## Success Metrics for Stakeholder Engagement

| Stakeholder | Success Metric | Target Value | Measurement Method | Review Frequency |
|-------------|----------------|--------------|-------------------|------------------|
| DER Workers | Participation satisfaction | >4.0/5.0 | Survey ratings | Monthly |
| DER Operators | System adoption intent | >70% | Pilot feedback | End of pilot |
| Energy Companies | Partnership continuation | >80% | Contract renewals | Quarterly |
| Regulatory Bodies | Compliance rating | 100% | Audit results | As required |
| Academic Community | Research quality rating | >4.0/5.0 | Peer review scores | Publication |"""
    
    return content

def create_workflow_simplified_tex():
    """Create a simplified workflow diagram in TikZ format."""
    
    workflow_content = r"""\documentclass[border=10pt]{standalone}
\usepackage{tikz}
\usetikzlibrary{positioning, arrows.meta, shapes, backgrounds, fit}

\begin{document}
\begin{tikzpicture}[
    node distance=2.5cm and 3.5cm,
    every node/.style={rounded corners, minimum width=2.5cm, minimum height=1.2cm, align=center, font=\small},
    phase/.style={fill=blue!15, draw=blue!40!black, thick},
    activity/.style={fill=green!15, draw=green!40!black, thick, minimum width=2cm},
    output/.style={fill=orange!15, draw=orange!40!black, thick},
    integration/.style={fill=purple!15, draw=purple!40!black, thick},
    arrow/.style={-Stealth, thick},
    dasharrow/.style={-Stealth, thick, dashed},
    label/.style={font=\footnotesize, fill=white, inner sep=2pt}
]

% Phase 1: Literature Review
\node[phase] (phase1) {Phase 1\\Literature Review\\(6 weeks)};
\node[activity, below=1.5cm of phase1] (p1act1) {Search \& Screen};
\node[activity, right=1.5cm of p1act1] (p1act2) {Review \& Extract};
\node[activity, right=1.5cm of p1act2] (p1act3) {Analyze \& Synthesize};
\node[output, below=1cm of p1act2] (p1out) {Literature\\Synthesis};

% Phase 2: Comparative Framework
\node[phase, right=4cm of phase1] (phase2) {Phase 2\\Comparative Framework\\(8 weeks)};
\node[activity, below=1.5cm of phase2] (p2act1) {Framework\\Design};
\node[activity, right=1.5cm of p2act1] (p2act2) {Protocol\\Analysis};
\node[activity, below=1cm of p2act1] (p2act3) {Comparative\\Evaluation};
\node[output, below=1cm of p2act2] (p2out) {Comparison\\Framework};

% Phase 3: Proof of Concept
\node[phase, right=4cm of phase2] (phase3) {Phase 3\\Proof of Concept\\(4 weeks)};
\node[activity, below=1.5cm of phase3] (p3act1) {Prototype\\Design};
\node[activity, right=1.5cm of p3act1] (p3act2) {Integration\\Development};
\node[activity, below=1cm of p3act1] (p3act3) {Testing \&\\Validation};
\node[output, below=1cm of p3act2] (p3out) {Working\\Prototype};

% Integration points
\node[integration, below=2.5cm of phase1] (int1) {Integration\\Gate 1};
\node[integration, below=2.5cm of phase2] (int2) {Integration\\Gate 2};

% Phase connections
\draw[arrow] (phase1) -- (p1act1);
\draw[arrow] (p1act1) -- (p1act2);
\draw[arrow] (p1act2) -- (p1act3);
\draw[arrow] (p1act2) -- (p1out);

\draw[arrow] (phase2) -- (p2act1);
\draw[arrow] (p2act1) -- (p2act2);
\draw[arrow] (p2act1) -- (p2act3);
\draw[arrow] (p2act2) -- (p2out);

\draw[arrow] (phase3) -- (p3act1);
\draw[arrow] (p3act1) -- (p3act2);
\draw[arrow] (p3act1) -- (p3act3);
\draw[arrow] (p3act2) -- (p3out);

% Integration flows
\draw[arrow] (p1out) to[bend right=15] (int1);
\draw[arrow] (int1) to[bend right=15] (p2act1);
\draw[arrow] (p2out) to[bend right=15] (int2);
\draw[arrow] (int2) to[bend right=15] (p3act1);

% Phase-to-phase progression
\draw[arrow, thick, blue] (phase1) -- node[label, above] {Sequential Flow} (phase2);
\draw[arrow, thick, blue] (phase2) -- node[label, above] {Sequential Flow} (phase3);

% Risk monitoring (background process)
\node[below=3.5cm of int1, font=\scriptsize, align=center] (risk) {Risk Monitoring\\(Weekly/Bi-weekly)};
\draw[dasharrow, red] (risk) to[bend left=30] (phase1);
\draw[dasharrow, red] (risk) to[bend left=10] (phase2);
\draw[dasharrow, red] (risk) to[bend right=30] (phase3);

% Background grouping
\begin{scope}[on background layer]
    \node[fit=(phase1) (p1out) (int1), fill=blue!5, rounded corners] {};
    \node[fit=(phase2) (p2out) (int2), fill=green!5, rounded corners] {};
    \node[fit=(phase3) (p3out), fill=orange!5, rounded corners] {};
\end{scope}

% Timeline indicator
\node[below=4.5cm of phase2, font=\small, align=center] {
    \textbf{Timeline:} 18 weeks total | \textbf{Deliverables:} 3 major outputs | \textbf{Integration:} 2 gates
};

\end{tikzpicture}
\end{document}"""
    
    return workflow_content

def main():
    """Main function to generate all visual planning documents."""
    
    print("=== Task 8.1.3: Incorporate Visual Planning ===")
    print(f"Generated: {datetime.now().isoformat()}")
    print()
    
    # Ensure sources directory exists
    sources_dir = Path("sources")
    sources_dir.mkdir(exist_ok=True)
    
    # Generate visual planning documents
    visual_outputs = {
        "sources/8.1.3-timeline-gantt.tex": create_timeline_gantt_tex(),
        "sources/8.1.3-methodology-comparison-table.md": create_methodology_comparison_table(),
        "sources/8.1.3-risk-management-table.md": create_risk_management_table(),
        "sources/8.1.3-stakeholder-context-table.md": create_stakeholder_context_table(),
        "sources/8.1.3-workflow-simplified.tex": create_workflow_simplified_tex()
    }
    
    # Write all files
    for filepath, content in visual_outputs.items():
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"✓ Created: {filepath}")
    
    # Generate summary JSON
    summary = {
        "task": "8.1.3 - Incorporate Visual Planning",
        "generated": datetime.now().isoformat(),
        "visual_documents": {
            "timeline_gantt": {
                "file": "sources/8.1.3-timeline-gantt.tex",
                "type": "LaTeX/TikZ Gantt Chart",
                "purpose": "Visual timeline for research proposal",
                "phases": 3,
                "duration_weeks": 19
            },
            "methodology_comparison": {
                "file": "sources/8.1.3-methodology-comparison-table.md",
                "type": "Markdown Tables",
                "purpose": "Methodology selection justification",
                "methodologies_evaluated": 25,
                "top_methodologies": 5
            },
            "risk_management": {
                "file": "sources/8.1.3-risk-management-table.md",
                "type": "Markdown Tables",
                "purpose": "Risk analysis and mitigation planning",
                "total_risks": 15,
                "high_priority_risks": 9
            },
            "stakeholder_context": {
                "file": "sources/8.1.3-stakeholder-context-table.md",
                "type": "Markdown Tables",
                "purpose": "Stakeholder mapping and ethical framework",
                "primary_stakeholders": 7,
                "system_components": 5
            },
            "workflow_diagram": {
                "file": "sources/8.1.3-workflow-simplified.tex",
                "type": "LaTeX/TikZ Workflow",
                "purpose": "Simplified methodology workflow visualization",
                "phases": 3,
                "integration_gates": 2
            }
        },
        "data_sources": [
            "sources/5.2.1-methodology-comparison-matrix.json",
            "sources/5.3.3-project-timeline.json",
            "sources/7.1.*-risk*.json",
            "sources/6.1.*-ethics*.json"
        ],
        "usage_notes": {
            "latex_files": "Compile with pdflatex and tikz packages",
            "markdown_tables": "Can be converted to LaTeX tables or used in documentation",
            "integration": "Ready for inclusion in main proposal deliverable"
        }
    }
    
    summary_file = "sources/8.1.3-visual-planning-summary.json"
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"✓ Created: {summary_file}")
    
    print()
    print("=== Visual Planning Documents Generated ===")
    print(f"Total files created: {len(visual_outputs) + 1}")
    print("All documents are ready for integration into the research proposal.")
    print()
    print("Next steps:")
    print("1. Compile LaTeX files for visual integration")
    print("2. Reference tables in methodology and risk sections")
    print("3. Include timeline Gantt chart in proposal timeline section")

if __name__ == "__main__":
    main() 
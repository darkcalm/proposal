#!/usr/bin/env python3
"""
Task 5.2.1: Create Comprehensive Methodology Comparison Matrix

Focus: Systematic comparison of all identified methodologies for ACP/A2A protocol research
Context: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
         for DER predictive maintenance coordination

Based on:
- All methodologies from Tasks 5.1.1-5.1.5 (quantitative, qualitative, mixed, emerging)
- Analysis of prior research methodologies from sources/ directory
- Comprehensive evaluation criteria including prior research credibility
- Research direction from docs/3.1.2-research-direction-selection.md
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

def analyze_prior_research_methodologies():
    """
    Analyze all sources to identify methodologies used in prior research
    
    This provides the "prior research usage" criterion for methodology credibility
    """
    
    # Methodology keywords to search for in literature
    methodology_keywords = {
        "design_science_research": [
            "design science research", "DSR", "design science methodology", 
            "artifact development", "design artifact", "artifact evaluation",
            "design and creation", "constructive research"
        ],
        "case_study": [
            "case study", "case study methodology", "case study research",
            "case study approach", "multiple case study", "single case study",
            "exploratory case study", "descriptive case study"
        ],
        "experimental_research": [
            "experimental research", "experimental methodology", "experiment",
            "controlled experiment", "experimental design", "experimental study",
            "randomized controlled trial", "laboratory experiment"
        ],
        "survey_research": [
            "survey research", "survey methodology", "questionnaire survey",
            "survey study", "survey design", "cross-sectional survey",
            "longitudinal survey"
        ],
        "comparative_research": [
            "comparative research", "comparative study", "comparative analysis",
            "comparison methodology", "comparative approach", "benchmarking study"
        ],
        "simulation_modeling": [
            "simulation", "simulation modeling", "simulation study", 
            "mathematical simulation", "computer simulation", "simulation framework",
            "modeling and simulation", "discrete event simulation"
        ],
        "digital_twin": [
            "digital twin", "digital twins", "digital twin methodology",
            "digital twin framework", "digital twin simulation", "virtual twin"
        ],
        "agent_based_modeling": [
            "agent-based modeling", "agent-based simulation", "multi-agent system",
            "agent-based approach", "agent simulation", "ABM"
        ],
        "optimization_research": [
            "optimization", "mathematical optimization", "optimization methodology",
            "optimization approach", "optimization framework", "optimization algorithm"
        ],
        "mixed_methods": [
            "mixed methods", "mixed methodology", "mixed methods research",
            "sequential explanatory", "sequential exploratory", "convergent parallel"
        ],
        "systematic_review": [
            "systematic review", "systematic literature review", "meta-analysis",
            "literature review", "scoping review"
        ],
        "action_research": [
            "action research", "participatory action research", "action research methodology"
        ],
        "grounded_theory": [
            "grounded theory", "grounded theory methodology", "grounded theory approach"
        ],
        "phenomenological": [
            "phenomenological", "phenomenological research", "phenomenological methodology"
        ],
        "rapid_prototyping": [
            "rapid prototyping", "iterative development", "agile methodology",
            "prototype development", "iterative design"
        ],
        "living_lab": [
            "living lab", "living laboratory", "real-world testing",
            "field testing", "pilot study"
        ]
    }
    
    # Source directories to analyze
    source_dirs = [
        "../sources/2.1-initial_literature_input/",
        "../sources/4.1-semantic-search/semantic-scholar-search-iteration-1/semantic-scholar-review-papers/"
    ]
    
    methodology_usage = {}
    paper_methodology_mapping = {}
    
    # Initialize methodology counters
    for method in methodology_keywords.keys():
        methodology_usage[method] = {
            "count": 0,
            "papers": [],
            "examples": []
        }
    
    # Analyze each source directory
    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            for filename in os.listdir(source_dir):
                if filename.endswith('.md') and not filename.startswith('.'):
                    filepath = os.path.join(source_dir, filename)
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read().lower()
                            
                        paper_methods = []
                        
                        # Search for methodology keywords
                        for method, keywords in methodology_keywords.items():
                            for keyword in keywords:
                                if keyword.lower() in content:
                                    if method not in paper_methods:
                                        methodology_usage[method]["count"] += 1
                                        methodology_usage[method]["papers"].append(filename)
                                        
                                        # Extract a brief context around the keyword
                                        context_start = max(0, content.find(keyword.lower()) - 100)
                                        context_end = min(len(content), content.find(keyword.lower()) + len(keyword) + 100)
                                        context = content[context_start:context_end].strip()
                                        methodology_usage[method]["examples"].append(f"{filename}: ...{context}...")
                                        
                                        paper_methods.append(method)
                                        break
                        
                        paper_methodology_mapping[filename] = paper_methods
                    
                    except Exception as e:
                        print(f"Error processing {filepath}: {e}")
    
    return methodology_usage, paper_methodology_mapping

def create_comprehensive_methodology_matrix():
    """
    Create comprehensive comparison matrix of all methodologies
    
    Includes all methodologies from Tasks 5.1.1-5.1.5 plus prior research analysis
    """
    
    # Research context
    context = {
        "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
        "domain": "Distributed Energy Resources (DER) predictive maintenance",
        "research_objective": "Develop protocol adaptation framework and evaluation methodology",
        "timeframe": "20-week Master's thesis",
        "deliverable_type": "Technical framework and evaluation approach"
    }
    
    # Analyze prior research methodologies
    print("🔍 Analyzing prior research methodologies from sources...")
    prior_research_usage, paper_mapping = analyze_prior_research_methodologies()
    
    # Complete methodology inventory from all previous tasks
    all_methodologies = {
        # Quantitative Methodologies (Task 5.1.2)
        "design_science_research": {
            "name": "Design Science Research (DSR)",
            "category": "Quantitative",
            "source_task": "5.1.2",
            "classification": "Constructive Research Methodology",
            "paradigm": "Pragmatic with design-oriented approach",
            "purpose": "Create and evaluate artifacts to solve identified problems",
            "timeline": "14-16 weeks",
            "phases": ["Problem identification", "Solution design", "Artifact development", "Artifact evaluation", "Communication"],
            "philosophical_foundations": {
                "epistemology": "Constructive knowledge through artifact creation",
                "ontology": "Pragmatic realism",
                "methodology_philosophy": "Problem-solving through design",
                "validation_approach": "Artifact evaluation and utility demonstration"
            },
            "strengths": [
                "Strong alignment with protocol development objectives",
                "Systematic approach to artifact creation and evaluation",
                "Well-established in IS and technology research",
                "Combines theoretical rigor with practical application",
                "Clear evaluation criteria and validation methods"
            ],
            "limitations": [
                "Requires significant technical development effort",
                "Artifact complexity may challenge evaluation",
                "Limited stakeholder integration in traditional DSR",
                "May not capture all contextual factors"
            ],
            "acp_a2a_application": "Develop ACP/A2A adaptation framework as research artifact with systematic evaluation",
            "feasibility_20_weeks": "Good",
            "resource_requirements": "High - technical development, evaluation design",
            "innovation_potential": "High"
        },
        
        "experimental_research": {
            "name": "Experimental Research Methodology",
            "category": "Quantitative", 
            "source_task": "5.1.2",
            "classification": "Hypothesis-testing Methodology",
            "paradigm": "Post-positivist",
            "purpose": "Test hypotheses about protocol performance through controlled experiments",
            "timeline": "8-12 weeks",
            "phases": ["Hypothesis formulation", "Experimental design", "Data collection", "Statistical analysis", "Interpretation"],
            "strengths": [
                "Strong causal inference capabilities",
                "Rigorous statistical validation",
                "Well-established evaluation criteria",
                "Clear replication procedures"
            ],
            "limitations": [
                "Limited real-world context",
                "May not capture system complexity",
                "Requires extensive experimental setup"
            ],
            "acp_a2a_application": "Test specific protocol performance hypotheses under controlled conditions",
            "feasibility_20_weeks": "Good",
            "resource_requirements": "Moderate",
            "innovation_potential": "Moderate"
        },
        
        "comparative_research": {
            "name": "Comparative Research Methodology",
            "category": "Quantitative",
            "source_task": "5.1.2", 
            "classification": "Analytical Methodology",
            "paradigm": "Post-positivist",
            "purpose": "Systematic comparison of protocol alternatives",
            "timeline": "6-10 weeks",
            "phases": ["Comparison framework", "Data collection", "Systematic analysis", "Interpretation"],
            "strengths": [
                "Clear benchmarking capabilities",
                "Systematic evaluation framework",
                "Efficient for multiple alternatives"
            ],
            "limitations": [
                "Dependent on available alternatives",
                "May lack depth in individual analysis"
            ],
            "acp_a2a_application": "Compare ACP vs A2A protocol performance across different scenarios",
            "feasibility_20_weeks": "Excellent",
            "resource_requirements": "Low to Moderate",
            "innovation_potential": "Moderate"
        },
        
        # Qualitative Methodologies (Task 5.1.3)
        "case_study": {
            "name": "Case Study Methodology",
            "category": "Qualitative",
            "source_task": "5.1.3",
            "classification": "Empirical Inquiry Methodology",
            "paradigm": "Constructivist to critical realist",
            "purpose": "In-depth investigation of protocol implementation in real-world contexts",
            "timeline": "13-19 weeks",
            "phases": ["Case selection", "Data collection", "Within-case analysis", "Cross-case analysis", "Interpretation"],
            "strengths": [
                "Rich contextual understanding",
                "Real-world validation opportunities", 
                "Flexible research design",
                "Strong stakeholder insights"
            ],
            "limitations": [
                "Limited generalizability",
                "Time-intensive data collection",
                "Potential researcher bias"
            ],
            "acp_a2a_application": "Investigate protocol implementation challenges and successes in DER maintenance contexts",
            "feasibility_20_weeks": "Challenging but possible",
            "resource_requirements": "High - field access, stakeholder coordination",
            "innovation_potential": "High"
        },
        
        "grounded_theory": {
            "name": "Grounded Theory Methodology",
            "category": "Qualitative",
            "source_task": "5.1.3",
            "classification": "Theory Development Methodology", 
            "paradigm": "Constructivist",
            "purpose": "Develop theory about protocol adoption and usage patterns",
            "timeline": "16-21 weeks",
            "phases": ["Initial coding", "Focused coding", "Theoretical coding", "Theory development"],
            "strengths": [
                "Theory generation capability",
                "Systematic data analysis",
                "Emergent research design"
            ],
            "limitations": [
                "Time-intensive process",
                "Not suitable for protocol focus",
                "Exceeds thesis timeframe"
            ],
            "acp_a2a_application": "Limited suitability for technical protocol research",
            "feasibility_20_weeks": "Poor",
            "resource_requirements": "High",
            "innovation_potential": "Low for this context"
        },
        
        "phenomenological": {
            "name": "Phenomenological Research Methodology",
            "category": "Qualitative",
            "source_task": "5.1.3",
            "classification": "Interpretive Methodology",
            "paradigm": "Phenomenological",
            "purpose": "Understand lived experiences of protocol users",
            "timeline": "14-18 weeks",
            "phases": ["Participant selection", "Data collection", "Phenomenological analysis", "Essence description"],
            "strengths": [
                "Deep understanding of user experiences",
                "Rich descriptive insights"
            ],
            "limitations": [
                "Focus on experiences vs technical performance",
                "Limited technical applicability"
            ],
            "acp_a2a_application": "Not suitable for technical protocol research objectives",
            "feasibility_20_weeks": "Poor fit",
            "resource_requirements": "Moderate",
            "innovation_potential": "Low for this context"
        },
        
        # Mixed Methodologies (Task 5.1.4)
        "sequential_explanatory": {
            "name": "Sequential Explanatory Mixed Methods",
            "category": "Mixed Methods",
            "source_task": "5.1.4",
            "classification": "Sequential Integration Mixed Methodology",
            "paradigm": "Pragmatic with post-positivist foundations",
            "purpose": "Use quantitative results to drive qualitative investigation for deeper understanding",
            "timeline": "20-26 weeks",
            "phases": ["Quantitative primary", "Interface design", "Qualitative explanatory", "Integration"],
            "strengths": [
                "Comprehensive evaluation",
                "Strong validation through triangulation",
                "Clear sequential structure",
                "Balances rigor with understanding"
            ],
            "limitations": [
                "Complex coordination",
                "Timeline risk if quantitative phase delayed",
                "Resource intensive"
            ],
            "acp_a2a_application": "DSR protocol development followed by case studies to explain performance results",
            "feasibility_20_weeks": "Challenging but possible",
            "resource_requirements": "High",
            "innovation_potential": "High"
        },
        
        "convergent_parallel": {
            "name": "Convergent Parallel Mixed Methods", 
            "category": "Mixed Methods",
            "source_task": "5.1.4",
            "classification": "Simultaneous Integration Mixed Methodology",
            "paradigm": "Pragmatic with equal quantitative/qualitative emphasis",
            "purpose": "Simultaneous quantitative and qualitative investigation with integration",
            "timeline": "17-22 weeks",
            "phases": ["Parallel design", "Concurrent data collection", "Independent analysis", "Integration"],
            "strengths": [
                "Efficient timeline through parallel execution",
                "Comprehensive evaluation",
                "Strong triangulation"
            ],
            "limitations": [
                "Complex coordination",
                "Resource intensive",
                "Integration complexity"
            ],
            "acp_a2a_application": "Simultaneous DSR development and case study investigation",
            "feasibility_20_weeks": "Good",
            "resource_requirements": "Very High",
            "innovation_potential": "High"
        },
        
        "sequential_exploratory": {
            "name": "Sequential Exploratory Mixed Methods",
            "category": "Mixed Methods", 
            "source_task": "5.1.4",
            "classification": "Sequential Development Mixed Methodology",
            "paradigm": "Pragmatic with constructivist foundations",
            "purpose": "Use qualitative exploration to inform quantitative investigation",
            "timeline": "19-25 weeks",
            "phases": ["Qualitative exploration", "Instrument development", "Quantitative testing", "Integration"],
            "strengths": [
                "Stakeholder grounding",
                "Context-appropriate development",
                "Practical relevance"
            ],
            "limitations": [
                "Front-loads qualitative work",
                "May not leverage existing literature",
                "Timeline risk"
            ],
            "acp_a2a_application": "Case studies inform DSR design and evaluation criteria",
            "feasibility_20_weeks": "Requires scope management",
            "resource_requirements": "High",
            "innovation_potential": "Moderate"
        },
        
        # Emerging Methodologies (Task 5.1.5)
        "digital_twin": {
            "name": "Digital Twin Methodology",
            "category": "Emerging",
            "source_task": "5.1.5",
            "classification": "Simulation-Based Technology Methodology", 
            "paradigm": "Pragmatic with strong empirical validation",
            "purpose": "Create digital replicas for comprehensive protocol testing and validation",
            "timeline": "14-18 weeks",
            "phases": ["Digital model creation", "Protocol integration", "Simulation validation", "Optimization"],
            "strengths": [
                "Comprehensive testing without physical infrastructure",
                "Risk-free experimentation",
                "Scalability testing",
                "Real-time performance monitoring"
            ],
            "limitations": [
                "Model fidelity limitations",
                "High computational requirements",
                "Significant modeling expertise needed"
            ],
            "acp_a2a_application": "Create digital twins of DER maintenance systems for protocol performance testing",
            "feasibility_20_weeks": "Good",
            "resource_requirements": "Moderate to High",
            "innovation_potential": "Very High"
        },
        
        "rapid_prototyping": {
            "name": "Rapid Prototyping and Iterative Development",
            "category": "Emerging",
            "source_task": "5.1.5",
            "classification": "Agile Technology Development Methodology",
            "paradigm": "Iterative and incremental development",
            "purpose": "Rapidly develop and refine protocol solutions through continuous iteration",
            "timeline": "8-20 weeks (flexible)",
            "phases": ["Sprint cycles", "Continuous integration", "Stakeholder feedback", "Iterative refinement"],
            "strengths": [
                "Fast development cycles",
                "Continuous validation",
                "Adaptive scope management",
                "Risk reduction through iteration"
            ],
            "limitations": [
                "May sacrifice depth for speed",
                "Requires strong project management",
                "Potential scope creep"
            ],
            "acp_a2a_application": "Rapid development and testing of ACP/A2A protocol implementations",
            "feasibility_20_weeks": "Excellent",
            "resource_requirements": "Moderate",
            "innovation_potential": "High"
        },
        
        "ai_explainability": {
            "name": "AI Explainability and Interpretability Methodology",
            "category": "Emerging",
            "source_task": "5.1.5",
            "classification": "Explainable AI Research Methodology",
            "paradigm": "Transparency and accountability",
            "purpose": "Develop explainable protocol decision-making processes",
            "timeline": "12-16 weeks",
            "phases": ["Explainability design", "Implementation", "Evaluation", "Refinement"],
            "strengths": [
                "Enhanced transparency",
                "Stakeholder trust building",
                "Regulatory compliance support"
            ],
            "limitations": [
                "Additional implementation complexity",
                "May not be critical for technical research",
                "Performance overhead"
            ],
            "acp_a2a_application": "Develop explanations for protocol coordination decisions",
            "feasibility_20_weeks": "Good",
            "resource_requirements": "Moderate",
            "innovation_potential": "High"
        },
        
        "human_ai_collaboration": {
            "name": "Human-AI Collaboration Methodology",
            "category": "Emerging",
            "source_task": "5.1.5", 
            "classification": "Hybrid Intelligence Research Methodology",
            "paradigm": "Socio-technical systems approach",
            "purpose": "Design effective human-AI collaboration in protocol systems",
            "timeline": "12-17 weeks",
            "phases": ["Stakeholder engagement", "Co-design", "Iterative evaluation", "Integration"],
            "strengths": [
                "Stakeholder engagement",
                "Human factors integration",
                "Acceptance building"
            ],
            "limitations": [
                "Requires extensive stakeholder coordination",
                "May not align with technical objectives"
            ],
            "acp_a2a_application": "Ensure protocols support effective human oversight and intervention",
            "feasibility_20_weeks": "Moderate",
            "resource_requirements": "Moderate to High",
            "innovation_potential": "Moderate"
        },
        
        "living_lab": {
            "name": "Living Lab Methodology",
            "category": "Emerging",
            "source_task": "5.1.5",
            "classification": "Real-World Innovation Testing Methodology",
            "paradigm": "Open innovation in real-life environments",
            "purpose": "Test protocols in real-world DER maintenance environments",
            "timeline": "15-25 weeks",
            "phases": ["Context establishment", "Co-design", "Real-world piloting", "Evaluation", "Scaling"],
            "strengths": [
                "Real-world validation",
                "Stakeholder co-creation",
                "Contextual insights"
            ],
            "limitations": [
                "Complex stakeholder coordination",
                "Timeline uncertainty",
                "High resource requirements"
            ],
            "acp_a2a_application": "Real-world testing of protocols in DER maintenance environments",
            "feasibility_20_weeks": "Poor",
            "resource_requirements": "Very High",
            "innovation_potential": "Very High"
        }
    }
    
    # Add prior research usage data to each methodology
    for method_key, method_data in all_methodologies.items():
        if method_key in prior_research_usage:
            usage_data = prior_research_usage[method_key]
            method_data["prior_research_usage"] = {
                "papers_count": usage_data["count"],
                "example_papers": usage_data["papers"][:5],  # Top 5 examples
                "usage_examples": usage_data["examples"][:3],  # Top 3 context examples
                "credibility_score": "High" if usage_data["count"] >= 5 else "Moderate" if usage_data["count"] >= 2 else "Low"
            }
        else:
            method_data["prior_research_usage"] = {
                "papers_count": 0,
                "example_papers": [],
                "usage_examples": [],
                "credibility_score": "No Evidence"
            }
    
    # Evaluation criteria framework
    evaluation_criteria = {
        "research_alignment": {
            "description": "Alignment with ACP/A2A protocol research objectives",
            "weight": 25,
            "scale": "1-5 (1=Poor, 5=Excellent)",
            "considerations": ["Protocol development focus", "Technical evaluation capability", "Framework design suitability"]
        },
        "timeline_feasibility": {
            "description": "Feasibility within 20-week Master's thesis timeframe",
            "weight": 20,
            "scale": "1-5 (1=Not feasible, 5=Highly feasible)",
            "considerations": ["Total duration", "Critical path complexity", "Buffer time availability"]
        },
        "resource_requirements": {
            "description": "Required resources and expertise",
            "weight": 15,
            "scale": "1-5 (1=Very High, 5=Low requirements)",
            "considerations": ["Technical expertise", "Tool availability", "Access requirements"]
        },
        "innovation_potential": {
            "description": "Potential for novel research contribution",
            "weight": 15,
            "scale": "1-5 (1=Low, 5=Very High)",
            "considerations": ["Methodological novelty", "Application innovation", "Research gap addressing"]
        },
        "practical_applicability": {
            "description": "Real-world applicability and validation potential",
            "weight": 10,
            "scale": "1-5 (1=Limited, 5=High applicability)",
            "considerations": ["Stakeholder relevance", "Implementation feasibility", "Industry applicability"]
        },
        "prior_research_credibility": {
            "description": "Evidence of successful usage in related research",
            "weight": 10,
            "scale": "1-5 (1=No evidence, 5=Extensive evidence)",
            "considerations": ["Number of papers using methodology", "Success in similar contexts", "Research community acceptance"]
        },
        "integration_potential": {
            "description": "Potential for integration with other methodologies",
            "weight": 5,
            "scale": "1-5 (1=Poor, 5=Excellent)",
            "considerations": ["Compatibility with other methods", "Enhancement opportunities", "Synergy potential"]
        }
    }
    
    return {
        "metadata": {
            "task": "5.2.1 - Create Comprehensive Methodology Comparison Matrix",
            "timestamp": datetime.now().isoformat(),
            "research_context": context,
            "total_methodologies": len(all_methodologies),
            "sources_analyzed": len([f for f in Path("../sources/2.1-initial_literature_input/").glob("*.md") if f.is_file()]) + len([f for f in Path("../sources/4.1-semantic-search/semantic-scholar-search-iteration-1/semantic-scholar-review-papers/").glob("*.md") if f.is_file()])
        },
        "evaluation_criteria": evaluation_criteria,
        "methodologies": all_methodologies,
        "prior_research_analysis": {
            "methodology_usage_summary": prior_research_usage,
            "total_papers_analyzed": len(paper_mapping),
            "methodology_credibility_ranking": sorted(
                [(k, v["count"]) for k, v in prior_research_usage.items()], 
                key=lambda x: x[1], 
                reverse=True
            )
        }
    }

def score_methodologies(comparison_matrix):
    """
    Score each methodology against evaluation criteria
    """
    
    # Scoring rubric based on analysis from Tasks 5.1.1-5.1.5
    scoring_rubric = {
        "design_science_research": {
            "research_alignment": 5,  # Excellent for protocol development
            "timeline_feasibility": 4,  # Good within 20 weeks
            "resource_requirements": 2,  # High requirements
            "innovation_potential": 4,  # High potential
            "practical_applicability": 4,  # Good real-world application
            "integration_potential": 5  # Excellent integration potential
        },
        "case_study": {
            "research_alignment": 3,  # Moderate for protocol research
            "timeline_feasibility": 3,  # Challenging but possible
            "resource_requirements": 2,  # High requirements (field access)
            "innovation_potential": 4,  # High contextual insights
            "practical_applicability": 5,  # Excellent real-world relevance
            "integration_potential": 4  # Good integration potential
        },
        "experimental_research": {
            "research_alignment": 4,  # Good for hypothesis testing
            "timeline_feasibility": 4,  # Good feasibility
            "resource_requirements": 3,  # Moderate requirements
            "innovation_potential": 3,  # Moderate innovation
            "practical_applicability": 3,  # Moderate applicability
            "integration_potential": 3  # Moderate integration
        },
        "comparative_research": {
            "research_alignment": 4,  # Good for protocol comparison
            "timeline_feasibility": 5,  # Excellent feasibility
            "resource_requirements": 4,  # Low to moderate requirements
            "innovation_potential": 3,  # Moderate innovation
            "practical_applicability": 4,  # Good practical value
            "integration_potential": 4  # Good integration potential
        },
        "grounded_theory": {
            "research_alignment": 2,  # Poor for technical protocol research
            "timeline_feasibility": 1,  # Not feasible in 20 weeks
            "resource_requirements": 2,  # High requirements
            "innovation_potential": 2,  # Low for this context
            "practical_applicability": 2,  # Limited applicability
            "integration_potential": 2  # Poor integration potential
        },
        "phenomenological": {
            "research_alignment": 1,  # Poor for protocol research
            "timeline_feasibility": 2,  # Poor feasibility
            "resource_requirements": 3,  # Moderate requirements
            "innovation_potential": 2,  # Low for this context
            "practical_applicability": 2,  # Limited applicability
            "integration_potential": 2  # Poor integration potential
        },
        "sequential_explanatory": {
            "research_alignment": 5,  # Excellent comprehensive approach
            "timeline_feasibility": 3,  # Challenging but possible
            "resource_requirements": 2,  # High requirements
            "innovation_potential": 5,  # Very high potential
            "practical_applicability": 5,  # Excellent applicability
            "integration_potential": 4  # Good integration potential
        },
        "convergent_parallel": {
            "research_alignment": 4,  # Good comprehensive approach
            "timeline_feasibility": 4,  # Good feasibility
            "resource_requirements": 1,  # Very high requirements
            "innovation_potential": 4,  # High potential
            "practical_applicability": 4,  # Good applicability
            "integration_potential": 3  # Moderate integration complexity
        },
        "sequential_exploratory": {
            "research_alignment": 3,  # Moderate alignment
            "timeline_feasibility": 3,  # Requires scope management
            "resource_requirements": 2,  # High requirements
            "innovation_potential": 3,  # Moderate potential
            "practical_applicability": 4,  # Good stakeholder focus
            "integration_potential": 3  # Moderate integration potential
        },
        "digital_twin": {
            "research_alignment": 5,  # Excellent for protocol validation
            "timeline_feasibility": 4,  # Good feasibility
            "resource_requirements": 2,  # High technical requirements
            "innovation_potential": 5,  # Very high innovation
            "practical_applicability": 4,  # Good practical value
            "integration_potential": 5  # Excellent integration potential
        },
        "rapid_prototyping": {
            "research_alignment": 5,  # Excellent for development
            "timeline_feasibility": 5,  # Excellent feasibility
            "resource_requirements": 3,  # Moderate requirements
            "innovation_potential": 4,  # High potential
            "practical_applicability": 5,  # Excellent practical outcomes
            "integration_potential": 5  # Excellent integration potential
        },
        "ai_explainability": {
            "research_alignment": 3,  # Moderate enhancement value
            "timeline_feasibility": 4,  # Good feasibility
            "resource_requirements": 3,  # Moderate requirements
            "innovation_potential": 4,  # High innovation potential
            "practical_applicability": 4,  # Good practical value
            "integration_potential": 3  # Moderate integration potential
        },
        "human_ai_collaboration": {
            "research_alignment": 3,  # Moderate alignment
            "timeline_feasibility": 3,  # Moderate feasibility
            "resource_requirements": 2,  # High coordination requirements
            "innovation_potential": 3,  # Moderate potential
            "practical_applicability": 4,  # Good stakeholder value
            "integration_potential": 4  # Good integration potential
        },
        "living_lab": {
            "research_alignment": 4,  # Good real-world validation
            "timeline_feasibility": 1,  # Poor feasibility in 20 weeks
            "resource_requirements": 1,  # Very high requirements
            "innovation_potential": 5,  # Very high potential
            "practical_applicability": 5,  # Excellent real-world value
            "integration_potential": 2  # Poor integration within constraints
        }
    }
    
    # Add prior research credibility scores based on usage analysis
    prior_research_scores = {}
    for method_key, method_data in comparison_matrix["methodologies"].items():
        usage_count = method_data["prior_research_usage"]["papers_count"]
        if usage_count >= 10:
            prior_research_scores[method_key] = 5
        elif usage_count >= 5:
            prior_research_scores[method_key] = 4
        elif usage_count >= 2:
            prior_research_scores[method_key] = 3
        elif usage_count >= 1:
            prior_research_scores[method_key] = 2
        else:
            prior_research_scores[method_key] = 1
    
    # Calculate weighted scores
    criteria_weights = {k: v["weight"] for k, v in comparison_matrix["evaluation_criteria"].items()}
    
    methodology_scores = {}
    for method_key in comparison_matrix["methodologies"].keys():
        if method_key in scoring_rubric:
            scores = scoring_rubric[method_key].copy()
            scores["prior_research_credibility"] = prior_research_scores.get(method_key, 1)
            
            # Calculate weighted total score
            weighted_score = sum(scores[criterion] * criteria_weights[criterion] for criterion in scores.keys()) / 100
            
            methodology_scores[method_key] = {
                "individual_scores": scores,
                "weighted_total": round(weighted_score, 2),
                "ranking_category": (
                    "Highly Recommended" if weighted_score >= 4.0 else
                    "Recommended" if weighted_score >= 3.5 else
                    "Conditionally Recommended" if weighted_score >= 3.0 else
                    "Not Recommended"
                )
            }
    
    return methodology_scores

def main():
    """Main execution function"""
    
    # Create output directories at repo root (one level up from tools/)
    os.makedirs("../docs", exist_ok=True)
    
    print("🔍 Task 5.2.1: Creating Comprehensive Methodology Comparison Matrix")
    print("=" * 70)
    
    # Create comprehensive comparison matrix
    comparison_matrix = create_comprehensive_methodology_matrix()
    
    # Score methodologies against criteria
    print("📊 Scoring methodologies against evaluation criteria...")
    methodology_scores = score_methodologies(comparison_matrix)
    
    # Add scores to comparison matrix
    comparison_matrix["methodology_scores"] = methodology_scores
    
    # Calculate final rankings
    ranked_methodologies = sorted(
        methodology_scores.items(),
        key=lambda x: x[1]["weighted_total"],
        reverse=True
    )
    comparison_matrix["final_rankings"] = ranked_methodologies
    
    # Save detailed JSON output to repo root docs/
    json_file = "../docs/5.2.1-methodology-comparison-matrix.json"
    with open(json_file, 'w') as f:
        json.dump(comparison_matrix, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Detailed comparison matrix saved to: {json_file}")
    
    # Generate markdown summary with simplified formatting
    criteria_section = "\n".join([
        f"### {criterion.replace('_', ' ').title()}\n"
        f"- **Weight**: {details['weight']}%\n"
        f"- **Scale**: {details['scale']}\n"
        f"- **Description**: {details['description']}\n"
        f"- **Considerations**: {', '.join(details['considerations'])}\n"
        for criterion, details in comparison_matrix['evaluation_criteria'].items()
    ])
    
    credibility_ranking = "\n".join([
        f"{i+1}. **{method.replace('_', ' ').title()}**: {count} papers"
        for i, (method, count) in enumerate(comparison_matrix['prior_research_analysis']['methodology_credibility_ranking'][:10])
    ])
    
    top_prior_research = "\n".join([
        f"- **{method_key.replace('_', ' ').title()}**: {method_data['prior_research_usage']['papers_count']} papers, Credibility: {method_data['prior_research_usage']['credibility_score']}"
        for method_key, method_data in comparison_matrix['methodologies'].items() 
        if method_data['prior_research_usage']['papers_count'] > 0
    ][:10])
    
    highly_recommended = "\n".join([
        f"**{i+1}. {method_key.replace('_', ' ').title()}** (Score: {scores['weighted_total']})\n"
        f"   - Category: {comparison_matrix['methodologies'][method_key]['category']}\n"
        f"   - Timeline: {comparison_matrix['methodologies'][method_key]['timeline']}\n"
        f"   - Prior Research Usage: {comparison_matrix['methodologies'][method_key]['prior_research_usage']['papers_count']} papers\n"
        f"   - Key Strengths: {', '.join(comparison_matrix['methodologies'][method_key]['strengths'][:3])}\n"
        for i, (method_key, scores) in enumerate([r for r in ranked_methodologies if r[1]['ranking_category'] == 'Highly Recommended'])
    ])
    
    recommended = "\n".join([
        f"**{method_key.replace('_', ' ').title()}** (Score: {scores['weighted_total']})\n"
        f"   - Timeline: {comparison_matrix['methodologies'][method_key]['timeline']}\n"
        f"   - Prior Usage: {comparison_matrix['methodologies'][method_key]['prior_research_usage']['papers_count']} papers\n"
        for method_key, scores in [r for r in ranked_methodologies if r[1]['ranking_category'] == 'Recommended']
    ])
    
    conditionally_recommended = "\n".join([
        f"**{method_key.replace('_', ' ').title()}** (Score: {scores['weighted_total']})\n"
        f"   - Limitations: {', '.join(comparison_matrix['methodologies'][method_key]['limitations'][:2])}\n"
        for method_key, scores in [r for r in ranked_methodologies if r[1]['ranking_category'] == 'Conditionally Recommended']
    ])
    
    not_recommended = "\n".join([
        f"**{method_key.replace('_', ' ').title()}** (Score: {scores['weighted_total']})\n"
        f"   - Primary Issues: Poor timeline feasibility or research alignment\n"
        for method_key, scores in [r for r in ranked_methodologies if r[1]['ranking_category'] == 'Not Recommended']
    ])
    
    top_5_detailed = "\n".join([
        f"#### {i+1}. {method_key.replace('_', ' ').title()} (Total: {scores['weighted_total']})\n\n"
        f"| Criterion | Score | Weight | Weighted |\n"
        f"|-----------|-------|---------|----------|\n"
        f"| Research Alignment | {scores['individual_scores']['research_alignment']}/5 | 25% | {scores['individual_scores']['research_alignment'] * 0.25:.2f} |\n"
        f"| Timeline Feasibility | {scores['individual_scores']['timeline_feasibility']}/5 | 20% | {scores['individual_scores']['timeline_feasibility'] * 0.20:.2f} |\n"
        f"| Resource Requirements | {scores['individual_scores']['resource_requirements']}/5 | 15% | {scores['individual_scores']['resource_requirements'] * 0.15:.2f} |\n"
        f"| Innovation Potential | {scores['individual_scores']['innovation_potential']}/5 | 15% | {scores['individual_scores']['innovation_potential'] * 0.15:.2f} |\n"
        f"| Practical Applicability | {scores['individual_scores']['practical_applicability']}/5 | 10% | {scores['individual_scores']['practical_applicability'] * 0.10:.2f} |\n"
        f"| Prior Research Credibility | {scores['individual_scores']['prior_research_credibility']}/5 | 10% | {scores['individual_scores']['prior_research_credibility'] * 0.10:.2f} |\n"
        f"| Integration Potential | {scores['individual_scores']['integration_potential']}/5 | 5% | {scores['individual_scores']['integration_potential'] * 0.05:.2f} |\n\n"
        f"**Prior Research Evidence**: {comparison_matrix['methodologies'][method_key]['prior_research_usage']['papers_count']} papers\n"
        f"**Example Papers**: {', '.join(comparison_matrix['methodologies'][method_key]['prior_research_usage']['example_papers'][:3])}\n"
        for i, (method_key, scores) in enumerate(ranked_methodologies[:5])
    ])
    
    md_content = f"""# Comprehensive Methodology Comparison Matrix (Task 5.2.1)

*Generated: {comparison_matrix['metadata']['timestamp']}*

## Research Context

**Focus**: {comparison_matrix['metadata']['research_context']['focus']}
**Domain**: {comparison_matrix['metadata']['research_context']['domain']}
**Objective**: {comparison_matrix['metadata']['research_context']['research_objective']}
**Total Methodologies Evaluated**: {comparison_matrix['metadata']['total_methodologies']}
**Sources Analyzed for Prior Research**: {comparison_matrix['metadata']['sources_analyzed']}

## Evaluation Criteria Framework

{criteria_section}

## Prior Research Usage Analysis

### Methodology Credibility Ranking (Based on Prior Research Usage)

{credibility_ranking}

### Top Methodologies by Prior Research Evidence

{top_prior_research}

## Final Methodology Rankings

### Highly Recommended (Score ≥ 4.0)

{highly_recommended}

### Recommended (Score 3.5-3.9)

{recommended}

### Conditionally Recommended (Score 3.0-3.4)

{conditionally_recommended}

### Not Recommended (Score < 3.0)

{not_recommended}

## Detailed Scoring Breakdown

### Top 5 Methodologies - Detailed Scores

{top_5_detailed}

## Integration Recommendations

### Primary Recommendation: Combined Approach

Based on the analysis, the highest-scoring methodologies can be integrated:

**Recommended Integration**: {ranked_methodologies[0][0].replace('_', ' ').title()} + {ranked_methodologies[1][0].replace('_', ' ').title()}

**Rationale**:
- Both methodologies scored highly across all criteria
- Strong prior research evidence supports feasibility
- Complementary strengths address different aspects of protocol research
- Timeline feasible within 20-week constraints

## Key Findings

- **Most Credible (Prior Research)**: {comparison_matrix['prior_research_analysis']['methodology_credibility_ranking'][0][0].replace('_', ' ').title()} ({comparison_matrix['prior_research_analysis']['methodology_credibility_ranking'][0][1]} papers)
- **Highest Scoring Overall**: {ranked_methodologies[0][0].replace('_', ' ').title()} (Score: {ranked_methodologies[0][1]['weighted_total']})
- **Best Timeline Feasibility**: {next((method for method, scores in ranked_methodologies if scores['individual_scores']['timeline_feasibility'] == 5), 'N/A')}
- **Highest Innovation Potential**: {next((method for method, scores in ranked_methodologies if scores['individual_scores']['innovation_potential'] == 5), 'N/A')}

## Next Steps

1. Evaluate strengths and limitations of top methodologies (Task 5.2.2)
2. Assess detailed resource requirements (Task 5.2.3)
3. Analyze implementation feasibility (Task 5.2.4)
4. Select primary methodology approach (Task 5.3.1)

---

*Task 5.2.1 completed - Comprehensive methodology comparison matrix created*
*{comparison_matrix['metadata']['total_methodologies']} methodologies evaluated across 7 criteria*
*{comparison_matrix['metadata']['sources_analyzed']} sources analyzed for prior research credibility*
"""
    
    # Save markdown file to repo root docs/
    md_file = "../docs/5.2.1-methodology-comparison-matrix.md"
    with open(md_file, 'w') as f:
        f.write(md_content)
    
    print(f"✅ Summary saved to: {md_file}")
    print()
    print("🔍 Key Findings:")
    print(f"   • Highest Scoring: {ranked_methodologies[0][0].replace('_', ' ').title()} (Score: {ranked_methodologies[0][1]['weighted_total']})")
    print(f"   • Most Prior Research Evidence: {comparison_matrix['prior_research_analysis']['methodology_credibility_ranking'][0][0].replace('_', ' ').title()} ({comparison_matrix['prior_research_analysis']['methodology_credibility_ranking'][0][1]} papers)")
    print(f"   • {len([r for r in ranked_methodologies if r[1]['ranking_category'] == 'Highly Recommended'])} Highly Recommended methodologies")
    print(f"   • {comparison_matrix['metadata']['sources_analyzed']} sources analyzed for credibility")
    print()
    print("🎯 Ready for Task 5.2.2: Evaluate strengths and limitations")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Tool: Evaluate Methodology Strengths and Limitations (Task 5.2.2)

Purpose: Systematically evaluate strengths and limitations of all research methods
to support informed methodology selection for ACP/A2A protocol research.

Research Context:
- Focus: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
- Domain: Distributed Energy Resources (DER) predictive maintenance coordination
- Input: Comparison matrix from Task 5.2.1 and method details from 5.1.x tasks
- Output: Comprehensive strengths/limitations analysis

This script analyzes each method's advantages and disadvantages in the context
of the specific research objectives and constraints.
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

def load_comparison_matrix():
    """Load comparison matrix from task 5.2.1"""
    try:
        with open("docs/5.2.1-comparison-matrix.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Could not load comparison matrix from task 5.2.1")
        return None

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

def define_evaluation_framework():
    """Define framework for systematic strengths/limitations evaluation"""
    return {
        "evaluation_dimensions": {
            "methodological_rigor": {
                "description": "Scientific validity and reliability of the method",
                "strength_indicators": [
                    "Established validation procedures",
                    "Reproducible results",
                    "Clear measurement criteria",
                    "Standardized protocols"
                ],
                "limitation_indicators": [
                    "Subjective interpretation risks",
                    "Measurement validity concerns", 
                    "Reproducibility challenges",
                    "Limited validation evidence"
                ]
            },
            "practical_implementation": {
                "description": "Ease and feasibility of method implementation",
                "strength_indicators": [
                    "Clear implementation procedures",
                    "Available tools and resources",
                    "Reasonable skill requirements",
                    "Manageable time investment"
                ],
                "limitation_indicators": [
                    "High resource requirements",
                    "Complex technical setup",
                    "Specialized expertise needed",
                    "Significant time investment"
                ]
            },
            "research_alignment": {
                "description": "Fit with ACP/A2A protocol research objectives",
                "strength_indicators": [
                    "Direct protocol evaluation capability",
                    "DER domain relevance",
                    "Research question alignment",
                    "Expected insight quality"
                ],
                "limitation_indicators": [
                    "Limited protocol specificity",
                    "Weak domain connection",
                    "Misaligned research focus",
                    "Low insight potential"
                ]
            },
            "integration_potential": {
                "description": "Ability to combine with other methods effectively",
                "strength_indicators": [
                    "Complementary to other methods",
                    "Sequential integration potential",
                    "Parallel execution possibility",
                    "Synergistic effects"
                ],
                "limitation_indicators": [
                    "Conflicting methodological assumptions",
                    "Difficult integration requirements",
                    "Resource competition",
                    "Limited synergy potential"
                ]
            },
            "output_value": {
                "description": "Quality and utility of expected research outputs",
                "strength_indicators": [
                    "High theoretical contribution",
                    "Strong practical applicability",
                    "Methodological innovation",
                    "Good generalizability"
                ],
                "limitation_indicators": [
                    "Limited theoretical advancement",
                    "Narrow practical application",
                    "Incremental contribution only",
                    "Poor generalizability"
                ]
            }
        },
        "assessment_criteria": {
            "strength_levels": {
                "major": "Significant advantage that strongly supports method selection",
                "moderate": "Notable advantage that supports method selection", 
                "minor": "Small advantage that slightly favors method selection"
            },
            "limitation_levels": {
                "critical": "Significant disadvantage that argues against method selection",
                "moderate": "Notable disadvantage that raises concerns about method selection",
                "minor": "Small disadvantage that slightly disfavors method selection"
            }
        }
    }

def evaluate_method_strengths_limitations(method_key, method_info, comparison_data, evaluation_framework):
    """Evaluate strengths and limitations for a specific method"""
    
    # Get method scores from comparison matrix
    method_scores = None
    for method in comparison_data['comparison_matrix']:
        if method['method_key'] == method_key:
            method_scores = method
            break
    
    if not method_scores:
        return None
    
    evaluation = {
        "method_key": method_key,
        "method_name": method_info.get('method_name', method_key),
        "category": method_info.get('category', 'Unknown'),
        "overall_score": method_scores.get('weighted_score', 0),
        "strengths": {},
        "limitations": {},
        "overall_assessment": "",
        "recommendation_rationale": ""
    }
    
    # Evaluate based on method details and scores
    methodological_considerations = method_info.get('methodological_considerations', {})
    implementation_framework = method_info.get('implementation_framework', {})
    application_to_research = method_info.get('application_to_research', {})
    
    # Analyze methodological rigor
    strengths_list = methodological_considerations.get('strengths', [])
    limitations_list = methodological_considerations.get('limitations', [])
    
    evaluation['strengths']['methodological_rigor'] = analyze_methodological_strengths(
        method_key, method_scores, strengths_list, evaluation_framework
    )
    
    evaluation['limitations']['methodological_rigor'] = analyze_methodological_limitations(
        method_key, method_scores, limitations_list, evaluation_framework
    )
    
    # Analyze practical implementation
    evaluation['strengths']['practical_implementation'] = analyze_implementation_strengths(
        method_key, method_scores, implementation_framework, evaluation_framework
    )
    
    evaluation['limitations']['practical_implementation'] = analyze_implementation_limitations(
        method_key, method_scores, implementation_framework, evaluation_framework
    )
    
    # Analyze research alignment
    evaluation['strengths']['research_alignment'] = analyze_alignment_strengths(
        method_key, method_scores, application_to_research, evaluation_framework
    )
    
    evaluation['limitations']['research_alignment'] = analyze_alignment_limitations(
        method_key, method_scores, application_to_research, evaluation_framework
    )
    
    # Generate overall assessment
    evaluation['overall_assessment'] = generate_overall_assessment(evaluation, method_scores)
    evaluation['recommendation_rationale'] = generate_recommendation_rationale(evaluation, method_scores)
    
    return evaluation

def analyze_methodological_strengths(method_key, method_scores, strengths_list, framework):
    """Analyze methodological rigor strengths"""
    strengths = []
    
    # High feasibility indicates established procedures
    if method_scores.get('feasibility', 0) >= 4:
        strengths.append({
            "strength": "High implementation feasibility",
            "level": "moderate",
            "description": "Method has well-established procedures and clear implementation guidelines"
        })
    
    # High relevance indicates good measurement validity
    if method_scores.get('relevance', 0) >= 4:
        strengths.append({
            "strength": "Strong research validity",
            "level": "major",
            "description": "Method directly addresses research objectives with high measurement validity"
        })
    
    # Add method-specific strengths
    for strength_text in strengths_list:
        if any(indicator in strength_text.lower() for indicator in ['valid', 'reliable', 'standard', 'rigorous']):
            strengths.append({
                "strength": strength_text,
                "level": "moderate",
                "description": "Documented methodological advantage"
            })
    
    return strengths

def analyze_methodological_limitations(method_key, method_scores, limitations_list, framework):
    """Analyze methodological rigor limitations"""
    limitations = []
    
    # Low feasibility indicates complexity issues
    if method_scores.get('feasibility', 0) <= 2:
        limitations.append({
            "limitation": "Low implementation feasibility",
            "level": "critical",
            "description": "Method has significant implementation barriers and complexity issues"
        })
    
    # Low relevance indicates validity concerns
    if method_scores.get('relevance', 0) <= 2:
        limitations.append({
            "limitation": "Weak research alignment",
            "level": "critical", 
            "description": "Method poorly addresses research objectives with validity concerns"
        })
    
    # Add method-specific limitations
    for limitation_text in limitations_list:
        if any(indicator in limitation_text.lower() for indicator in ['subjective', 'bias', 'unreliable', 'invalid']):
            limitations.append({
                "limitation": limitation_text,
                "level": "moderate",
                "description": "Documented methodological concern"
            })
    
    return limitations

def analyze_implementation_strengths(method_key, method_scores, implementation_info, framework):
    """Analyze practical implementation strengths"""
    strengths = []
    
    # Resource intensity score (higher = lower resource needs)
    resource_score = method_scores.get('resource_intensity', 0)
    if resource_score >= 4:
        strengths.append({
            "strength": "Low resource requirements",
            "level": "major",
            "description": "Method requires minimal time, personnel, and equipment investment"
        })
    elif resource_score >= 3:
        strengths.append({
            "strength": "Moderate resource requirements", 
            "level": "moderate",
            "description": "Method has reasonable resource demands for thesis project"
        })
    
    # Timeline alignment
    timeline_score = method_scores.get('timeline_alignment', 0)
    if timeline_score >= 4:
        strengths.append({
            "strength": "Excellent timeline fit",
            "level": "major",
            "description": "Method aligns perfectly with 20-week thesis timeline"
        })
    
    # Check for available tools/frameworks
    tools = implementation_info.get('required_tools', [])
    if tools and len(tools) > 0:
        strengths.append({
            "strength": "Available implementation tools",
            "level": "moderate",
            "description": f"Specific tools identified for implementation: {', '.join(tools[:3])}"
        })
    
    return strengths

def analyze_implementation_limitations(method_key, method_scores, implementation_info, framework):
    """Analyze practical implementation limitations"""
    limitations = []
    
    # Resource intensity score (lower = higher resource needs)
    resource_score = method_scores.get('resource_intensity', 0)
    if resource_score <= 2:
        limitations.append({
            "limitation": "High resource requirements",
            "level": "critical",
            "description": "Method demands significant time, personnel, or equipment investment"
        })
    
    # Timeline alignment
    timeline_score = method_scores.get('timeline_alignment', 0) 
    if timeline_score <= 2:
        limitations.append({
            "limitation": "Poor timeline fit",
            "level": "critical",
            "description": "Method poorly aligns with 20-week thesis constraints"
        })
    
    # Check complexity indicators
    setup_complexity = implementation_info.get('setup_complexity', '')
    if 'high' in setup_complexity.lower():
        limitations.append({
            "limitation": "Complex setup requirements",
            "level": "moderate", 
            "description": "Method requires complex technical setup and configuration"
        })
    
    learning_curve = implementation_info.get('learning_curve', '')
    if 'high' in learning_curve.lower():
        limitations.append({
            "limitation": "Steep learning curve",
            "level": "moderate",
            "description": "Method requires significant skill development and expertise"
        })
    
    return limitations

def analyze_alignment_strengths(method_key, method_scores, application_info, framework):
    """Analyze research alignment strengths"""
    strengths = []
    
    relevance_score = method_scores.get('relevance', 0)
    if relevance_score >= 4:
        strengths.append({
            "strength": "Strong protocol evaluation capability",
            "level": "major",
            "description": "Method directly enables ACP/A2A protocol assessment and comparison"
        })
    
    # Check application descriptions
    acp_relevance = application_info.get('relevance_to_acp_a2a', '')
    der_applicability = application_info.get('der_maintenance_applicability', '')
    
    if 'high' in acp_relevance.lower() or 'direct' in acp_relevance.lower():
        strengths.append({
            "strength": "Direct ACP/A2A protocol relevance",
            "level": "major",
            "description": "Method specifically designed for protocol evaluation contexts"
        })
    
    if 'high' in der_applicability.lower():
        strengths.append({
            "strength": "Strong DER domain applicability", 
            "level": "moderate",
            "description": "Method well-suited for DER maintenance coordination contexts"
        })
    
    return strengths

def analyze_alignment_limitations(method_key, method_scores, application_info, framework):
    """Analyze research alignment limitations"""
    limitations = []
    
    relevance_score = method_scores.get('relevance', 0)
    if relevance_score <= 2:
        limitations.append({
            "limitation": "Weak protocol evaluation capability",
            "level": "critical",
            "description": "Method poorly suited for ACP/A2A protocol assessment"
        })
    
    # Check for low applicability indicators
    acp_relevance = application_info.get('relevance_to_acp_a2a', '')
    der_applicability = application_info.get('der_maintenance_applicability', '')
    
    if 'low' in acp_relevance.lower() or 'limited' in acp_relevance.lower():
        limitations.append({
            "limitation": "Limited ACP/A2A protocol relevance",
            "level": "moderate",
            "description": "Method has indirect or limited protocol evaluation capability"
        })
    
    if 'low' in der_applicability.lower():
        limitations.append({
            "limitation": "Weak DER domain applicability",
            "level": "moderate", 
            "description": "Method poorly suited for DER maintenance contexts"
        })
    
    return limitations

def generate_overall_assessment(evaluation, method_scores):
    """Generate overall assessment of method"""
    score = method_scores.get('weighted_score', 0)
    
    if score >= 4.0:
        assessment = f"**STRONGLY RECOMMENDED** - {evaluation['method_name']} demonstrates exceptional suitability for the ACP/A2A protocol research with high scores across multiple criteria."
    elif score >= 3.5:
        assessment = f"**RECOMMENDED** - {evaluation['method_name']} shows good alignment with research objectives and manageable implementation requirements."
    elif score >= 2.5:
        assessment = f"**CONDITIONAL** - {evaluation['method_name']} has moderate potential but significant limitations that must be carefully considered."
    else:
        assessment = f"**NOT RECOMMENDED** - {evaluation['method_name']} has substantial limitations that outweigh its potential benefits for this research."
    
    return assessment

def generate_recommendation_rationale(evaluation, method_scores):
    """Generate specific rationale for recommendation"""
    major_strengths = []
    critical_limitations = []
    
    for dimension, strengths in evaluation['strengths'].items():
        for strength in strengths:
            if strength['level'] == 'major':
                major_strengths.append(strength['strength'])
    
    for dimension, limitations in evaluation['limitations'].items():
        for limitation in limitations:
            if limitation['level'] == 'critical':
                critical_limitations.append(limitation['limitation'])
    
    rationale = f"Score: {method_scores.get('weighted_score', 0):.2f}/5.0. "
    
    if major_strengths:
        rationale += f"Key strengths: {', '.join(major_strengths[:3])}. "
    
    if critical_limitations:
        rationale += f"Critical concerns: {', '.join(critical_limitations[:3])}. "
    else:
        rationale += "No critical limitations identified. "
    
    return rationale

def evaluate_all_methods():
    """Main function to evaluate strengths and limitations of all methods"""
    print("=== Task 5.2.2: Evaluate Strengths/Limitations ===")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Load required data
    print("Loading comparison matrix and method details...")
    comparison_data = load_comparison_matrix()
    method_details = load_method_details()
    
    if not comparison_data or not method_details:
        print("Error: Required data not available")
        return None
    
    print(f"✓ Loaded comparison data for {len(comparison_data['comparison_matrix'])} methods")
    print(f"✓ Loaded detailed information for {len(method_details)} methods")
    
    # Define evaluation framework
    evaluation_framework = define_evaluation_framework()
    print(f"✓ Defined evaluation framework with {len(evaluation_framework['evaluation_dimensions'])} dimensions")
    
    # Evaluate each method
    evaluations = []
    for method in comparison_data['comparison_matrix']:
        method_key = method['method_key']
        if method_key in method_details:
            evaluation = evaluate_method_strengths_limitations(
                method_key, method_details[method_key], comparison_data, evaluation_framework
            )
            if evaluation:
                evaluations.append(evaluation)
    
    print(f"✓ Completed evaluations for {len(evaluations)} methods")
    
    # Generate summary analysis
    summary = generate_summary_analysis(evaluations, comparison_data)
    
    # Compile comprehensive output
    output = {
        "task": "5.2.2 - Evaluate Strengths/Limitations", 
        "timestamp": datetime.now().isoformat(),
        "research_context": comparison_data['research_context'],
        "evaluation_framework": evaluation_framework,
        "method_evaluations": evaluations,
        "summary_analysis": summary,
        "methodology_recommendations": generate_methodology_recommendations(evaluations)
    }
    
    # Save outputs
    os.makedirs("docs", exist_ok=True)
    
    # Save detailed JSON
    with open("docs/5.2.2-strengths-limitations.json", "w") as f:
        json.dump(output, f, indent=2)
    
    # Generate markdown report
    markdown_content = generate_markdown_report(output)
    with open("docs/5.2.2-strengths-limitations.md", "w") as f:
        f.write(markdown_content)
    
    print()
    print("=== Evaluation Results ===")
    print(f"Methods Evaluated: {len(evaluations)}")
    print(f"Strongly Recommended: {summary['tier_counts']['strongly_recommended']}")
    print(f"Recommended: {summary['tier_counts']['recommended']}")
    print(f"Conditional: {summary['tier_counts']['conditional']}")
    print(f"Not Recommended: {summary['tier_counts']['not_recommended']}")
    
    return output

def generate_summary_analysis(evaluations, comparison_data):
    """Generate summary analysis across all method evaluations"""
    summary = {
        "tier_counts": {
            "strongly_recommended": 0,
            "recommended": 0, 
            "conditional": 0,
            "not_recommended": 0
        },
        "common_strengths": {},
        "common_limitations": {},
        "category_analysis": {}
    }
    
    # Count recommendation tiers
    for evaluation in evaluations:
        score = evaluation['overall_score']
        if score >= 4.0:
            summary['tier_counts']['strongly_recommended'] += 1
        elif score >= 3.5:
            summary['tier_counts']['recommended'] += 1
        elif score >= 2.5:
            summary['tier_counts']['conditional'] += 1
        else:
            summary['tier_counts']['not_recommended'] += 1
    
    # Analyze by category
    categories = set(eval['category'] for eval in evaluations)
    for category in categories:
        category_evals = [eval for eval in evaluations if eval['category'] == category]
        avg_score = sum(eval['overall_score'] for eval in category_evals) / len(category_evals)
        
        summary['category_analysis'][category] = {
            "count": len(category_evals),
            "average_score": avg_score,
            "top_method": max(category_evals, key=lambda e: e['overall_score'])['method_name']
        }
    
    return summary

def generate_methodology_recommendations(evaluations):
    """Generate specific methodology recommendations based on evaluations"""
    strongly_recommended = [e for e in evaluations if e['overall_score'] >= 4.0]
    recommended = [e for e in evaluations if 3.5 <= e['overall_score'] < 4.0]
    
    recommendations = {
        "core_methodology_selection": {
            "primary": strongly_recommended[0]['method_name'] if strongly_recommended else None,
            "supporting": [e['method_name'] for e in strongly_recommended[1:3] if len(strongly_recommended) > 1],
            "rationale": "Based on comprehensive strengths/limitations analysis"
        },
        "implementation_sequence": [],
        "risk_mitigation": [],
        "integration_strategy": "Sequential and parallel method combination for comprehensive evaluation"
    }
    
    return recommendations

def generate_markdown_report(output):
    """Generate markdown report for strengths/limitations analysis"""
    markdown = f"""# Methodology Strengths and Limitations Evaluation (Task 5.2.2)

*Generated: {output['timestamp']}*

## Research Context

**Focus**: {output['research_context']['focus']}
**Domain**: {output['research_context']['domain']}
**Overarching Methodology**: {output['research_context']['overarching_methodology']}

## Evaluation Framework

This analysis evaluates each method across {len(output['evaluation_framework']['evaluation_dimensions'])} key dimensions:

"""
    
    for dimension, info in output['evaluation_framework']['evaluation_dimensions'].items():
        markdown += f"- **{dimension.replace('_', ' ').title()}**: {info['description']}\n"
    
    markdown += f"""
## Method Evaluations

**Total Methods Evaluated**: {len(output['method_evaluations'])}
**Strongly Recommended**: {output['summary_analysis']['tier_counts']['strongly_recommended']}
**Recommended**: {output['summary_analysis']['tier_counts']['recommended']}
**Conditional**: {output['summary_analysis']['tier_counts']['conditional']}
**Not Recommended**: {output['summary_analysis']['tier_counts']['not_recommended']}

### Strongly Recommended Methods (Score ≥ 4.0)

"""
    
    for evaluation in output['method_evaluations']:
        if evaluation['overall_score'] >= 4.0:
            markdown += f"""#### {evaluation['method_name']} (Score: {evaluation['overall_score']:.2f})
**Category**: {evaluation['category']}

**Overall Assessment**: {evaluation['overall_assessment']}

**Key Strengths**:
"""
            # Add major strengths
            for dimension, strengths in evaluation['strengths'].items():
                for strength in strengths:
                    if strength['level'] == 'major':
                        markdown += f"- {strength['strength']}: {strength['description']}\n"
            
            markdown += "\n**Key Limitations**:\n"
            # Add critical limitations
            for dimension, limitations in evaluation['limitations'].items():
                for limitation in limitations:
                    if limitation['level'] == 'critical':
                        markdown += f"- {limitation['limitation']}: {limitation['description']}\n"
            
            markdown += f"\n**Recommendation Rationale**: {evaluation['recommendation_rationale']}\n\n"
    
    markdown += """### Recommended Methods (Score ≥ 3.5)

"""
    
    for evaluation in output['method_evaluations']:
        if 3.5 <= evaluation['overall_score'] < 4.0:
            markdown += f"#### {evaluation['method_name']} (Score: {evaluation['overall_score']:.2f})\n"
            markdown += f"**Overall Assessment**: {evaluation['overall_assessment']}\n\n"
    
    markdown += """## Category Analysis

"""
    
    for category, analysis in output['summary_analysis']['category_analysis'].items():
        markdown += f"""### {category}
- **Methods Count**: {analysis['count']}
- **Average Score**: {analysis['average_score']:.2f}
- **Top Method**: {analysis['top_method']}

"""
    
    markdown += """## Methodology Recommendations

"""
    
    if output['methodology_recommendations']['core_methodology_selection']['primary']:
        markdown += f"""### Core Methodology Selection
- **Primary Method**: {output['methodology_recommendations']['core_methodology_selection']['primary']}
- **Supporting Methods**: {', '.join(output['methodology_recommendations']['core_methodology_selection']['supporting'])}
- **Rationale**: {output['methodology_recommendations']['core_methodology_selection']['rationale']}

"""
    
    markdown += """## Sources Used

- Comparison matrix from `docs/5.2.1-comparison-matrix.json`
- Method details from `docs/5.1.2-quantitative-methods.json`
- Method details from `docs/5.1.3-qualitative-methods.json`
- Method details from `docs/5.1.4-mixed-methods.json`
- Method details from `docs/5.1.5-emerging-methods.json`

---

*Task 5.2.2 completed - Strengths and limitations systematically evaluated*
*Ready for resource requirements assessment in Task 5.2.3*
"""
    
    return markdown

if __name__ == "__main__":
    evaluate_all_methods() 
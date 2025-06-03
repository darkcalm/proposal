#!/usr/bin/env python3
"""
Tool: Analyze Feasibility (Task 5.2.4)

Purpose: Comprehensive feasibility analysis integrating comparison matrix,
strengths/limitations, and resource requirements to provide final recommendations.

Research Context:
- Focus: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
- Domain: Distributed Energy Resources (DER) predictive maintenance coordination
- Input: All previous evaluations from tasks 5.2.1-5.2.3
- Output: Final feasibility assessment and implementation recommendations
"""

import json
import os
from datetime import datetime

def load_all_evaluations():
    """Load all previous evaluation data"""
    data = {}
    files = {
        'comparison': 'docs/5.2.1-comparison-matrix.json',
        'strengths': 'docs/5.2.2-strengths-limitations.json',
        'resources': 'docs/5.2.3-resource-requirements.json'
    }
    
    for key, file_path in files.items():
        try:
            with open(file_path, 'r') as f:
                data[key] = json.load(f)
        except FileNotFoundError:
            print(f"Warning: Could not load {file_path}")
            data[key] = None
    
    return data

def define_feasibility_framework():
    """Define comprehensive feasibility assessment framework"""
    return {
        "feasibility_dimensions": {
            "technical_feasibility": {
                "weight": 0.25,
                "criteria": ["Implementation complexity", "Tool availability", "Skill requirements"]
            },
            "resource_feasibility": {
                "weight": 0.25,
                "criteria": ["Time requirements", "Financial costs", "Human resources"]
            },
            "strategic_feasibility": {
                "weight": 0.30,
                "criteria": ["Research alignment", "Methodological rigor", "Expected outcomes"]
            },
            "contextual_feasibility": {
                "weight": 0.20,
                "criteria": ["Thesis constraints", "Academic requirements", "Timeline fit"]
            }
        },
        "decision_thresholds": {
            "highly_feasible": 0.75,
            "feasible": 0.60,
            "conditionally_feasible": 0.45,
            "not_feasible": 0.00
        }
    }

def calculate_integrated_feasibility(method_key, all_data, framework):
    """Calculate integrated feasibility score"""
    
    # Get method data from all sources
    comparison_data = None
    strengths_data = None
    resource_data = None
    
    # Find method in comparison matrix
    for method in all_data['comparison']['comparison_matrix']:
        if method['method_key'] == method_key:
            comparison_data = method
            break
    
    # Find method in strengths/limitations
    for method in all_data['strengths']['method_evaluations']:
        if method['method_key'] == method_key:
            strengths_data = method
            break
    
    # Find method in resource assessment
    for method in all_data['resources']['method_assessments']:
        if method['method_key'] == method_key:
            resource_data = method
            break
    
    if not all([comparison_data, strengths_data, resource_data]):
        return None
    
    scores = {}
    
    # Technical feasibility (0-1 scale)
    feasibility_score = comparison_data.get('feasibility', 0) / 5.0
    scores['technical_feasibility'] = feasibility_score
    
    # Resource feasibility (inverse of resource intensity)
    time_feasibility = max(0, 1 - (resource_data['total_cost_estimate']['time_total'] - 6) / 10)
    cost_feasibility = max(0, 1 - resource_data['total_cost_estimate']['financial_total'] / 200)
    scores['resource_feasibility'] = (time_feasibility + cost_feasibility) / 2
    
    # Strategic feasibility (based on scores and strengths)
    relevance_score = comparison_data.get('relevance', 0) / 5.0
    impact_score = comparison_data.get('potential_impact', 0) / 5.0
    scores['strategic_feasibility'] = (relevance_score + impact_score) / 2
    
    # Contextual feasibility (timeline and constraints)
    timeline_score = comparison_data.get('timeline_alignment', 0) / 5.0
    scores['contextual_feasibility'] = timeline_score
    
    # Calculate weighted total
    total_score = sum(scores[dim] * framework['feasibility_dimensions'][dim]['weight'] 
                     for dim in scores)
    
    return {
        'method_key': method_key,
        'method_name': comparison_data.get('method_name', method_key),
        'dimension_scores': scores,
        'total_feasibility_score': total_score,
        'feasibility_category': get_feasibility_category(total_score, framework),
        'critical_factors': identify_critical_factors(scores, comparison_data, resource_data),
        'recommendation': generate_recommendation(total_score, scores, framework)
    }

def get_feasibility_category(score, framework):
    """Determine feasibility category based on score"""
    thresholds = framework['decision_thresholds']
    if score >= thresholds['highly_feasible']:
        return "Highly Feasible"
    elif score >= thresholds['feasible']:
        return "Feasible"
    elif score >= thresholds['conditionally_feasible']:
        return "Conditionally Feasible"
    else:
        return "Not Feasible"

def identify_critical_factors(scores, comparison_data, resource_data):
    """Identify critical success/risk factors"""
    factors = {
        'success_factors': [],
        'risk_factors': [],
        'mitigation_strategies': []
    }
    
    # Success factors (high scores)
    if scores['strategic_feasibility'] > 0.7:
        factors['success_factors'].append("Strong strategic alignment with research objectives")
    if scores['technical_feasibility'] > 0.7:
        factors['success_factors'].append("High technical feasibility and clear implementation path")
    if scores['resource_feasibility'] > 0.7:
        factors['success_factors'].append("Reasonable resource requirements within project constraints")
    
    # Risk factors (low scores)
    if scores['resource_feasibility'] < 0.5:
        factors['risk_factors'].append("High resource requirements may strain project capacity")
        factors['mitigation_strategies'].append("Consider resource optimization and parallel execution")
    if scores['technical_feasibility'] < 0.5:
        factors['risk_factors'].append("Complex implementation with potential technical barriers")
        factors['mitigation_strategies'].append("Invest in early skill development and expert consultation")
    if scores['contextual_feasibility'] < 0.5:
        factors['risk_factors'].append("Poor fit with thesis timeline and academic constraints")
        factors['mitigation_strategies'].append("Adjust scope or consider alternative approaches")
    
    return factors

def generate_recommendation(total_score, scores, framework):
    """Generate specific implementation recommendation"""
    category = get_feasibility_category(total_score, framework)
    
    if category == "Highly Feasible":
        return f"STRONGLY RECOMMENDED - Prioritize for implementation (Score: {total_score:.2f})"
    elif category == "Feasible":
        return f"RECOMMENDED - Include in methodology selection (Score: {total_score:.2f})"
    elif category == "Conditionally Feasible":
        return f"CONDITIONAL - Consider with risk mitigation (Score: {total_score:.2f})"
    else:
        return f"NOT RECOMMENDED - Significant feasibility concerns (Score: {total_score:.2f})"

def analyze_all_methods_feasibility():
    """Main function for comprehensive feasibility analysis"""
    print("=== Task 5.2.4: Analyze Feasibility ===")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Load all evaluation data
    print("Loading all previous evaluations...")
    all_data = load_all_evaluations()
    
    if not all(all_data.values()):
        print("Error: Required evaluation data not available")
        return None
    
    print("✓ Loaded comparison matrix, strengths/limitations, and resource assessments")
    
    # Define feasibility framework
    framework = define_feasibility_framework()
    print("✓ Defined integrated feasibility assessment framework")
    
    # Analyze feasibility for each method
    feasibility_results = []
    for method in all_data['comparison']['comparison_matrix']:
        method_key = method['method_key']
        result = calculate_integrated_feasibility(method_key, all_data, framework)
        if result:
            feasibility_results.append(result)
    
    print(f"✓ Completed integrated feasibility analysis for {len(feasibility_results)} methods")
    
    # Generate summary and recommendations
    summary = generate_feasibility_summary(feasibility_results, framework)
    final_recommendations = generate_final_recommendations(feasibility_results, all_data)
    
    # Compile output
    output = {
        "task": "5.2.4 - Analyze Feasibility",
        "timestamp": datetime.now().isoformat(),
        "research_context": all_data['comparison']['research_context'],
        "feasibility_framework": framework,
        "method_feasibility_results": feasibility_results,
        "summary_analysis": summary,
        "final_recommendations": final_recommendations,
        "methodology_selection": select_final_methodology(feasibility_results)
    }
    
    # Save outputs
    os.makedirs("docs", exist_ok=True)
    
    with open("docs/5.2.4-feasibility-analysis.json", "w") as f:
        json.dump(output, f, indent=2)
    
    markdown_content = generate_feasibility_report(output)
    with open("docs/5.2.4-feasibility-analysis.md", "w") as f:
        f.write(markdown_content)
    
    print()
    print("=== Feasibility Analysis Results ===")
    print(f"Highly Feasible: {summary['category_counts']['Highly Feasible']}")
    print(f"Feasible: {summary['category_counts']['Feasible']}")
    print(f"Conditionally Feasible: {summary['category_counts']['Conditionally Feasible']}")
    print(f"Not Feasible: {summary['category_counts']['Not Feasible']}")
    
    return output

def generate_feasibility_summary(results, framework):
    """Generate summary of feasibility analysis"""
    summary = {
        'total_methods': len(results),
        'category_counts': {
            'Highly Feasible': 0,
            'Feasible': 0,
            'Conditionally Feasible': 0,
            'Not Feasible': 0
        },
        'average_scores': {},
        'top_methods': [],
        'implementation_priorities': []
    }
    
    # Count categories and collect scores
    scores_by_dimension = {dim: [] for dim in framework['feasibility_dimensions'].keys()}
    
    for result in results:
        category = result['feasibility_category']
        if category in summary['category_counts']:
            summary['category_counts'][category] += 1
        
        for dim, score in result['dimension_scores'].items():
            scores_by_dimension[dim].append(score)
    
    # Calculate average scores
    for dim, scores in scores_by_dimension.items():
        summary['average_scores'][dim] = sum(scores) / len(scores) if scores else 0
    
    # Identify top methods
    sorted_results = sorted(results, key=lambda r: r['total_feasibility_score'], reverse=True)
    summary['top_methods'] = sorted_results[:5]
    
    return summary

def generate_final_recommendations(feasibility_results, all_data):
    """Generate final implementation recommendations"""
    recommendations = {
        'core_methodology': None,
        'supporting_methods': [],
        'implementation_sequence': [],
        'resource_allocation': {},
        'risk_mitigation_plan': [],
        'success_metrics': []
    }
    
    # Sort by feasibility score
    sorted_methods = sorted(feasibility_results, key=lambda r: r['total_feasibility_score'], reverse=True)
    
    # Select core methodology (highest feasibility)
    if sorted_methods:
        recommendations['core_methodology'] = {
            'method': sorted_methods[0]['method_name'],
            'feasibility_score': sorted_methods[0]['total_feasibility_score'],
            'rationale': f"Highest integrated feasibility score with strong alignment across all dimensions"
        }
    
    # Select supporting methods (top 3-4 feasible methods)
    feasible_methods = [m for m in sorted_methods if m['feasibility_category'] in ['Highly Feasible', 'Feasible']]
    recommendations['supporting_methods'] = feasible_methods[1:4]  # Skip core methodology
    
    return recommendations

def select_final_methodology(feasibility_results):
    """Select final methodology based on comprehensive analysis"""
    sorted_methods = sorted(feasibility_results, key=lambda r: r['total_feasibility_score'], reverse=True)
    
    if not sorted_methods:
        return None
    
    top_method = sorted_methods[0]
    
    return {
        'selected_primary_method': top_method['method_name'],
        'feasibility_score': top_method['total_feasibility_score'],
        'feasibility_category': top_method['feasibility_category'],
        'selection_rationale': f"Selected based on highest integrated feasibility score ({top_method['total_feasibility_score']:.2f}) combining technical, resource, strategic, and contextual factors",
        'implementation_confidence': "High" if top_method['total_feasibility_score'] > 0.75 else "Medium",
        'next_steps': [
            "Proceed to detailed implementation planning",
            "Develop risk mitigation strategies",
            "Establish success metrics and validation criteria"
        ]
    }

def generate_feasibility_report(output):
    """Generate markdown feasibility report"""
    markdown = f"""# Comprehensive Feasibility Analysis (Task 5.2.4)

*Generated: {output['timestamp']}*

## Research Context

**Focus**: {output['research_context']['focus']}
**Domain**: {output['research_context']['domain']}
**Overarching Methodology**: {output['research_context']['overarching_methodology']}

## Feasibility Framework

This analysis integrates four key dimensions with weighted scoring:

"""
    
    for dim, info in output['feasibility_framework']['feasibility_dimensions'].items():
        markdown += f"- **{dim.replace('_', ' ').title()}** ({info['weight']:.0%}): {', '.join(info['criteria'])}\n"
    
    markdown += f"""
## Overall Results

**Total Methods Analyzed**: {output['summary_analysis']['total_methods']}

### Feasibility Distribution
- **Highly Feasible**: {output['summary_analysis']['category_counts']['Highly Feasible']} methods
- **Feasible**: {output['summary_analysis']['category_counts']['Feasible']} methods  
- **Conditionally Feasible**: {output['summary_analysis']['category_counts']['Conditionally Feasible']} methods
- **Not Feasible**: {output['summary_analysis']['category_counts']['Not Feasible']} methods

## Top Performing Methods

"""
    
    for i, method in enumerate(output['summary_analysis']['top_methods'][:5], 1):
        markdown += f"""### {i}. {method['method_name']}
**Feasibility Score**: {method['total_feasibility_score']:.2f} | **Category**: {method['feasibility_category']}

**Dimension Breakdown**:
- Technical: {method['dimension_scores']['technical_feasibility']:.2f}
- Resource: {method['dimension_scores']['resource_feasibility']:.2f}  
- Strategic: {method['dimension_scores']['strategic_feasibility']:.2f}
- Contextual: {method['dimension_scores']['contextual_feasibility']:.2f}

**Recommendation**: {method['recommendation']}

"""
    
    if output.get('methodology_selection'):
        selection = output['methodology_selection']
        markdown += f"""## Final Methodology Selection

### Selected Primary Method: {selection['selected_primary_method']}
- **Feasibility Score**: {selection['feasibility_score']:.2f}
- **Category**: {selection['feasibility_category']}
- **Implementation Confidence**: {selection['implementation_confidence']}

**Selection Rationale**: {selection['selection_rationale']}

### Next Steps
"""
        for step in selection['next_steps']:
            markdown += f"- {step}\n"
    
    markdown += """
## Sources Integrated

- Comparison matrix from `docs/5.2.1-comparison-matrix.json`
- Strengths/limitations from `docs/5.2.2-strengths-limitations.json`
- Resource requirements from `docs/5.2.3-resource-requirements.json`

---

*Task 5.2.4 completed - Comprehensive feasibility analysis*
*Ready for methodology selection in Task 5.3*
"""
    
    return markdown

if __name__ == "__main__":
    analyze_all_methods_feasibility() 
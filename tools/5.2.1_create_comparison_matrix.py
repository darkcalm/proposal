#!/usr/bin/env python3
"""
Tool: Create Methodology Comparison Matrix (Task 5.2.1)

Purpose: Systematically compare all identified research methods across standardized criteria
to support methodology selection for the ACP/A2A protocol research.

Research Context:
- Focus: Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)
- Domain: Distributed Energy Resources (DER) predictive maintenance coordination
- Overarching Methodology: Design Science Research (established)
- Comparison Scope: All methods documented in tasks 5.1.1-5.1.5

This script creates a comprehensive comparison matrix using consistent evaluation criteria
and generates both tabular and analytical outputs for methodology selection.
"""

import json
import os
import csv
import statistics
from datetime import datetime
from typing import Dict, List, Tuple, Optional

def load_method_data():
    """Load all method data from tasks 5.1.1-5.1.5"""
    method_data = {}
    
    # Load from each task's JSON output
    for task_num in ['5.1.1', '5.1.2', '5.1.3', '5.1.4', '5.1.5']:
        json_files = {
            '5.1.1': 'docs/5.1.1-relevant-methods.json',
            '5.1.2': 'docs/5.1.2-quantitative-methods.json', 
            '5.1.3': 'docs/5.1.3-qualitative-methods.json',
            '5.1.4': 'docs/5.1.4-mixed-methods.json',
            '5.1.5': 'docs/5.1.5-emerging-methods.json'
        }
        
        try:
            with open(json_files[task_num], 'r') as f:
                task_data = json.load(f)
                if 'documented_methods' in task_data:
                    for method_key, method_info in task_data['documented_methods'].items():
                        method_data[method_key] = method_info
                elif 'methods' in task_data:
                    for method_key, method_info in task_data['methods'].items():
                        method_data[method_key] = method_info
        except FileNotFoundError:
            print(f"Warning: Could not load {json_files[task_num]}")
    
    return method_data

def define_comparison_criteria():
    """Define standardized comparison criteria for all methods"""
    return {
        "feasibility": {
            "description": "Practical implementability within thesis constraints",
            "scale": "1-5 (1=Very Difficult, 5=Very Easy)",
            "weight": 0.25,
            "sub_criteria": [
                "Resource requirements",
                "Technical complexity", 
                "Access to data/tools",
                "Timeline compatibility"
            ]
        },
        "relevance": {
            "description": "Direct alignment with ACP/A2A protocol research objectives",
            "scale": "1-5 (1=Poor Fit, 5=Perfect Fit)",
            "weight": 0.30,
            "sub_criteria": [
                "Protocol evaluation capability",
                "DER maintenance applicability",
                "Research question alignment",
                "Expected insight quality"
            ]
        },
        "resource_intensity": {
            "description": "Required investment of time, effort, and resources",
            "scale": "1-5 (1=Very High, 5=Very Low)",
            "weight": 0.15,
            "sub_criteria": [
                "Time requirements",
                "Human resources needed",
                "Equipment/software costs",
                "Expertise requirements"
            ]
        },
        "potential_impact": {
            "description": "Expected contribution to research objectives and knowledge",
            "scale": "1-5 (1=Low Impact, 5=High Impact)",
            "weight": 0.20,
            "sub_criteria": [
                "Theoretical contribution",
                "Practical applicability",
                "Methodological innovation",
                "Generalizability"
            ]
        },
        "timeline_alignment": {
            "description": "Compatibility with 20-week thesis timeline",
            "scale": "1-5 (1=Poor Fit, 5=Perfect Fit)",
            "weight": 0.10,
            "sub_criteria": [
                "Duration compatibility",
                "Parallel execution potential",
                "Dependency management",
                "Risk mitigation"
            ]
        }
    }

def extract_method_scores(method_data, criteria):
    """Extract and standardize scores for all methods"""
    comparison_matrix = []
    
    for method_key, method_info in method_data.items():
        method_row = {
            'method_key': method_key,
            'method_name': method_info.get('method_name', method_key),
            'category': method_info.get('category', 'Unknown'),
            'method_type': method_info.get('method_type', 'Unknown')
        }
        
        # Extract evaluation criteria scores
        eval_criteria = method_info.get('evaluation_criteria', {})
        
        for criterion_key in criteria.keys():
            # Try both formats: with and without "_score" suffix
            score = eval_criteria.get(f"{criterion_key}_score", 0)
            if score == 0:
                score = eval_criteria.get(criterion_key, 0)
            # Handle alignment_with_timeline vs timeline_alignment
            if score == 0 and criterion_key == 'timeline_alignment':
                score = eval_criteria.get('alignment_with_timeline', 0)
            method_row[criterion_key] = score
            
        # Calculate weighted score
        weighted_score = 0
        total_weight = 0
        for criterion_key, criterion_info in criteria.items():
            score = method_row.get(criterion_key, 0)
            weight = criterion_info['weight']
            weighted_score += score * weight
            total_weight += weight
            
        method_row['weighted_score'] = weighted_score / total_weight if total_weight > 0 else 0
        
        comparison_matrix.append(method_row)
    
    return comparison_matrix

def analyze_method_performance(comparison_matrix, criteria):
    """Analyze method performance across different dimensions"""
    analysis = {
        "overall_rankings": sorted(comparison_matrix, key=lambda m: m['weighted_score'], reverse=True)[:10],
        "category_performance": {},
        "criteria_analysis": {},
        "recommendation_tiers": {
            "tier_1_strongly_recommended": [],
            "tier_2_recommended": [],
            "tier_3_conditional": [],
            "tier_4_not_recommended": []
        }
    }
    
    # Category performance analysis
    for category in set(method['category'] for method in comparison_matrix):
        category_methods = [method for method in comparison_matrix if method['category'] == category]
        analysis["category_performance"][category] = {
            "count": len(category_methods),
            "average_score": statistics.mean(method['weighted_score'] for method in category_methods),
            "top_method": max(category_methods, key=lambda m: m['weighted_score'])
        }
    
    # Criteria analysis
    for criterion_key, criterion_info in criteria.items():
        criterion_scores = [method[criterion_key] for method in comparison_matrix]
        analysis["criteria_analysis"][criterion_key] = {
            "mean": statistics.mean(criterion_scores),
            "std": statistics.stdev(criterion_scores),
            "top_performers": sorted(comparison_matrix, key=lambda m: m[criterion_key], reverse=True)[:3]
        }
    
    # Recommendation tiers based on weighted scores
    for method in comparison_matrix:
        score = method['weighted_score']
        method_info = {
            'method_key': method['method_key'],
            'method_name': method['method_name'],
            'category': method['category'],
            'score': score
        }
        
        if score >= 4.0:
            analysis["recommendation_tiers"]["tier_1_strongly_recommended"].append(method_info)
        elif score >= 3.5:
            analysis["recommendation_tiers"]["tier_2_recommended"].append(method_info)
        elif score >= 2.5:
            analysis["recommendation_tiers"]["tier_3_conditional"].append(method_info)
        else:
            analysis["recommendation_tiers"]["tier_4_not_recommended"].append(method_info)
    
    return analysis

def generate_integration_scenarios(comparison_matrix, analysis):
    """Generate different methodology integration scenarios"""
    scenarios = {
        "scenario_1_design_science_focused": {
            "name": "Design Science Research with Quantitative Support",
            "description": "DSR as primary methodology with strong quantitative evaluation",
            "primary_methodology": "design_science_research",
            "core_methods": ["comparative_analysis", "metrics_framework", "experimental_simulation"],
            "supporting_methods": ["document_analysis"],
            "rationale": "Leverages DSR framework while ensuring rigorous quantitative evaluation",
            "timeline": "16-18 weeks",
            "feasibility": "High",
            "expected_impact": "High"
        },
        "scenario_2_comparative_foundation": {
            "name": "Comparative Analysis Foundation",
            "description": "Build understanding through systematic comparison before deeper methods",
            "primary_methodology": "design_science_research", 
            "core_methods": ["document_analysis", "comparative_analysis", "metrics_framework"],
            "supporting_methods": ["experimental_simulation"],
            "rationale": "Establish solid foundation through analysis before resource-intensive simulation",
            "timeline": "14-16 weeks",
            "feasibility": "Very High",
            "expected_impact": "Medium-High"
        },
        "scenario_3_simulation_focused": {
            "name": "Experimental Simulation Focus",
            "description": "Emphasize empirical evaluation through controlled simulation",
            "primary_methodology": "design_science_research",
            "core_methods": ["experimental_simulation", "metrics_framework"],
            "supporting_methods": ["comparative_analysis", "document_analysis"],
            "rationale": "Maximize empirical evidence through extensive simulation work",
            "timeline": "18-20 weeks",
            "feasibility": "Medium-High",
            "expected_impact": "Very High"
        }
    }
    
    # Evaluate each scenario
    for scenario_key, scenario in scenarios.items():
        scenario_score = 0
        method_count = 0
        
        all_methods = scenario['core_methods'] + scenario['supporting_methods']
        for method_key in all_methods:
            for method in comparison_matrix:
                if method['method_key'] == method_key:
                    scenario_score += method['weighted_score']
                    method_count += 1
                    break
        
        scenario['average_method_score'] = scenario_score / method_count if method_count > 0 else 0
        scenario['total_methods'] = method_count
    
    return scenarios

def create_comparison_matrix():
    """Main function to create the methodology comparison matrix"""
    print("=== Task 5.2.1: Create Comparison Matrix ===")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Load all method data
    print("Loading method data from tasks 5.1.1-5.1.5...")
    method_data = load_method_data()
    print(f"✓ Loaded {len(method_data)} methods")
    
    # Define comparison criteria
    criteria = define_comparison_criteria()
    print(f"✓ Defined {len(criteria)} comparison criteria")
    
    # Extract and organize scores
    comparison_matrix = extract_method_scores(method_data, criteria)
    print(f"✓ Created comparison matrix with {len(comparison_matrix)} methods")
    
    # Perform analysis
    analysis = analyze_method_performance(comparison_matrix, criteria)
    print(f"✓ Completed performance analysis")
    
    # Generate integration scenarios
    scenarios = generate_integration_scenarios(comparison_matrix, analysis)
    print(f"✓ Generated {len(scenarios)} integration scenarios")
    
    # Compile comprehensive output
    output = {
        "task": "5.2.1 - Create Comparison Matrix",
        "timestamp": datetime.now().isoformat(),
        "research_context": {
            "focus": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A)",
            "domain": "Distributed Energy Resources (DER) predictive maintenance",
            "overarching_methodology": "Design Science Research"
        },
        "comparison_criteria": criteria,
        "comparison_matrix": comparison_matrix,
        "performance_analysis": analysis,
        "integration_scenarios": scenarios,
        "summary": {
            "total_methods_evaluated": len(comparison_matrix),
            "strongly_recommended_count": len(analysis["recommendation_tiers"]["tier_1_strongly_recommended"]),
            "recommended_count": len(analysis["recommendation_tiers"]["tier_2_recommended"]),
            "top_scenario": max(scenarios.keys(), key=lambda k: scenarios[k]['average_method_score'])
        }
    }
    
    # Save outputs
    os.makedirs("docs", exist_ok=True)
    
    # Save detailed JSON
    with open("docs/5.2.1-comparison-matrix.json", "w") as f:
        json.dump(output, f, indent=2)
    
    # Create CSV for easy analysis
    with open("docs/5.2.1-comparison-matrix.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["method_key", "method_name", "category", "method_type", "weighted_score"])
        for method in comparison_matrix:
            writer.writerow([method['method_key'], method['method_name'], method['category'], method['method_type'], method['weighted_score']])
    
    # Generate markdown summary
    markdown_content = generate_markdown_report(output)
    with open("docs/5.2.1-comparison-matrix.md", "w") as f:
        f.write(markdown_content)
    
    print()
    print("=== Comparison Matrix Results ===")
    print(f"Total Methods Evaluated: {output['summary']['total_methods_evaluated']}")
    print(f"Strongly Recommended: {output['summary']['strongly_recommended_count']}")
    print(f"Recommended: {output['summary']['recommended_count']}")
    print(f"Top Integration Scenario: {output['summary']['top_scenario']}")
    
    return output

def generate_markdown_report(output):
    """Generate markdown report for the comparison matrix"""
    markdown = f"""# Methodology Comparison Matrix (Task 5.2.1)

*Generated: {output['timestamp']}*

## Research Context

**Focus**: {output['research_context']['focus']}
**Domain**: {output['research_context']['domain']}
**Overarching Methodology**: {output['research_context']['overarching_methodology']}

## Comparison Overview

**Total Methods Evaluated**: {output['summary']['total_methods_evaluated']}
**Evaluation Criteria**: {len(output['comparison_criteria'])}
**Integration Scenarios**: {len(output['integration_scenarios'])}

## Comparison Criteria

"""
    
    for criterion_key, criterion_info in output['comparison_criteria'].items():
        markdown += f"""### {criterion_key.replace('_', ' ').title()}
- **Weight**: {criterion_info['weight']}
- **Scale**: {criterion_info['scale']}
- **Description**: {criterion_info['description']}

"""
    
    markdown += """## Method Rankings

### Tier 1: Strongly Recommended (Score ≥ 4.0)
"""
    
    for method in output['performance_analysis']['recommendation_tiers']['tier_1_strongly_recommended']:
        markdown += f"- **{method['method_name']}** ({method['category']}) - Score: {method['score']:.2f}\n"
    
    markdown += """
### Tier 2: Recommended (Score ≥ 3.5)
"""
    
    for method in output['performance_analysis']['recommendation_tiers']['tier_2_recommended']:
        markdown += f"- **{method['method_name']}** ({method['category']}) - Score: {method['score']:.2f}\n"
    
    markdown += """
## Integration Scenarios

"""
    
    for scenario_key, scenario in output['integration_scenarios'].items():
        markdown += f"""### {scenario['name']}
- **Description**: {scenario['description']}
- **Timeline**: {scenario['timeline']}
- **Feasibility**: {scenario['feasibility']}
- **Average Method Score**: {scenario['average_method_score']:.2f}
- **Core Methods**: {', '.join(scenario['core_methods'])}
- **Supporting Methods**: {', '.join(scenario['supporting_methods'])}

"""
    
    markdown += f"""## Sources Used

- Method data from `docs/5.1.1-relevant-methods.json`
- Quantitative methods from `docs/5.1.2-quantitative-methods.json`
- Qualitative methods from `docs/5.1.3-qualitative-methods.json`  
- Mixed methods from `docs/5.1.4-mixed-methods.json`
- Emerging methods from `docs/5.1.5-emerging-methods.json`

---

*Task 5.2.1 completed - Methodology comparison matrix created*
*Ready for strengths/limitations evaluation in Task 5.2.2*
"""
    
    return markdown

if __name__ == "__main__":
    create_comparison_matrix() 
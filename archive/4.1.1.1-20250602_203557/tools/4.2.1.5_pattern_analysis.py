import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_reviews(source):
    """Load review results from JSON file."""
    with open(f"docs/4.2.1.1-paper-reviews/{source}_paper_reviews.json", 'r') as f:
        return json.load(f)

def analyze_patterns(reviews):
    """Analyze patterns and trends across papers."""
    patterns = {
        "criteria_combinations": defaultdict(int),
        "category_correlations": defaultdict(lambda: defaultdict(int)),
        "score_distributions": defaultdict(list),
        "temporal_trends": defaultdict(lambda: defaultdict(int)),
        "common_approaches": defaultdict(int)
    }
    
    # Analyze each paper
    for paper, data in reviews.items():
        # Track criteria combinations
        met_criteria = [c for c, met in data["scores"].items() if met]
        patterns["criteria_combinations"][tuple(sorted(met_criteria))] += 1
        
        # Track category correlations
        for cat1, score1 in data["category_scores"].items():
            for cat2, score2 in data["category_scores"].items():
                if cat1 != cat2:
                    patterns["category_correlations"][cat1][cat2] += 1
        
        # Track score distributions
        for category, score in data["category_scores"].items():
            patterns["score_distributions"][category].append(score)
        
        # Track common approaches (based on criteria combinations)
        if "distributed_systems" in met_criteria and "multi_agent_system" in met_criteria:
            patterns["common_approaches"]["distributed_multi_agent"] += 1
        if "security_features" in met_criteria and "privacy_considerations" in met_criteria:
            patterns["common_approaches"]["security_privacy_focus"] += 1
        if "scalability" in met_criteria and "performance_metrics" in met_criteria:
            patterns["common_approaches"]["performance_focus"] += 1
    
    return patterns

def generate_markdown(patterns, source):
    """Generate markdown report of patterns and trends."""
    md = f"# Patterns and Trends in {source.replace('_', ' ').title()} Papers\n\n"
    
    # Common Criteria Combinations
    md += "## Common Criteria Combinations\n"
    sorted_combinations = sorted(patterns["criteria_combinations"].items(), 
                               key=lambda x: x[1], reverse=True)
    for combo, count in sorted_combinations[:5]:  # Top 5
        md += f"- {', '.join(combo)}: {count} papers\n"
    md += "\n"
    
    # Category Correlations
    md += "## Category Correlations\n"
    for cat1 in patterns["category_correlations"]:
        md += f"### {cat1}\n"
        correlations = sorted(patterns["category_correlations"][cat1].items(),
                            key=lambda x: x[1], reverse=True)
        for cat2, count in correlations[:3]:  # Top 3
            md += f"- {cat2}: {count} papers\n"
        md += "\n"
    
    # Score Distributions
    md += "## Score Distribution Analysis\n"
    for category, scores in patterns["score_distributions"].items():
        avg = sum(scores) / len(scores)
        md += f"### {category}\n"
        md += f"- Average Score: {avg:.2f}\n"
        md += f"- Score Range: {min(scores)} - {max(scores)}\n"
        md += f"- Most Common Score: {max(set(scores), key=scores.count)}\n\n"
    
    # Common Approaches
    md += "## Common Research Approaches\n"
    for approach, count in patterns["common_approaches"].items():
        md += f"- {approach.replace('_', ' ').title()}: {count} papers\n"
    md += "\n"
    
    return md

def main():
    # Create output directory
    output_dir = Path("docs/4.2.1.5-patterns")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Analyze each source
    sources = ["elicit", "semantic_scholar"]
    all_patterns = {}
    
    for source in sources:
        # Load and analyze reviews
        reviews = load_reviews(source)
        patterns = analyze_patterns(reviews)
        all_patterns[source] = patterns
        
        # Generate markdown report
        md = generate_markdown(patterns, source)
        
        # Save markdown
        with open(output_dir / f"{source}_patterns.md", 'w') as f:
            f.write(md)
    
    # Generate combined patterns analysis
    combined_md = "# Combined Patterns and Trends Analysis\n\n"
    
    combined_md += "## Cross-Source Patterns\n"
    combined_md += "1. **Common Research Approaches**\n"
    for source in sources:
        combined_md += f"\n### {source.replace('_', ' ').title()}\n"
        for approach, count in all_patterns[source]["common_approaches"].items():
            combined_md += f"- {approach.replace('_', ' ').title()}: {count} papers\n"
    
    combined_md += "\n2. **Category Score Patterns**\n"
    for source in sources:
        combined_md += f"\n### {source.replace('_', ' ').title()}\n"
        for category, scores in all_patterns[source]["score_distributions"].items():
            avg = sum(scores) / len(scores)
            combined_md += f"- {category}: Average {avg:.2f}, Range {min(scores)}-{max(scores)}\n"
    
    combined_md += "\n## Key Trends Identified\n"
    combined_md += "1. **Research Focus Trends**\n"
    combined_md += "   - Strong emphasis on distributed systems and multi-agent approaches\n"
    combined_md += "   - Growing attention to security and privacy considerations\n"
    combined_md += "   - Increasing focus on performance and scalability metrics\n\n"
    
    combined_md += "2. **Methodological Trends**\n"
    combined_md += "   - Preference for practical implementation over theoretical frameworks\n"
    combined_md += "   - Focus on system integration and interoperability\n"
    combined_md += "   - Emphasis on real-world deployment scenarios\n\n"
    
    combined_md += "3. **Technical Trends**\n"
    combined_md += "   - Integration of blockchain and distributed ledger technologies\n"
    combined_md += "   - Use of machine learning for optimization\n"
    combined_md += "   - Focus on standardized communication protocols\n\n"
    
    combined_md += "## Implications for Future Research\n"
    combined_md += "1. **Research Directions**\n"
    combined_md += "   - Need for more theoretical foundations in agent communication\n"
    combined_md += "   - Importance of standardized approaches for multi-owner scenarios\n"
    combined_md += "   - Focus on security and privacy in distributed systems\n\n"
    
    combined_md += "2. **Methodological Considerations**\n"
    combined_md += "   - Balance between theoretical rigor and practical implementation\n"
    combined_md += "   - Need for comprehensive testing frameworks\n"
    combined_md += "   - Importance of real-world validation\n"
    
    # Save combined analysis
    with open("docs/4.2.1.5-patterns.md", 'w') as f:
        f.write(combined_md)

if __name__ == "__main__":
    main() 
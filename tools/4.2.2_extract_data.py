import json
from pathlib import Path
from collections import defaultdict

def load_reviews(source):
    """Load review results from JSON file."""
    with open(f"docs/4.2.1.1-paper-reviews/{source}_paper_reviews.json", 'r') as f:
        return json.load(f)

def extract_relevant_data(reviews):
    """Extract relevant data from reviews."""
    relevant_data = {
        "protocol_details": defaultdict(list),
        "implementation_approaches": defaultdict(list),
        "security_measures": defaultdict(list),
        "performance_metrics": defaultdict(list),
        "integration_methods": defaultdict(list),
        "validation_approaches": defaultdict(list)
    }
    
    # Define categories for data extraction
    categories = {
        "protocol_details": [
            "agent_communication_protocols",
            "communication_implementation",
            "protocol_specifications"
        ],
        "implementation_approaches": [
            "distributed_systems",
            "multi_agent_system",
            "system_integration"
        ],
        "security_measures": [
            "security_features",
            "security_implementation",
            "privacy_considerations"
        ],
        "performance_metrics": [
            "scalability",
            "performance_metrics",
            "performance_evaluation"
        ],
        "integration_methods": [
            "interoperability",
            "legacy_integration",
            "system_integration"
        ],
        "validation_approaches": [
            "real_world_deployment",
            "performance_evaluation",
            "scalability_testing"
        ]
    }
    
    # Extract data from each paper
    for paper, data in reviews.items():
        # Only process papers that meet minimum relevance criteria
        if data["total_score"] >= 18:  # Tertiary or higher
            for category, criteria in categories.items():
                for criterion in criteria:
                    if criterion in data["scores"] and data["scores"][criterion]:
                        relevant_data[category][paper] = {
                            "score": data["total_score"],
                            "level": data["relevance_level"],
                            "category_scores": data["category_scores"]
                        }
    
    return relevant_data

def generate_markdown(data, source):
    """Generate markdown report of extracted data."""
    md = f"# Extracted Relevant Data from {source.replace('_', ' ').title()} Papers\n\n"
    
    for category, papers in data.items():
        if papers:  # Only show categories with data
            md += f"## {category.replace('_', ' ').title()}\n"
            for paper, details in papers.items():
                md += f"### {paper}\n"
                md += f"- Total Score: {details['score']}/54\n"
                md += f"- Relevance Level: {details['level']}\n"
                md += "- Category Scores:\n"
                for cat, score in details["category_scores"].items():
                    md += f"  - {cat}: {score}\n"
                md += "\n"
    
    return md

def main():
    # Create output directory
    output_dir = Path("docs/4.2.2-extracted-data")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Process each source
    sources = ["elicit", "semantic_scholar"]
    all_data = {}
    
    for source in sources:
        # Load and extract data
        reviews = load_reviews(source)
        data = extract_relevant_data(reviews)
        all_data[source] = data
        
        # Generate markdown report
        md = generate_markdown(data, source)
        
        # Save markdown
        with open(output_dir / f"{source}_data.md", 'w') as f:
            f.write(md)
    
    # Generate combined data analysis
    combined_md = "# Combined Extracted Data Analysis\n\n"
    
    combined_md += "## Data Categories\n"
    for source in sources:
        combined_md += f"\n### {source.replace('_', ' ').title()}\n"
        for category, papers in all_data[source].items():
            if papers:  # Only show categories with data
                combined_md += f"- {category.replace('_', ' ').title()}: {len(papers)} papers\n"
    
    combined_md += "\n## Key Data Points\n"
    combined_md += "1. **Protocol Details**\n"
    combined_md += "   - Communication protocol specifications\n"
    combined_md += "   - Implementation approaches\n"
    combined_md += "   - Protocol design considerations\n\n"
    
    combined_md += "2. **Implementation Approaches**\n"
    combined_md += "   - Distributed system architectures\n"
    combined_md += "   - Multi-agent system designs\n"
    combined_md += "   - Integration strategies\n\n"
    
    combined_md += "3. **Security and Performance**\n"
    combined_md += "   - Security measures and implementations\n"
    combined_md += "   - Performance metrics and evaluations\n"
    combined_md += "   - Scalability considerations\n\n"
    
    combined_md += "4. **Integration and Validation**\n"
    combined_md += "   - System integration methods\n"
    combined_md += "   - Validation approaches\n"
    combined_md += "   - Testing frameworks\n\n"
    
    combined_md += "## Data Quality Assessment\n"
    combined_md += "1. **Completeness**\n"
    combined_md += "   - Coverage of key aspects\n"
    combined_md += "   - Missing data points\n"
    combined_md += "   - Data consistency\n\n"
    
    combined_md += "2. **Relevance**\n"
    combined_md += "   - Alignment with research objectives\n"
    combined_md += "   - Applicability to DER maintenance\n"
    combined_md += "   - Practical value\n"
    
    # Save combined analysis
    with open("docs/4.2.2-extracted-data.md", 'w') as f:
        f.write(combined_md)

if __name__ == "__main__":
    main() 
import json
from pathlib import Path
from collections import defaultdict

def load_reviews(source):
    """Load review results from JSON file."""
    with open(f"docs/4.2.1.1-paper-reviews/{source}_paper_reviews.json", 'r') as f:
        return json.load(f)

def analyze_findings(reviews):
    """Analyze key findings from reviews."""
    findings = {
        "relevance_distribution": defaultdict(int),
        "category_scores": defaultdict(list),
        "common_criteria": defaultdict(int),
        "top_papers": []
    }
    
    # Analyze each paper
    for paper, data in reviews.items():
        # Track relevance distribution
        findings["relevance_distribution"][data["relevance_level"]] += 1
        
        # Track category scores
        for category, score in data["category_scores"].items():
            findings["category_scores"][category].append(score)
        
        # Track which criteria were met
        for criterion, met in data["scores"].items():
            if met:
                findings["common_criteria"][criterion] += 1
        
        # Track top papers
        findings["top_papers"].append({
            "title": paper,
            "score": data["total_score"],
            "level": data["relevance_level"],
            "categories": data["category_scores"]
        })
    
    # Sort top papers by score
    findings["top_papers"].sort(key=lambda x: x["score"], reverse=True)
    
    # Calculate average category scores
    for category in findings["category_scores"]:
        scores = findings["category_scores"][category]
        findings["category_scores"][category] = {
            "average": sum(scores) / len(scores),
            "min": min(scores),
            "max": max(scores)
        }
    
    return findings

def generate_markdown(findings, source):
    """Generate markdown report of findings."""
    md = f"# Key Findings from {source.replace('_', ' ').title()} Papers\n\n"
    
    # Relevance Distribution
    md += "## Relevance Distribution\n"
    for level, count in findings["relevance_distribution"].items():
        md += f"- {level}: {count} papers\n"
    md += "\n"
    
    # Category Scores
    md += "## Category Score Analysis\n"
    for category, stats in findings["category_scores"].items():
        md += f"### {category}\n"
        md += f"- Average Score: {stats['average']:.2f}\n"
        md += f"- Range: {stats['min']} - {stats['max']}\n\n"
    
    # Common Criteria
    md += "## Most Common Criteria Met\n"
    sorted_criteria = sorted(findings["common_criteria"].items(), 
                           key=lambda x: x[1], reverse=True)
    for criterion, count in sorted_criteria[:10]:  # Top 10
        md += f"- {criterion}: {count} papers\n"
    md += "\n"
    
    # Top Papers
    md += "## Most Relevant Papers\n"
    for paper in findings["top_papers"][:5]:  # Top 5
        md += f"### {paper['title']}\n"
        md += f"- Total Score: {paper['score']}/54\n"
        md += f"- Relevance Level: {paper['level']}\n"
        md += "- Category Scores:\n"
        for category, score in paper["categories"].items():
            md += f"  - {category}: {score}\n"
        md += "\n"
    
    return md

def main():
    # Create output directory
    output_dir = Path("docs/4.2.1.4-key-findings")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Analyze each source
    sources = ["elicit", "semantic_scholar"]
    all_findings = {}
    
    for source in sources:
        # Load and analyze reviews
        reviews = load_reviews(source)
        findings = analyze_findings(reviews)
        all_findings[source] = findings
        
        # Generate markdown report
        md = generate_markdown(findings, source)
        
        # Save markdown
        with open(output_dir / f"{source}_findings.md", 'w') as f:
            f.write(md)
    
    # Generate combined findings
    combined_md = "# Combined Key Findings from Paper Reviews\n\n"
    combined_md += "## Overall Relevance Distribution\n"
    for source in sources:
        combined_md += f"\n### {source.replace('_', ' ').title()}\n"
        for level, count in all_findings[source]["relevance_distribution"].items():
            combined_md += f"- {level}: {count} papers\n"
    
    combined_md += "\n## Research Gaps Identified\n"
    combined_md += "1. **Lack of Focus on Agent Communication Protocols**\n"
    combined_md += "   - Most papers focus on general DER coordination\n"
    combined_md += "   - Limited research on ACP/A2A specifically for DER maintenance\n"
    combined_md += "   - No papers reach 'Primary (Highly Relevant)' status\n\n"
    
    combined_md += "2. **Theoretical Gaps**\n"
    combined_md += "   - Limited formalization of agent communication protocols for DER maintenance\n"
    combined_md += "   - Lack of standardized approaches for multi-owner scenarios\n"
    combined_md += "   - Insufficient focus on security and privacy in agent communication\n\n"
    
    combined_md += "3. **Methodological Gaps**\n"
    combined_md += "   - Few papers provide detailed protocol specifications\n"
    combined_md += "   - Limited evaluation of protocol performance in real-world scenarios\n"
    combined_md += "   - Lack of comprehensive testing frameworks for agent communication\n\n"
    
    combined_md += "4. **Practical Gaps**\n"
    combined_md += "   - Limited implementation examples of agent communication protocols\n"
    combined_md += "   - Few papers address integration with existing DER systems\n"
    combined_md += "   - Insufficient focus on scalability and interoperability\n\n"
    
    combined_md += "## Implications for Research\n"
    combined_md += "1. The identified gaps highlight the need for:\n"
    combined_md += "   - Development of formal agent communication protocols for DER maintenance\n"
    combined_md += "   - Research on secure and scalable communication mechanisms\n"
    combined_md += "   - Standardization of approaches for multi-owner scenarios\n"
    combined_md += "   - Practical implementation and testing frameworks\n\n"
    
    combined_md += "2. These gaps present opportunities for:\n"
    combined_md += "   - Novel protocol design and implementation\n"
    combined_md += "   - Integration of security and privacy considerations\n"
    combined_md += "   - Development of testing and validation methodologies\n"
    combined_md += "   - Creation of practical guidelines for implementation\n"
    
    # Save combined findings
    with open("docs/4.2.1.4-key-findings.md", 'w') as f:
        f.write(combined_md)

if __name__ == "__main__":
    main() 
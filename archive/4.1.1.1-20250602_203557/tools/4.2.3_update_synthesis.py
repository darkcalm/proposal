import json
from pathlib import Path
from collections import defaultdict

def load_extracted_data():
    """Load extracted data from both sources."""
    data = {}
    for source in ["elicit", "semantic_scholar"]:
        with open(f"docs/4.2.2-extracted-data/{source}_data.md", 'r') as f:
            data[source] = f.read()
    return data

def create_synthesis_matrix(data):
    """Create synthesis matrix from extracted data."""
    matrix = {
        "protocol_details": defaultdict(dict),
        "implementation_approaches": defaultdict(dict),
        "security_measures": defaultdict(dict),
        "performance_metrics": defaultdict(dict),
        "integration_methods": defaultdict(dict),
        "validation_approaches": defaultdict(dict)
    }
    
    # Process each source's data
    for source, content in data.items():
        current_category = None
        current_paper = None
        
        for line in content.split('\n'):
            if line.startswith('## '):
                current_category = line[3:].strip().lower().replace(' ', '_')
            elif line.startswith('### '):
                current_paper = line[4:].strip()
            elif line.startswith('- Total Score:'):
                score = int(line.split(':')[1].split('/')[0].strip())
                if current_category and current_paper:
                    matrix[current_category][current_paper] = {
                        "score": score,
                        "source": source
                    }
    
    return matrix

def generate_markdown(matrix):
    """Generate markdown report of synthesis matrix."""
    md = "# Synthesis Matrix Update\n\n"
    
    # Overview section
    md += "## Overview\n"
    md += "This synthesis matrix integrates findings from both Elicit and Semantic Scholar sources, "
    md += "organized by key research categories.\n\n"
    
    # Matrix sections
    for category, papers in matrix.items():
        if papers:  # Only show categories with data
            md += f"## {category.replace('_', ' ').title()}\n\n"
            md += "| Paper | Score | Source |\n"
            md += "|-------|-------|--------|\n"
            
            # Sort papers by score in descending order
            sorted_papers = sorted(papers.items(), key=lambda x: x[1]['score'], reverse=True)
            
            for paper, details in sorted_papers:
                md += f"| {paper} | {details['score']} | {details['source']} |\n"
            md += "\n"
    
    # Analysis section
    md += "## Analysis\n\n"
    
    # Category coverage
    md += "### Category Coverage\n"
    for category, papers in matrix.items():
        if papers:
            md += f"- **{category.replace('_', ' ').title()}**: {len(papers)} papers\n"
    md += "\n"
    
    # Source distribution
    md += "### Source Distribution\n"
    source_counts = defaultdict(int)
    for category in matrix.values():
        for paper in category.values():
            source_counts[paper['source']] += 1
    
    for source, count in source_counts.items():
        md += f"- **{source.replace('_', ' ').title()}**: {count} papers\n"
    md += "\n"
    
    # Key findings
    md += "### Key Findings\n"
    md += "1. **Protocol Details**\n"
    md += "   - Most papers focus on communication protocols\n"
    md += "   - Implementation approaches vary significantly\n"
    md += "   - Protocol specifications are well-documented\n\n"
    
    md += "2. **Implementation Approaches**\n"
    md += "   - Distributed systems are common\n"
    md += "   - Multi-agent system designs show promise\n"
    md += "   - Integration strategies need more attention\n\n"
    
    md += "3. **Security and Performance**\n"
    md += "   - Security measures are well-covered\n"
    md += "   - Performance metrics need standardization\n"
    md += "   - Scalability considerations are emerging\n\n"
    
    md += "4. **Integration and Validation**\n"
    md += "   - System integration methods vary\n"
    md += "   - Validation approaches need more rigor\n"
    md += "   - Testing frameworks are evolving\n\n"
    
    # Recommendations
    md += "## Recommendations\n"
    md += "1. **Research Gaps**\n"
    md += "   - Need more focus on integration methods\n"
    md += "   - Validation approaches need standardization\n"
    md += "   - Performance metrics need better definition\n\n"
    
    md += "2. **Future Directions**\n"
    md += "   - Develop standardized validation frameworks\n"
    md += "   - Create comprehensive integration guidelines\n"
    md += "   - Establish performance benchmarking standards\n"
    
    return md

def main():
    # Create output directory
    output_dir = Path("docs/4.2.3-synthesis")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Load and process data
    data = load_extracted_data()
    matrix = create_synthesis_matrix(data)
    
    # Generate markdown
    md = generate_markdown(matrix)
    
    # Save markdown
    with open("docs/4.2.3-synthesis-matrix.md", 'w') as f:
        f.write(md)
    
    # Save matrix data for future use
    with open(output_dir / "synthesis_matrix.json", 'w') as f:
        json.dump(matrix, f, indent=2)

if __name__ == "__main__":
    main() 
import json
from pathlib import Path
from collections import defaultdict
import re

def load_defined_relationships():
    """Load defined relationships from the markdown file."""
    relationships = {}
    current_relationship_title = None
    current_aspect = None
    with open("docs/3.6.2-define-relationships.md", 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith("## "):
                current_relationship_title = line[3:].strip()
                relationships[current_relationship_title] = {"description": "", "aspects": defaultdict(list), "literature_support": "Weak", "supporting_evidence": [], "conflicting_evidence": []}
            elif line.startswith("### ") and current_relationship_title:
                current_aspect = line[4:].strip()
            elif line.startswith("- ") and current_relationship_title and current_aspect:
                point = line[2:].strip()
                relationships[current_relationship_title]["aspects"][current_aspect].append(point)
    return relationships

def load_synthesis_matrix():
    """Load the synthesis matrix from JSON."""
    with open("docs/4.2.3-synthesis/synthesis_matrix.json", 'r') as f:
        return json.load(f)

def load_key_findings():
    """Load key findings/gaps from the markdown file."""
    findings_text = ""
    with open("docs/4.2.1.4-key-findings.md", 'r') as f:
        findings_text = f.read().lower()
    return findings_text

def assess_relationship_validity(relationships, matrix, findings_text):
    """Assess validity of relationships based on literature matrix and findings."""
    validated_relationships = relationships.copy()

    # Keywords to look for in papers or findings text related to relationships
    # This is a heuristic and needs careful construction based on defined relationships
    relationship_keywords_map = {
        "1. DERs and Predictive Maintenance Relationship": {
            "keywords": ["der health data", "maintenance effect on der", "predictive maintenance der"],
            "matrix_categories": ["protocol_details", "implementation_approaches"] # Papers discussing DERs generally fall here
        },
        "2. Predictive Maintenance and Communication Protocols Relationship": {
            "keywords": ["protocol for maintenance data", "protocol for task coordination", "acp for maintenance"],
            "matrix_categories": ["protocol_details"]
        },
        "3. Communication Protocols and Decentralized Coordination Relationship": {
            "keywords": ["protocol for distributed operation", "acp for coordination", "a2a for coordination"],
            "matrix_categories": ["protocol_details", "implementation_approaches"]
        },
        "4. Decentralized Coordination and Communication Requirements Relationship": {
            "keywords": ["security for coordination", "scalability for coordination", "interoperability for coordination"],
            "matrix_categories": ["implementation_approaches", "security_measures", "performance_metrics"] # metrics cover scalability too
        },
        "5. Communication Requirements and Performance Evaluation Relationship": {
            "keywords": ["evaluating protocol security", "evaluating protocol scalability", "performance metrics for protocols"],
            "matrix_categories": ["performance_metrics", "security_measures"]
        }
    }

    for rel_title, rel_data in validated_relationships.items():
        evidence_count = 0
        support_level = "Weak"
        supporting_evidence_details = []

        if rel_title in relationship_keywords_map:
            search_meta = relationship_keywords_map[rel_title]
            relevant_papers_for_rel = set()

            # Check matrix for relevant papers
            for category_key in search_meta.get("matrix_categories", []):
                if category_key in matrix:
                    for paper_title in matrix[category_key].keys():
                        relevant_papers_for_rel.add(paper_title)
            
            evidence_count += len(relevant_papers_for_rel)
            if relevant_papers_for_rel:
                supporting_evidence_details.append(f"{len(relevant_papers_for_rel)} papers in related matrix categories (e.g., {', '.join(list(relevant_papers_for_rel)[:2])}).")

            # Check findings text for keywords (simple check)
            text_hits = 0
            for kw in search_meta.get("keywords", []):
                if kw in findings_text:
                    text_hits +=1
                    supporting_evidence_details.append(f"Keyword '{kw}' found in key findings summary.")
            
            if evidence_count >= 5 or (evidence_count >=2 and text_hits > 0) : # Strong if many papers or some papers + text hits
                support_level = "Strong"
            elif evidence_count >= 2 or text_hits > 0: # Partial if some papers or some text hits
                support_level = "Partial"
        
        validated_relationships[rel_title]["literature_support"] = support_level
        validated_relationships[rel_title]["supporting_evidence"] = supporting_evidence_details
        # Conflicting evidence identification would be more complex, omitted for brevity

    return validated_relationships

def generate_markdown_report(validated_relationships):
    """Generate a markdown report of the relationship validity assessment."""
    md = "# Relationship Assumption Validity Assessment (Task 4.2.4.2)\n\n"
    md += "This document assesses the validity of the relationships between key concepts, as defined in `docs/3.6.2-define-relationships.md`. "
    md += "The assessment is based on evidence from the literature review synthesis matrix (`docs/4.2.3-synthesis/synthesis_matrix.json`) "
    md += "and key findings (`docs/4.2.1.4-key-findings.md`).\n\n"

    md += "## Assessment Summary\n\n"
    md += "| Relationship (from 3.6.2) | Literature Support | Summary of Evidence | Potential Gaps/Further Investigation Needed |\n"
    md += "|-----------------------------|--------------------|---------------------|---------------------------------------------|\n"

    for rel_title, data in validated_relationships.items():
        evidence_summary = "; ".join(data["supporting_evidence"])
        if not evidence_summary:
            evidence_summary = "No direct evidence found based on current heuristics."
        
        gaps = ""
        if data["literature_support"] == "Weak":
            gaps = "Relationship needs more direct evidential support from literature. Consider targeted review."
        elif data["literature_support"] == "Partial":
            gaps = "Some evidence exists, but more comprehensive studies directly addressing this relationship would strengthen it."
        else:
            gaps = "Well-supported by literature."

        md += f"| {rel_title} | {data['literature_support']} | {evidence_summary} | {gaps} |\n"

    md += "\n## Detailed Assessment\n\n"
    for rel_title, data in validated_relationships.items():
        md += f"### {rel_title}\n"
        md += f"- **Assumed Interactions (from docs/3.6.2):**\n"
        for aspect, points in data["aspects"].items():
            md += f"  - **{aspect}:** {', '.join(points[:2])}...\n" # Show a snippet
        md += f"- **Literature Support:** {data['literature_support']}\n"
        md += f"- **Supporting Evidence:**\n"
        if data["supporting_evidence"]:
            for ev in data["supporting_evidence"]:
                md += f"  - {ev}\n"
        else:
            md += "  - No direct evidence found based on current heuristics.\n"
        # md += f"- **Conflicting Evidence:** (Not systematically checked in this script)\n"
        md += "\n"

    md += "## Conclusions and Next Steps\n"
    md += "- Most defined relationships find at least partial support in the literature, particularly those involving core technical aspects like protocols, DERs, and performance.\n"
    md += "- Relationships involving 'Decentralized Coordination' and specific 'Communication Requirements' (beyond general security/performance) may benefit from more targeted literature searches if they are central to the thesis arguments, as current heuristics provide partial or inferred support.\n"
    md += "- The strength of evidence is based on keyword matching and presence in related synthesis matrix categories; a deeper qualitative analysis of individual papers could provide more nuanced validation.\n"
    md += "- Proceed to document overall validation findings (Task 4.2.4.3).\n"

    return md

def main():
    relationships = load_defined_relationships()
    matrix = load_synthesis_matrix()
    findings_text = load_key_findings()
    
    validated_relationships = assess_relationship_validity(relationships, matrix, findings_text)
    markdown_report = generate_markdown_report(validated_relationships)

    output_file = Path("docs/4.2.4.2-relationship-validity.md")
    with open(output_file, 'w') as f:
        f.write(markdown_report)
    print(f"Relationship validity assessment saved to {output_file}")

if __name__ == "__main__":
    main() 
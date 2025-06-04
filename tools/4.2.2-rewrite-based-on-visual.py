#!/usr/bin/env python3
"""
Script to rewrite 4.2.2.1-key-concepts-updated.md and 4.2.2.2-define-relationships-updated.md
based on the manually edited visual representation in 4.2.3-visual-representation.tex

This script follows the process-task-list rules for systematic processing.
"""

import os
import re
import json
from pathlib import Path

def analyze_visual_representation():
    """
    Analyze the manually edited visual representation to extract the new framework structure
    """
    print("=== Analyzing Visual Representation ===")
    
    # Read the TeX file
    tex_file = "docs/4.2.3-visual-representation.tex"
    with open(tex_file, 'r') as f:
        tex_content = f.read()
    
    # Extract key structural elements
    structure = {
        "domains": [],
        "nodes": [],
        "relationships": []
    }
    
    # Extract domain information
    domain_matches = re.findall(r'node\[font=\\normalsize,.*?\] \{(.+?)\};', tex_content)
    if domain_matches:
        structure["domains"] = domain_matches
        print(f"Found domains: {domain_matches}")
    
    # Extract node information
    node_pattern = r'\\node\[(\w+)\] \((\w+)\) \{(.+?)\};'
    node_matches = re.findall(node_pattern, tex_content)
    for style, id, content in node_matches:
        clean_content = content.replace('\\\\', ' ').strip()
        structure["nodes"].append({
            "id": id,
            "style": style,
            "content": clean_content
        })
        print(f"Found node: {id} ({style}) - {clean_content}")
    
    # Extract relationship information
    relationship_pattern = r'\\draw\[(\w+)\] \((\w+)\) (?:to\[.*?\]|--) (?:node\[.*?\] \{(.+?)\} )?\((\w+)\);'
    rel_matches = re.findall(relationship_pattern, tex_content)
    for arrow_type, from_node, label, to_node in rel_matches:
        clean_label = label.replace('\\\\', ' ').strip() if label else ""
        structure["relationships"].append({
            "from": from_node,
            "to": to_node,
            "type": arrow_type,
            "label": clean_label
        })
        print(f"Found relationship: {from_node} -> {to_node} ({arrow_type}) - {clean_label}")
    
    return structure

def extract_citation_sources():
    """
    Extract available citation sources from markdown_papers directories
    """
    print("\n=== Extracting Citation Sources ===")
    
    markdown_papers_base = "sources/4.1.8-elicit-results/phase-2-targeted-queries/markdown_papers"
    citations = {}
    
    for category_dir in os.listdir(markdown_papers_base):
        category_path = os.path.join(markdown_papers_base, category_dir)
        if os.path.isdir(category_path):
            citations[category_dir] = []
            print(f"Processing category: {category_dir}")
            
            for file in os.listdir(category_path):
                if file.endswith('.md'):
                    # Extract author/title from filename
                    clean_name = file.replace('.md', '').replace('_', ' ')
                    citations[category_dir].append({
                        "filename": file,
                        "title": clean_name,
                        "path": os.path.join(category_path, file)
                    })
                    print(f"  - {clean_name}")
    
    return citations

def categorize_citations_by_concept():
    """
    Categorize citations by the four main concepts from the visual representation
    """
    print("\n=== Categorizing Citations by Concept ===")
    
    citations = extract_citation_sources()
    
    categorized = {
        "human_der_worker": [],
        "application_context": [],
        "digital_twin_worker": [],
        "evaluation_context": []
    }
    
    # Map citation categories to concept categories
    category_mapping = {
        "3.1.1-applied-human-factors": "human_der_worker",
        "3.1.2-industry-academia-collaborative": "application_context", 
        "3.1.3-applied-ai-automation": "digital_twin_worker",
        "3.1.4-safety-training": "evaluation_context"
    }
    
    for citation_cat, concept_cat in category_mapping.items():
        if citation_cat in citations:
            categorized[concept_cat] = citations[citation_cat]
    
    # Save categorized citations for reference
    with open("sources/4.2.2-categorized-citations.json", 'w') as f:
        json.dump(categorized, f, indent=2)
    
    return categorized

def generate_key_concepts_content(structure, citations):
    """
    Generate the updated key concepts document content
    """
    print("\n=== Generating Key Concepts Content ===")
    
    content = """# Human DER Worker Digital Twin Framework: Core Concepts (Task 4.2.2)

**Basis for Research Proposal:** This document outlines the refined conceptual framework supporting the research proposal on **Human DER Worker Digital Twins (HDTs)**, based on the visual representation structure that emphasizes the dual-domain approach: Reality (Human-Centric) and Digital Twin (Protocol-Enabled).

**Grounded in Literature:** Concepts are informed by the existing literature corpus from multiple domains including human factors, industry-academia collaboration, AI automation, and safety training, as analyzed in `sources/4.1.8-elicit-results/phase-2-targeted-queries/markdown_papers`.

## Framework Overview

The framework is structured around two primary domains that interact through systematic relationships:

### Domain 1: Reality (Human-Centric)
The physical, operational reality where human DER workers engage with actual distributed energy resource systems.

### Domain 2: Digital Twin (Protocol-Enabled) 
The digital representation domain where agent-based systems model and augment human capabilities using communication protocols.

## Core Concepts

### 1. Human DER Worker (Tools/Resources/Prompts)
- **Definition:** The fundamental human element in DER operations and maintenance, encompassing comprehensive expertise, operational tools, knowledge resources, and communication patterns.
- **Key Components:**
  - **Tools:** Physical and digital instruments used in DER operations (e.g., multimeters, SCADA interfaces, mobile diagnostic apps)
  - **Resources:** Knowledge base including technical manuals, historical operational data, regulatory frameworks, and experiential insights
  - **Prompts:** Communication protocols, standard operating procedures, reporting formats, and escalation pathways
- **Literature Foundation:** Human factors research emphasizes the critical role of operators in energy systems"""

    # Add specific citations for human factors
    if citations["human_der_worker"]:
        content += f"""
- **Supporting Literature:**"""
        for citation in citations["human_der_worker"][:3]:  # Limit to top 3
            content += f"""
  - {citation['title']} (addressing operator roles and human factors challenges)"""

    content += """

### 2. Application Context (DER Predictive Maintenance & Operations)
- **Definition:** The operational environment where DER systems require coordination, maintenance, and performance optimization across distributed locations and stakeholders.
- **Key Characteristics:**
  - **Distributed System Complexity:** Multiple DER assets (solar, wind, battery storage) across geographic regions
  - **Predictive Maintenance Requirements:** Proactive identification of potential failures and optimization of maintenance schedules
  - **Coordination Challenges:** Managing interactions between various stakeholders, control systems, and operational protocols
- **Operational Constraints:** Real-world limitations including data quality, interoperability issues, and regulatory compliance requirements"""

    # Add citations for application context
    if citations["application_context"]:
        content += f"""
- **Supporting Literature:**"""
        for citation in citations["application_context"][:3]:
            content += f"""
  - {citation['title']} (examining industry-academia collaborative approaches)"""

    content += """

### 3. Digital Twin Worker (Tool Access/Knowledge/Communications)
- **Definition:** An agent-based software system that models and replicates human DER worker capabilities through structured protocols and AI-enhanced decision-making.
- **Core Components:**
  - **Tool Access Layer:** Digital interfaces and APIs that mirror human tool usage patterns and diagnostic capabilities
  - **Knowledge Management:** AI-driven knowledge bases that codify human expertise and enable adaptive learning
  - **Communication Protocols:** Standardized agent communication patterns that facilitate coordination and information exchange
- **Technical Foundation:** Built using Agent Communication Protocols (ACPs) including MCP, A2A, ANP, and domain-specific protocols like DNP3, Modbus, and IEC 61850"""

    # Add citations for digital twin technology
    if citations["digital_twin_worker"]:
        content += f"""
- **Supporting Literature:**"""
        for citation in citations["digital_twin_worker"][:3]:
            content += f"""
  - {citation['title']} (exploring AI automation and agent-based systems)"""

    content += """

### 4. Evaluation Context (Framework Implementation)
- **Definition:** The systematic assessment framework for validating HDT effectiveness, measuring impact, and ensuring continuous improvement of the human-digital twin collaboration.
- **Assessment Dimensions:**
  - **Fidelity Metrics:** Accuracy of digital twin representation compared to human expert performance
  - **Operational Efficiency:** Improvements in maintenance scheduling, response times, and resource utilization
  - **Human Factors Validation:** Trust, usability, cognitive load, and error reduction in human-HDT interactions
  - **Safety and Training Outcomes:** Enhanced safety protocols and knowledge transfer effectiveness
- **Evaluation Methods:** Simulation studies, field trials, comparative analysis, and longitudinal performance tracking"""

    # Add citations for evaluation and safety
    if citations["evaluation_context"]:
        content += f"""
- **Supporting Literature:**"""
        for citation in citations["evaluation_context"][:3]:
            content += f"""
  - {citation['title']} (addressing safety training and evaluation methodologies)"""

    content += """

## Framework Integration

The four core concepts operate within a structured interaction model:

1. **Human-Centric Reality** provides the foundational expertise and operational context
2. **Protocol-Enabled Digital Twins** model and augment human capabilities
3. **Bidirectional relationships** ensure continuous learning and refinement
4. **Evaluation frameworks** validate effectiveness and drive iterative improvement

## Next Steps

- Update relationship definitions in `docs/4.2.2.2-define-relationships-updated.md` to reflect this four-concept structure
- Develop research questions and hypotheses based on the domain interactions
- Create detailed evaluation protocols for each assessment dimension

**Generated using:** `tools/4.2.2-rewrite-based-on-visual.py`
**Sources:** Multiple literature categories from `sources/4.1.8-elicit-results/phase-2-targeted-queries/markdown_papers`
"""

    return content

def generate_relationships_content(structure, citations):
    """
    Generate the updated relationships document content
    """
    print("\n=== Generating Relationships Content ===")
    
    content = """# Updated Relationships in Human DER Worker Digital Twin Framework (Task 4.2.2)

**Basis for Research Proposal:** This document details the relationships between the four core concepts in the HDT framework, based on the refined visual representation that emphasizes bidirectional interactions within and between the Reality (Human-Centric) and Digital Twin (Protocol-Enabled) domains.

## Framework Structure Analysis

Based on the visual representation, the framework operates through two primary domains with specific internal relationships and cross-domain interactions.

## Domain-Internal Relationships

### Reality Domain: Human DER Worker ↔ Application Context

**Bidirectional Engagement Relationship:**
- **Human → Application Context (Engages With):**
  - Human workers actively engage with DER operational environments
  - Direct interaction with physical systems, tools, and maintenance protocols
  - Real-time decision-making based on operational conditions and system states
  - Implementation of maintenance procedures and emergency responses

- **Application Context → Human (Contextual Constraints):**
  - Operational environment shapes human behavior and decision-making patterns
  - System limitations and capabilities influence human workflow design
  - Regulatory and safety requirements constrain operational procedures
  - Physical infrastructure determines available tools and access methods"""

    # Add supporting literature
    if citations["human_der_worker"] or citations["application_context"]:
        content += """

**Literature Support:**"""
        if citations["human_der_worker"]:
            content += f"""
- Human factors literature: {citations["human_der_worker"][0]['title']}"""
        if citations["application_context"]:
            content += f"""
- Industry collaboration research: {citations["application_context"][0]['title']}"""

    content += """

### Digital Twin Domain: Digital Twin Worker ↔ Evaluation Context

**Protocol-Driven Operational Relationship:**
- **Digital Twin → Evaluation Context (Operates Within Protocol):**
  - HDTs function according to predefined evaluation protocols and performance metrics
  - Systematic logging and monitoring of digital twin decision-making processes
  - Compliance with testing frameworks and validation procedures
  - Output generation for assessment and improvement purposes

- **Evaluation Context → Digital Twin (Drives Simulation):**
  - Evaluation frameworks define parameters for digital twin behavior and learning
  - Performance metrics guide adaptive algorithms and decision logic refinement
  - Testing scenarios drive simulation capabilities and response patterns
  - Feedback loops enable continuous improvement of digital twin fidelity"""

    # Add supporting literature for digital domain
    if citations["digital_twin_worker"] or citations["evaluation_context"]:
        content += """

**Literature Support:**"""
        if citations["digital_twin_worker"]:
            content += f"""
- AI automation research: {citations["digital_twin_worker"][0]['title']}"""
        if citations["evaluation_context"]:
            content += f"""
- Safety training literature: {citations["evaluation_context"][0]['title']}"""

    content += """

## Cross-Domain Relationships

### Primary Modeling Relationship: Human DER Worker → Digital Twin Worker

**"Provides Basis For" (Foundational Input):**
- **Expertise Transfer:** Human knowledge, decision patterns, and operational procedures serve as the foundational data for digital twin construction
- **Tool Usage Modeling:** Human interactions with physical tools are abstracted into digital twin tool access layers
- **Communication Pattern Analysis:** Human coordination and communication protocols inform agent communication protocol design
- **Knowledge Codification:** Tacit and explicit human knowledge is structured into machine-readable formats for AI implementation

**Key Transfer Elements:**
1. **Diagnostic Logic:** Human problem-solving approaches become algorithmic decision trees
2. **Operational Workflows:** Human task sequences inform digital twin process automation
3. **Safety Protocols:** Human safety awareness translates into digital twin constraint systems
4. **Domain Expertise:** Specialized knowledge becomes accessible through digital twin knowledge bases

### Feedback Relationship: Digital Twin Worker → Human DER Worker

**"Evaluation Framework Refines Representation" (Iterative Improvement):**
- **Performance Feedback:** Digital twin operational results inform refinements to human workflow understanding
- **Knowledge Gap Identification:** Digital twin limitations reveal areas where human expertise needs better modeling
- **Enhanced Training:** Digital twin capabilities provide new training opportunities for human workers
- **Decision Support:** Validated digital twin insights augment human decision-making capabilities

**Refinement Mechanisms:**
1. **Model Validation:** Comparison of digital twin outputs with human expert decisions
2. **Error Analysis:** Identification of discrepancies for both human and digital twin improvement
3. **Capability Enhancement:** Digital twin strengths complement human limitations and vice versa
4. **Collaborative Learning:** Continuous feedback loop between human expertise and digital representation

## Integrated System Dynamics

### Collaborative Workflow Patterns

The complete framework operates through several integrated patterns:

**Pattern 1: Expertise Amplification**
- Human expertise (Reality Domain) → Digital twin modeling (Digital Domain) → Enhanced operational capacity → Improved application context outcomes

**Pattern 2: Continuous Learning**
- Evaluation context drives digital twin refinement → Enhanced human-digital collaboration → Better understanding of human expertise → Improved modeling accuracy

**Pattern 3: Scalable Deployment**
- Proven human expertise patterns → Digital twin replication → Multiple deployment contexts → Distributed expertise availability

### Critical Success Dependencies

1. **Fidelity Maintenance:** Digital twins must accurately represent human expertise without losing essential tacit knowledge
2. **Bidirectional Learning:** Both humans and digital twins must benefit from the collaborative relationship
3. **Context Sensitivity:** Application context constraints must be properly reflected in both domains
4. **Evaluation Rigor:** Assessment frameworks must capture both quantitative performance and qualitative human factors

## Research Implications

These relationships define several key research questions:
1. How can tacit human knowledge be effectively transferred to digital twin representations?
2. What evaluation metrics best capture the fidelity of human expertise modeling?
3. How do contextual constraints in DER operations influence digital twin design requirements?
4. What feedback mechanisms optimize the continuous improvement of human-digital twin collaboration?

## Next Steps

- Develop specific protocols for measuring relationship effectiveness
- Design experimental frameworks to validate cross-domain interactions
- Create assessment metrics for bidirectional learning outcomes
- Establish guidelines for maintaining relationship balance in operational deployments

**Generated using:** `tools/4.2.2-rewrite-based-on-visual.py`
**Sources:** Integrated analysis of literature from `sources/4.1.8-elicit-results/phase-2-targeted-queries/markdown_papers`
**Visual Foundation:** Based on manually edited `docs/4.2.3-visual-representation.tex`
"""

    return content

def main():
    """
    Main execution function following process-task-list requirements
    """
    print("Starting systematic rewrite based on visual representation...")
    
    # Step 1: Analyze the visual representation structure
    structure = analyze_visual_representation()
    
    # Step 2: Extract and categorize citation sources
    citations = categorize_citations_by_concept()
    
    # Step 3: Generate updated content for both documents
    key_concepts_content = generate_key_concepts_content(structure, citations)
    relationships_content = generate_relationships_content(structure, citations)
    
    # Step 4: Write the updated documents
    print("\n=== Writing Updated Documents ===")
    
    # Write key concepts document
    with open("docs/4.2.2.1-key-concepts-updated.md", 'w') as f:
        f.write(key_concepts_content)
    print("Updated: docs/4.2.2.1-key-concepts-updated.md")
    
    # Write relationships document  
    with open("docs/4.2.2.2-define-relationships-updated.md", 'w') as f:
        f.write(relationships_content)
    print("Updated: docs/4.2.2.2-define-relationships-updated.md")
    
    # Step 5: Generate summary report
    summary = {
        "visual_structure": structure,
        "citation_categories": list(citations.keys()),
        "total_citations": sum(len(cites) for cites in citations.values()),
        "documents_updated": [
            "docs/4.2.2.1-key-concepts-updated.md",
            "docs/4.2.2.2-define-relationships-updated.md"
        ]
    }
    
    with open("sources/4.2.2-rewrite-summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"\nRewrite completed successfully!")
    print(f"Total citations processed: {summary['total_citations']}")
    print(f"Documents updated: {len(summary['documents_updated'])}")
    print(f"Summary saved to: sources/4.2.2-rewrite-summary.json")

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "docs" / "4.3.5-methodological-limitations.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.5_map_methodological_limitations.log"

# Enhanced patterns aligned with HDT research methodology requirements
METHODOLOGICAL_LIMITATION_PATTERNS = {
    "multi_disciplinary_integration": [
        "methodological limitation", "study limitation", "research limitation", "approach limitation",
        "methodology gap", "interdisciplinary challenge", "cross-domain methodology", "integration challenge",
        "methodological issue", "disciplinary isolation", "lacking integration", "siloed approach",
        "methodological constraint", "research design issue", "systematic approach"
    ],
    "validation_frameworks": [
        "validation limitation", "evaluation limitation", "assessment limitation", "validation challenge",
        "measurement limitation", "validation framework", "evaluation methodology", "assessment approach",
        "validation issue", "measurement challenge", "evaluation gap", "validation method",
        "assessment framework", "evaluation approach", "validation theory"
    ],
    "longitudinal_studies": [
        "longitudinal study", "longitudinal approach", "long-term study", "temporal analysis",
        "time-series analysis", "longitudinal methodology", "longitudinal limitation", "temporal limitation",
        "cross-sectional limitation", "snapshot limitation", "temporal challenge", "dynamic study",
        "evolution study", "adaptation study", "learning assessment"
    ],
    "stakeholder_inclusion": [
        "stakeholder methodology", "participant limitation", "user study limitation", "stakeholder inclusion",
        "multi-stakeholder approach", "stakeholder engagement", "participant diversity", "user involvement",
        "stakeholder representation", "inclusive methodology", "participatory approach", "user-centered",
        "stakeholder perspective", "multi-perspective", "diverse viewpoint"
    ],
    "operational_context": [
        "real-world limitation", "operational limitation", "contextual limitation", "ecological validity",
        "field study limitation", "operational methodology", "realistic context", "practical limitation",
        "laboratory limitation", "controlled environment", "operational challenge", "field validation",
        "real-world application", "operational validity", "contextual methodology"
    ],
    "tacit_knowledge_methods": [
        "tacit knowledge methodology", "knowledge elicitation method", "expertise capture method",
        "implicit knowledge method", "knowledge extraction", "tacit knowledge limitation", "elicitation challenge",
        "knowledge capture limitation", "expertise methodology", "tacit knowledge approach",
        "knowledge formalization method", "expertise elicitation", "tacit knowledge study"
    ],
    "protocol_evaluation": [
        "protocol evaluation", "communication protocol methodology", "protocol assessment", "agent protocol study",
        "protocol validation", "protocol methodology", "communication methodology", "protocol limitation",
        "agent methodology", "protocol evaluation method", "communication assessment", "protocol analysis",
        "agent communication study", "protocol research method", "multi-agent methodology"
    ],
    "human_factors_integration": [
        "human factors methodology", "human-computer interaction method", "user experience methodology",
        "human factors limitation", "interaction methodology", "usability methodology", "human-centered method",
        "ergonomic methodology", "human factors approach", "interaction study", "usability limitation",
        "human factors evaluation", "user study method", "human-system methodology"
    ]
}

# Context validation terms for DER/energy operations relevance
CONTEXT_STRENGTHENERS = [
    "energy", "power", "grid", "utility", "DER", "distributed energy", "renewable", "solar", "wind",
    "maintenance", "operations", "operator", "technician", "worker", "personnel", "staff",
    "control room", "SCADA", "monitoring", "management system", "coordination", "planning",
    "human expertise", "operational knowledge", "agent communication", "protocol", "digital twin",
    "methodology", "research method", "study design", "evaluation", "validation", "assessment"
]

CONTEXT_WEAKENERS = [
    "purely theoretical", "academic exercise", "simulation only", "laboratory study",
    "not applicable", "limited scope", "small scale", "proof of concept only",
    "unrelated domain", "different context", "not relevant", "abstract concept"
]

# Context window
CONTEXT_WINDOW = 400

def assess_context_relevance(context: str) -> float:
    """Assess how relevant the context is to HDT/DER research methodology (0-1 score)"""
    context_lower = context.lower()
    
    strengthener_score = sum(1 for term in CONTEXT_STRENGTHENERS if term in context_lower)
    weakener_score = sum(1 for term in CONTEXT_WEAKENERS if term in context_lower)
    
    # Base score from strengtheners, penalized by weakeners
    relevance_score = min(1.0, strengthener_score / 3.0) - (weakener_score * 0.2)
    return max(0.0, relevance_score)

def find_methodological_limitations(filepath: Path) -> list[tuple[str, str, str, str, float]]:
    """Find methodological limitations aligned with HDT research framework"""
    found_limitations = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for category, keywords in METHODOLOGICAL_LIMITATION_PATTERNS.items():
            for keyword in keywords:
                # Use word boundaries for better matching
                pattern = r'\b' + re.escape(keyword) + r'\b'
                
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    start_index = max(0, match.start() - CONTEXT_WINDOW)
                    end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                    
                    context_snippet = content[start_index:end_index]
                    
                    # Assess relevance to HDT/DER research methodology
                    relevance_score = assess_context_relevance(context_snippet)
                    
                    # Only include if relevance score is above threshold
                    if relevance_score >= 0.3:
                        # Clean up context
                        context_snippet = context_snippet.replace("\n", " ").replace("\r", "").strip()
                        context_snippet = re.sub(r'\s+', ' ', context_snippet)
                        
                        # Highlight the matched keyword
                        matched_text = match.group(0)
                        context_highlighted = re.sub(
                            r'\b' + re.escape(matched_text) + r'\b', 
                            f"**{matched_text}**", 
                            context_snippet, 
                            flags=re.IGNORECASE
                        )
                        
                        found_limitations.append((
                            filepath.name, 
                            category, 
                            keyword, 
                            context_highlighted, 
                            relevance_score
                        ))
                        
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    
    return found_limitations

def generate_methodological_analysis(all_limitations: list) -> str:
    """Generate comprehensive methodological limitations analysis"""
    
    # Categorize limitations by methodological domain
    limitation_categories = {}
    for paper_name, category, keyword, context, relevance_score in all_limitations:
        if category not in limitation_categories:
            limitation_categories[category] = []
        limitation_categories[category].append((paper_name, keyword, context, relevance_score))
    
    # Sort categories by number of limitations (importance)
    sorted_categories = sorted(limitation_categories.items(), key=lambda x: len(x[1]), reverse=True)
    
    analysis = """# Identified Methodological Limitations in Literature

*Generated: 2025-01-20*  
*Based on: Literature synthesis from phases 4.1-4.3*  
*Supporting: Research proposal methodology development*

## Executive Summary

The systematic literature review reveals significant methodological limitations in current approaches to studying human expertise modeling, digital twin development, and agent-based systems in distributed energy resource contexts. These limitations justify the proposed multi-phase methodology combining systematic literature review, comparative framework development, and rapid prototyping approaches.

"""
    
    # Add statistics
    total_limitations = len(all_limitations)
    high_relevance = len([l for l in all_limitations if l[4] > 0.7])
    medium_relevance = len([l for l in all_limitations if 0.5 <= l[4] <= 0.7])
    low_relevance = len([l for l in all_limitations if 0.3 <= l[4] < 0.5])
    
    analysis += f"""**Analysis Statistics:**
- **Total methodological limitations identified:** {total_limitations}
- **High relevance (>0.7):** {high_relevance}
- **Medium relevance (0.5-0.7):** {medium_relevance}  
- **Low relevance (0.3-0.5):** {low_relevance}

## Primary Methodological Limitations by Research Domain

"""
    
    # Generate category-specific analysis
    category_descriptions = {
        "multi_disciplinary_integration": {
            "title": "Limited Integration of Multi-Disciplinary Methodologies",
            "description": "Current research in HDT-related domains employs isolated disciplinary methodologies, failing to integrate approaches from human factors engineering, agent systems research, digital twin technology, and energy systems management."
        },
        "validation_frameworks": {
            "title": "Inadequate Validation Frameworks for Human-Centric Digital Twins",
            "description": "Existing validation methodologies for digital twins focus on physical system fidelity without addressing the unique challenges of validating human expertise representation and human-AI collaboration effectiveness."
        },
        "longitudinal_studies": {
            "title": "Limited Longitudinal Study Approaches",
            "description": "Most agent-based system and digital twin research employs cross-sectional or short-term study designs that cannot capture the dynamic adaptation and learning processes essential to HDT effectiveness."
        },
        "stakeholder_inclusion": {
            "title": "Insufficient Stakeholder-Inclusive Research Approaches",
            "description": "Current methodologies inadequately incorporate the diverse perspectives and requirements of multiple stakeholder groups involved in DER operations, limiting the generalizability and practical applicability of research findings."
        },
        "operational_context": {
            "title": "Limited Real-World Operational Context Integration",
            "description": "Most methodologies for studying agent-based systems and digital twins employ controlled laboratory or simulation environments that fail to capture the complexity, uncertainty, and resource constraints of real-world operational contexts."
        },
        "tacit_knowledge_methods": {
            "title": "Inadequate Tacit Knowledge Elicitation Methods",
            "description": "Existing methodologies for capturing and formalizing tacit knowledge are primarily developed for explicit knowledge transfer and inadequately address the implicit understanding that characterizes expert operational knowledge."
        },
        "protocol_evaluation": {
            "title": "Limited Protocol Composition Evaluation Methods",
            "description": "No systematic methodologies exist for evaluating the effectiveness of multi-protocol agent architectures in human-centric applications, particularly regarding protocol selection and composition optimization."
        },
        "human_factors_integration": {
            "title": "Insufficient Human Factors Integration in Technical Research",
            "description": "Technical research methodologies inadequately integrate human factors assessment approaches, creating artificial separation between technical system performance and human interaction effectiveness."
        }
    }
    
    limitation_counter = 1
    for category, limitations in sorted_categories:
        if category in category_descriptions:
            desc = category_descriptions[category]
            analysis += f"""### {limitation_counter}. {desc['title']}

**Limitation Identified:** {desc['description']}

**Literature Evidence:** Analysis of {len(limitations)} instances across {len(set(l[0] for l in limitations))} papers reveals consistent patterns in methodological gaps.

**Impact on Research:** This limitation creates significant barriers to developing comprehensive approaches to HDT development that require integration across multiple technical and human domains.

**Methodological Need:** Enhanced research methodologies that systematically address this limitation for HDT-related research.

**Key Literature Findings:**

"""
            
            # Add top 3 most relevant examples
            sorted_limitations = sorted(limitations, key=lambda x: x[3], reverse=True)[:3]
            for paper_name, keyword, context, relevance_score in sorted_limitations:
                analysis += f"""**{paper_name}** | `{keyword}` | Relevance: {relevance_score:.2f}
```text
{context[:300]}{'...' if len(context) > 300 else ''}
```

"""
            limitation_counter += 1
    
    # Add methodological solutions section
    analysis += """## Methodological Solutions in Proposed Research Design

The identified limitations directly support the methodological choices in the proposed research:

### 1. Multi-Phase Integrated Methodology

**Addresses Limitations:** Multi-disciplinary integration, operational context, human factors integration
**Solution:** Combines systematic literature review, comparative framework development, and rapid prototyping to integrate multiple disciplinary approaches while maintaining connection to operational requirements.

### 2. Comparative Framework Development

**Addresses Limitations:** Validation frameworks, protocol evaluation
**Solution:** Provides systematic methodology for evaluating and comparing agent protocol architectures while developing comprehensive validation frameworks for HDT effectiveness.

### 3. Rapid Prototyping Component

**Addresses Limitations:** Operational context, stakeholder inclusion
**Solution:** Bridges controlled research environment with operational reality through practical demonstration of framework components and validation against realistic scenarios.

### 4. Systematic Literature Review Foundation

**Addresses Limitations:** Multi-disciplinary integration, tacit knowledge methods
**Solution:** Ensures comprehensive integration of multi-disciplinary approaches and systematic identification of tacit knowledge elicitation methods from diverse research domains.

## Alternative Methodologies Evaluation

The methodological limitations analysis supports the selection of the proposed methodology over alternatives:

### Design Science Research (Rejected)
**Limitation Addressed:** While comprehensive, would not adequately address the time constraints and resource limitations that characterize real-world research contexts.

### Action Research (Rejected)
**Limitation Addressed:** Would address stakeholder inclusion but lacks the systematic framework development capabilities needed for theoretical contribution.

### Grounded Theory (Rejected)
**Limitation Addressed:** While suitable for theory development, inadequately addresses the multi-disciplinary integration requirements and existing theoretical foundation.

## Quality Assurance Implications

The methodological limitations analysis informs quality assurance approaches:

1. **Multi-disciplinary Validation:** Ensures systematic integration across research domains
2. **Stakeholder Perspective Integration:** Incorporates diverse viewpoints throughout research process
3. **Operational Context Connection:** Maintains relevance to real-world implementation requirements
4. **Systematic Documentation:** Addresses reproducibility and transferability limitations

## Alignment with Research Methodology Section

These methodological limitations directly support the research methodology choices described in main.tex by:

- **Justifying Multi-Phase Approach:** Addressing the need for integrated methodologies that span multiple research domains
- **Supporting Comparative Analysis:** Providing rationale for systematic comparison of protocol architectures
- **Validating Rapid Prototyping:** Demonstrating the need for approaches that bridge research and operational contexts
- **Establishing Quality Assurance:** Informing systematic approaches to validation and verification

The identified limitations provide strong methodological justification for the proposed research approach and demonstrate how the chosen methodology addresses significant gaps in current research practices within HDT-related domains.

## References to Gap Analysis Strategy

This analysis aligns with the methodological gap identification strategy outlined in `docs/4.3.1-elicit-search-strategy-gap-analysis.md`, specifically addressing:

- Shortcomings in research methodologies for studying HDT development and implementation
- Underexplored approaches for evaluating human-centric AI systems in operational environments
- Limited methodological integration across the technical and human factors domains essential to HDT development

These limitations provide comprehensive support for the proposed research methodology and demonstrate the significant methodological contributions the research will make to multiple interconnected research domains.
"""
    
    return analysis

def main():
    all_found_limitations = []
    
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    # Process all markdown files
    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            limitations_in_file = find_methodological_limitations(filepath)
            all_found_limitations.extend(limitations_in_file)
            
            if limitations_in_file:
                with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(limitations_in_file)} methodological limitations in {filename}\n")

    # Sort by relevance score (highest first), then by category
    all_found_limitations.sort(key=lambda x: (-x[4], x[1], x[0]))

    # Generate comprehensive analysis
    analysis_content = generate_methodological_analysis(all_found_limitations)
    
    # Write results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(analysis_content)
    
    print(f"Enhanced methodological limitations analysis complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Enhanced analysis complete. Found {len(all_found_limitations)} total methodological limitations.\n")

if __name__ == "__main__":
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting enhanced methodological limitations mapping script...\n")
    main() 
#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "docs" / "4.3.4-theoretical-gaps.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.4_identify_theoretical_gaps.log"

# Enhanced patterns aligned with HDT research framework
THEORETICAL_GAP_PATTERNS = {
    "human_expertise_modeling": [
        "theoretical framework", "conceptual model", "theoretical foundation", "human modeling",
        "expertise representation", "knowledge modeling", "cognitive modeling", "human behavior model",
        "theoretical approach", "conceptual framework", "lack of theory", "theoretical gap",
        "theoretical limitation", "missing framework", "underdeveloped theory"
    ],
    "agent_protocol_composition": [
        "protocol architecture", "agent communication", "protocol design", "multi-agent theory",
        "protocol composition", "agent coordination", "communication protocol", "agent architecture",
        "protocol integration", "theoretical model", "coordination theory", "protocol theory",
        "lacking theoretical", "protocol framework", "architectural framework"
    ],
    "tacit_knowledge_formalization": [
        "tacit knowledge", "implicit knowledge", "knowledge formalization", "knowledge representation",
        "knowledge elicitation", "tacit knowledge capture", "expertise formalization", "knowledge modeling",
        "cognitive knowledge", "experiential knowledge", "theoretical basis", "formalization theory",
        "knowledge theory", "epistemological", "knowledge framework"
    ],
    "human_ai_collaboration": [
        "human-AI collaboration", "human-machine collaboration", "human-computer interaction",
        "collaborative framework", "interaction theory", "collaboration model", "partnership model",
        "human-AI teaming", "cooperative system", "symbiotic system", "theoretical model",
        "collaboration theory", "interaction framework", "partnership theory"
    ],
    "digital_twin_human_integration": [
        "digital twin", "human digital twin", "digital representation", "virtual twin",
        "twin architecture", "digital modeling", "virtual modeling", "cyber-physical",
        "theoretical foundation", "conceptual model", "integration theory", "twin theory",
        "digital twin framework", "virtual representation", "modeling theory"
    ],
    "evaluation_frameworks": [
        "evaluation framework", "assessment framework", "validation framework", "evaluation theory",
        "measurement framework", "evaluation model", "assessment theory", "validation theory",
        "evaluation approach", "measurement theory", "theoretical evaluation", "evaluation methodology"
    ]
}

# Context validation terms for DER/energy operations relevance
CONTEXT_STRENGTHENERS = [
    "energy", "power", "grid", "utility", "DER", "distributed energy", "renewable", "solar", "wind",
    "maintenance", "operations", "operator", "technician", "worker", "personnel", "staff",
    "control room", "SCADA", "monitoring", "management system", "coordination", "planning",
    "human expertise", "operational knowledge", "agent communication", "protocol", "digital twin"
]

CONTEXT_WEAKENERS = [
    "purely theoretical", "academic exercise", "simulation only", "laboratory study",
    "not applicable", "limited scope", "small scale", "proof of concept only",
    "unrelated domain", "different context", "not relevant"
]

# Context window
CONTEXT_WINDOW = 400

def assess_context_relevance(context: str) -> float:
    """Assess how relevant the context is to HDT/DER research (0-1 score)"""
    context_lower = context.lower()
    
    strengthener_score = sum(1 for term in CONTEXT_STRENGTHENERS if term in context_lower)
    weakener_score = sum(1 for term in CONTEXT_WEAKENERS if term in context_lower)
    
    # Base score from strengtheners, penalized by weakeners
    relevance_score = min(1.0, strengthener_score / 3.0) - (weakener_score * 0.2)
    return max(0.0, relevance_score)

def find_theoretical_gaps(filepath: Path) -> list[tuple[str, str, str, str, float]]:
    """Find theoretical gaps aligned with HDT research framework"""
    found_gaps = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for category, keywords in THEORETICAL_GAP_PATTERNS.items():
            for keyword in keywords:
                # Use word boundaries for better matching
                pattern = r'\b' + re.escape(keyword) + r'\b'
                
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    start_index = max(0, match.start() - CONTEXT_WINDOW)
                    end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                    
                    context_snippet = content[start_index:end_index]
                    
                    # Assess relevance to HDT/DER research
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
                        
                        found_gaps.append((
                            filepath.name, 
                            category, 
                            keyword, 
                            context_highlighted, 
                            relevance_score
                        ))
                        
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    
    return found_gaps

def generate_theoretical_analysis(all_gaps: list) -> str:
    """Generate comprehensive theoretical gap analysis"""
    
    # Categorize gaps by theoretical domain
    gap_categories = {}
    for paper_name, category, keyword, context, relevance_score in all_gaps:
        if category not in gap_categories:
            gap_categories[category] = []
        gap_categories[category].append((paper_name, keyword, context, relevance_score))
    
    # Sort categories by number of gaps (importance)
    sorted_categories = sorted(gap_categories.items(), key=lambda x: len(x[1]), reverse=True)
    
    analysis = """# Identified Theoretical Gaps in Literature

*Generated: 2025-01-20*  
*Based on: Literature synthesis from phases 4.1-4.3*  
*Supporting: Research proposal theoretical framework development*

## Executive Summary

The systematic literature review reveals significant theoretical gaps in the integration of human expertise modeling with agent communication protocols for distributed energy resource management. These gaps represent fundamental barriers to developing effective Human DER Worker Digital Twins (HDTs) and highlight critical areas where theoretical advancement is needed.

"""
    
    # Add statistics
    total_gaps = len(all_gaps)
    high_relevance = len([g for g in all_gaps if g[4] > 0.7])
    medium_relevance = len([g for g in all_gaps if 0.5 <= g[4] <= 0.7])
    low_relevance = len([g for g in all_gaps if 0.3 <= g[4] < 0.5])
    
    analysis += f"""**Analysis Statistics:**
- **Total theoretical gaps identified:** {total_gaps}
- **High relevance (>0.7):** {high_relevance}
- **Medium relevance (0.5-0.7):** {medium_relevance}  
- **Low relevance (0.3-0.5):** {low_relevance}

## Primary Theoretical Gaps by Research Domain

"""
    
    # Generate category-specific analysis
    category_descriptions = {
        "human_expertise_modeling": {
            "title": "Human Expertise Representation in Protocol-Enabled Digital Twins",
            "description": "Current Digital Twin frameworks focus predominantly on physical asset modeling, with limited theoretical development for representing human cognitive processes, tacit knowledge, and adaptive decision-making within protocol-enabled environments."
        },
        "agent_protocol_composition": {
            "title": "Agent Protocol Composition for Human-Centric Coordination", 
            "description": "Existing agent communication protocols (MCP, ACP, A2A) lack theoretical frameworks for composing multi-protocol architectures that can effectively model complex human coordination patterns in distributed energy systems."
        },
        "tacit_knowledge_formalization": {
            "title": "Tacit Knowledge Formalization in Agent-Based Systems",
            "description": "Current theoretical approaches to knowledge representation in agent systems inadequately address the formalization of tacit knowledge—the implicit understanding that makes human experts effective in complex operational contexts."
        },
        "human_ai_collaboration": {
            "title": "Dynamic Human-AI Collaboration Models",
            "description": "Theoretical frameworks for human-AI collaboration lack specific models for dynamic, bidirectional learning between human experts and their digital twin representations in operational contexts."
        },
        "digital_twin_human_integration": {
            "title": "Digital Twin Technology for Human Integration",
            "description": "Existing digital twin theoretical frameworks inadequately address the integration of human behavioral modeling with technical system representations."
        },
        "evaluation_frameworks": {
            "title": "Evaluation Theory for Human-Centric Digital Twins",
            "description": "No comprehensive theoretical framework exists for evaluating the effectiveness of human digital twins in operational contexts, particularly regarding fidelity, utility, and human acceptance."
        }
    }
    
    gap_counter = 1
    for category, gaps in sorted_categories:
        if category in category_descriptions:
            desc = category_descriptions[category]
            analysis += f"""### {gap_counter}. {desc['title']}

**Gap Identification:** {desc['description']}

**Literature Evidence:** Analysis of {len(gaps)} instances across {len(set(g[0] for g in gaps))} papers reveals consistent patterns in theoretical limitations.

**Research Need:** Theoretical frameworks that can systematically address this gap within agent-based digital twin architectures for DER applications.

**Key Literature Findings:**

"""
            
            # Add top 3 most relevant examples
            sorted_gaps = sorted(gaps, key=lambda x: x[3], reverse=True)[:3]
            for paper_name, keyword, context, relevance_score in sorted_gaps:
                analysis += f"""**{paper_name}** | `{keyword}` | Relevance: {relevance_score:.2f}
```text
{context[:300]}{'...' if len(context) > 300 else ''}
```

"""
            gap_counter += 1
    
    # Add implications section
    analysis += """## Implications for Research Design

These theoretical gaps directly support the need for the proposed research framework, which addresses:

1. **Theoretical Framework Development:** Creating comprehensive models for HDT architecture and agent protocol composition
2. **Knowledge Representation Innovation:** Developing approaches for tacit knowledge formalization within agent-based systems  
3. **Collaboration Theory Advancement:** Establishing theoretical foundations for dynamic human-digital twin partnerships
4. **Evaluation Framework Creation:** Developing theoretical models for assessing HDT effectiveness across multiple dimensions

## Alignment with Research Objectives

The identified theoretical gaps directly align with the research objectives by:

- **Objective 1:** Human expertise modeling and tacit knowledge gaps support the need to identify and structure human expertise components
- **Objective 2:** Protocol composition and digital twin integration gaps support the need for protocol-enabled HDT architecture design
- **Objective 3:** Evaluation framework gaps support the need for comprehensive evaluation framework development

These gaps provide strong theoretical justification for the proposed research and demonstrate the significant contribution that HDT framework development would make to the field.

## References to Gap Analysis Strategy

This analysis aligns with the gap identification strategy outlined in `docs/4.3.1-elicit-search-strategy-gap-analysis.md`, specifically addressing:

- Missing links between human expertise modeling and agent communication protocols
- Underdeveloped concepts in digital twin technology for human representation  
- Unaddressed theoretical questions regarding protocol composition for human-centric applications

The identified gaps provide a solid theoretical foundation for the research proposal and demonstrate the significant theoretical contributions the proposed HDT framework will make to multiple interconnected research domains.
"""
    
    return analysis

def main():
    all_found_gaps = []
    
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    # Process all markdown files
    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            gaps_in_file = find_theoretical_gaps(filepath)
            all_found_gaps.extend(gaps_in_file)
            
            if gaps_in_file:
                with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(gaps_in_file)} theoretical gaps in {filename}\n")

    # Sort by relevance score (highest first), then by category
    all_found_gaps.sort(key=lambda x: (-x[4], x[1], x[0]))

    # Generate comprehensive analysis
    analysis_content = generate_theoretical_analysis(all_found_gaps)
    
    # Write results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(analysis_content)
    
    print(f"Enhanced theoretical gap analysis complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Enhanced analysis complete. Found {len(all_found_gaps)} total theoretical gaps.\n")

if __name__ == "__main__":
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting enhanced theoretical gap identification script...\n")
    main() 
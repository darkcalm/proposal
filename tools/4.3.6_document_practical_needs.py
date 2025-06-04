#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "docs" / "4.3.6-practical-needs.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.6_document_practical_needs.log"

# Enhanced keywords aligned with gap analysis strategy
PRACTICAL_CHALLENGE_PATTERNS = {
    "human_expertise_management": [
        "knowledge transfer", "expertise retention", "tacit knowledge", "human knowledge", 
        "institutional memory", "operator experience", "expert knowledge", "knowledge preservation",
        "skill gap", "expertise gap", "knowledge management", "human capital", "workforce knowledge"
    ],
    "human_system_interaction": [
        "human-machine interface", "human-computer interaction", "operator interface", 
        "user experience", "human factors", "cognitive load", "situational awareness",
        "automation bias", "trust in automation", "human-AI collaboration", "operator support",
        "decision support", "interaction challenges", "interface design"
    ],
    "coordination_challenges": [
        "coordination difficulty", "coordination challenge", "communication gap", "information sharing",
        "multi-stakeholder", "distributed coordination", "collaborative decision", "consensus building",
        "stakeholder alignment", "organizational silos", "coordination complexity", "handoff issues"
    ],
    "operational_complexity": [
        "operational challenge", "complexity management", "system complexity", "operational burden",
        "cognitive complexity", "decision complexity", "adaptive management", "dynamic environment",
        "uncertainty management", "real-time decision", "operational overhead"
    ],
    "scalability_issues": [
        "scalability challenge", "scaling expertise", "scaling operations", "resource constraints",
        "deployment challenge", "adoption barrier", "implementation challenge", "rollout difficulty",
        "standardization issue", "replication challenge"
    ],
    "digital_transformation": [
        "digital transformation", "digitalization challenge", "technology adoption", "digital tool",
        "automation impact", "technology integration", "digital workflow", "system modernization",
        "legacy system", "digital divide"
    ]
}

# Context validation terms that strengthen relevance
CONTEXT_STRENGTHENERS = [
    "energy", "power", "grid", "utility", "DER", "distributed energy", "renewable", "solar", "wind",
    "maintenance", "operations", "operator", "technician", "worker", "personnel", "staff",
    "control room", "SCADA", "monitoring", "management system", "coordination", "planning"
]

# Negative context terms that weaken relevance
CONTEXT_WEAKENERS = [
    "purely theoretical", "academic exercise", "simulation only", "laboratory study",
    "not applicable", "limited scope", "small scale", "proof of concept only"
]

# Context window
CONTEXT_WINDOW = 400

def assess_context_relevance(context: str) -> float:
    """Assess how relevant the context is to DER/energy operations (0-1 score)"""
    context_lower = context.lower()
    
    strengthener_score = sum(1 for term in CONTEXT_STRENGTHENERS if term in context_lower)
    weakener_score = sum(1 for term in CONTEXT_WEAKENERS if term in context_lower)
    
    # Base score from strengtheners, penalized by weakeners
    relevance_score = min(1.0, strengthener_score / 3.0) - (weakener_score * 0.2)
    return max(0.0, relevance_score)

def find_practical_challenges(filepath: Path) -> list[tuple[str, str, str, str, float]]:
    """Find practical challenges aligned with gap analysis strategy"""
    found_challenges = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for category, keywords in PRACTICAL_CHALLENGE_PATTERNS.items():
            for keyword in keywords:
                # Use word boundaries for better matching
                pattern = r'\b' + re.escape(keyword) + r'\b'
                
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    start_index = max(0, match.start() - CONTEXT_WINDOW)
                    end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                    
                    context_snippet = content[start_index:end_index]
                    
                    # Assess relevance to DER/energy operations
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
                        
                        found_challenges.append((
                            filepath.name, 
                            category, 
                            keyword, 
                            context_highlighted, 
                            relevance_score
                        ))
                        
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    
    return found_challenges

def main():
    all_challenges = []
    
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    # Process all markdown files
    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            challenges_in_file = find_practical_challenges(filepath)
            all_challenges.extend(challenges_in_file)
            
            if challenges_in_file:
                with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(challenges_in_file)} practical challenges in {filename}\n")

    # Sort by relevance score (highest first), then by category
    all_challenges.sort(key=lambda x: (-x[4], x[1], x[0]))

    # Write results
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Practical Challenges Identified in Literature\n\n")
        f.write("*Aligned with gap analysis strategy for Human DER Worker Digital Twins*\n\n")
        
        if not all_challenges:
            f.write("No practical challenges identified meeting the relevance criteria.\n")
        else:
            f.write(f"**Total challenges found:** {len(all_challenges)}\n")
            f.write(f"**High relevance (>0.7):** {len([c for c in all_challenges if c[4] > 0.7])}\n")
            f.write(f"**Medium relevance (0.5-0.7):** {len([c for c in all_challenges if 0.5 <= c[4] <= 0.7])}\n")
            f.write(f"**Low relevance (0.3-0.5):** {len([c for c in all_challenges if 0.3 <= c[4] < 0.5])}\n\n")
            
            # Group by category
            current_category = None
            for paper_name, category, keyword, context, relevance_score in all_challenges:
                if category != current_category:
                    f.write(f"\n## {category.replace('_', ' ').title()}\n\n")
                    current_category = category
                
                f.write(f"### {paper_name} | `{keyword}` | Relevance: {relevance_score:.2f}\n")
                f.write("```text\n")
                f.write(context + "\n")
                f.write("```\n\n")
    
    print(f"Enhanced practical challenges analysis complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Enhanced analysis complete. Found {len(all_challenges)} total challenges.\n")

if __name__ == "__main__":
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting enhanced practical challenges analysis...\n")
    main() 
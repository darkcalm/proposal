#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.6-practical-needs.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.6_document_practical_needs.log"

# Keywords for practical needs
PRACTICAL_NEED_KEYWORDS = [
    "practical need", "industry requirement", "real-world application", "operational challenge", 
    "future work", # Context will be checked for practical relevance
    "unmet need", "practical implication", "need for tool", "need for framework", "practical gap",
    "application challenge", "implementation challenge", "deployment issue"
]

# Context window (number of characters before and after the keyword)
CONTEXT_WINDOW = 300 # Slightly larger to capture more context for "future work"

KEYWORDS_REQUIRING_CONTEXT_CHECK = ["future work"] # Keywords that need stronger contextual validation
CONTEXT_VALIDATION_TERMS = ["practical", "implement", "deploy", "real-world", "industry", "tool", "framework", "application", "operational"]

def find_needs_in_file(filepath: Path) -> list[tuple[str, str, str]]:
    found_needs = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for keyword in PRACTICAL_NEED_KEYWORDS:
            for match in re.finditer(re.escape(keyword), content, re.IGNORECASE):
                start_index = max(0, match.start() - CONTEXT_WINDOW)
                end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                
                context_snippet = content[start_index:end_index]
                
                # Context validation for ambiguous keywords like "future work"
                if keyword.lower() in KEYWORDS_REQUIRING_CONTEXT_CHECK:
                    is_relevant_context = False
                    for term in CONTEXT_VALIDATION_TERMS:
                        if term in context_snippet.lower():
                            is_relevant_context = True
                            break
                    if not is_relevant_context:
                        continue # Skip this match if context validation fails

                context_snippet = context_snippet.replace("\n", " ").replace("\r", "").strip()
                context_snippet = re.sub(r'\s+', ' ', context_snippet)
                
                matched_text = match.group(0)
                context_snippet_highlighted = context_snippet.replace(matched_text, f"**{matched_text}**")
                found_needs.append((filepath.name, keyword, context_snippet_highlighted))
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    return found_needs

def main():
    all_found_needs = []
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            needs_in_file = find_needs_in_file(filepath)
            all_found_needs.extend(needs_in_file)
            if needs_in_file:
                with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(needs_in_file)} potential practical needs in {filename}\n")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Identified Practical Needs in Literature\n\n")
        if not all_found_needs:
            f.write("No specific practical needs identified based on the keyword search and context validation.\n")
        else:
            all_found_needs.sort(key=lambda x: (x[0], x[1]))
            current_paper = None
            for paper_name, keyword, context in all_found_needs:
                if paper_name != current_paper:
                    f.write(f"\n## Paper: {paper_name}\n\n")
                    current_paper = paper_name
                f.write(f"### Keyword: `{keyword}`\n")
                f.write("```text\n")
                f.write(context + "\n")
                f.write("```\n\n")
    
    print(f"Practical needs documentation complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Practical needs documentation complete. Results saved to {OUTPUT_FILE}\n")

if __name__ == "__main__":
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting practical needs documentation script...\n")
    main() 
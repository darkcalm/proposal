#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.4-theoretical-gaps.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.4_identify_theoretical_gaps.log"

# Keywords for theoretical gaps
THEORETICAL_GAP_KEYWORDS = [
    "theoretical gap", "conceptual limitation", "theoretical challenge", 
    "future theoretical work", "unexplored theory", "lack of theory", 
    "theoretical framework needs", "underlying principles lacking", "gap in theory",
    "theoretical understanding", "conceptual gap", "foundational gap", "theoretical underpinning"
]

# Context window (number of characters before and after the keyword)
CONTEXT_WINDOW = 250

def find_gaps_in_file(filepath: Path) -> list[tuple[str, str, str]]:
    found_gaps = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Normalize content for easier searching (optional, consider case sensitivity)
        # content_lower = content.lower()

        for keyword in THEORETICAL_GAP_KEYWORDS:
            # Using re.finditer to find all occurrences with their positions
            for match in re.finditer(re.escape(keyword), content, re.IGNORECASE):
                start_index = max(0, match.start() - CONTEXT_WINDOW)
                end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                
                context_snippet = content[start_index:end_index]
                # Sanitize context for markdown (e.g. escape special characters if any, though usually not needed for text)
                context_snippet = context_snippet.replace("\n", " ").replace("\r", "").strip()
                context_snippet = re.sub(r'\s+', ' ', context_snippet)


                # Highlight the keyword in the snippet
                # This needs to be done carefully if keyword might have regex special chars
                # For simple string keywords, direct replace works.
                # For regex keywords, match.group(0) gives the actual matched string.
                matched_text = match.group(0)
                context_snippet_highlighted = context_snippet.replace(matched_text, f"**{matched_text}**")

                found_gaps.append((filepath.name, keyword, context_snippet_highlighted))
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    return found_gaps

def main():
    all_found_gaps = []
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            gaps_in_file = find_gaps_in_file(filepath)
            all_found_gaps.extend(gaps_in_file)
            if gaps_in_file:
                 with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(gaps_in_file)} potential theoretical gaps in {filename}\n")


    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Identified Theoretical Gaps in Literature\n\n")
        if not all_found_gaps:
            f.write("No specific theoretical gaps identified based on the keyword search.\n")
        else:
            # Sort by paper, then by keyword for consistent output
            all_found_gaps.sort(key=lambda x: (x[0], x[1]))
            current_paper = None
            for paper_name, keyword, context in all_found_gaps:
                if paper_name != current_paper:
                    f.write(f"\n## Paper: {paper_name}\n\n")
                    current_paper = paper_name
                f.write(f"### Keyword: `{keyword}`\n")
                f.write("```text\n")
                f.write(context + "\n")
                f.write("```\n\n")
    
    print(f"Theoretical gap identification complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Theoretical gap identification complete. Results saved to {OUTPUT_FILE}\n")

if __name__ == "__main__":
    # Initialize log file
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting theoretical gap identification script...\n")
    main() 
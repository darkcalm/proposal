#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_PAPERS_DIR = Path(__file__).resolve().parent.parent / "sources" / "4.3.1-elicit-results" / "markdown_papers"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.5-methodological-limitations.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.5_map_methodological_limitations.log"

# Keywords for methodological limitations
METHODOLOGICAL_KEYWORDS = [
    "methodological limitation", "study limitation", "methodological challenge", 
    "research design issue", "data collection limitation", "analysis limitation", 
    "validation issue", "lack of method", "methodological gap", "limitation of method",
    "methodological concern", "methodological constraint", "empirical gap"
]

# Context window (number of characters before and after the keyword)
CONTEXT_WINDOW = 250

def find_limitations_in_file(filepath: Path) -> list[tuple[str, str, str]]:
    found_limitations = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for keyword in METHODOLOGICAL_KEYWORDS:
            for match in re.finditer(re.escape(keyword), content, re.IGNORECASE):
                start_index = max(0, match.start() - CONTEXT_WINDOW)
                end_index = min(len(content), match.end() + CONTEXT_WINDOW)
                
                context_snippet = content[start_index:end_index]
                context_snippet = context_snippet.replace("\n", " ").replace("\r", "").strip()
                context_snippet = re.sub(r'\s+', ' ', context_snippet)
                
                matched_text = match.group(0)
                context_snippet_highlighted = context_snippet.replace(matched_text, f"**{matched_text}**")
                found_limitations.append((filepath.name, keyword, context_snippet_highlighted))
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name}: {e}\n")
    return found_limitations

def main():
    all_found_limitations = []
    if not MARKDOWN_PAPERS_DIR.exists() or not MARKDOWN_PAPERS_DIR.is_dir():
        with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
            log_f.write(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}\n")
        print(f"Error: Markdown papers directory not found at {MARKDOWN_PAPERS_DIR}")
        return

    for filename in os.listdir(MARKDOWN_PAPERS_DIR):
        if filename.endswith(".md"):
            filepath = MARKDOWN_PAPERS_DIR / filename
            limitations_in_file = find_limitations_in_file(filepath)
            all_found_limitations.extend(limitations_in_file)
            if limitations_in_file:
                with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
                    log_f.write(f"Found {len(limitations_in_file)} potential methodological limitations in {filename}\n")

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Identified Methodological Limitations in Literature\n\n")
        if not all_found_limitations:
            f.write("No specific methodological limitations identified based on the keyword search.\n")
        else:
            all_found_limitations.sort(key=lambda x: (x[0], x[1]))
            current_paper = None
            for paper_name, keyword, context in all_found_limitations:
                if paper_name != current_paper:
                    f.write(f"\n## Paper: {paper_name}\n\n")
                    current_paper = paper_name
                f.write(f"### Keyword: `{keyword}`\n")
                f.write("```text\n")
                f.write(context + "\n")
                f.write("```\n\n")
    
    print(f"Methodological limitation mapping complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Methodological limitation mapping complete. Results saved to {OUTPUT_FILE}\n")

if __name__ == "__main__":
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting methodological limitation mapping script...\n")
    main() 
#!/usr/bin/env python3

import os
import re
from pathlib import Path

# Configuration
THEORETICAL_GAPS_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.4-theoretical-gaps.md"
METHODOLOGICAL_LIMITATIONS_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.5-methodological-limitations.md"
PRACTICAL_NEEDS_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.6-practical-needs.md"
OUTPUT_FILE = Path(__file__).resolve().parent.parent / "sources" / "4.3.7-preliminary-gap-statement.md"
LOG_FILE = Path(__file__).resolve().parent / "4.3.7_formulate_gap_statement.log"

MAX_ENTRIES_PER_CATEGORY = 10 # Max entries to include from each file to keep summary concise

def extract_key_points(filepath: Path, section_title: str, max_entries: int) -> list[str]:
    """Extracts paper names and keyword contexts from the gap/limitation/need files."""
    key_points = []
    if not filepath.exists():
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Warning: File not found {filepath}. Skipping for {section_title}.\n")
        return [f"- Data file missing: {filepath.name}"]

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find paper sections and then keyword sections within them
        # This is a simplified parser; assumes a certain structure of the input .md files
        paper_sections = re.split(r'\n## Paper: ', content)[1:] # Split by paper, skip header
        entries_count = 0

        for paper_section in paper_sections:
            if entries_count >= max_entries:
                break
            
            paper_name_match = re.match(r'(.*?)\n', paper_section)
            if not paper_name_match:
                continue
            paper_name = paper_name_match.group(1).strip()
            
            keyword_sections = re.split(r'### Keyword: ', paper_section)[1:]
            for keyword_section in keyword_sections:
                if entries_count >= max_entries:
                    break
                
                keyword_match = re.match(r'`(.*?)`\n```text\n(.*?)\n```', keyword_section, re.DOTALL)
                if keyword_match:
                    keyword = keyword_match.group(1).strip()
                    context = keyword_match.group(2).strip()
                    # Take first ~150 chars of context for brevity in summary
                    brief_context = context[:150] + ("..." if len(context) > 150 else "")
                    key_points.append(f"- **{paper_name}** (Keyword: `{keyword}`): {brief_context}")
                    entries_count += 1
        
        if not key_points:
            key_points.append("- No specific points extracted.")
        elif entries_count >= max_entries:
            key_points.append("- *Further entries exist but are omitted for brevity.*")
            
    except Exception as e:
        with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
            log_f.write(f"Error processing file {filepath.name} for {section_title}: {e}\n")
        key_points.append(f"- Error processing {filepath.name}")
    return key_points

def main():
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write("Starting gap statement formulation script...\n")

    theoretical_points = extract_key_points(THEORETICAL_GAPS_FILE, "Theoretical Gaps", MAX_ENTRIES_PER_CATEGORY)
    methodological_points = extract_key_points(METHODOLOGICAL_LIMITATIONS_FILE, "Methodological Limitations", MAX_ENTRIES_PER_CATEGORY)
    practical_points = extract_key_points(PRACTICAL_NEEDS_FILE, "Practical Needs", MAX_ENTRIES_PER_CATEGORY)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write("# Preliminary Research Gap Statement\n\n")
        f.write("This document synthesizes identified gaps from the literature to formulate a preliminary research gap statement. It draws upon analyses of theoretical gaps, methodological limitations, and practical needs highlighted in the reviewed papers.\n\n")
        f.write("The source files for this synthesis are:\n")
        f.write(f"- Theoretical Gaps: `{THEORETICAL_GAPS_FILE.name}`\n")
        f.write(f"- Methodological Limitations: `{METHODOLOGICAL_LIMITATIONS_FILE.name}`\n")
        f.write(f"- Practical Needs: `{PRACTICAL_NEEDS_FILE.name}`\n\n")

        f.write("## 1. Summary of Identified Theoretical Gaps\n")
        f.write("The literature review points to several areas where theoretical underpinnings may be lacking or require further development. Key points include:\n")
        for point in theoretical_points:
            f.write(f"{point}\n")
        f.write("\n")

        f.write("## 2. Summary of Identified Methodological Limitations\n")
        f.write("Existing research exhibits certain methodological limitations that could be addressed. Key points include:\n")
        for point in methodological_points:
            f.write(f"{point}\n")
        f.write("\n")

        f.write("## 3. Summary of Identified Practical Needs\n")
        f.write("Several practical needs and real-world challenges have been highlighted, suggesting areas for impactful research. Key points include:\n")
        for point in practical_points:
            f.write(f"{point}\n")
        f.write("\n")
        
        f.write("## 4. Preliminary Gap Formulation\n")
        f.write("Based on the synthesis above, a preliminary research gap can be formulated. This research aims to address the confluence of:\n")
        f.write("- **Theoretical Gaps:** [Synthesize 1-2 key theoretical themes from section 1]\n")
        f.write("- **Methodological Limitations:** [Synthesize 1-2 key methodological themes from section 2]\n")
        f.write("- **Practical Needs:** [Synthesize 1-2 key practical themes from section 3]\n\n")
        f.write("Specifically, there is an opportunity to [describe the proposed research focus that addresses these combined gaps, e.g., 'develop a novel framework for X that overcomes identified theoretical and methodological limitations to meet the practical need for Y in the context of AI Agent Protocols']. Further refinement of this statement will be undertaken based on these initial findings.\n")

    print(f"Preliminary gap statement formulation complete. Results saved to {OUTPUT_FILE}")
    with open(LOG_FILE, 'a', encoding='utf-8') as log_f:
        log_f.write(f"Preliminary gap statement formulation complete. Results saved to {OUTPUT_FILE}\n")

if __name__ == "__main__":
    main() 
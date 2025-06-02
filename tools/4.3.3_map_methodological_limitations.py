#!/usr/bin/env python3
"""
Map Methodological Limitations Script (Task 4.3.3)
Aggregates and categorizes methodological limitations from research outputs.

This script:
1. Loads methodological limitations from:
   - docs/4.2.4.3-document-validation-findings.md
   - docs/4.3.2-theoretical-gaps-analysis.md
   - docs/4.2.4.4-updated-framework.md
2. Synthesizes and categorizes limitations
3. Outputs a structured markdown file for Task 4.3.3
"""

import os
import re
from datetime import datetime
from pathlib import Path

def extract_limitations_from_validation_findings():
    path = Path("../docs/4.2.4.3-document-validation-findings.md")
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract Methodological Limitations section
    match = re.search(r"### 3.2 Methodological Limitations\n(.*?)(?=###|##|$)", content, re.DOTALL)
    if match:
        lines = [line.strip('- ').strip() for line in match.group(1).split('\n') if line.strip() and not line.startswith('###')]
        return lines
    return []

def extract_limitations_from_theoretical_gaps():
    path = Path("../docs/4.3.2-theoretical-gaps-analysis.md")
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract Methodological Gaps section
    match = re.search(r"### 4\. Methodological Gaps\n(.*?)(?=###|##|$)", content, re.DOTALL)
    if match:
        lines = [line.strip('- ').strip() for line in match.group(1).split('\n') if line.strip() and not line.startswith('####')]
        return lines
    return []

def extract_limitations_from_updated_framework():
    path = Path("../docs/4.2.4.4-updated-framework.md")
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract Identified Limitations section
    match = re.search(r"### Identified Limitations\n(.*?)(?=###|##|$)", content, re.DOTALL)
    if match:
        lines = [line.strip('- ').strip() for line in match.group(1).split('\n') if line.strip() and not line.startswith('###')]
        return lines
    return []

def synthesize_limitations():
    findings = extract_limitations_from_validation_findings()
    gaps = extract_limitations_from_theoretical_gaps()
    framework = extract_limitations_from_updated_framework()
    all_limitations = findings + gaps + framework
    # Deduplicate and categorize
    unique = list(dict.fromkeys([l for l in all_limitations if l]))
    categories = {
        'Practical Validation': [],
        'System Evaluation': [],
        'Heuristic/Indirect Evidence': [],
        'Scope/Corpus': [],
        'Integration/Extensions': [],
        'Other': []
    }
    for lim in unique:
        l = lim.lower()
        if 'practical validation' in l:
            categories['Practical Validation'].append(lim)
        elif 'system-level evaluation' in l or 'system evaluation' in l:
            categories['System Evaluation'].append(lim)
        elif 'heuristic' in l or 'indirect evidence' in l:
            categories['Heuristic/Indirect Evidence'].append(lim)
        elif 'corpus' in l or 'scope' in l:
            categories['Scope/Corpus'].append(lim)
        elif 'integration' in l or 'extension' in l:
            categories['Integration/Extensions'].append(lim)
        else:
            categories['Other'].append(lim)
    return categories

def generate_report(categories):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    doc = f"""# Methodological Limitations Mapping (Task 4.3.3)

*Generated: {timestamp}*

This document aggregates and categorizes methodological limitations identified in previous research tasks.

## Summary Table

| Category | Count |
|----------|-------|
"""
    for cat, items in categories.items():
        doc += f"| {cat} | {len(items)} |\n"
    doc += "\n## Detailed Limitations by Category\n"
    for cat, items in categories.items():
        doc += f"\n### {cat}\n"
        if items:
            for lim in items:
                doc += f"- {lim}\n"
        else:
            doc += "- None\n"
    doc += """

## Sources Used
- docs/4.2.4.3-document-validation-findings.md
- docs/4.3.2-theoretical-gaps-analysis.md
- docs/4.2.4.4-updated-framework.md

---
*Ready for: Task 4.3.4 - Document practical needs*
"""
    return doc

def main():
    print("Mapping methodological limitations...")
    categories = synthesize_limitations()
    report = generate_report(categories)
    output_file = "../docs/4.3.3-methodological-limitations.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✅ Methodological limitations mapping complete: {output_file}")
    print(f"Categories: {[(k, len(v)) for k,v in categories.items()]}")
    print("Ready for Task 4.3.4 - Document practical needs.")

if __name__ == "__main__":
    main() 
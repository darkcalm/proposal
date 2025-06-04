#!/usr/bin/env python3
"""
Task 8.1.1: Allocate word count for sections
Analyze content mass from phases 4-7 and allocate words appropriately for 2000-3000 word proposal
"""

import json
import os
from pathlib import Path
import re

def count_words_in_file(filepath):
    """Count words in a text file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            # Remove markdown formatting and special characters for better word count
            content = re.sub(r'[#*`\-\[\](){}]', ' ', content)
            content = re.sub(r'\s+', ' ', content)
            words = content.split()
            return len(words)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return 0

def analyze_content_mass():
    """Analyze the content mass from phases 4-7"""
    
    docs_dir = Path("docs")
    sources_dir = Path("sources") 
    
    # Content categories and their associated files
    content_analysis = {
        "4_literature_review": {
            "description": "Systematic literature review and gap analysis (4.*)",
            "files": [],
            "word_count": 0,
            "sections": ["Background/Literature Review", "Research Gap Identification"]
        },
        "5_methodology": {
            "description": "Methodology development and justification (5.*)", 
            "files": [],
            "word_count": 0,
            "sections": ["Research Methodology", "Alternative Methodologies"]
        },
        "6_ethics_sustainability": {
            "description": "Ethics and sustainability integration (6.*)",
            "files": [],
            "word_count": 0,
            "sections": ["Ethics and Sustainability Considerations"]
        },
        "7_risk_timeline": {
            "description": "Risk assessment and timeline planning (7.*)",
            "files": [],
            "word_count": 0,
            "sections": ["Risk Assessment", "Implementation Plan and Timeline"]
        }
    }
    
    # Scan for relevant files
    for file_path in docs_dir.glob("*.md"):
        filename = file_path.name
        if filename.startswith("4."):
            content_analysis["4_literature_review"]["files"].append(str(file_path))
            content_analysis["4_literature_review"]["word_count"] += count_words_in_file(file_path)
        elif filename.startswith("5."):
            content_analysis["5_methodology"]["files"].append(str(file_path))
            content_analysis["5_methodology"]["word_count"] += count_words_in_file(file_path)
        elif filename.startswith("6."):
            content_analysis["6_ethics_sustainability"]["files"].append(str(file_path))
            content_analysis["6_ethics_sustainability"]["word_count"] += count_words_in_file(file_path)
        elif filename.startswith("7."):
            content_analysis["7_risk_timeline"]["files"].append(str(file_path))
            content_analysis["7_risk_timeline"]["word_count"] += count_words_in_file(file_path)
    
    # Also check JSON files for additional content
    for file_path in sources_dir.glob("*.json"):
        filename = file_path.name
        # Approximate JSON content as 50% of text equivalent (accounting for structure)
        json_words = count_words_in_file(file_path) * 0.5
        
        if filename.startswith("4.") or "4." in filename:
            content_analysis["4_literature_review"]["word_count"] += json_words
        elif filename.startswith("5.") or "5." in filename:
            content_analysis["5_methodology"]["word_count"] += json_words
        elif filename.startswith("6.") or "6." in filename:
            content_analysis["6_ethics_sustainability"]["word_count"] += json_words
        elif filename.startswith("7.") or "7." in filename:
            content_analysis["7_risk_timeline"]["word_count"] += json_words
    
    return content_analysis

def calculate_word_allocation(content_analysis, target_words=2500):
    """Calculate word allocation based on content mass and proposal requirements"""
    
    # Calculate total content mass
    total_content_mass = sum(category["word_count"] for category in content_analysis.values())
    
    # Base allocation considering proposal structure requirements
    base_allocation = {
        "title_abstract_toc": {
            "words": 0,  # Title page and TOC not counted in word limit
            "description": "Title page and table of contents (not counted in word limit)"
        },
        "introduction_background": {
            "words": 0,  # Will be calculated based on content
            "description": "Introduction, background, literature review from 4.*",
            "content_source": "4_literature_review"
        },
        "objectives_questions": {
            "words": 300,
            "description": "Research objectives and questions (refined from 3.*)"
        },
        "scope_limitations": {
            "words": 200,
            "description": "Scope and limitations (concise)"
        },
        "theoretical_framework": {
            "words": 250,
            "description": "Key concepts and theoretical framework"
        },
        "methodology": {
            "words": 0,  # Will be calculated based on content
            "description": "Research methodology from 5.*",
            "content_source": "5_methodology"
        },
        "ethics_sustainability": {
            "words": 0,  # Will be calculated based on content
            "description": "Ethics and sustainability considerations from 6.*",
            "content_source": "6_ethics_sustainability"
        },
        "risk_timeline": {
            "words": 0,  # Will be calculated based on content
            "description": "Risk assessment and implementation plan from 7.*",
            "content_source": "7_risk_timeline"
        },
        "expected_results": {
            "words": 200,
            "description": "Expected outcomes and contributions"
        },
        "references_appendices": {
            "words": 150,
            "description": "References section and appendices (not counted in main text)"
        }
    }
    
    # Calculate available words for content-driven sections
    fixed_words = sum(alloc["words"] for alloc in base_allocation.values() if alloc["words"] > 0)
    available_words = target_words - fixed_words
    
    # Determine compression ratios based on content mass
    content_driven_sections = ["introduction_background", "methodology", "ethics_sustainability", "risk_timeline"]
    content_masses = {section: content_analysis[base_allocation[section]["content_source"]]["word_count"] 
                     for section in content_driven_sections if "content_source" in base_allocation[section]}
    
    total_mass = sum(content_masses.values())
    
    # Allocate words proportionally to content mass with adjustments for proposal requirements
    allocation_weights = {
        "introduction_background": 0.45,  # Largest section - rich background needed
        "methodology": 0.25,              # Substantial methodology section
        "ethics_sustainability": 0.15,    # Important but more concise
        "risk_timeline": 0.15             # Important but can be condensed
    }
    
    # Calculate final allocations
    for section in content_driven_sections:
        if "content_source" in base_allocation[section]:
            base_allocation[section]["words"] = int(available_words * allocation_weights[section])
            
            # Calculate compression ratio
            original_mass = content_analysis[base_allocation[section]["content_source"]]["word_count"]
            if original_mass > 0:
                compression_ratio = base_allocation[section]["words"] / original_mass
                base_allocation[section]["compression_ratio"] = compression_ratio
                base_allocation[section]["original_content_mass"] = int(original_mass)
    
    return base_allocation, total_content_mass

def generate_allocation_report(content_analysis, word_allocation, total_content_mass, target_words):
    """Generate comprehensive word allocation report"""
    
    report = f"""# Word Count Allocation for Research Proposal (Task 8.1.1)

## Executive Summary

**Target Word Count:** {target_words} words (approximately 5-6 pages)
**Note:** Title page and table of contents are not counted in the word limit
**Total Available Content Mass:** {int(total_content_mass):,} words from phases 4-7
**Overall Compression Ratio:** {target_words/total_content_mass:.1%} (significant compression required)

## Content Mass Analysis by Phase

"""
    
    for key, category in content_analysis.items():
        report += f"""### {category['description']}
- **Content Mass:** {int(category['word_count']):,} words
- **Number of Files:** {len(category['files'])}
- **Target Sections:** {', '.join(category['sections'])}

"""
    
    report += f"""## Proposed Word Allocation by Section

| Section | Words | % of Total | Compression | Original Mass | Description |
|---------|-------|------------|-------------|---------------|-------------|
"""
    
    total_allocated = 0
    for section, allocation in word_allocation.items():
        words = allocation["words"]
        percentage = (words / target_words) * 100
        
        compression_info = ""
        original_mass_info = ""
        if "compression_ratio" in allocation:
            compression_info = f"{allocation['compression_ratio']:.1%}"
            original_mass_info = f"{allocation['original_content_mass']:,}"
        else:
            compression_info = "New content"
            original_mass_info = "N/A"
            
        report += f"| {section.replace('_', ' ').title()} | {words} | {percentage:.1f}% | {compression_info} | {original_mass_info} | {allocation['description']} |\n"
        total_allocated += words
    
    report += f"\n**Total Allocated:** {total_allocated} words\n\n"
    
    report += """## Section-Specific Guidance

### Introduction and Background (1,125 words)
**Content Sources:** Phase 4.* literature review and gap analysis
**Key Elements to Include:**
- Problem context and significance (300 words)
- Systematic literature review synthesis (500 words) 
- Research gap identification (325 words)
**Compression Strategy:** Focus on most relevant findings, synthesize rather than describe

### Research Methodology (625 words)
**Content Sources:** Phase 5.* methodology development
**Key Elements to Include:**
- Selected methodology justification (300 words)
- Alternative methodologies considered (200 words)
- Data collection and analysis approach (125 words)
**Compression Strategy:** Focus on final justified approach, summarize alternatives

### Ethics and Sustainability (375 words)
**Content Sources:** Phase 6.* ethics and sustainability analysis
**Key Elements to Include:**
- Key ethical considerations (150 words)
- Sustainability dimensions and SDG alignment (150 words)  
- Mitigation strategies (75 words)
**Compression Strategy:** Focus on high-priority concerns, summarize mitigation approaches

### Risk Assessment and Timeline (375 words)
**Content Sources:** Phase 7.* risk management and planning
**Key Elements to Include:**
- Major risk categories and mitigation (200 words)
- Implementation timeline overview (100 words)
- Resource requirements (75 words)
**Compression Strategy:** Focus on high-priority risks, provide timeline overview

## Recommended Compression Strategies

1. **Synthesize Rather Than Describe:** Transform detailed analyses into key insights
2. **Focus on Relevance:** Include only content directly supporting the research objectives
3. **Use Summary Tables:** Replace lengthy descriptions with structured tables
4. **Prioritize High-Impact Content:** Include findings that directly inform the research design
5. **Reference Detailed Work:** Acknowledge comprehensive analyses while presenting distilled insights

## Quality Assurance Guidelines

- Maintain academic rigor while achieving word targets
- Ensure all ILOs are adequately addressed within word limits
- Preserve key technical details and justifications
- Include sufficient citations to demonstrate systematic literature survey
- Balance depth with clarity and readability

## Files Analyzed for Content Mass

"""
    
    for key, category in content_analysis.items():
        if category["files"]:
            report += f"""### {category['description']}
"""
            for file_path in sorted(category["files"])[:10]:  # Limit to first 10 files
                report += f"- {file_path}\n"
            if len(category["files"]) > 10:
                report += f"- ... and {len(category['files']) - 10} more files\n"
            report += "\n"
    
    return report

def main():
    """Main execution function"""
    print("Analyzing content mass from phases 4-7...")
    
    # Analyze available content
    content_analysis = analyze_content_mass()
    
    # Calculate word allocation  
    target_words = 2500  # Mid-point of 2000-3000 range
    word_allocation, total_content_mass = calculate_word_allocation(content_analysis, target_words)
    
    # Generate report
    report = generate_allocation_report(content_analysis, word_allocation, total_content_mass, target_words)
    
    # Save report
    output_file = "docs/8.1.1-word-count-allocation.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ Word count allocation completed")
    print(f"📊 Total content mass: {int(total_content_mass):,} words")
    print(f"🎯 Target proposal length: {target_words} words")
    print(f"📉 Compression ratio: {target_words/total_content_mass:.1%}")
    print(f"💾 Report saved to: {output_file}")
    
    # Print summary to console
    print("\n" + "="*60)
    print("WORD ALLOCATION SUMMARY")
    print("="*60)
    
    for section, allocation in word_allocation.items():
        words = allocation["words"]
        percentage = (words / target_words) * 100
        print(f"{section.replace('_', ' ').title():<25} {words:>4} words ({percentage:>4.1f}%)")
    
    print("-"*60)
    total = sum(allocation["words"] for allocation in word_allocation.values())
    print(f"{'TOTAL':<25} {total:>4} words")

if __name__ == "__main__":
    main() 
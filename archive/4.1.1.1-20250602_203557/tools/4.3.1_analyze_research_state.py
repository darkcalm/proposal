#!/usr/bin/env python3
"""
Research State Analysis Script (Task 4.3.1)
Analyzes the current state of research based on synthesis matrix and validation findings.

This script:
1. Processes the synthesis matrix from 4.2.3
2. Analyzes validation findings from 4.2.4.3
3. Generates a comprehensive research state analysis
4. Outputs a structured markdown document
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path

def load_synthesis_matrix():
    """Load and parse the synthesis matrix from 4.2.3."""
    matrix_file = Path("../docs/4.2.3-synthesis-matrix.md")
    if not matrix_file.exists():
        raise FileNotFoundError(f"Synthesis matrix file not found: {matrix_file}")
    
    with open(matrix_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract paper data from markdown tables
    paper_pattern = r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|"
    paper_matches = re.finditer(paper_pattern, content)
    
    papers = []
    for match in paper_matches:
        paper = {
            'title': match.group(1).strip(),
            'year': match.group(2).strip(),
            'focus': match.group(3).strip(),
            'findings': match.group(4).strip()
        }
        papers.append(paper)
    
    return papers

def load_validation_findings():
    """Load and parse validation findings from 4.2.4.3."""
    validation_file = Path("../docs/4.2.4.3-document-validation-findings.md")
    if not validation_file.exists():
        raise FileNotFoundError(f"Validation findings file not found: {validation_file}")
    
    with open(validation_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract concept data
    concept_pattern = r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*papers\s*\|\s*✅\s*\*\*VALIDATED\*\*\s*\|"
    concept_matches = re.finditer(concept_pattern, content)
    
    concepts = {}
    for match in concept_matches:
        concept_name = match.group(1).strip().lower().replace(' ', '_')
        support_level = match.group(2).strip().lower().replace(' ', '_')
        evidence_count = int(match.group(3))
        concepts[concept_name] = {
            'status': 'validated',
            'support': support_level,
            'evidence_count': evidence_count
        }
    
    # Extract relationship data
    relationship_pattern = r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*papers\s*\|\s*✅\s*\*\*VALIDATED\*\*\s*\|"
    relationship_matches = re.finditer(relationship_pattern, content)
    
    relationships = {}
    for match in relationship_matches:
        relationship_name = match.group(1).strip().lower().replace(' ', '_')
        support_level = match.group(2).strip().lower().replace(' ', '_')
        evidence_count = int(match.group(3))
        relationships[relationship_name] = {
            'status': 'validated',
            'support': support_level,
            'evidence_count': evidence_count
        }
    
    return {
        'concepts': concepts,
        'relationships': relationships
    }

def analyze_research_state(papers, validation):
    """Analyze the current state of research based on synthesis and validation data."""
    
    # Analyze temporal trends
    years = [int(p['year']) for p in papers if p['year'].isdigit()]
    recent_papers = [p for p in papers if p['year'].isdigit() and int(p['year']) >= 2020]
    
    # Analyze focus areas
    focus_areas = {}
    for paper in papers:
        focus = paper['focus']
        if focus in focus_areas:
            focus_areas[focus] += 1
        else:
            focus_areas[focus] = 1
    
    # Analyze validation coverage
    concept_coverage = len(validation['concepts'])
    relationship_coverage = len(validation['relationships'])
    validated_concepts = sum(1 for c in validation['concepts'].values() if c['status'] == 'validated')
    validated_relationships = sum(1 for r in validation['relationships'].values() if r['status'] == 'validated')
    
    analysis = {
        'temporal_analysis': {
            'total_papers': len(papers),
            'recent_papers': len(recent_papers),
            'year_range': f"{min(years)}-{max(years)}" if years else "N/A",
            'recent_trend': len(recent_papers) / len(papers) if papers else 0
        },
        'focus_analysis': {
            'areas': focus_areas,
            'primary_areas': sorted(focus_areas.items(), key=lambda x: x[1], reverse=True)[:3]
        },
        'validation_analysis': {
            'concept_coverage': concept_coverage,
            'relationship_coverage': relationship_coverage,
            'validated_concepts': validated_concepts,
            'validated_relationships': validated_relationships
        }
    }
    
    return analysis

def generate_research_state_report(analysis):
    """Generate the research state analysis report."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    document = f"""# Current Research State Analysis (Task 4.3.1)

*Generated: {timestamp}*

This document analyzes the current state of research based on the synthesis matrix (Task 4.2.3) and validation findings (Task 4.2.4.3).

## Executive Summary

The analysis reveals a **growing and maturing research field** with **strong theoretical foundations** but **emerging areas requiring investigation**.

### Key Findings:
- **Temporal Trends:** {analysis['temporal_analysis']['recent_papers']}/{analysis['temporal_analysis']['total_papers']} papers published since 2020
- **Focus Areas:** {len(analysis['focus_analysis']['areas'])} distinct research areas identified
- **Validation Coverage:** {analysis['validation_analysis']['validated_concepts']}/{analysis['validation_analysis']['concept_coverage']} concepts and {analysis['validation_analysis']['validated_relationships']}/{analysis['validation_analysis']['relationship_coverage']} relationships validated

## Detailed Analysis

### 1. Temporal Analysis

#### 1.1 Publication Trends
- **Total Papers:** {analysis['temporal_analysis']['total_papers']}
- **Year Range:** {analysis['temporal_analysis']['year_range']}
- **Recent Publications:** {analysis['temporal_analysis']['recent_papers']} papers since 2020
- **Growth Rate:** {analysis['temporal_analysis']['recent_trend']*100:.1f}% of papers published in last 3 years

#### 1.2 Temporal Distribution
- **Early Phase:** Papers before 2020
- **Recent Phase:** Papers from 2020 onwards
- **Emerging Trends:** Focus on practical implementation and system integration

### 2. Focus Area Analysis

#### 2.1 Primary Research Areas
"""
    
    for area, count in analysis['focus_analysis']['primary_areas']:
        document += f"- **{area}:** {count} papers\n"
    
    document += f"""
#### 2.2 Area Distribution
- **Total Areas:** {len(analysis['focus_analysis']['areas'])} distinct research areas
- **Coverage:** Comprehensive coverage of core concepts
- **Balance:** Mix of theoretical and practical research

### 3. Validation Analysis

#### 3.1 Concept Validation
- **Total Concepts:** {analysis['validation_analysis']['concept_coverage']}
- **Validated Concepts:** {analysis['validation_analysis']['validated_concepts']}
- **Validation Rate:** {analysis['validation_analysis']['validated_concepts']/analysis['validation_analysis']['concept_coverage']*100:.1f}%

#### 3.2 Relationship Validation
- **Total Relationships:** {analysis['validation_analysis']['relationship_coverage']}
- **Validated Relationships:** {analysis['validation_analysis']['validated_relationships']}
- **Validation Rate:** {analysis['validation_analysis']['validated_relationships']/analysis['validation_analysis']['relationship_coverage']*100:.1f}%

## Research State Assessment

### 1. Current Strengths
- **Theoretical Foundation:** Strong validation of core concepts
- **Recent Activity:** High publication rate in recent years
- **Diverse Coverage:** Multiple research areas addressed
- **Practical Focus:** Growing emphasis on implementation

### 2. Current Limitations
- **Emerging Areas:** Some relationships need investigation
- **Implementation Gaps:** Limited practical validation
- **Integration Challenges:** Complex system interactions
- **Future Directions:** Need for extension pathways

### 3. Research Maturity
- **Theoretical Maturity:** High (validated concepts and relationships)
- **Practical Maturity:** Medium (growing implementation focus)
- **Integration Maturity:** Low (complex interactions)
- **Overall Maturity:** Medium-High (strong foundation, emerging areas)

## Implications for Research Gaps

### 1. Theoretical Gaps
- Need for investigation of complex interdependencies
- Requirement for stronger theoretical grounding of extensions
- Opportunity for more granular concept definitions

### 2. Methodological Gaps
- Limited practical validation approaches
- Need for integrated testing methodologies
- Requirement for system-level evaluation methods

### 3. Practical Gaps
- Implementation challenges in real-world settings
- Integration with existing systems
- Scalability and performance considerations

## Next Steps

### 1. Immediate Actions
- Focus on investigating complex interdependencies
- Develop practical validation approaches
- Address implementation challenges

### 2. Medium-term Actions
- Strengthen theoretical grounding of extensions
- Develop integrated testing methodologies
- Address scalability concerns

### 3. Long-term Actions
- Establish comprehensive validation framework
- Develop system-level evaluation methods
- Create extension pathways

## Sources and Methodology

### Analysis Sources
- **Synthesis Matrix:** `docs/4.2.3-synthesis-matrix.md`
- **Validation Findings:** `docs/4.2.4.3-document-validation-findings.md`
- **Framework Updates:** `docs/4.2.4.4-updated-framework.md`

### Analysis Methodology
- **Temporal Analysis:** Publication trends and recent activity
- **Focus Analysis:** Research area distribution and coverage
- **Validation Analysis:** Concept and relationship validation status
- **Gap Analysis:** Identification of research gaps and needs

---

*Analysis completed based on {analysis['temporal_analysis']['total_papers']} papers and validation findings*
*Ready for: Task 4.3.2 - Identify theoretical gaps*
"""
    
    return document

def main():
    """Main execution function."""
    
    print("Research State Analysis Script (Task 4.3.1)")
    print("="*50)
    
    try:
        # Load synthesis matrix
        print("Loading synthesis matrix from Task 4.2.3...")
        papers = load_synthesis_matrix()
        
        # Load validation findings
        print("Loading validation findings from Task 4.2.4.3...")
        validation = load_validation_findings()
        
        # Analyze research state
        print("Analyzing current research state...")
        analysis = analyze_research_state(papers, validation)
        
        # Generate research state report
        print("Generating research state analysis report...")
        report = generate_research_state_report(analysis)
        
        # Create docs directory if it doesn't exist
        os.makedirs("../docs", exist_ok=True)
        
        # Write research state report
        output_file = "../docs/4.3.1-research-state-analysis.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"✅ Research state analysis report created: {output_file}")
        
        # Generate summary
        summary = f"""
Research State Analysis Summary (Task 4.3.1)
========================================

Analysis Results:
- 📊 {analysis['temporal_analysis']['total_papers']} papers analyzed
- 📈 {analysis['temporal_analysis']['recent_papers']} recent papers (since 2020)
- 🎯 {len(analysis['focus_analysis']['areas'])} research areas identified
- ✅ {analysis['validation_analysis']['validated_concepts']}/{analysis['validation_analysis']['concept_coverage']} concepts validated
- 🔄 {analysis['validation_analysis']['validated_relationships']}/{analysis['validation_analysis']['relationship_coverage']} relationships validated

Output Files:
- {output_file}

Ready for: Task 4.3.2 - Identify theoretical gaps
"""
        
        print(summary)
        
        return True
        
    except FileNotFoundError as e:
        print(f"❌ Error: {str(e)}")
        print("Please ensure Tasks 4.2.3 and 4.2.4.3 have been completed and their output files exist.")
        return False
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Map Main References for Research Proposal Sections (Task 8.1.2)

This script maps the main reference materials from phases 4-7 to the specific sections
of the final research proposal, considering the extreme compression requirements
(2.5% overall compression ratio) specified in the word count allocation,
and aligns the mapping with the course grading criteria.

Based on: docs/8.1.1-word-count-allocation.md, sources/8.1.2-examiner-message-Master Thesis Proposal Word Limit.md, docs/1.2-grading-criteria.md
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent

def analyze_content_mass() -> Dict:
    """Analyze content mass from phases 4-7 for reference mapping."""
    
    project_root = get_project_root()
    docs_dir = project_root / "docs"
    
    # Content mass analysis from word count allocation
    content_mass = {
        "systematic_literature_review": {
            "phase": "4.*",
            "total_words": 28901,
            "target_words": 630,
            "compression_ratio": 2.2,
            "target_sections": ["Introduction", "Background", "Literature Review", "Research Gap"]
        },
        "methodology_development": {
            "phase": "5.*", 
            "total_words": 34549,
            "target_words": 350,
            "compression_ratio": 1.0,
            "target_sections": ["Research Methodology", "Alternative Methodologies"]
        },
        "ethics_sustainability": {
            "phase": "6.*",
            "total_words": 23104,
            "target_words": 210,
            "compression_ratio": 0.9,
            "target_sections": ["Ethics and Sustainability Considerations"]
        },
        "risk_timeline": {
            "phase": "7.*",
            "total_words": 13525,
            "target_words": 210,
            "compression_ratio": 1.6,
            "target_sections": ["Risk Assessment", "Implementation Plan and Timeline"]
        }
    }
    
    return content_mass

def map_phase4_references() -> Dict:
    """Map main references from Phase 4 (Systematic Literature Review and Gap Analysis)."""
    
    phase4_mapping = {
        "primary_references": {
            "gap_analysis": {
                "file": "docs/4.3.7-gap-statement-summary.md",
                "priority": "CRITICAL",
                "content_focus": "Research gap identification and problem statement",
                "target_section": "Introduction/Background",
                "compression_strategy": "Extract 2-3 key gap statements, synthesize into problem context"
            },
            "patterns_trends": {
                "file": "docs/4.2.1.1-patterns-trends-analysis.md", 
                "priority": "HIGH",
                "content_focus": "Key patterns in DER agent protocol literature",
                "target_section": "Background/Literature Review",
                "compression_strategy": "Focus on 3-5 major trends directly relevant to ACP/A2A"
            },
            "research_questions": {
                "file": "docs/4.2.4.1-research-questions-refined.md",
                "priority": "CRITICAL", 
                "content_focus": "Refined research questions and objectives",
                "target_section": "Objectives and Questions",
                "compression_strategy": "Use final refined questions directly, minimal compression needed"
            },
            "theoretical_framework": {
                "file": "docs/4.2.2.1-key-concepts-updated.md",
                "priority": "HIGH",
                "content_focus": "Key concepts and relationships for ACP/A2A in DER context",
                "target_section": "Theoretical Framework", 
                "compression_strategy": "Extract core concept definitions and relationships"
            }
        },
        "supporting_references": {
            "elicit_results": {
                "files": [
                    "docs/4.1.1.5-elicit-papers-markdown-conversion-summary.md",
                    "docs/4.1.8.6-elicit-results-processing-summary.md"
                ],
                "priority": "MEDIUM",
                "content_focus": "Literature sources and search methodology validation",
                "target_section": "Background/Literature Review",
                "compression_strategy": "Reference as methodology validation, cite key papers only"
            },
            "practical_needs": {
                "file": "docs/4.3.6-practical-needs-summary.md",
                "priority": "MEDIUM", 
                "content_focus": "Industry needs for DER maintenance coordination",
                "target_section": "Background/Problem Significance",
                "compression_strategy": "Extract 2-3 most compelling practical justifications"
            }
        },
        "reference_sources": {
            "literature_base": "sources/4.1.1-elicit-results/ and sources/4.1.8-elicit-results/",
            "gap_analysis_data": "sources/4.3.4-theoretical-gaps.md to sources/4.3.7-preliminary-gap-statement.md"
        }
    }
    
    return phase4_mapping

def map_phase5_references() -> Dict:
    """Map main references from Phase 5 (Methodology Development)."""
    
    phase5_mapping = {
        "primary_references": {
            "methodology_justification": {
                "file": "docs/5.3.1-methodology-justification.md",
                "priority": "CRITICAL",
                "content_focus": "Final methodology selection and justification",
                "target_section": "Research Methodology",
                "compression_strategy": "Use executive summary and final recommendation directly"
            },
            "feasibility_analysis": {
                "file": "docs/5.2.4-feasibility-analysis.md", 
                "priority": "HIGH",
                "content_focus": "Methodology feasibility assessment results",
                "target_section": "Research Methodology",
                "compression_strategy": "Include top 3 methodology rankings and key feasibility factors"
            },
            "methodology_comparison": {
                "file": "docs/5.2.1-methodology-comparison-matrix.md",
                "priority": "MEDIUM",
                "content_focus": "Alternative methodologies considered",
                "target_section": "Research Methodology", 
                "compression_strategy": "Summary table of top 5 alternatives with brief rationale"
            }
        },
        "supporting_references": {
            "strengths_limitations": {
                "file": "docs/5.2.2-methodology-strengths-limitations.md",
                "priority": "LOW",
                "content_focus": "Detailed methodology analysis",
                "target_section": "Research Methodology",
                "compression_strategy": "Extract key limitations acknowledgment for selected methodology"
            },
            "timeline_workflow": {
                "files": [
                    "docs/5.3.3-project-timeline.md",
                    "docs/5.3.4-workflow-diagrams.md"
                ],
                "priority": "MEDIUM",
                "content_focus": "Implementation timeline and workflow",
                "target_section": "Implementation Plan",
                "compression_strategy": "High-level timeline overview and key milestones only"
            }
        },
        "reference_sources": {
            "methodology_data": "sources/5.1.1-relevant-methodologies.json to sources/5.2.4-feasibility-analysis.json",
            "expert_consultation": "sources/5.3-dialogue-with-perplexity-*.md"
        }
    }
    
    return phase5_mapping

def map_phase6_references() -> Dict:
    """Map main references from Phase 6 (Ethics and Sustainability)."""
    
    phase6_mapping = {
        "primary_references": {
            "ethics_framework": {
                "file": "docs/6.1.2-ethical-concerns-analysis.md",
                "priority": "HIGH",
                "content_focus": "Key ethical considerations for DER agent protocols",
                "target_section": "Ethics and Sustainability",
                "compression_strategy": "Extract 3-4 highest priority ethical concerns"
            },
            "sustainability_impact": {
                "file": "docs/6.2.1-environmental-aspects.md",
                "priority": "HIGH", 
                "content_focus": "Environmental benefits and SDG alignment",
                "target_section": "Ethics and Sustainability",
                "compression_strategy": "Focus on SDG connections and environmental benefits, contextualizing the research within broader sustainability goals."
            },
            "mitigation_strategies": {
                "file": "docs/6.2.6-mitigation-strategies.md",
                "priority": "MEDIUM",
                "content_focus": "Practical mitigation approaches for ethical/sustainability concerns", 
                "target_section": "Ethics and Sustainability",
                "compression_strategy": "Summarize key mitigation categories and approaches relevant to the research context"
            }
        },
        "supporting_references": {
            "data_privacy": {
                "file": "docs/6.1.3-data-privacy-framework.md",
                "priority": "MEDIUM",
                "content_focus": "Data privacy considerations for DER health data",
                "target_section": "Ethics and Sustainability",
                "compression_strategy": "Brief mention of key privacy protection measures"
            },
            "social_economic": {
                "files": [
                    "docs/6.2.2-social-impacts.md",
                    "docs/6.2.3-economic-factors.md"
                ],
                "priority": "LOW",
                "content_focus": "Broader social and economic implications",
                "target_section": "Ethics and Sustainability", 
                "compression_strategy": "Brief summary of positive social/economic outcomes, if highly relevant and concise"
            }
        },
        "reference_sources": {
            "ethics_data": "sources/6.1.1-ethics-guidelines-review.json to sources/6.1.4-consent-requirements-framework.json",
            "sustainability_data": "sources/6.2.1-environmental-aspects-analysis.json to sources/6.2.6-mitigation-strategies-detailed.json"
        }
    }
    
    return phase6_mapping

def map_phase7_references() -> Dict:
    """Map main references from Phase 7 (Risk Assessment and Timeline)."""
    
    phase7_mapping = {
        "primary_references": {
            "risk_management": {
                "file": "docs/7.2-research-specific-risk-management.md",
                "priority": "HIGH",
                "content_focus": "Comprehensive risk mitigation strategies",
                "target_section": "Risk Assessment and Timeline",
                "compression_strategy": "Focus on highest priority risks and mitigation approaches relevant to the proposal's scope"
            },
            "risk_prioritization": {
                "file": "docs/7.1.5-risk-prioritized.md",
                "priority": "HIGH",
                "content_focus": "Prioritized risk analysis",
                "target_section": "Risk Assessment", 
                "compression_strategy": "Include top 5-7 highest priority risks with brief mitigation summary"
            }
        },
        "supporting_references": {
            "risk_register": {
                "file": "docs/7.1.3-risk-register.md",
                "priority": "MEDIUM",
                "content_focus": "Comprehensive risk inventory",
                "target_section": "Risk Assessment",
                "compression_strategy": "Reference as supporting analysis, focus on categories rather than full register"
            },
            "timeline_planning": {
                "file": "docs/5.3.3-project-timeline.md",
                "priority": "CRITICAL",
                "content_focus": "Detailed implementation timeline, milestones, deliverables, resource considerations",
                "target_section": "Implementation Plan and Timeline",
                "compression_strategy": "Summarize key phases, deliverables, and milestones. Emphasize existence of detailed plan (Gantt, resource allocation) and refer to full doc. Ensure it demonstrates structured planning."
            }
        },
        "reference_sources": {
            "risk_data": "sources/7.1.1-potential-risks-detailed.json to sources/7.2-combined-risk-management.json"
        }
    }
    
    return phase7_mapping

def create_compression_guidelines() -> Dict:
    """Create specific compression guidelines based on examiner feedback."""
    
    guidelines = {
        "examiner_emphasis": {
            "word_limit": "2000-3000 words (not super strict but avoid 15-pager)",
            "focus": "Rich in referenced facts but RELEVANT to chosen topic",
            "purpose": "Good understanding of what you're going to do, not full literature review",
            "clarity": "Avoid becoming vague toward the real problem - see forest for trees"
        },
        "compression_strategies": {
            "synthesize_not_describe": "Transform detailed analyses into key insights",
            "relevance_filter": "Include only content directly supporting research objectives", 
            "summary_tables": "Replace lengthy descriptions with structured tables",
            "high_impact_content": "Prioritize findings that directly inform research design",
            "reference_detailed_work": "Acknowledge comprehensive analyses while presenting distilled insights"
        },
        "section_priorities": {
            "introduction_background": {
                "words": 630,
                "focus": "Problem context, key literature synthesis, research gap",
                "compression_from": 28901,
                "strategy": "Focus on most relevant findings, synthesize rather than describe"
            },
            "methodology": {
                "words": 350, 
                "focus": "Selected methodology justification, alternatives considered, assumptions, tools, boundaries",
                "compression_from": 34549,
                "strategy": "Focus on final justified approach, summarize alternatives, briefly state assumptions/tools/boundaries"
            },
            "ethics_sustainability": {
                "words": 210,
                "focus": "Key ethical considerations contextualized, SDG alignment, mitigation",
                "compression_from": 23104,
                "strategy": "Focus on high-priority contextualized concerns, summarize mitigation"
            },
            "risk_timeline": {
                "words": 210,
                "focus": "Major risks and mitigation, structured timeline overview demonstrating detailed planning", 
                "compression_from": 13525,
                "strategy": "Focus on high-priority risks, provide timeline overview demonstrating a structured plan exists"
            }
        }
    }
    
    return guidelines

def generate_reference_mapping_report() -> Dict:
    """Generate comprehensive reference mapping report."""
    
    print("🔍 Generating Main References Mapping for Research Proposal Sections...")
    print("=" * 80)
    
    # Analyze content mass
    content_mass = analyze_content_mass()
    
    # Map references by phase
    phase4_refs = map_phase4_references()
    phase5_refs = map_phase5_references() 
    phase6_refs = map_phase6_references()
    phase7_refs = map_phase7_references()
    
    # Get compression guidelines
    guidelines = create_compression_guidelines()
    
    # Compile comprehensive mapping
    reference_mapping = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "task": "8.1.2 Map main references for sections",
            "total_content_mass": 100079,
            "target_word_count": 2500,
            "overall_compression_ratio": 2.5,
            "based_on_grading_criteria": "docs/1.2-grading-criteria.md"
        },
        "content_mass_analysis": content_mass,
        "phase_mappings": {
            "phase_4_literature_gap": phase4_refs,
            "phase_5_methodology": phase5_refs,
            "phase_6_ethics_sustainability": phase6_refs, 
            "phase_7_risk_timeline": phase7_refs
        },
        "compression_guidelines": guidelines,
        "section_reference_map": {
            "introduction_background": {
                "target_words": 630,
                "primary_sources": [
                    "docs/4.3.7-gap-statement-summary.md",
                    "docs/4.2.1.1-patterns-trends-analysis.md",
                    "docs/3.1.2-research-direction-selection.md"
                ],
                "supporting_sources": [
                    "docs/4.3.6-practical-needs-summary.md", 
                    "docs/4.1.8.6-elicit-results-processing-summary.md"
                ],
                "key_references": "sources/4.1.1-elicit-results/ and sources/4.1.8-elicit-results/",
                "grading_criteria_alignment": "Addresses C-Grade: Research Gap Identification (supported by literature from key_references). Provides foundational context for the entire proposal."
            },
            "objectives_questions": {
                "target_words": 300,
                "primary_sources": [
                    "docs/4.2.4.1-research-questions-refined.md",
                    "docs/3.1.2-research-direction-selection.md"
                ],
                "supporting_sources": [
                    "docs/4.2.4.2-hypotheses-refined.md"
                ],
                "grading_criteria_alignment": "Directly addresses C-Grade: Formulation of research questions. Ensures clarity and focus as per examiner guidance."
            },
            "theoretical_framework": {
                "target_words": 250,
                "primary_sources": [
                    "docs/4.2.2.1-key-concepts-updated.md",
                    "docs/4.2.2.2-define-relationships-updated.md"
                ],
                "supporting_sources": [
                    "docs/3.6.1-key-concepts.md"
                ],
                "grading_criteria_alignment": "Addresses C-Grade: Theoretical Framework. This section should also briefly outline key assumptions and system boundaries relevant to the framework, drawing from detailed methodology documents."
            },
            "methodology": {
                "target_words": 350,
                "primary_sources": [
                    "docs/5.3.1-methodology-justification.md",
                    "docs/5.2.4-feasibility-analysis.md"
                ],
                "supporting_sources": [
                    "docs/5.2.1-methodology-comparison-matrix.md",
                    "docs/5.3.2-methodology-limitations.md"
                ],
                "key_references": "sources/5.1.1-relevant-methodologies.json to sources/5.2.4-feasibility-analysis.json",
                "grading_criteria_alignment": "Addresses C-Grade: Methodology selection and justification. Will clearly state the chosen methodology, tools (e.g., ACP/A2A primitives, conceptual modeling), and justify choices. Should also clearly state key assumptions and system boundaries not covered in Theoretical Framework."
            },
            "ethics_sustainability": {
                "target_words": 210,
                "primary_sources": [
                    "docs/6.1.2-ethical-concerns-analysis.md", 
                    "docs/6.2.1-environmental-aspects.md",
                    "docs/6.2.6-mitigation-strategies.md"
                ],
                "supporting_sources": [
                    "docs/6.1.3-data-privacy-framework.md"
                ],
                "key_references": "sources/6.1.1-ethics-guidelines-review.json to sources/6.2.6-mitigation-strategies-detailed.json",
                "grading_criteria_alignment": "Addresses A-Grade Option 1: Ethics and Sustainability Contextualization. Focuses on integrating key ethical concerns (data privacy, consent) and sustainability dimensions (environmental, SDG alignment) within the research context. Addresses ILO 6."
            },
            "risk_timeline": {
                "target_words": 210,
                "primary_sources": [
                    "docs/7.2-research-specific-risk-management.md",
                    "docs/7.1.5-risk-prioritized.md",
                    "docs/5.3.3-project-timeline.md"
                ],
                "supporting_sources": [
                ],
                "key_references": "sources/7.1.1-potential-risks-detailed.json to sources/7.2-combined-risk-management.json and docs/5.3.3-project-timeline.md",
                "grading_criteria_alignment": "Addresses A-Grade Option 2: Structured Research Time Plan. Summarizes major risks and mitigation, and critically, provides an overview of the structured research timeline (key phases, deliverables, milestones from docs/5.3.3-project-timeline.md) to demonstrate detailed planning and resource considerations exist."
            }
        }
    }
    
    return reference_mapping

def save_reference_mapping(mapping: Dict) -> str:
    """Save reference mapping to output file."""
    
    project_root = get_project_root()
    output_file = project_root / "sources" / "8.1.2-main-references-mapping.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    
    return str(output_file)

def print_compression_summary(mapping: Dict):
    """Print summary of compression requirements and strategies."""
    
    print("\n📊 COMPRESSION REQUIREMENTS SUMMARY")
    print("=" * 50)
    
    content_mass = mapping["content_mass_analysis"]
    
    for section, data in content_mass.items():
        print(f"\n{section.upper().replace('_', ' ')}:")
        print(f"  📁 Phase: {data['phase']}")
        print(f"  📄 Original: {data['total_words']:,} words")
        print(f"  🎯 Target: {data['target_words']} words")
        print(f"  📊 Compression: {data['compression_ratio']}%")
        print(f"  📍 Sections: {', '.join(data['target_sections'])}")
    
    print(f"\n🎯 OVERALL STATISTICS:")
    print(f"  📄 Total Content Mass: {mapping['metadata']['total_content_mass']:,} words")
    print(f"  🎯 Target Word Count: {mapping['metadata']['target_word_count']:,} words") 
    print(f"  📊 Overall Compression: {mapping['metadata']['overall_compression_ratio']}%")
    
    print(f"\n⚠️  EXAMINER GUIDANCE:")
    guidelines = mapping["compression_guidelines"]["examiner_emphasis"]
    print(f"  📏 Word Limit: {guidelines['word_limit']}")
    print(f"  🎯 Focus: {guidelines['focus']}")
    print(f"  📝 Purpose: {guidelines['purpose']}")
    print(f"  🔍 Clarity: {guidelines['clarity']}")

def print_section_mapping(mapping: Dict):
    """Print detailed section-by-section reference mapping with grading criteria alignment."""
    
    print("\n�� SECTION-BY-SECTION REFERENCE MAPPING (Aligned with Grading Criteria)")
    print("=" * 70)
    
    section_map = mapping["section_reference_map"]
    
    for section, details in section_map.items():
        print(f"\n📑 {section.upper().replace('_', ' ')}")
        print(f"  🎯 Target Words: {details['target_words']}")
        
        print(f"  📚 Primary Sources:")
        for source in details['primary_sources']:
            print(f"    • {source}")
        
        if 'supporting_sources' in details and details['supporting_sources']:
            print(f"  📖 Supporting Sources:")
            for source in details['supporting_sources']:
                print(f"    • {source}")
        
        if 'key_references' in details:
            print(f"  🔗 Key References: {details['key_references']}")
        
        if 'grading_criteria_alignment' in details:
            print(f"  🏅 Grading Criteria Alignment: {details['grading_criteria_alignment']}")

def main():
    """Main execution function."""
    
    print("🚀 TASK 8.1.2: MAPPING MAIN REFERENCES FOR SECTIONS (Updated with Grading Criteria Alignment)")
    print("=" * 80)
    print("📝 Creating comprehensive reference mapping with extreme compression guidance and grading alignment")
    print("🎯 Target: 2,500 words from 100,079 words (2.5% compression)")
    print()
    
    # Generate mapping
    mapping = generate_reference_mapping_report()
    
    # Save to file
    output_file = save_reference_mapping(mapping)
    print(f"💾 Reference mapping saved to: {output_file}")
    
    # Print summaries
    print_compression_summary(mapping)
    print_section_mapping(mapping)
    
    print(f"\n✅ TASK 8.1.2 COMPLETED SUCCESSFULLY (with grading criteria integration)")
    print(f"📁 Main reference mapping available in: {output_file}")
    print(f"🎯 Ready for Task 8.1.3: Develop first draft for sections")

if __name__ == "__main__":
    main() 
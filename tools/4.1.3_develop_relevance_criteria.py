#!/usr/bin/env python3

import json
import os
from pathlib import Path
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(str(WORKSPACE_ROOT / "tools" / "relevance_filtering.log")),
        logging.StreamHandler()
    ])

# Determine workspace root assuming script is in tools/
WORKSPACE_ROOT = Path(__file__).resolve().parent.parent

def define_relevance_criteria():
    """
    Define relevance criteria based on the theoretical framework and research direction.
    
    Based on:
    - docs/3.1.2-research-direction-selection.md (primary research focus)
    - docs/3.6.1-key-concepts.md (theoretical framework concepts)
    - docs/3.6.2-define-relationships.md (concept relationships)
    - docs/3.5.1-define-boundaries.md (research boundaries)
    """
    
    criteria = {
        "metadata": {
            "task": "4.1.3",
            "created_date": datetime.now().isoformat(),
            "source_documents": [
                "docs/3.1.2-research-direction-selection.md",
                "docs/3.6.1-key-concepts.md", 
                "docs/3.6.2-define-relationships.md",
                "docs/3.5.1-define-boundaries.md",
                "docs/3.2.3-define-scope.md"
            ],
            "description": "Relevance criteria for evaluating literature against theoretical framework and research direction"
        },
        
        "primary_research_focus": {
            "title": "Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) for Decentralized DER Predictive Maintenance Coordination",
            "core_question": "How can ACP and A2A be applied to enable secure, scalable, and interoperable communication for decentralized predictive maintenance coordination among diverse, multi-owner DERs?",
            "subfocus": "Designing conceptual framework and specifying core messaging patterns for decentralized DER health data exchange and predictive maintenance task initiation"
        },
        
        "relevance_dimensions": {
            "1_core_concepts": {
                "weight": 0.25,
                "description": "Coverage of theoretical framework core concepts",
                "subcriteria": {
                    "der_systems": {
                        "weight": 0.20,
                        "keywords": ["distributed energy resources", "DER", "decentralized energy", "renewable energy systems", "energy storage", "microgrids", "grid-connected"],
                        "description": "Papers addressing DER systems, characteristics, or applications"
                    },
                    "predictive_maintenance": {
                        "weight": 0.25, 
                        "keywords": ["predictive maintenance", "condition monitoring", "health monitoring", "fault prediction", "maintenance scheduling", "asset management", "preventive maintenance"],
                        "description": "Papers addressing predictive maintenance approaches, especially in energy systems"
                    },
                    "agent_protocols": {
                        "weight": 0.25,
                        "keywords": ["agent communication protocol", "ACP", "A2A", "agent-to-agent", "multi-agent systems", "agent coordination", "FIPA", "message passing"],
                        "description": "Papers addressing agent communication protocols, standards, or implementations"
                    },
                    "decentralized_coordination": {
                        "weight": 0.20,
                        "keywords": ["decentralized coordination", "distributed coordination", "multi-agent coordination", "peer-to-peer", "distributed systems", "collaborative systems"],
                        "description": "Papers addressing decentralized or distributed coordination mechanisms"
                    },
                    "communication_frameworks": {
                        "weight": 0.10,
                        "keywords": ["communication protocols", "messaging frameworks", "interoperability", "system integration", "data exchange"],
                        "description": "Papers addressing communication frameworks and protocols"
                    }
                }
            },
            
            "2_application_domain": {
                "weight": 0.20,
                "description": "Relevance to energy systems and maintenance domains",
                "subcriteria": {
                    "energy_systems": {
                        "weight": 0.40,
                        "keywords": ["energy systems", "power systems", "electrical grid", "smart grid", "energy infrastructure", "utility systems"],
                        "description": "Papers focused on energy systems applications"
                    },
                    "industrial_automation": {
                        "weight": 0.30,
                        "keywords": ["industrial automation", "process control", "SCADA", "industrial IoT", "cyber-physical systems", "automation systems"],
                        "description": "Papers addressing industrial automation relevant to energy systems"
                    },
                    "maintenance_operations": {
                        "weight": 0.30,
                        "keywords": ["maintenance operations", "asset management", "reliability engineering", "maintenance planning", "service coordination"],
                        "description": "Papers addressing maintenance operations and coordination"
                    }
                }
            },
            
            "3_technical_requirements": {
                "weight": 0.20,
                "description": "Coverage of key technical requirements from research scope",
                "subcriteria": {
                    "security": {
                        "weight": 0.30,
                        "keywords": ["security", "cybersecurity", "authentication", "authorization", "encryption", "privacy", "secure communication"],
                        "description": "Papers addressing security aspects of communication or systems"
                    },
                    "scalability": {
                        "weight": 0.30,
                        "keywords": ["scalability", "scalable systems", "performance", "throughput", "latency", "resource utilization"],
                        "description": "Papers addressing scalability or performance characteristics"
                    },
                    "interoperability": {
                        "weight": 0.25,
                        "keywords": ["interoperability", "standardization", "compatibility", "integration", "heterogeneous systems"],
                        "description": "Papers addressing interoperability or standardization"
                    },
                    "real_time": {
                        "weight": 0.15,
                        "keywords": ["real-time", "real time", "time-sensitive", "low latency", "response time", "time-critical"],
                        "description": "Papers addressing real-time or time-sensitive requirements"
                    }
                }
            },
            
            "4_methodology_alignment": {
                "weight": 0.15,
                "description": "Alignment with research methodology and evaluation approaches",
                "subcriteria": {
                    "framework_design": {
                        "weight": 0.30,
                        "keywords": ["framework design", "conceptual framework", "system architecture", "design methodology", "modeling"],
                        "description": "Papers presenting framework design or architectural approaches"
                    },
                    "protocol_evaluation": {
                        "weight": 0.30,
                        "keywords": ["protocol evaluation", "performance evaluation", "benchmarking", "metrics", "assessment methodology"],
                        "description": "Papers addressing protocol or system evaluation methodologies"
                    },
                    "case_studies": {
                        "weight": 0.25,
                        "keywords": ["case study", "implementation", "deployment", "validation", "experimental evaluation"],
                        "description": "Papers presenting case studies or implementations"
                    },
                    "literature_reviews": {
                        "weight": 0.15,
                        "keywords": ["survey", "review", "state of the art", "systematic review", "literature review"],
                        "description": "Comprehensive review papers providing domain overview"
                    }
                }
            },
            
            "5_innovation_potential": {
                "weight": 0.10,
                "description": "Papers presenting novel approaches or identifying research gaps",
                "subcriteria": {
                    "novel_approaches": {
                        "weight": 0.40,
                        "keywords": ["novel", "innovative", "new approach", "original", "breakthrough"],
                        "description": "Papers presenting novel or innovative approaches"
                    },
                    "research_gaps": {
                        "weight": 0.35,
                        "keywords": ["research gap", "future work", "limitations", "challenges", "open issues"],
                        "description": "Papers identifying research gaps or future directions"
                    },
                    "emerging_technologies": {
                        "weight": 0.25,
                        "keywords": ["emerging", "next generation", "future", "trends", "evolution"],
                        "description": "Papers addressing emerging technologies or future trends"
                    }
                }
            },
            
            "6_recency_and_quality": {
                "weight": 0.10,
                "description": "Publication recency and quality indicators",
                "subcriteria": {
                    "publication_year": {
                        "weight": 0.40,
                        "description": "Recent publications (2018-2024) weighted higher",
                        "scoring": {
                            "2023-2024": 1.0,
                            "2021-2022": 0.8,
                            "2019-2020": 0.6,
                            "2018": 0.4,
                            "2015-2017": 0.2,
                            "before_2015": 0.1
                        }
                    },
                    "venue_quality": {
                        "weight": 0.30,
                        "description": "Publication venue quality indicators",
                        "indicators": ["journal impact factor", "conference ranking", "citation count"]
                    },
                    "citation_count": {
                        "weight": 0.30,
                        "description": "Citation count as quality indicator",
                        "thresholds": {
                            "high": ">100 citations",
                            "medium": "20-100 citations", 
                            "low": "<20 citations"
                        }
                    }
                }
            }
        },
        
        "exclusion_criteria": {
            "out_of_scope": [
                "Papers focused solely on general AI without agent protocols",
                "Papers on energy systems without communication/coordination aspects",
                "Papers on maintenance without predictive or automated aspects",
                "Papers on protocols without agent-based or energy domain applications",
                "Papers focused on hardware design without communication protocols",
                "Papers on pure economic/policy analysis without technical content",
                "Papers on human factors without technical system integration",
                "Papers on theoretical computer science without practical applications"
            ],
            "methodology_mismatch": [
                "Papers requiring extensive empirical data collection",
                "Papers focused on mathematical proofs without applications",
                "Papers requiring multi-year longitudinal studies",
                "Papers requiring extensive human subject research"
            ]
        },
        
        "inclusion_thresholds": {
            "minimum_score": 0.3,
            "description": "Papers must achieve minimum 0.3 weighted score across all dimensions",
            "core_concept_requirement": 0.2,
            "description_core": "Papers must score at least 0.2 in core concepts dimension"
        },
        
        "scoring_methodology": {
            "keyword_matching": {
                "method": "Text analysis of title, abstract, and keywords",
                "scoring": {
                    "title_match": "2x weight",
                    "abstract_match": "1x weight", 
                    "keyword_match": "0.5x weight"
                }
            },
            "manual_assessment": {
                "method": "Expert review for borderline cases",
                "criteria": "Relevance to research questions and framework validation needs"
            },
            "final_score": "Weighted sum across all dimensions, normalized to 0-1 scale"
        }
    }
    
    return criteria

def save_criteria_to_file(criteria, output_path):
    """Save relevance criteria to JSON file with formatting."""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(criteria, f, indent=2, ensure_ascii=False)
    
    logging.info(f"Relevance criteria saved to: {output_path}")

def create_summary_document(criteria, output_path):
    """Create a comprehensive markdown summary of the relevance criteria."""
    
    content = f"""# Task 4.1.3: Relevance Criteria for Literature Evaluation

**Creation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Task:** 4.1.3 Develop Relevance Criteria  
**Source Documents:** {', '.join([f'`{doc}`' for doc in criteria['metadata']['source_documents']])}  
**JSON Criteria File:** `sources/4.1.3-relevance-criteria/relevance_criteria.json`

## Overview

This document defines comprehensive relevance criteria for evaluating literature against the theoretical framework and research direction established in previous tasks. The criteria enable systematic assessment of papers from both Elicit.com and Semantic Scholar searches.

### Primary Research Focus

**Main Question:** {criteria['primary_research_focus']['core_question']}

**Specific Subfocus:** {criteria['primary_research_focus']['subfocus']}

## Relevance Dimensions

The evaluation framework consists of six main dimensions with weighted subcriteria:

"""

    # Add each dimension
    for dim_key, dimension in criteria['relevance_dimensions'].items():
        dim_name = dim_key.split('_', 1)[1].replace('_', ' ').title()
        content += f"### {dim_name} (Weight: {dimension['weight']})\n\n"
        content += f"{dimension['description']}\n\n"
        
        if 'subcriteria' in dimension:
            content += "**Subcriteria:**\n\n"
            for sub_key, subcrit in dimension['subcriteria'].items():
                sub_name = sub_key.replace('_', ' ').title()
                weight = subcrit.get('weight', 'N/A')
                content += f"- **{sub_name}** (Weight: {weight}): {subcrit['description']}\n"
                
                if 'keywords' in subcrit:
                    keywords = ', '.join([f'"{kw}"' for kw in subcrit['keywords'][:5]])  # Show first 5
                    if len(subcrit['keywords']) > 5:
                        keywords += f", ... ({len(subcrit['keywords'])} total)"
                    content += f"  - Keywords: {keywords}\n"
                
                content += "\n"
        
        content += "\n"

    # Add exclusion criteria
    content += "## Exclusion Criteria\n\n"
    content += "### Out of Scope\n\n"
    for item in criteria['exclusion_criteria']['out_of_scope']:
        content += f"- {item}\n"
    
    content += "\n### Methodology Mismatch\n\n"
    for item in criteria['exclusion_criteria']['methodology_mismatch']:
        content += f"- {item}\n"

    # Add scoring methodology
    content += f"""

## Scoring Methodology

### Inclusion Thresholds
- **Minimum Score:** {criteria['inclusion_thresholds']['minimum_score']} - {criteria['inclusion_thresholds']['description']}
- **Core Concept Requirement:** {criteria['inclusion_thresholds']['core_concept_requirement']} - {criteria['inclusion_thresholds']['description_core']}

### Keyword Matching
- **Title Match:** {criteria['scoring_methodology']['keyword_matching']['scoring']['title_match']}
- **Abstract Match:** {criteria['scoring_methodology']['keyword_matching']['scoring']['abstract_match']}
- **Keyword Match:** {criteria['scoring_methodology']['keyword_matching']['scoring']['keyword_match']}

### Manual Assessment
{criteria['scoring_methodology']['manual_assessment']['criteria']}

## Application Strategy

### Phase 1: Automated Screening
1. Apply keyword matching across all dimensions
2. Calculate weighted scores for each paper
3. Filter papers meeting minimum thresholds
4. Rank papers by total relevance score

### Phase 2: Manual Review
1. Review borderline cases (scores 0.25-0.35)
2. Validate high-scoring papers for quality
3. Apply exclusion criteria
4. Final relevance classification

### Phase 3: Documentation
1. Document evaluation results
2. Categorize papers by relevance level
3. Identify gaps in literature coverage
4. Prepare recommendations for additional searches

## Validation Requirements

These criteria support the literature validation needs identified in the theoretical framework:

1. **Concept Validation:** Verify alignment with established practices in DER maintenance and agent protocols
2. **Relationship Validation:** Confirm theoretical framework relationships through literature evidence
3. **Gap Identification:** Identify areas where literature support is limited
4. **Framework Refinement:** Guide updates to theoretical framework based on literature findings

## Next Steps

1. **Task 4.1.4:** Test these criteria against sample papers
2. **Task 4.1.5:** Implement Semantic Scholar API papers storage with relevance scoring
3. **Task 4.2.1:** Apply criteria to review all papers from Elicit.com and Semantic Scholar
4. **Task 4.2.2:** Use results for theoretical framework validation

## Files Created

- `sources/4.1.3-relevance-criteria/relevance_criteria.json` - Detailed criteria specification
- `docs/4.1.3-relevance-criteria-summary.md` - This summary document
- `tools/4.1.3_develop_relevance_criteria.py` - Script used to generate criteria

The relevance criteria provide a systematic, weighted approach to literature evaluation that aligns with the research direction and theoretical framework while supporting the validation needs of subsequent tasks.
"""

    # Write summary to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    logging.info(f"Summary document saved to: {output_path}")

def main():
    """Main function to develop and save relevance criteria."""
    
    # Create output directories
    criteria_dir = WORKSPACE_ROOT / "sources" / "4.1.3-relevance-criteria"
    criteria_dir.mkdir(parents=True, exist_ok=True)
    
    docs_dir = WORKSPACE_ROOT / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate relevance criteria
    logging.info("Developing relevance criteria based on theoretical framework and research direction...")
    criteria = define_relevance_criteria()
    
    # Save criteria to JSON
    criteria_path = criteria_dir / "relevance_criteria.json"
    save_criteria_to_file(criteria, criteria_path)
    
    # Create summary document
    summary_path = docs_dir / "4.1.3-relevance-criteria-summary.md"
    create_summary_document(criteria, summary_path)
    
    # Log summary statistics
    total_subcriteria = sum(
        len(dim.get('subcriteria', {})) 
        for dim in criteria['relevance_dimensions'].values()
    )
    
    total_keywords = sum(
        len(subcrit.get('keywords', [])) 
        for dim in criteria['relevance_dimensions'].values()
        for subcrit in dim.get('subcriteria', {}).values()
    )
    
    logging.info(f"""
Relevance criteria development completed:
- 6 main dimensions defined
- {total_subcriteria} subcriteria specified  
- {total_keywords} evaluation keywords identified
- {len(criteria['exclusion_criteria']['out_of_scope'])} out-of-scope exclusions defined
- {len(criteria['exclusion_criteria']['methodology_mismatch'])} methodology mismatch exclusions defined

Files created:
- {criteria_path.relative_to(WORKSPACE_ROOT)}
- {summary_path.relative_to(WORKSPACE_ROOT)}

Ready for Task 4.1.4: Test Relevance Criteria
""")

if __name__ == "__main__":
    main() 
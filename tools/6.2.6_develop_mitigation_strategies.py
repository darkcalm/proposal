#!/usr/bin/env python3
"""
Develop Mitigation Strategies (Task 6.2.6)

This script synthesizes the findings from environmental (6.2.1), social (6.2.2),
economic (6.2.3), equity (6.2.4), and policy (6.2.5) analyses.
It tailors these findings to the specific research context (RQs, hypotheses,
methodology, limitations, timeline, workflow) to develop specific, actionable
mitigation strategies. It also aims to incorporate insights from the broader
literature review.
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tools/6.2.6_develop_mitigation_strategies.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define file paths for input data
BASE_SOURCES_PATH = Path("sources")
BASE_DOCS_PATH = Path("docs")

# Input JSON summaries from previous tasks
INPUT_JSON_PATHS = {
    "environmental": BASE_SOURCES_PATH / "6.2.1-environmental-aspects-summary.json",
    "social": BASE_SOURCES_PATH / "6.2.2-social-impacts-summary.json",
    "economic": BASE_SOURCES_PATH / "6.2.3-economic-factors-summary.json",
    "equity": BASE_SOURCES_PATH / "6.2.4-equity-aspects-summary.json",
    "policy": BASE_SOURCES_PATH / "6.2.5-policy-implications-summary.json",
}

# Input Markdown context documents
INPUT_MD_PATHS = {
    "rQs": BASE_DOCS_PATH / "4.2.4.1-research-questions-refined.md",
    "hypotheses": BASE_DOCS_PATH / "4.2.4.2-hypotheses-refined.md",
    "methodology_justification": BASE_DOCS_PATH / "5.3.1-methodology-justification.md",
    "methodology_limitations": BASE_DOCS_PATH / "5.3.2-methodology-limitations.md",
    "timeline": BASE_DOCS_PATH / "5.3.3-project-timeline.md",
    "workflow": BASE_DOCS_PATH / "5.3.4-workflow-diagrams.md",
}

# Output files
OUTPUT_DETAILED_JSON = BASE_SOURCES_PATH / "6.2.6-mitigation-strategies-detailed.json"
OUTPUT_SUMMARY_JSON = BASE_SOURCES_PATH / "6.2.6-mitigation-strategies-summary.json"

# --- Data Loading Functions ---

def load_json_data(file_path: Path) -> Dict[str, Any]:
    """Loads data from a JSON file."""
    logger.info(f"Loading JSON data from: {file_path}")
    try:
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from: {file_path}")
        return {}

def load_markdown_data(file_path: Path) -> str:
    """Loads content from a Markdown file."""
    logger.info(f"Loading Markdown data from: {file_path}")
    try:
        with file_path.open('r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return ""

# --- Core Logic for Tailoring and Mitigation ---

def extract_key_info_from_analysis(analysis_data: Dict[str, Any], impact_area: str) -> Dict[str, Any]:
    """Extracts key impacts and recommendations from loaded analysis summaries."""
    impacts = analysis_data.get("key_impacts", [])
    if not impacts and "primary_domains" in analysis_data:  # for policy
        impacts = analysis_data.get("primary_domains", [])
    
    recommendations = analysis_data.get("key_recommendations", [])
    
    logger.info(f"Extracted for {impact_area}: {len(impacts)} impacts/domains, {len(recommendations)} generic recommendations.")
    return {
        "identified_impacts_or_domains": impacts,
        "generic_recommendations": recommendations,
        "net_impact_assessment": analysis_data.get("net_impact", analysis_data.get("net_policy_impact", "N/A"))
    }

def tailor_impact_and_develop_strategy(
    impact_area: str,
    identified_element: str,
    generic_recommendations: List[str],
    research_context: Dict[str, str],
    literature_insights: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Tailors a single impact/domain to the research context and develops specific mitigation.
    """
    tailored_description = f"The {impact_area} element '{identified_element}' needs to be considered specifically in the context of this research. "
    specific_mitigation_strategies = []

    if "rQs" in research_context and research_context["rQs"]:
        tailored_description += f"This is particularly relevant given the research questions focusing on HDTs, agent protocols (MCP, ACP, A2A), and DER operations. "
        if "human" in identified_element.lower() or "social" in impact_area or "equity" in impact_area:
            specific_mitigation_strategies.append({
                "strategy": "Ensure RQs related to human-agent collaboration, user trust, and equitable outcomes (SRQ3) are directly addressed in system design and evaluation phases.",
                "justification": "Mitigates risks of poor adoption, negative human factors, or inequitable impacts, aligning with SRQ3.",
                "monitoring_indicators": ["User feedback scores", "Task completion efficiency with HDT", "Distribution of benefits/burdens across stakeholder groups"]
            })

    if "methodology_justification" in research_context and research_context["methodology_justification"]:
        if "Systematic Literature Review" in research_context["methodology_justification"] and ("policy" in impact_area or "ethical" in identified_element.lower()):
            specific_mitigation_strategies.append({
                "strategy": "During the SLR phase (Phase 1), explicitly search for and analyze policy, ethical guidelines, and best practices related to AI agents in critical infrastructure and DERs.",
                "justification": "Proactively addresses policy/ethical implications early in the research, aligning with the chosen methodology (Phase 1).",
                "monitoring_indicators": ["Number of relevant policy/ethical papers analyzed in SLR", "Integration of findings into subsequent phases"]
            })
        if "Rapid Prototyping" in research_context["methodology_justification"] and ("economic" in impact_area or "resource" in identified_element.lower() or "feasibility" in identified_element.lower()):
            specific_mitigation_strategies.append({
                "strategy": "Employ iterative rapid prototyping (Phase 3) with cost-effective tools and off-the-shelf components where possible for the Proof of Concept to manage economic risks and resource constraints.",
                "justification": "Aligns with methodology (Phase 3) and mitigates risks of over-investment or unmanageable resource demands in early-stage unproven concepts.",
                "monitoring_indicators": ["Cost of prototype iterations", "Adherence to budget for PoC phase", "Time to develop PoC iterations"]
            })

    if "methodology_limitations" in research_context and research_context["methodology_limitations"]:
        if "Limited Real World Data" in research_context["methodology_limitations"] and ("social" in impact_area or "equity" in impact_area or "validation" in identified_element.lower()):
            specific_mitigation_strategies.append({
                "strategy": "Compensate for limited real-world DER/HDT implementation data by using diverse stakeholder workshops, expert elicitation, and simulated scenarios for validating social/equity impacts and HDT effectiveness.",
                "justification": "Addresses a key methodological limitation to ensure broader perspectives and robust validation are included, as per identified limitations.",
                "monitoring_indicators": ["Number and diversity of stakeholders engaged", "Range of scenarios considered for simulation/validation", "Qualitative feedback from experts/stakeholders"]
            })
        if "Protocol Evolution Speed" in research_context["methodology_limitations"] and ("standardization" in identified_element.lower() or "interoperability" in identified_element.lower()):
            specific_mitigation_strategies.append({
                "strategy": "Establish a continuous monitoring process for agent communication protocol evolution (ACP, A2A, MCP, ANP) and relevant standards throughout the research timeline. Design HDT architecture with modularity to accommodate updates.",
                "justification": "Mitigates the risk of research becoming outdated due to rapid protocol changes, as per identified limitations.",
                "monitoring_indicators": ["Frequency of protocol standard reviews", "Documented architectural adaptability for protocol changes"]
            })

    if "timeline" in research_context and research_context["timeline"] and "workflow" in research_context and research_context["workflow"]:
        if "environmental" in impact_area and ("energy consumption" in identified_element.lower() or "resource efficiency" in identified_element.lower()):
            specific_mitigation_strategies.append({
                "strategy": "During Phase 3 (Proof of Concept), specifically evaluate and document the computational resource requirements and potential energy consumption of the HDT prototype. Explore design choices for efficiency.",
                "justification": "Integrates environmental considerations into the PoC development and evaluation, aligning with the project workflow.",
                "monitoring_indicators": ["Estimated computational cost of HDT operations", "Comparison of different agent configurations for efficiency"]
            })
        if "governance" in identified_element.lower() and "Phase 2: Comparative Framework Development" in research_context["timeline"]:
            specific_mitigation_strategies.append({
                "strategy": "In Phase 2, when developing the comparative framework for ACP vs A2A, explicitly include governance models suitable for HDT operations within DER ecosystems.",
                "justification": "Ensures governance considerations are structurally integrated into the core research outputs from Phase 2.",
                "monitoring_indicators": ["Inclusion of governance criteria in comparative framework", "Analysis of governance implications for different protocol choices"]
            })

    if not specific_mitigation_strategies:
        if generic_recommendations:
            for rec in generic_recommendations:
                specific_mitigation_strategies.append({
                    "strategy": f"(Generic recommendation - requires specific tailoring for this research) Implement: {rec}",
                    "justification": f"Based on general best practices for {impact_area} concerning '{identified_element}'. Needs to be contextualized for HDTs and agent protocols in DERs.",
                    "monitoring_indicators": ["Development of a specific action plan for this recommendation within the research context"]
                })
        else:
            specific_mitigation_strategies.append({
                "strategy": f"A specific mitigation strategy for the {impact_area} element '{identified_element}' needs to be actively developed and documented, tailored to the research on HDTs and agent protocols.",
                "justification": "No generic recommendation available or specific heuristics did not trigger; requires focused effort to ensure this aspect is addressed within the research proposal.",
                "monitoring_indicators": ["Completion of investigation and documentation of a tailored strategy"]
            })
    
    if literature_insights.get("example_theme_from_papers"):
        tailored_description += f"Insights from broader literature on '{literature_insights['example_theme_from_papers']}' (e.g., from papers like those in 'markdown_papers') should inform the approach. "

    return {
        "original_element": identified_element,
        "tailored_contextual_description": tailored_description,
        "specific_mitigation_strategies": specific_mitigation_strategies
    }

def develop_all_mitigation_strategies(
    analyses_data: Dict[str, Dict[str, Any]],
    research_context_md: Dict[str, str]
) -> List[Dict[str, Any]]:
    """
    Develops tailored mitigation strategies for all impact areas.
    """
    all_mitigation_details = []
    logger.info("Starting development of all mitigation strategies.")

    literature_insights_loaded = {
        "example_theme_from_papers": "Human-in-the-loop AI, explainable AI (XAI) for critical systems, and ethical AI development frameworks"
    }

    for area, data in analyses_data.items():
        logger.info(f"Processing impact area: {area}")
        # Ensure data is not empty before processing
        if not data:
            logger.warning(f"Skipping area {area} due to no data loaded.")
            # Optionally add a placeholder to all_mitigation_details for this area
            all_mitigation_details.append({
                "impact_area": area.capitalize(),
                "overall_net_impact": "N/A - Data not loaded",
                "generic_recommendations_from_initial_analysis": [],
                "tailored_impacts_and_mitigations": [{
                    "original_element": "Data Not Loaded",
                    "tailored_contextual_description": f"No analysis data was loaded for the {area} impact area. Mitigation strategies could not be developed.",
                    "specific_mitigation_strategies": []
                }]
            })
            continue
            
        extracted_info = extract_key_info_from_analysis(data, area)
        
        area_mitigations = {
            "impact_area": area.capitalize(),
            "overall_net_impact": extracted_info["net_impact_assessment"],
            "generic_recommendations_from_initial_analysis": extracted_info["generic_recommendations"],
            "tailored_impacts_and_mitigations": []
        }

        for element in extracted_info["identified_impacts_or_domains"]:
            tailored_strategy_info = tailor_impact_and_develop_strategy(
                impact_area=area,
                identified_element=str(element),  # Ensure element is a string
                generic_recommendations=extracted_info["generic_recommendations"],
                research_context=research_context_md,
                literature_insights=literature_insights_loaded
            )
            area_mitigations["tailored_impacts_and_mitigations"].append(tailored_strategy_info)
        
        all_mitigation_details.append(area_mitigations)
        logger.info(f"Finished processing for area: {area}. Developed {len(area_mitigations['tailored_impacts_and_mitigations'])} tailored items.")

    logger.info("Finished development of all mitigation strategies.")
    return all_mitigation_details

# --- Main Execution ---
def main():
    logger.info("Starting Task 6.2.6: Develop Mitigation Strategies")

    logger.info("--- Loading Input Data ---")
    loaded_analyses = {}
    for area, path in INPUT_JSON_PATHS.items():
        loaded_analyses[area] = load_json_data(path)
        if not loaded_analyses[area]:
            logger.warning(f"No data loaded for {area} from {path}. Downstream processing for this area might be affected.")

    loaded_md_context = {}
    for ctx_name, path in INPUT_MD_PATHS.items():
        loaded_md_context[ctx_name] = load_markdown_data(path)
        if not loaded_md_context[ctx_name]:
            logger.warning(f"No context data loaded for {ctx_name} from {path}. Tailoring might be less effective.")
    
    logger.info("--- Developing Tailored Mitigation Strategies ---")
    comprehensive_mitigation_strategies = develop_all_mitigation_strategies(
        loaded_analyses,
        loaded_md_context
    )

    output_data_detailed = {
        "metadata": {
            "task": "6.2.6 - Develop Mitigation Strategies",
            "generated_date": datetime.now().isoformat(),
            "description": "Tailored mitigation strategies based on integrated analysis of environmental, social, economic, equity, and policy impacts within the specific research proposal context.",
            "data_sources_analyses": {k: str(v) for k, v in INPUT_JSON_PATHS.items()},
            "data_sources_context_docs": {k: str(v) for k, v in INPUT_MD_PATHS.items()},
        },
        "comprehensive_mitigation_strategies": comprehensive_mitigation_strategies
    }
    
    total_mitigation_elements = sum(len(area.get("tailored_impacts_and_mitigations", [])) for area in comprehensive_mitigation_strategies)
    output_data_summary = {
        "metadata": output_data_detailed["metadata"],
        "summary_of_mitigation_effort": {
            "total_impact_areas_processed": len(comprehensive_mitigation_strategies),
            "total_tailored_elements_with_mitigations": total_mitigation_elements,
            "key_cross_cutting_themes_for_mitigation": [
                "Proactive integration of sustainability and ethics (environmental, social, equity, policy) directly into the research methodology phases (SLR, Comparative Framework, PoC).",
                "Emphasis on human-centered design (HCD) principles for HDTs, focusing on user trust, usability, and collaboration, particularly addressing SRQ3.",
                "Iterative risk management and mitigation strategy refinement aligned with the project timeline, workflow, and identified methodological limitations (e.g., real-world data access, protocol evolution).",
                "Leverage modular design and recognized standards to enhance interoperability, manage economic factors, and address standardization implications."
            ],
            "data_loading_status": {
                area: "Loaded" if data else "Not Loaded/Empty" for area, data in loaded_analyses.items()
            },
            "context_loading_status": {
                ctx: "Loaded" if data else "Not Loaded/Empty" for ctx, data in loaded_md_context.items()
            }
        }
    }

    logger.info("--- Saving Results ---")
    try:
        with OUTPUT_DETAILED_JSON.open('w', encoding='utf-8') as f:
            json.dump(output_data_detailed, f, indent=2, ensure_ascii=False)
        logger.info(f"Detailed mitigation strategies saved to: {OUTPUT_DETAILED_JSON}")

        with OUTPUT_SUMMARY_JSON.open('w', encoding='utf-8') as f:
            json.dump(output_data_summary, f, indent=2, ensure_ascii=False)
        logger.info(f"Summary mitigation strategies saved to: {OUTPUT_SUMMARY_JSON}")
    except IOError as e:
        logger.error(f"Error saving results: {e}")
        raise

    logger.info("Task 6.2.6: Develop Mitigation Strategies - COMPLETED SUCCESSFULLY")
    print_summary_to_console(output_data_summary)

def print_summary_to_console(summary_data: Dict[str, Any]):
    """Prints a brief summary of the outcomes to the console."""
    print("\n" + "=" * 80)
    print("MITIGATION STRATEGY DEVELOPMENT COMPLETED (Task 6.2.6)")
    print("=" * 80)
    summary_info = summary_data.get("summary_of_mitigation_effort", {})
    print(f"Total impact areas processed: {summary_info.get('total_impact_areas_processed')}")
    print(f"Total tailored elements with mitigations: {summary_info.get('total_tailored_elements_with_mitigations')}")
    
    print("\nData Loading Status (Analyses):")
    for area, status in summary_info.get("data_loading_status", {}).items():
        print(f"  • {area.capitalize()}: {status}")
        
    print("\nData Loading Status (Context Docs):")
    for ctx, status in summary_info.get("context_loading_status", {}).items():
        print(f"  • {ctx.capitalize()}: {status}")
        
    print("\nKey Cross-Cutting Themes for Mitigation:")
    for theme in summary_info.get("key_cross_cutting_themes_for_mitigation", []):
        print(f"  • {theme}")
    print(f"\nDetailed results saved to: {OUTPUT_DETAILED_JSON}")
    print(f"Summary results saved to: {OUTPUT_SUMMARY_JSON}")
    print("=" * 80)

if __name__ == "__main__":
    main() 
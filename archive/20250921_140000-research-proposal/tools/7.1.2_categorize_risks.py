#!/usr/bin/env python3
"""
Categorize Risks (Task 7.1.2)

This script performs detailed categorization of the risks identified in task 7.1.1.
It analyzes risks across multiple dimensions including:
- Primary category (Technical, Methodological, Resource, Impact, Timeline)
- Risk type (Strategic, Operational, Tactical)
- Time sensitivity (Immediate, Short-term, Long-term)
- Dependencies (Internal, External, Mixed)
- Controllability (High, Medium, Low)
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
        logging.FileHandler('tools/7.1.2_categorize_risks.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define file paths
BASE_SOURCES_PATH = Path("sources")
BASE_DOCS_PATH = Path("docs")

# Input files
INPUT_RISKS = BASE_SOURCES_PATH / "7.1.1-potential-risks-detailed.json"

# Output files
OUTPUT_DETAILED_JSON = BASE_SOURCES_PATH / "7.1.2-risk-categories-detailed.json"
OUTPUT_SUMMARY_JSON = BASE_SOURCES_PATH / "7.1.2-risk-categories-summary.json"

def load_risks() -> List[Dict[str, Any]]:
    """Loads the previously identified risks."""
    try:
        with INPUT_RISKS.open('r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('risks', [])
    except FileNotFoundError:
        logger.error(f"Risk file not found: {INPUT_RISKS}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from: {INPUT_RISKS}")
        return []

def categorize_risks(risks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Performs detailed categorization of risks.
    """
    categorized_risks = []
    
    # Define categorization mappings
    risk_type_mapping = {
        "TECH-001": "Strategic",  # Protocol evolution affects long-term strategy
        "TECH-002": "Operational",  # Integration is an operational concern
        "TECH-003": "Tactical",  # Resource limitations are tactical
        "METH-001": "Operational",  # Data access affects operations
        "METH-002": "Strategic",  # Human-agent evaluation is strategic
        "METH-003": "Operational",  # Protocol comparison is operational
        "RES-001": "Strategic",  # Time constraints affect strategy
        "RES-002": "Tactical",  # Expertise access is tactical
        "RES-003": "Operational",  # Budget affects operations
        "IMP-001": "Strategic",  # Social impact is strategic
        "IMP-002": "Operational",  # Environmental impact affects operations
        "IMP-003": "Strategic",  # Policy compliance is strategic
        "TIME-001": "Operational",  # Literature review delays affect operations
        "TIME-002": "Operational",  # Prototype development is operational
        "TIME-003": "Tactical"  # Feedback cycles are tactical
    }
    
    time_sensitivity_mapping = {
        "TECH-001": "Long-term",  # Protocol evolution is long-term
        "TECH-002": "Short-term",  # Integration is short-term
        "TECH-003": "Immediate",  # Resource limitations are immediate
        "METH-001": "Short-term",  # Data access is short-term
        "METH-002": "Long-term",  # Human-agent evaluation is long-term
        "METH-003": "Short-term",  # Protocol comparison is short-term
        "RES-001": "Immediate",  # Time constraints are immediate
        "RES-002": "Short-term",  # Expertise access is short-term
        "RES-003": "Immediate",  # Budget is immediate
        "IMP-001": "Long-term",  # Social impact is long-term
        "IMP-002": "Short-term",  # Environmental impact is short-term
        "IMP-003": "Long-term",  # Policy compliance is long-term
        "TIME-001": "Immediate",  # Literature review delays are immediate
        "TIME-002": "Short-term",  # Prototype development is short-term
        "TIME-003": "Immediate"  # Feedback cycles are immediate
    }
    
    dependency_mapping = {
        "TECH-001": "External",  # Protocol evolution is external
        "TECH-002": "Mixed",  # Integration involves both internal and external
        "TECH-003": "Internal",  # Resource limitations are internal
        "METH-001": "External",  # Data access is external
        "METH-002": "Mixed",  # Human-agent evaluation involves both
        "METH-003": "Internal",  # Protocol comparison is internal
        "RES-001": "Internal",  # Time constraints are internal
        "RES-002": "Mixed",  # Expertise access involves both
        "RES-003": "Internal",  # Budget is internal
        "IMP-001": "External",  # Social impact is external
        "IMP-002": "Internal",  # Environmental impact is internal
        "IMP-003": "External",  # Policy compliance is external
        "TIME-001": "Internal",  # Literature review delays are internal
        "TIME-002": "Internal",  # Prototype development is internal
        "TIME-003": "Mixed"  # Feedback cycles involve both
    }
    
    controllability_mapping = {
        "TECH-001": "Low",  # Protocol evolution is hard to control
        "TECH-002": "Medium",  # Integration is somewhat controllable
        "TECH-003": "High",  # Resource limitations are controllable
        "METH-001": "Medium",  # Data access is somewhat controllable
        "METH-002": "High",  # Human-agent evaluation is controllable
        "METH-003": "High",  # Protocol comparison is controllable
        "RES-001": "Medium",  # Time constraints are somewhat controllable
        "RES-002": "Medium",  # Expertise access is somewhat controllable
        "RES-003": "Medium",  # Budget is somewhat controllable
        "IMP-001": "Low",  # Social impact is hard to control
        "IMP-002": "High",  # Environmental impact is controllable
        "IMP-003": "Low",  # Policy compliance is hard to control
        "TIME-001": "High",  # Literature review delays are controllable
        "TIME-002": "Medium",  # Prototype development is somewhat controllable
        "TIME-003": "Medium"  # Feedback cycles are somewhat controllable
    }
    
    for risk in risks:
        risk_id = risk["risk_id"]
        categorized_risk = risk.copy()
        
        # Add categorization details
        categorized_risk.update({
            "risk_type": risk_type_mapping.get(risk_id, "Unknown"),
            "time_sensitivity": time_sensitivity_mapping.get(risk_id, "Unknown"),
            "dependency": dependency_mapping.get(risk_id, "Unknown"),
            "controllability": controllability_mapping.get(risk_id, "Unknown")
        })
        
        categorized_risks.append(categorized_risk)
    
    return categorized_risks

def generate_output_files(categorized_risks: List[Dict[str, Any]]):
    """Generates detailed and summary JSON output files."""
    # Prepare detailed output
    detailed_output = {
        "metadata": {
            "task": "7.1.2 - Categorize Risks",
            "generated_date": datetime.now().isoformat(),
            "description": "Detailed categorization of identified risks across multiple dimensions",
            "total_risks_categorized": len(categorized_risks)
        },
        "categorized_risks": categorized_risks
    }
    
    # Prepare summary output
    summary = {
        "metadata": detailed_output["metadata"],
        "categorization_summary": {
            "by_risk_type": {},
            "by_time_sensitivity": {},
            "by_dependency": {},
            "by_controllability": {},
            "by_category": {}
        }
    }
    
    # Calculate summary statistics
    for risk in categorized_risks:
        # Count by risk type
        risk_type = risk["risk_type"]
        if risk_type not in summary["categorization_summary"]["by_risk_type"]:
            summary["categorization_summary"]["by_risk_type"][risk_type] = 0
        summary["categorization_summary"]["by_risk_type"][risk_type] += 1
        
        # Count by time sensitivity
        time_sensitivity = risk["time_sensitivity"]
        if time_sensitivity not in summary["categorization_summary"]["by_time_sensitivity"]:
            summary["categorization_summary"]["by_time_sensitivity"][time_sensitivity] = 0
        summary["categorization_summary"]["by_time_sensitivity"][time_sensitivity] += 1
        
        # Count by dependency
        dependency = risk["dependency"]
        if dependency not in summary["categorization_summary"]["by_dependency"]:
            summary["categorization_summary"]["by_dependency"][dependency] = 0
        summary["categorization_summary"]["by_dependency"][dependency] += 1
        
        # Count by controllability
        controllability = risk["controllability"]
        if controllability not in summary["categorization_summary"]["by_controllability"]:
            summary["categorization_summary"]["by_controllability"][controllability] = 0
        summary["categorization_summary"]["by_controllability"][controllability] += 1
        
        # Count by primary category
        category = risk["category"]
        if category not in summary["categorization_summary"]["by_category"]:
            summary["categorization_summary"]["by_category"][category] = 0
        summary["categorization_summary"]["by_category"][category] += 1
    
    # Save outputs
    try:
        with OUTPUT_DETAILED_JSON.open('w', encoding='utf-8') as f:
            json.dump(detailed_output, f, indent=2, ensure_ascii=False)
        logger.info(f"Detailed categorization saved to: {OUTPUT_DETAILED_JSON}")
        
        with OUTPUT_SUMMARY_JSON.open('w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        logger.info(f"Summary categorization saved to: {OUTPUT_SUMMARY_JSON}")
    except IOError as e:
        logger.error(f"Error saving output files: {e}")
        raise

def print_summary_to_console(summary_data: Dict[str, Any]):
    """Prints a brief summary of the risk categorization to the console."""
    print("\n" + "=" * 80)
    print("RISK CATEGORIZATION COMPLETED (Task 7.1.2)")
    print("=" * 80)
    
    metadata = summary_data["metadata"]
    print(f"Total risks categorized: {metadata['total_risks_categorized']}")
    
    summary = summary_data["categorization_summary"]
    
    print("\nRisks by Type:")
    for risk_type, count in summary["by_risk_type"].items():
        print(f"  • {risk_type}: {count} risks")
    
    print("\nRisks by Time Sensitivity:")
    for sensitivity, count in summary["by_time_sensitivity"].items():
        print(f"  • {sensitivity}: {count} risks")
    
    print("\nRisks by Dependency:")
    for dependency, count in summary["by_dependency"].items():
        print(f"  • {dependency}: {count} risks")
    
    print("\nRisks by Controllability:")
    for controllability, count in summary["by_controllability"].items():
        print(f"  • {controllability}: {count} risks")
    
    print("\nRisks by Primary Category:")
    for category, count in summary["by_category"].items():
        print(f"  • {category}: {count} risks")
    
    print(f"\nDetailed results saved to: {OUTPUT_DETAILED_JSON}")
    print(f"Summary results saved to: {OUTPUT_SUMMARY_JSON}")
    print("=" * 80)

def main():
    logger.info("Starting Task 7.1.2: Categorize Risks")
    
    # Load previously identified risks
    risks = load_risks()
    if not risks:
        logger.error("No risks found to categorize")
        return
    
    # Categorize risks
    categorized_risks = categorize_risks(risks)
    
    # Generate output files
    generate_output_files(categorized_risks)
    
    # Load and print summary
    with OUTPUT_SUMMARY_JSON.open('r', encoding='utf-8') as f:
        summary_data = json.load(f)
    print_summary_to_console(summary_data)
    
    logger.info("Task 7.1.2: Categorize Risks - COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main() 
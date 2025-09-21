#!/usr/bin/env python3
"""
Create Risk Register (Task 7.1.3)

This script creates a comprehensive risk register based on the categorized risks
from task 7.1.2. The risk register includes:
- Risk ID and description
- Categories and classifications
- Current status and ownership
- Risk level and priority
- Monitoring and review information
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
        logging.FileHandler('tools/7.1.3_create_risk_register.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define file paths
BASE_SOURCES_PATH = Path("sources")
BASE_DOCS_PATH = Path("docs")

# Input files
INPUT_CATEGORIZED_RISKS = BASE_SOURCES_PATH / "7.1.2-risk-categories-detailed.json"

# Output files
OUTPUT_RISK_REGISTER = BASE_SOURCES_PATH / "7.1.3-risk-register.json"
OUTPUT_RISK_REGISTER_MD = BASE_DOCS_PATH / "7.1.3-risk-register.md"

def load_categorized_risks() -> List[Dict[str, Any]]:
    """Loads the categorized risks from task 7.1.2."""
    try:
        with INPUT_CATEGORIZED_RISKS.open('r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('categorized_risks', [])
    except FileNotFoundError:
        logger.error(f"Categorized risks file not found: {INPUT_CATEGORIZED_RISKS}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from: {INPUT_CATEGORIZED_RISKS}")
        return []

def create_risk_register(categorized_risks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Creates a comprehensive risk register from categorized risks.
    """
    risk_register = []
    
    # Define risk owners based on category
    owner_mapping = {
        "Technical": "Technical Lead",
        "Methodological": "Research Lead",
        "Resource": "Project Manager",
        "Impact": "Sustainability Lead",
        "Timeline": "Project Manager"
    }
    
    # Define initial status
    status_mapping = {
        "Immediate": "Active",
        "Short-term": "Active",
        "Long-term": "Monitoring"
    }
    
    # Define review frequency based on time sensitivity
    review_frequency_mapping = {
        "Immediate": "Weekly",
        "Short-term": "Bi-weekly",
        "Long-term": "Monthly"
    }
    
    for risk in categorized_risks:
        register_entry = {
            "risk_id": risk["risk_id"],
            "description": risk["description"],
            "category": risk["category"],
            "risk_type": risk["risk_type"],
            "time_sensitivity": risk["time_sensitivity"],
            "dependency": risk["dependency"],
            "controllability": risk["controllability"],
            "current_status": status_mapping[risk["time_sensitivity"]],
            "risk_owner": owner_mapping[risk["category"]],
            "review_frequency": review_frequency_mapping[risk["time_sensitivity"]],
            "last_review_date": datetime.now().isoformat(),
            "next_review_date": None,  # To be calculated based on review frequency
            "risk_level": None,  # To be determined in task 7.1.4
            "priority": None,  # To be determined in task 7.1.5
            "mitigation_strategy": None,  # To be developed in task 7.2.1
            "contingency_plan": None,  # To be developed in task 7.2.2
            "notes": []
        }
        
        risk_register.append(register_entry)
    
    return risk_register

def generate_output_files(risk_register: List[Dict[str, Any]]):
    """Generates JSON and Markdown output files for the risk register."""
    # Save JSON output
    try:
        with OUTPUT_RISK_REGISTER.open('w', encoding='utf-8') as f:
            json.dump(risk_register, f, indent=2, ensure_ascii=False)
        logger.info(f"Risk register JSON saved to: {OUTPUT_RISK_REGISTER}")
    except IOError as e:
        logger.error(f"Error saving JSON output: {e}")
        raise
    
    # Generate Markdown output
    md_content = generate_markdown_content(risk_register)
    
    # Save Markdown output
    try:
        with OUTPUT_RISK_REGISTER_MD.open('w', encoding='utf-8') as f:
            f.write(md_content)
        logger.info(f"Risk register Markdown saved to: {OUTPUT_RISK_REGISTER_MD}")
    except IOError as e:
        logger.error(f"Error saving Markdown output: {e}")
        raise

def generate_markdown_content(data: List[Dict[str, Any]]) -> str:
    """Generates Markdown content for the risk register."""
    md_lines = [
        "# Risk Register (Task 7.1.3)",
        "",
        "## 1. Executive Summary",
        "",
        f"This risk register contains {len(data)} identified risks for the research project on Agent Communication Protocols (ACP) for Human DER Worker Digital Twins (HDTs).",
        "",
        "## 2. Risk Register",
        "",
        "| Risk ID | Description | Category | Type | Time Sensitivity | Status | Owner | Review Frequency |",
        "|---------|-------------|----------|------|------------------|---------|--------|-----------------|"
    ]
    
    for risk in data:
        md_lines.append(
            f"| {risk['risk_id']} | {risk['description']} | {risk['category']} | "
            f"{risk['risk_type']} | {risk['time_sensitivity']} | {risk['current_status']} | "
            f"{risk['risk_owner']} | {risk['review_frequency']} |"
        )
    
    md_lines.extend([
        "",
        "## 3. Risk Details",
        ""
    ])
    
    for risk in data:
        md_lines.extend([
            f"### {risk['risk_id']}: {risk['description']}",
            "",
            f"- **Category**: {risk['category']}",
            f"- **Risk Type**: {risk['risk_type']}",
            f"- **Time Sensitivity**: {risk['time_sensitivity']}",
            f"- **Dependency**: {risk['dependency']}",
            f"- **Controllability**: {risk['controllability']}",
            f"- **Current Status**: {risk['current_status']}",
            f"- **Risk Owner**: {risk['risk_owner']}",
            f"- **Review Frequency**: {risk['review_frequency']}",
            f"- **Last Review Date**: {risk['last_review_date']}",
            "",
            "#### Notes",
            "No notes available yet.",
            ""
        ])
    
    md_lines.extend([
        "## 4. Next Steps",
        "",
        "The following information will be added in subsequent tasks:",
        "- Risk levels (Task 7.1.4)",
        "- Risk priorities (Task 7.1.5)",
        "- Mitigation strategies (Task 7.2.1)",
        "- Contingency plans (Task 7.2.2)",
        "",
        "## 5. Maintenance",
        "",
        "This risk register will be regularly updated as part of the project's risk management process. Each risk will be reviewed according to its specified review frequency."
    ])
    
    return "\n".join(md_lines)

def print_summary_to_console(data: List[Dict[str, Any]]):
    """Prints a brief summary of the risk register to the console."""
    print("\n" + "=" * 80)
    print("RISK REGISTER CREATED (Task 7.1.3)")
    print("=" * 80)
    
    print(f"Total risks in register: {len(data)}")
    
    # Count risks by category
    categories = {}
    for risk in data:
        category = risk["category"]
        if category not in categories:
            categories[category] = 0
        categories[category] += 1
    
    print("\nRisks by Category:")
    for category, count in categories.items():
        print(f"  • {category}: {count} risks")
    
    # Count risks by status
    statuses = {}
    for risk in data:
        status = risk["current_status"]
        if status not in statuses:
            statuses[status] = 0
        statuses[status] += 1
    
    print("\nRisks by Status:")
    for status, count in statuses.items():
        print(f"  • {status}: {count} risks")
    
    print(f"\nDetailed register saved to: {OUTPUT_RISK_REGISTER}")
    print(f"Markdown documentation saved to: {OUTPUT_RISK_REGISTER_MD}")
    print("=" * 80)

def main():
    logger.info("Starting Task 7.1.3: Create Risk Register")
    
    # Load categorized risks
    categorized_risks = load_categorized_risks()
    if not categorized_risks:
        logger.error("No categorized risks found")
        return
    
    # Create risk register
    risk_register = create_risk_register(categorized_risks)
    
    # Generate output files
    json_output = {
        "metadata": {
            "task": "7.1.3 - Create Risk Register",
            "generated_date": datetime.now().isoformat(),
            "description": "Comprehensive risk register for the research project",
            "total_risks": len(risk_register)
        },
        "risk_register": risk_register
    }
    
    generate_output_files(risk_register)
    
    # Load and print summary
    with OUTPUT_RISK_REGISTER.open('r', encoding='utf-8') as f:
        data = json.load(f)
    print_summary_to_console(data)
    
    logger.info("Task 7.1.3: Create Risk Register - COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main() 
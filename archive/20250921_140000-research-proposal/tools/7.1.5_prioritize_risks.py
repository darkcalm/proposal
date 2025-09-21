#!/usr/bin/env python3
"""
Prioritize Risks (Task 7.1.5)

This script loads the risk register from task 7.1.4, assigns a priority score to each risk,
and outputs updated JSON and Markdown documentation.
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
        logging.FileHandler('tools/7.1.5_prioritize_risks.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Define file paths
BASE_SOURCES_PATH = Path("sources")
BASE_DOCS_PATH = Path("docs")

# Input files
INPUT_RISK_REGISTER = BASE_SOURCES_PATH / "7.1.4-risk-register-likelihood-impact.json"

# Output files
OUTPUT_RISK_REGISTER = BASE_SOURCES_PATH / "7.1.5-risk-register-prioritized.json"
OUTPUT_RISK_REGISTER_MD = BASE_DOCS_PATH / "7.1.5-risk-prioritized.md"

# Priority score mapping based on risk level
PRIORITY_SCORE_MAPPING = {
    'Low': 1,
    'Medium': 2,
    'High': 3,
    'Critical': 4
}

def load_risk_register() -> List[Dict[str, Any]]:
    try:
        with INPUT_RISK_REGISTER.open('r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict) and 'risk_register' in data:
                return data['risk_register']
            return data
    except Exception as e:
        logger.error(f"Error loading risk register: {e}")
        return []

def prioritize_risks(risks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    updated_risks = []
    for risk in risks:
        # Assign priority score based on risk level
        priority_score = PRIORITY_SCORE_MAPPING.get(risk['risk_level'], 1)
        risk.update({
            'priority_score': priority_score
        })
        updated_risks.append(risk)
    return updated_risks

def generate_output_files(risks: List[Dict[str, Any]]):
    # Prepare JSON output
    json_output = {
        "metadata": {
            "task": "7.1.5 - Prioritize Risks",
            "generated_date": datetime.now().isoformat(),
            "description": "Risk register with priority scores",
            "total_risks": len(risks)
        },
        "risk_register": risks
    }
    try:
        with OUTPUT_RISK_REGISTER.open('w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=2, ensure_ascii=False)
        logger.info(f"Updated risk register JSON saved to: {OUTPUT_RISK_REGISTER}")
    except IOError as e:
        logger.error(f"Error saving JSON output: {e}")
        raise
    # Generate Markdown output
    md_content = generate_markdown_content(json_output)
    try:
        with OUTPUT_RISK_REGISTER_MD.open('w', encoding='utf-8') as f:
            f.write(md_content)
        logger.info(f"Updated risk register Markdown saved to: {OUTPUT_RISK_REGISTER_MD}")
    except IOError as e:
        logger.error(f"Error saving Markdown output: {e}")
        raise

def generate_markdown_content(data: Dict[str, Any]) -> str:
    md_lines = [
        "# Risk Register: Prioritized Risks (Task 7.1.5)",
        "",
        "## 1. Executive Summary",
        "",
        f"This risk register includes priority scores for {data['metadata']['total_risks']} risks.",
        "",
        "## 2. Risk Register Table",
        "",
        "| Risk ID | Description | Category | Risk Level | Priority Score |",
        "|---------|-------------|----------|------------|----------------|"
    ]
    for risk in data['risk_register']:
        md_lines.append(
            f"| {risk['risk_id']} | {risk['description']} | {risk['category']} | "
            f"{risk['risk_level']} | {risk['priority_score']} |"
        )
    md_lines.extend([
        "",
        "## 3. Risk Details",
        ""
    ])
    for risk in data['risk_register']:
        md_lines.extend([
            f"### {risk['risk_id']}: {risk['description']}",
            "",
            f"- **Category**: {risk['category']}",
            f"- **Risk Level**: {risk['risk_level']}",
            f"- **Priority Score**: {risk['priority_score']}",
            f"- **Current Status**: {risk['current_status']}",
            f"- **Risk Owner**: {risk['risk_owner']}",
            f"- **Review Frequency**: {risk['review_frequency']}",
            f"- **Last Review Date**: {risk['last_review_date']}",
            ""
        ])
    md_lines.extend([
        "## 4. Next Steps",
        "",
        "- Develop mitigation strategies (Task 7.2.1)",
        "- Create contingency plans (Task 7.2.2)",
        "",
        "## 5. Maintenance",
        "",
        "This risk register will be updated as part of ongoing risk management."
    ])
    return "\n".join(md_lines)

def print_summary_to_console(data: Dict[str, Any]):
    print("\n" + "=" * 80)
    print("RISK PRIORITIZATION COMPLETED (Task 7.1.5)")
    print("=" * 80)
    print(f"Total risks prioritized: {data['metadata']['total_risks']}")
    # Count by priority score
    priorities = {}
    for risk in data['risk_register']:
        priority = risk['priority_score']
        if priority not in priorities:
            priorities[priority] = 0
        priorities[priority] += 1
    print("\nRisks by Priority Score:")
    for priority, count in priorities.items():
        print(f"  • Priority {priority}: {count} risks")
    print(f"\nDetailed register saved to: {OUTPUT_RISK_REGISTER}")
    print(f"Markdown documentation saved to: {OUTPUT_RISK_REGISTER_MD}")
    print("=" * 80)

def main():
    logger.info("Starting Task 7.1.5: Prioritize Risks")
    risks = load_risk_register()
    if not risks:
        logger.error("No risks found in register.")
        return
    updated_risks = prioritize_risks(risks)
    generate_output_files(updated_risks)
    # Print summary
    with OUTPUT_RISK_REGISTER.open('r', encoding='utf-8') as f:
        data = json.load(f)
    print_summary_to_console(data)
    logger.info("Task 7.1.5: Prioritize Risks - COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    main() 
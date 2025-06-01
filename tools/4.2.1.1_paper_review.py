import os
import json
from pathlib import Path
from datetime import datetime
import re

# Define scoring criteria
CRITERIA = {
    "Protocol Focus": {
        "Must Have": {
            "agent_communication_protocols": 3,
            "distributed_systems": 3,
            "communication_implementation": 3
        },
        "Should Have": {
            "security_features": 2,
            "scalability": 2,
            "performance_metrics": 2
        },
        "Nice to Have": {
            "specific_acp_a2a": 1,
            "maintenance_applications": 1,
            "multi_owner": 1
        }
    },
    "Domain Context": {
        "Must Have": {
            "energy_system_focus": 3,
            "distributed_architecture": 3,
            "multi_agent_system": 3
        },
        "Should Have": {
            "maintenance_monitoring": 2,
            "real_world_deployment": 2,
            "system_integration": 2
        },
        "Nice to Have": {
            "predictive_maintenance": 1,
            "multi_owner_scenarios": 1,
            "privacy_considerations": 1
        }
    },
    "Technical Requirements": {
        "Must Have": {
            "security_implementation": 3,
            "protocol_specifications": 3,
            "performance_evaluation": 3
        },
        "Should Have": {
            "scalability_testing": 2,
            "interoperability": 2,
            "error_handling": 2
        },
        "Nice to Have": {
            "standard_compliance": 1,
            "legacy_integration": 1,
            "future_extensibility": 1
        }
    }
}

# Define keyword patterns for each criterion
KEYWORDS = {
    "agent_communication_protocols": [
        r"agent.*communication.*protocol",
        r"communication.*protocol.*agent",
        r"protocol.*agent.*communication",
        r"agent.*protocol",
        r"communication.*protocol"
    ],
    "distributed_systems": [
        r"distributed.*system",
        r"decentralized.*system",
        r"distributed.*architecture",
        r"decentralized.*architecture"
    ],
    "communication_implementation": [
        r"communication.*implementation",
        r"protocol.*implementation",
        r"communication.*mechanism",
        r"protocol.*mechanism"
    ],
    "security_features": [
        r"security.*feature",
        r"security.*consideration",
        r"secure.*protocol",
        r"security.*mechanism"
    ],
    "scalability": [
        r"scalability",
        r"scalable",
        r"scale.*up",
        r"scale.*out"
    ],
    "performance_metrics": [
        r"performance.*metric",
        r"performance.*measure",
        r"performance.*evaluation",
        r"performance.*analysis"
    ],
    "specific_acp_a2a": [
        r"ACP",
        r"A2A",
        r"agent.*to.*agent",
        r"agent.*communication.*protocol"
    ],
    "maintenance_applications": [
        r"maintenance.*application",
        r"predictive.*maintenance",
        r"preventive.*maintenance",
        r"condition.*monitoring"
    ],
    "multi_owner": [
        r"multi.*owner",
        r"multiple.*owner",
        r"ownership",
        r"stakeholder"
    ],
    "energy_system_focus": [
        r"energy.*system",
        r"smart.*grid",
        r"microgrid",
        r"DER",
        r"distributed.*energy"
    ],
    "distributed_architecture": [
        r"distributed.*architecture",
        r"decentralized.*architecture",
        r"distributed.*design",
        r"decentralized.*design"
    ],
    "multi_agent_system": [
        r"multi.*agent.*system",
        r"multi-agent.*system",
        r"MAS",
        r"agent.*based.*system"
    ],
    "maintenance_monitoring": [
        r"maintenance.*monitoring",
        r"condition.*monitoring",
        r"health.*monitoring",
        r"system.*monitoring"
    ],
    "real_world_deployment": [
        r"real.*world.*deployment",
        r"field.*test",
        r"pilot.*study",
        r"case.*study"
    ],
    "system_integration": [
        r"system.*integration",
        r"integration.*with",
        r"interoperability",
        r"compatibility"
    ],
    "predictive_maintenance": [
        r"predictive.*maintenance",
        r"prognostics",
        r"health.*prediction",
        r"failure.*prediction"
    ],
    "multi_owner_scenarios": [
        r"multi.*owner.*scenario",
        r"multiple.*stakeholder",
        r"ownership.*model",
        r"stakeholder.*management"
    ],
    "privacy_considerations": [
        r"privacy.*consideration",
        r"data.*privacy",
        r"privacy.*protection",
        r"confidentiality"
    ],
    "security_implementation": [
        r"security.*implementation",
        r"security.*mechanism",
        r"security.*protocol",
        r"secure.*communication"
    ],
    "protocol_specifications": [
        r"protocol.*specification",
        r"communication.*specification",
        r"protocol.*design",
        r"communication.*design"
    ],
    "performance_evaluation": [
        r"performance.*evaluation",
        r"performance.*analysis",
        r"performance.*assessment",
        r"performance.*measurement"
    ],
    "scalability_testing": [
        r"scalability.*test",
        r"scalability.*analysis",
        r"scalability.*evaluation",
        r"scalability.*assessment"
    ],
    "interoperability": [
        r"interoperability",
        r"compatibility",
        r"integration.*with",
        r"system.*integration"
    ],
    "error_handling": [
        r"error.*handling",
        r"fault.*tolerance",
        r"failure.*recovery",
        r"error.*recovery"
    ],
    "standard_compliance": [
        r"standard.*compliance",
        r"compliance.*with",
        r"standard.*adherence",
        r"standard.*conformance"
    ],
    "legacy_integration": [
        r"legacy.*integration",
        r"legacy.*system",
        r"backward.*compatibility",
        r"existing.*system"
    ],
    "future_extensibility": [
        r"future.*extensibility",
        r"extensibility",
        r"future.*proof",
        r"future.*compatibility"
    ]
}

def calculate_score(scores):
    """Calculate total score and category scores."""
    total_score = 0
    category_scores = {}
    
    for category, criteria in CRITERIA.items():
        category_score = 0
        for priority, items in criteria.items():
            for item, points in items.items():
                if item in scores and scores[item]:
                    category_score += points
        category_scores[category] = category_score
        total_score += category_score
    
    return total_score, category_scores

def get_relevance_level(total_score, category_scores):
    """Determine relevance level based on scores."""
    if total_score >= 36 and all(score >= 12 for score in category_scores.values()):
        return "Primary (Highly Relevant)"
    elif total_score >= 27 and all(score >= 9 for score in category_scores.values()):
        return "Secondary (Moderately Relevant)"
    elif total_score >= 18 and all(score >= 6 for score in category_scores.values()):
        return "Tertiary (Minimally Relevant)"
    else:
        return "Not Relevant"

def check_criterion(text, patterns):
    """Check if any pattern matches in the text."""
    text = text.lower()
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def review_paper(paper_path):
    """Review a single paper and return scores."""
    print(f"\nReviewing: {paper_path}")
    
    # Read paper content
    with open(paper_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Score each criterion
    scores = {}
    for criterion, patterns in KEYWORDS.items():
        scores[criterion] = check_criterion(content, patterns)
    
    return scores

def main():
    # Create output directory
    output_dir = Path("docs/4.2.1.1-paper-reviews")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Define paper directories
    directories = {
        "elicit": Path("sources/4.1-semantic-search/elicit-results/elicit-review-papers"),
        "semantic_scholar": Path("sources/4.1-semantic-search/semantic-scholar-search-iteration-1/semantic-scholar-review-papers")
    }
    
    # Review papers from each directory
    for source, papers_dir in directories.items():
        print(f"\n{'='*80}")
        print(f"Reviewing papers from {source}")
        print(f"{'='*80}")
        
        # Get list of markdown files
        markdown_files = list(papers_dir.glob("*.md"))
        
        # Review each paper
        reviews = {}
        for paper_path in markdown_files:
            print(f"\n{'='*80}")
            print(f"Reviewing paper {len(reviews) + 1} of {len(markdown_files)}")
            print(f"{'='*80}")
            
            scores = review_paper(paper_path)
            total_score, category_scores = calculate_score(scores)
            relevance_level = get_relevance_level(total_score, category_scores)
            
            reviews[paper_path.name] = {
                "scores": scores,
                "total_score": total_score,
                "category_scores": category_scores,
                "relevance_level": relevance_level,
                "review_date": datetime.now().isoformat()
            }
            
            # Save progress after each review
            with open(output_dir / f"{source}_paper_reviews.json", "w") as f:
                json.dump(reviews, f, indent=2)
            
            print(f"\nResults for {paper_path.name}:")
            print(f"Total Score: {total_score}/54")
            print(f"Category Scores: {category_scores}")
            print(f"Relevance Level: {relevance_level}")
        
        # Print summary for this source
        print(f"\n{'='*80}")
        print(f"Summary for {source}:")
        print(f"Total papers reviewed: {len(reviews)}")
        relevance_counts = {}
        for paper in reviews.values():
            level = paper["relevance_level"]
            relevance_counts[level] = relevance_counts.get(level, 0) + 1
        print("Relevance distribution:")
        for level, count in relevance_counts.items():
            print(f"- {level}: {count} papers")

if __name__ == "__main__":
    main() 
# Semantic Literature Search

This directory contains the implementation of our semantic literature search using both Elicit.com and Semantic Scholar API.

## Directory Structure

```
4.1-semantic-search/
├── primary/           # Primary search results
├── secondary/         # Secondary search results
├── tertiary/          # Tertiary search results
├── scripts/           # Python scripts
│   ├── 4.1.2_semantic_scholar_search.py
│   └── requirements.txt
└── README.md
```

## Setup Instructions

1. Install Python dependencies:
   ```bash
   cd scripts
   pip install -r requirements.txt
   ```

2. Get Semantic Scholar API key:
   - Visit https://www.semanticscholar.org/product/api
   - Sign up for an API key
   - Add the API key to the script (optional, but recommended for higher rate limits)

3. Run the search script:
   ```bash
   python 4.1.2_semantic_scholar_search.py
   ```

## Search Process

1. **Elicit.com Search**
   - Use the queries defined in `docs/4.1.1.1-elicit-search-strategy.md`
   - Document results in the respective directories
   - Export relevant papers

2. **Semantic Scholar Search**
   - Primary search: Focused on main research question
   - Secondary search: Supporting aspects and challenges
   - Tertiary search: Background and related topics

3. **Results Management**
   - Results are automatically saved in JSON format
   - Each search type has its own directory
   - Files are timestamped for tracking

## Search Queries

### Primary Query
```
How can Agent Communication Protocol (ACP) and Agent-to-Agent Protocol (A2A) 
be applied for secure, scalable, and interoperable communication in decentralized 
predictive maintenance coordination among multi-owner Distributed Energy Resources (DERs)?
```

### Secondary Queries
1. Protocol adaptation requirements and challenges
2. Security and scalability enhancements
3. Predictive maintenance approaches
4. Interoperability solutions
5. Performance evaluation metrics

### Tertiary Queries
1. DER maintenance coordination
2. ACP security
3. Predictive maintenance in energy
4. Multi-owner DER management
5. Protocol performance evaluation

## Next Steps

1. Review and screen search results
2. Extract relevant papers
3. Document findings
4. Prepare for detailed analysis 
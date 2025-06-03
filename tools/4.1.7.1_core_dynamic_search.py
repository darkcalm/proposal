# This file is being renamed to tools/4.1.7.1_core_dynamic_search.py
# The content will be moved to the new file.
# If this tool supports renaming, it should perform that. Otherwise, I'll handle it by creating a new file and deleting the old one.

#!/usr/bin/env python3

import requests
import json
import time
from pathlib import Path
import logging
from datetime import datetime
import os
import argparse
from typing import List, Dict, Any, Optional
from collections import Counter

# Basic list of English stopwords
STOPWORDS = set([
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being", 
    "have", "has", "had", "do", "does", "did", "will", "would", "should", "can", 
    "could", "may", "might", "must", "and", "but", "or", "nor", "for", "so", 
    "yet", "if", "then", "else", "when", "where", "why", "how", "what", "which", 
    "who", "whom", "whose", "this", "that", "these", "those", "am", 
    "i", "me", "my", "myself", "we", "us", "our", "ourselves", 
    "you", "your", "yourself", "yourselves", "he", "him", "his", "himself", 
    "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", 
    "their", "theirs", "themselves", "to", "of", "at", "by", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", 
    "here", "there", "all", "any", "both", "each", "few", "more", "most", 
    "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", 
    "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now",
    "abstract", "paper", "study", "research", "results", "method", "methods", "conclusion", "conclusions",
    "introduction", "discussion", "figure", "table", "chapter", "section", "references", "appendix",
    "doi", "org", "https", "http", "www", "com", "et", "al"
])

class CoreApiSearch:
    def __init__(
        self,
        api_key: Optional[str] = None,
        iteration: int = 1 # This might represent a "session" or major run, dynamic iterations will be internal
    ):
        self.iteration = iteration
        self.core_api_key = api_key # Store CORE API Key
        self.base_url = "https://api.core.ac.uk/v3" # Changed base URL
        
        # CORE API v3 uses apiKey as a query parameter, not typically in headers for search
        # Or, if it were a bearer token, it would be:
        # self.headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
        # For now, we'll add it to params in the request method.
        self.headers = {
            "Accept": "application/json" 
        }
        
        # Determine workspace root assuming script is in tools/
        self.workspace_root = Path(__file__).resolve().parent.parent

        # Adjusted for the new script's task number
        self.results_base_dir = self.workspace_root / "sources" / "4.1.7-core-dynamic-results"
        self.docs_base_dir = self.workspace_root / "docs"
        
        self.results_session_dir = self.results_base_dir / f"session-{self.iteration}"
        
        # Create directory structure for results
        self.results_session_dir.mkdir(parents=True, exist_ok=True)
        # Subdirs for raw search results from each dynamic step could be useful
        # e.g., self.results_session_dir / "dynamic_step_1" / "primary" / ...
        
        self.logs_dir = self.results_session_dir / 'logs'
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        # Ensure docs directory exists for summary
        self.docs_base_dir.mkdir(parents=True, exist_ok=True)
        
        self._setup_logging()
        self.relevance_criteria = None # Will be loaded in main after path resolution
        self.relevance_criteria_path_arg = "<REPLACE_WITH_ACTUAL_PATH_IN_MAIN>" # Will be updated in main

    def _load_relevance_criteria(self, criteria_file_path: Path):
        try:
            with open(criteria_file_path, 'r', encoding='utf-8') as f:
                criteria = json.load(f)
            logging.info(f"Successfully loaded relevance criteria from {criteria_file_path}")
            return criteria
        except FileNotFoundError:
            logging.error(f"FATAL: Relevance criteria file not found at {criteria_file_path}")
            raise
        except json.JSONDecodeError:
            logging.error(f"FATAL: Could not decode JSON from relevance criteria file {criteria_file_path}")
            raise

    def _setup_logging(self):
        logger = logging.getLogger()
        if logger.hasHandlers():
            logger.handlers.clear()
            
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        # Log for the current session
        session_log_file = self.logs_dir / f'search_log_session{self.iteration}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_handler = logging.FileHandler(session_log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        # General log for this script in tools/
        tools_log_dir = Path(__file__).resolve().parent 
        script_name = Path(__file__).stem
        script_log_file = tools_log_dir / f'{script_name}.log'
        tools_file_handler = logging.FileHandler(script_log_file) 
        tools_file_handler.setFormatter(formatter)
        logger.addHandler(tools_file_handler)

    # --- Helper for N-gram extraction ---
    def _extract_ngrams(self, text: str, n: int, stopwords: set) -> List[str]:
        if not text:
            return []
        words = [word.lower() for word in text.split() if word.isalnum() and word.lower() not in stopwords and len(word) > 2]
        ngrams = zip(*[words[i:] for i in range(n)])
        return [" ".join(ngram) for ngram in ngrams]

    # --- Scoring functions (to be adapted for CORE data) ---
    def _extract_text_from_core_paper(self, paper_data: Dict[str, Any]) -> str:
        """Extract title and abstract from CORE paper data for keyword matching."""
        title = paper_data.get('title', '') or ""
        abstract = paper_data.get('abstract', '') or ""
        # CORE doesn't have a direct 'tldr'. We can see if other fields like 'topics' or 'subjects' could be useful.
        # For now, just title and abstract.
        
        text_content = f"{title} {abstract}".lower()
        return text_content

    def _score_paper_fuzzy(self, paper_data: Dict[str, Any]) -> tuple[float, dict]:
        """Score a paper based on relevance criteria using keyword substring matching and CORE API metadata."""
        if not self.relevance_criteria:
            logging.error("Relevance criteria not loaded. Cannot score paper.")
            return 0.0, {}

        paper_score = 0.0
        dimension_scores = {}
        text_content = self._extract_text_from_core_paper(paper_data)

        # Use 'yearPublished' as the primary source for year.
        # It seems to be an integer directly from the sample logs.
        year = paper_data.get('yearPublished') 
        if year is None and paper_data.get('publishedDate'): 
            try:
                year = int(str(paper_data.get('publishedDate'))[:4])
            except (ValueError, TypeError):
                logging.warning(f"Could not parse year from publishedDate '{paper_data.get('publishedDate')}' for paper {paper_data.get('id', paper_data.get('doi'))}")
                year = None # Ensure year is None if parsing fails

        # CORE API's citationCount seems to be 0 often. 
        # For now, we will use it but be aware it might not be reliable.
        # If consistently an issue, this subcriterion might need to be removed or its weight reduced significantly.
        # TEMPORARILY DISABLING citation_count contribution for scoring due to unreliability.
        citation_count_original = paper_data.get('citationCount') 
        citation_count = 0 # Default to 0 for scoring logic to effectively disable it
        # if citation_count_original is None:
        #     citation_count = 0 
        # else:
        #     try:
        #         citation_count = int(citation_count_original)
        #     except (ValueError, TypeError):
        #         logging.warning(f\"Could not parse citationCount '{citation_count_original}' as int for paper {paper_data.get('id')}, using 0.\")
        #         citation_count = 0

        for dim_key, dimension in self.relevance_criteria.get('relevance_dimensions', {}).items():
            dim_score = 0.0 # Initialize as float
            dim_weight = dimension.get('weight', 0.0) # Ensure float
            matched_keywords_in_dim = {}

            if 'subcriteria' in dimension:
                for sub_key, subcrit in dimension['subcriteria'].items():
                    sub_item_score = 0.0 # Initialize as float
                    sub_weight = subcrit.get('weight', 0.0) # Ensure float
                    keywords = subcrit.get('keywords', [])
                    
                    if sub_key == 'publication_year' and year is not None:
                        year_score_value = 0.0
                        year_scoring_rules = subcrit.get('scoring', {})
                        # Ensure year is int for comparison
                        try:
                            year_int = int(year)
                            if year_int >= 2023: year_score_value = float(year_scoring_rules.get("2023-2024", 1.0))
                            elif year_int >= 2021: year_score_value = float(year_scoring_rules.get("2021-2022", 0.8))
                            elif year_int >= 2019: year_score_value = float(year_scoring_rules.get("2019-2020", 0.6))
                            elif year_int == 2018: year_score_value = float(year_scoring_rules.get("2018", 0.4))
                            elif year_int >= 2015: year_score_value = float(year_scoring_rules.get("2015-2017", 0.2))
                            else: year_score_value = float(year_scoring_rules.get("before_2015", 0.1))
                        except ValueError:
                             logging.warning(f"Could not parse year '{year}' as int for paper {paper_data.get('id', paper_data.get('doi'))}")
                        sub_item_score = year_score_value * sub_weight
                        if year_score_value > 0:
                            matched_keywords_in_dim[sub_key] = [f"Year: {year} (Norm. Score: {year_score_value})"]
                    
                    elif sub_key == 'citation_count':
                        # This sub-criterion is temporarily disabled by setting citation_count to 0 above.
                        # If we re-enable, the logic below would apply.
                        citation_score_value = 0.0
                        if citation_count > 0: # Only apply if we have a valid count and choose to use it
                            citation_thresholds = subcrit.get('thresholds', {}) 
                            cit_scoring = subcrit.get('scoring', {"high": 1.0, "medium": 0.6, "low": 0.2})
                            raw_high_thresh = citation_thresholds.get('high', 100)
                            raw_medium_thresh = citation_thresholds.get('medium', 20)
                            try:
                                cit_high_thresh = int(''.join(filter(str.isdigit, str(raw_high_thresh).split('-')[0])))
                            except ValueError:
                                cit_high_thresh = 100
                            try:
                                cit_medium_thresh = int(''.join(filter(str.isdigit, str(raw_medium_thresh).split('-')[0])))
                            except ValueError:
                                cit_medium_thresh = 20

                            if citation_count >= cit_high_thresh: citation_score_value = float(cit_scoring.get('high', 1.0))
                            elif citation_count >= cit_medium_thresh: citation_score_value = float(cit_scoring.get('medium', 0.6))
                            else: citation_score_value = float(cit_scoring.get('low', 0.2))
                        
                        sub_item_score = citation_score_value * sub_weight
                        if citation_score_value > 0:
                             matched_keywords_in_dim[sub_key] = [f"Citations: {citation_count_original} (Norm. Score: {citation_score_value})"] # Log original if available

                    elif sub_key == 'venue_quality':
                        # Simplified: actual venue quality requires external data/APIs
                        # Default placeholder score, can be overridden by criteria definition
                        venue_score_value = float(subcrit.get('default_score', 0.5)) 
                        sub_item_score = venue_score_value * sub_weight
                        if venue_score_value > 0:
                            matched_keywords_in_dim[sub_key] = [f"Assumed Venue Quality (Norm. Score: {venue_score_value})"]
                    
                    else: # Keyword-based subcriteria
                        matched_this_sub = False
                        current_matched_for_sub_list = [] # Renamed to avoid confusion
                        for kw in keywords:
                            if kw.lower() in text_content: # Substring matching
                                matched_this_sub = True
                                current_matched_for_sub_list.append(kw)
                        
                        if matched_this_sub:
                            # Score for subcriterion is 1.0 if any keyword hits, then weighted
                            sub_item_score = 1.0 * sub_weight 
                            matched_keywords_in_dim[sub_key] = list(set(current_matched_for_sub_list))
                    
                    dim_score += sub_item_score 
            
            dimension_scores[dim_key] = {
                "score_sum_sub_weighted": round(dim_score, 4), # This is sum of (sub_item_score_normalized * sub_weight)
                "dimension_weight": dim_weight, 
                "weighted_score": round(dim_score * dim_weight, 4), # Final weighted score for this dimension
                "matched_keywords_detail": matched_keywords_in_dim
            }
            paper_score += dim_score * dim_weight 
            
        return round(paper_score, 4), dimension_scores
    # --- End of scoring functions ---

    def search_papers_once(
        self,
        query: str,
        search_identifier: str,
        dynamic_step: int,
        limit: int = 100, # This is pageSize for CORE
        year_range: Optional[tuple[Optional[int], Optional[int]]] = None,
        max_total_papers_per_query: int = 200 # Max papers to fetch via pagination for a single query
    ) -> List[Dict[str, Any]]:
        search_url = f"{self.base_url}/search/works"
        all_papers_for_this_query = []
        current_page = 1
        papers_retrieved_count = 0

        query_with_filters = query
        if year_range:
            year_filters = []
            if year_range[0] is not None:
                year_filters.append(f"yearPublished:>={year_range[0]}")
            if year_range[1] is not None:
                year_filters.append(f"yearPublished:<={year_range[1]}")
            if year_filters:
                query_with_filters += " AND " + " AND ".join(year_filters)

        while True:
            params: Dict[str, Any] = {
                "q": query_with_filters,
                "pageSize": limit, # CORE uses pageSize
                "page": current_page,
                "apiKey": self.core_api_key
            }

            try:
                logging.info(f"Step {dynamic_step} - Query '{search_identifier}' (Page {current_page}): '{params['q'][:100]}...' with pageSize {limit}")
                response = requests.get(
                    search_url,
                    headers=self.headers,
                    params=params,
                    timeout=30 # Corrected timeout back to 30 seconds
                )
                time.sleep(3) # Reverted cool-off to 3 seconds
                response.raise_for_status()
                results_data = response.json()

                papers_found_raw_this_page = results_data.get('results', [])
                if not papers_found_raw_this_page and current_page == 1: # No results at all on first page
                    logging.warning(f"No papers found for query: {params['q']}")
                    break # Exit while loop for this query
                
                if papers_found_raw_this_page and current_page == 1: # Log structure only for the first paper of the first page
                    logging.info(f"Structure of the first paper object (keys): {list(papers_found_raw_this_page[0].keys())}")
                    try:
                        first_paper_sample_json = json.dumps(papers_found_raw_this_page[0], indent=2)
                        if len(first_paper_sample_json) < 2000: 
                            logging.info(f"First paper object sample:\\n{first_paper_sample_json}")
                        else:
                            logging.info(f"First paper object sample is too large to log directly (Length: {len(first_paper_sample_json)}). Logging only a few key fields.")
                            first_paper_sample_subset = {
                                "id": papers_found_raw_this_page[0].get("id"),
                                "doi": papers_found_raw_this_page[0].get("doi"),
                                "title": papers_found_raw_this_page[0].get("title"),
                                "abstract": papers_found_raw_this_page[0].get("abstract")[:200] + "..." if papers_found_raw_this_page[0].get("abstract") else None,
                                "yearPublished": papers_found_raw_this_page[0].get("yearPublished"),
                                "publishedDate": papers_found_raw_this_page[0].get("publishedDate"),
                                "citationCount": papers_found_raw_this_page[0].get("citationCount"),
                                "downloadUrl": papers_found_raw_this_page[0].get("downloadUrl"),
                                "journals": papers_found_raw_this_page[0].get("journals"),
                                "authors": papers_found_raw_this_page[0].get("authors")[:1]
                            }
                            logging.info(f"First paper sample (subset of fields):\\n{json.dumps(first_paper_sample_subset, indent=2)}")
                    except Exception as log_ex:
                        logging.warning(f"Could not serialize first paper for logging: {log_ex}")
                
                processed_papers_for_saving_this_page = []
                for paper_raw in papers_found_raw_this_page:
                    lang_obj = paper_raw.get("language")
                    language_name = None
                    if isinstance(lang_obj, dict):
                        language_name = lang_obj.get("name")
                    elif isinstance(lang_obj, str):
                        language_name = lang_obj
                    doc_type_obj = paper_raw.get("documentType")
                    doc_type_name = None
                    if isinstance(doc_type_obj, dict):
                        doc_type_name = doc_type_obj.get("name")
                    elif isinstance(doc_type_obj, str):
                        doc_type_name = doc_type_obj
                    paper_to_save = {
                        "id": paper_raw.get("id"), "doi": paper_raw.get("doi"),
                        "title": paper_raw.get("title"), "abstract": paper_raw.get("abstract"),
                        "yearPublished": paper_raw.get("yearPublished"), "publishedDate": paper_raw.get("publishedDate"),
                        "authors": paper_raw.get("authors"), "citationCount": paper_raw.get("citationCount"),
                        "downloadUrl": paper_raw.get("downloadUrl"), "publisher": paper_raw.get("publisher"),
                        "journals": paper_raw.get("journals"), "language": language_name,
                        "documentType": doc_type_name, "topics": paper_raw.get("topics")
                    }
                    processed_papers_for_saving_this_page.append(paper_to_save)
                
                all_papers_for_this_query.extend(processed_papers_for_saving_this_page)
                papers_retrieved_count += len(processed_papers_for_saving_this_page)

                total_hits = results_data.get('totalHits', 0)
                logging.info(f"Page {current_page}: Retrieved {len(processed_papers_for_saving_this_page)} papers. Total for query so far: {papers_retrieved_count}/{total_hits}")

                # Check if we should stop paginating
                if not papers_found_raw_this_page or papers_retrieved_count >= total_hits or papers_retrieved_count >= max_total_papers_per_query:
                    break # Exit while loop

                current_page += 1
                if current_page > 10 and max_total_papers_per_query > 100 : # Safety break for very large result sets if max_total_papers_per_query is also large
                     logging.warning(f"Stopping pagination for query '{search_identifier}' after 10 pages to prevent excessive calls. Consider adjusting max_total_papers_per_query or query specificity.")
                     break

            except requests.exceptions.Timeout:
                logging.error(f"Timeout on page {current_page} for query '{search_identifier}': '{params['q']}'")
                break # Stop processing this query on timeout
            except requests.exceptions.RequestException as e:
                logging.error(f"Error on page {current_page} for query '{search_identifier}': '{params['q']}': {e}")
                if hasattr(e, 'response') and e.response is not None:
                    logging.error(f"Response content: {e.response.text}")
                break # Stop processing this query on error
            except json.JSONDecodeError as e:
                response_text = "N/A (response object not available)"
                if 'response' in locals() and hasattr(response, 'text'): response_text = response.text
                logging.error(f"Error decoding JSON (Page {current_page}) for query '{search_identifier}': '{params['q']}': {e}")
                logging.error(f"Response content: {response_text}")
                break # Stop processing this query

        # After loop (or break), save all collected papers for this query identifier
        if all_papers_for_this_query:
            output_payload_to_save = {
                "totalHitsEncounteredAcrossPages": total_hits if 'total_hits' in locals() else papers_retrieved_count, # Store last known total_hits
                "retrievedCountForThisQuery": papers_retrieved_count,
                "searchIdentifier": search_identifier,
                "originalQuery": query_with_filters, # Log the actual query sent
                "results": all_papers_for_this_query
            }
            step_results_dir = self.results_session_dir / f"dynamic_step_{dynamic_step}"
            step_results_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = step_results_dir / f"{search_identifier}_results_{timestamp}.json"
            with open(output_file, 'w') as f:
                json.dump(output_payload_to_save, f, indent=2)
            logging.info(f"Saved {papers_retrieved_count} papers for query '{search_identifier}' to {output_file.relative_to(self.workspace_root)}")
        
        return all_papers_for_this_query

    def _generate_queries_from_relevant_papers(
        self, 
        relevant_papers: List[Dict[str, Any]], 
        query_id_to_text_map: Dict[str, str], # Map of all executed query IDs to their text
        max_new_queries: int = 5
        # min_relevance_for_analysis is part of the selection for relevant_papers already
        ) -> List[str]:
        """Generate new queries based on keywords and N-grams from relevant papers and their parent queries."""
        new_queries_to_run: List[str] = []
        
        # Store tuples: (term, term_type, parent_query_text) where term_type is 'keyword', 'bigram', 'trigram'
        all_terms_with_parent_query = [] 

        if not relevant_papers:
            logging.info("No relevant papers provided to generate new queries.")
            return []

        for paper_wrapper in relevant_papers:
            paper_data = paper_wrapper.get('original_data', {})
            parent_query_id = paper_wrapper.get('source_query_id')
            parent_query_text = query_id_to_text_map.get(parent_query_id)

            if not parent_query_text:
                logging.warning(f"Could not find parent query text for ID '{parent_query_id}'. Skipping paper for query gen.")
                continue

            text_content = self._extract_text_from_core_paper(paper_data)
            
            # Extract single keywords
            words = text_content.lower().split() 
            filtered_keywords = [word for word in words if word.isalnum() and word not in STOPWORDS and len(word) > 3]
            for keyword in filtered_keywords:
                all_terms_with_parent_query.append((keyword, "keyword", parent_query_text))

            # Extract bigrams
            bigrams = self._extract_ngrams(text_content, 2, STOPWORDS)
            for bigram in bigrams:
                all_terms_with_parent_query.append((bigram, "bigram", parent_query_text))

            # Extract trigrams
            trigrams = self._extract_ngrams(text_content, 3, STOPWORDS)
            for trigram in trigrams:
                all_terms_with_parent_query.append((trigram, "trigram", parent_query_text))
            
        if not all_terms_with_parent_query:
            logging.info("No keywords or N-grams extracted from relevant papers to generate new queries.")
            return []

        # Group terms by their parent query context
        parent_query_to_terms: Dict[str, Dict[str, List[str]]] = {} # parent_q_text -> {term_type: [terms]}
        for term, term_type, pq_text in all_terms_with_parent_query:
            if pq_text not in parent_query_to_terms:
                parent_query_to_terms[pq_text] = {"keyword": [], "bigram": [], "trigram": []}
            parent_query_to_terms[pq_text][term_type].append(term)

        # Keep track of generated/existing queries to avoid duplicates
        # existing_query_texts should be derived from query_id_to_text_map.values() before calling this function
        generated_query_texts = set(query_id_to_text_map.values()) 

        # Strategy: Combine parent query with top terms (keywords or N-grams) found within its children
        for parent_q_text, terms_from_children_typed in parent_query_to_terms.items():
            if len(new_queries_to_run) >= max_new_queries: break
            
            combined_child_terms = []
            for term_type, term_list in terms_from_children_typed.items():
                if term_list:
                    combined_child_terms.extend(term_list)
            
            if not combined_child_terms: continue

            term_counts = Counter(combined_child_terms)
            # Prioritize longer N-grams if counts are similar, or just take most common
            # For simplicity, let's take top 3 overall terms (keyword or N-gram) from this parent's children
            top_child_terms_for_parent = [term for term, count in term_counts.most_common(3)] 

            if top_child_terms_for_parent:
                meaningful_new_terms = []
                for term in top_child_terms_for_parent:
                    # Check if term (as a whole phrase) is already in parent query
                    if f'"{term}"'.lower() not in parent_q_text.lower() and term.lower() not in parent_q_text.lower():
                        meaningful_new_terms.append(term)
                
                if meaningful_new_terms:
                    # Construct OR part: "term1" OR "term2"
                    or_part = " OR ".join([f'"{t}"' for t in meaningful_new_terms])
                    potential_new_query = f"({parent_q_text}) AND ({or_part})"
                    
                    if potential_new_query not in generated_query_texts:
                        new_queries_to_run.append(potential_new_query)
                        generated_query_texts.add(potential_new_query)
                        logging.info(f"Generated new query (from parent '{parent_q_text[:50]}...'): {potential_new_query}")
        
        # Fallback Strategy: If not enough queries, use overall top N-grams/keywords
        # This is a simplified fallback, could be made more sophisticated
        if len(new_queries_to_run) < max_new_queries:
            overall_term_counts = Counter(term for term, term_type, pq_text in all_terms_with_parent_query)
            # Get more to pick from, favoring N-grams if possible
            top_overall_terms = [term for term, count in overall_term_counts.most_common(max_new_queries * 2)]

            idx = 0
            while len(new_queries_to_run) < max_new_queries and idx < len(top_overall_terms):
                term_to_try = top_overall_terms[idx]
                idx += 1

                # Try to combine with a base query (e.g., one of the initial primary queries)
                # This needs a more robust way to select a "base" or "seed" query.
                # For now, pick the first initial primary query if available.
                base_query_text = None
                for qid, qtext in query_id_to_text_map.items():
                    if qid.startswith("initial_primary"):
                        base_query_text = qtext
                        break
                
                if not base_query_text and query_id_to_text_map: # Fallback to any query text
                    base_query_text = next(iter(query_id_to_text_map.values()))

                if base_query_text:
                    if f'"{term_to_try}"'.lower() not in base_query_text.lower() and term_to_try.lower() not in base_query_text.lower():
                        potential_new_query = f'({base_query_text}) AND "{term_to_try}"'
                        if potential_new_query not in generated_query_texts:
                            new_queries_to_run.append(potential_new_query)
                            generated_query_texts.add(potential_new_query)
                            logging.info(f"Generated new query (fallback strategy with base '{base_query_text[:30]}...'): {potential_new_query}")
                else: # Absolute fallback: just the term itself (less ideal for complex topics)
                    potential_new_query = f'"{term_to_try}"'
                    if potential_new_query not in generated_query_texts:
                        new_queries_to_run.append(potential_new_query)
                        generated_query_texts.add(potential_new_query)
                        logging.info(f"Generated new query (absolute fallback): {potential_new_query}")


        logging.info(f"Generated {len(new_queries_to_run)} new queries for the next step.")
        return new_queries_to_run

    def dynamic_search_orchestrator(
        self,
        initial_query_dict: Dict[str, List[str]],
        num_dynamic_iterations: int = 2,
        papers_per_query_limit: int = 20,
        relevance_threshold_for_analysis: float = 0.5,
        max_new_queries_per_step: int = 3,
        year_range: Optional[tuple[Optional[int], Optional[int]]] = None,
        max_total_papers_to_fetch_per_query: int = 200,
        test_mode_limit_initial_queries: Optional[int] = None # For limiting initial queries in testing
    ):
        logging.info(f"Starting CORE API dynamic search: {num_dynamic_iterations} iterations, score threshold {relevance_threshold_for_analysis}")
        
        all_papers_scored_unique: Dict[str, Dict[str, Any]] = {} 
        executed_queries_by_step: Dict[int, List[Dict[str, str]]] = {} # step_num -> list of {id, text}
        query_id_to_text_map: Dict[str, str] = {} # New: Map of all query IDs to their text

        current_queries: List[Dict[str, str]] = []
        query_type_counters = {"primary": 0, "secondary": 0, "tertiary": 0, "dynamic":0}

        # Prepare initial queries
        initial_query_count = 0
        for q_type, queries in initial_query_dict.items():
            if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries:
                logging.info(f"Reached test_mode_limit_initial_queries ({test_mode_limit_initial_queries}), stopping addition of initial queries.")
                break
            for query_text in queries:
                if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries:
                    break
                query_id = f"initial_{q_type}_{query_type_counters[q_type]}"
                current_queries.append({"id": query_id, "text": query_text})
                query_id_to_text_map[query_id] = query_text # Populate map
                query_type_counters[q_type] += 1
                initial_query_count +=1
            if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries:
                break
        
        logging.info(f"Prepared {len(current_queries)} initial queries to run (test_mode_limit: {test_mode_limit_initial_queries}).")

        for dynamic_step in range(num_dynamic_iterations + 1): # +1 to include initial run (step 0)
            logging.info(f"--- Dynamic Search Step {dynamic_step} ---")
            if not current_queries:
                logging.info(f"No queries to run in dynamic step {dynamic_step}. Stopping.")
                break

            papers_from_this_step_scored = []
            
            # Use a temporary list for queries for this step to avoid modifying while iterating
            queries_for_this_step = list(current_queries) 
            current_queries = [] # Reset for next iteration's generated queries

            for query_obj in queries_for_this_step:
                query_text = query_obj["text"]
                query_id = query_obj["id"]
                
                raw_papers = self.search_papers_once(
                    query=query_text,
                    search_identifier=query_id,
                    dynamic_step=dynamic_step,
                    limit=papers_per_query_limit,
                    year_range=year_range,
                    max_total_papers_per_query=max_total_papers_to_fetch_per_query
                )

                for paper_data in raw_papers: # paper_data is now a CORE "work" object
                    # CORE ID: 'id' (integer) or 'doi' (string) are good candidates
                    core_paper_id_int = paper_data.get('id')
                    doi = paper_data.get('doi')
                    
                    unique_id_for_paper = doi if doi else str(core_paper_id_int) # Prefer DOI if available

                    if not unique_id_for_paper:
                        logging.warning(f"Skipping paper without a usable ID (DOI or CORE ID): {paper_data.get('title', '[Untitled]')}")
                        continue

                    score, dim_scores = self._score_paper_fuzzy(paper_data)
                    
                    scored_paper_wrapper = {
                        "original_data": paper_data,
                        "relevance_score": score,
                        "dimension_scores": dim_scores,
                        "source_query_id": query_id,
                        "dynamic_step": dynamic_step,
                        "core_id": core_paper_id_int, # Store for reference
                        "doi": doi # Store for reference
                    }
                    papers_from_this_step_scored.append(scored_paper_wrapper)

                    if unique_id_for_paper not in all_papers_scored_unique or score > all_papers_scored_unique[unique_id_for_paper].get("relevance_score", 0):
                        all_papers_scored_unique[unique_id_for_paper] = scored_paper_wrapper
            
            logging.info(f"Step {dynamic_step} found {len(papers_from_this_step_scored)} papers (before unique check with overall list).")
            logging.info(f"Total unique papers after step {dynamic_step}: {len(all_papers_scored_unique)}")

            if dynamic_step < num_dynamic_iterations: # Don't generate queries after last iteration
                relevant_for_next_step = [p for p in papers_from_this_step_scored if p['relevance_score'] >= relevance_threshold_for_analysis]
                logging.info(f"Found {len(relevant_for_next_step)} papers from step {dynamic_step} meeting threshold {relevance_threshold_for_analysis} for new query generation.")
                
                # Collect all query texts executed so far to avoid duplicates
                # This is now handled by passing query_id_to_text_map to _generate_queries_from_relevant_papers
                # and checking against generated_query_texts set within that function.

                new_query_strings = self._generate_queries_from_relevant_papers(
                    relevant_papers=relevant_for_next_step,
                    query_id_to_text_map=query_id_to_text_map, # Pass the map
                    max_new_queries=max_new_queries_per_step
                )
                
                query_idx = 0
                for q_text in new_query_strings:
                    # Check if this exact query text has been run before in any step to avoid loops (simple check)
                    # A more robust check would involve semantic similarity or normalized query strings
                    is_repeated = False
                    for step_info_dir in (self.results_session_dir).iterdir():
                        if step_info_dir.is_dir() and step_info_dir.name.startswith("dynamic_step_"):
                            for result_file in step_info_dir.glob("*.json"):
                                if q_text in result_file.name: # Very rough check
                                     # A better check would be to store all executed query strings
                                     pass # Needs better tracking of executed queries
                    
                    new_query_id = f"dynamic_s{dynamic_step+1}_g{query_idx}" # g for generated
                    current_queries.append({
                        "text": q_text,
                        "id": new_query_id,
                        "type": "generated"
                    })
                    query_id_to_text_map[new_query_id] = q_text # Add newly generated query to map
                    query_idx += 1
                logging.info(f"Generated {len(current_queries)} new queries for step {dynamic_step + 1}.")

        # Consolidate and save all unique papers
        final_results_list = list(all_papers_scored_unique.values())
        self._save_consolidated_results(final_results_list, "dynamic_search_complete")
        self._generate_markdown_summary(final_results_list, "dynamic_search_complete", num_dynamic_iterations)
        
        logging.info(f"CORE API Dynamic search completed. Found {len(final_results_list)} unique papers.")
        return all_papers_scored_unique


    def _save_consolidated_results(self, papers_list: List[Dict[str,Any]], stage_name: str):
        output_data = {
            "metadata": {
                "session_id": self.iteration, # Using "iteration" from constructor as session_id
                "timestamp": datetime.now().isoformat(),
                "script_used": f"tools/{Path(__file__).name}",
                "stage": stage_name,
                "relevance_criteria_source": str(self.relevance_criteria_path_arg)
            },
            "summary": {
                "total_unique_papers_retrieved": len(papers_list),
            },
            "papers": papers_list
        }
        
        # Save consolidated JSON results
        json_output_file = self.results_session_dir / f"consolidated_{stage_name}_session{self.iteration}.json"
        with open(json_output_file, 'w') as f:
            json.dump(output_data, f, indent=2)
        logging.info(f"Consolidated JSON results for stage '{stage_name}' saved to {json_output_file.relative_to(self.workspace_root)}")

    def _generate_markdown_summary(self, papers_list: List[Dict[str,Any]], stage_name: str, num_dynamic_iters_run: int):
        # Generate summary report in Markdown
        md_summary_file_path = self.docs_base_dir / f"4.1.7.1-core-dynamic-summary-session-{self.iteration}.md" # Updated name
        
        json_output_file = self.results_session_dir / f"consolidated_{stage_name}_session{self.iteration}.json"
        json_results_md_path = json_output_file.relative_to(self.workspace_root)

        # Calculate some stats for the summary
        total_papers = len(papers_list)
        
        # Score distribution (example)
        # This can be made more sophisticated if needed
        above_0_5_count = sum(1 for p in papers_list if p.get('relevance_score', 0) >= 0.5)
        above_0_3_count = sum(1 for p in papers_list if p.get('relevance_score', 0) >= 0.3)


        with open(md_summary_file_path, 'w') as f:
            f.write(f"# CORE API Dynamic Search Summary - Session {self.iteration}\n\n")
            f.write(f"**Completion Timestamp:** {datetime.now().isoformat()}\n")
            f.write(f"**Script Used:** `tools/{Path(__file__).name}`\n")
            f.write(f"**Relevance Criteria Used:** `{self.relevance_criteria_path_arg}`\n")
            f.write(f"**Number of Dynamic Iterations Configured (excluding initial):** {num_dynamic_iters_run}\n") # Or actual if stopped early
            f.write(f"**Raw Consolidated JSON Results:** `{json_results_md_path}`\n")
            f.write(f"**Individual query JSON files located in:** `{self.results_session_dir.relative_to(self.workspace_root)}/dynamic_step_*/`\n\n")
            
            f.write(f"## Overall Summary of Results\n\n")
            f.write(f"- **Total unique papers retrieved:** {total_papers}\n")
            f.write(f"- **Papers with relevance score >= 0.5:** {above_0_5_count}\n")
            f.write(f"- **Papers with relevance score >= 0.3:** {above_0_3_count}\n")
            
            # Could add more details about queries run in each step if logged appropriately
            f.write("\n## Notes\n\n")
            f.write("This summary provides an overview of the papers retrieved using the dynamic CORE API search. "
                    "The search process involved one or more dynamic iterations where queries were refined based on the relevance of papers found in previous steps. "
                    "For detailed information, refer to the consolidated JSON results file and individual query JSON files linked above.\n")

        logging.info(f"Markdown summary report saved to {md_summary_file_path.relative_to(self.workspace_root)}")


# Placeholder for the old main function, to be replaced by dynamic search logic
def main():
    parser = argparse.ArgumentParser(description="Run a dynamic CORE API search session.")
    parser.add_argument(
        "--session_id",
        type=int, 
        default=1, 
        help="Search session ID. Determines output subdirectories. Default: 1"
    )
    parser.add_argument(
        "--relevance_criteria_path",
        type=str,
        default=None, # Default to None, handle path construction below
        help="Path to the relevance criteria JSON file. Relative to workspace root or absolute."
    )
    parser.add_argument(
        "--dynamic_iterations", type=int, default=2, help="Number of dynamic query refinement iterations. Default: 2"
    )
    parser.add_argument(
        "--papers_per_query", type=int, default=20, help="Max papers to fetch per individual query. Default: 20"
    )
    parser.add_argument(
        "--relevance_threshold", 
        type=float, 
        default=0.5, 
        help="Minimum relevance score for a paper to be considered for query generation. Default: 0.5"
    )
    parser.add_argument(
        "--max_new_queries", 
        type=int, 
        default=3, 
        help="Maximum new queries to generate per dynamic step. Default: 3"
    )
    parser.add_argument(
        "--max_papers_per_query_run", 
        type=int, 
        default=200, 
        help="Maximum total papers to fetch via pagination for any single query. Default: 200"
    )
    parser.add_argument(
        "--test_limit_initial_queries", # Argument for CLI testing
        type=int, 
        default=None, 
        help="For testing: limit the number of initial queries run from the config. Default: None (all)"
    )
    parser.add_argument(
        "--start_year",
        type=int,
        default=None,
        help="Filter papers published from this year."
    )
    parser.add_argument(
        "--end_year",
        type=int,
        default=None,
        help="Filter papers published up to this year."
    )

    args = parser.parse_args()

    session_id = args.session_id
    
    # Construct the default path for relevance criteria if not provided
    default_criteria_path = Path(__file__).resolve().parent.parent / "sources" / "4.1.3-relevance-criteria" / "relevance_criteria.json"
    
    # Determine the final path for relevance criteria
    if args.relevance_criteria_path:
        # If path is absolute, Path() handles it. If relative, it's from cwd.
        # Assuming relative paths are given from workspace root for consistency.
        # Path.resolve() might be too aggressive if an absolute path is already given.
        # Let's ensure it's relative to workspace if not absolute.
        temp_path = Path(args.relevance_criteria_path)
        if not temp_path.is_absolute():
            final_criteria_path = Path(__file__).resolve().parent.parent / temp_path
        else:
            final_criteria_path = temp_path
    else:
        final_criteria_path = default_criteria_path

    # API Key for CORE
    core_api_key_env = os.getenv("CORE_API_KEY") 
    # User provided key takes precedence if script arg is added in future, for now, env var
    # For this run, we will use the one hardcoded if env var is not set, for immediate testing
    # This is not best practice for production but useful for this interactive session.
    
    provided_api_key = "FeJVa6KG3ISf8iqN7sZw9RCHBgQPTxW2" # Key from user

    final_api_key_to_use = core_api_key_env if core_api_key_env else provided_api_key

    if not final_api_key_to_use:
        logging.error("FATAL: CORE_API_KEY environment variable not set and no fallback provided. Exiting.")
        # In a real script, might exit here or raise error
        # For now, rely on the hardcoded one above if env is missing.
        # The line below will use the hardcoded `provided_api_key` if `core_api_key_env` is None.
        # This means if CORE_API_KEY is not set, it uses the one from the prompt.
    elif not core_api_key_env and provided_api_key:
        logging.warning(f"Using provided API key for CORE as CORE_API_KEY env var is not set.")
    elif core_api_key_env:
        logging.info(f"Using CORE_API_KEY from environment variable.")


    searcher = CoreApiSearch( # Use new class
        api_key=final_api_key_to_use, # Pass the determined API key
        iteration=session_id 
    )
    searcher.relevance_criteria_path_arg = str(final_criteria_path.relative_to(searcher.workspace_root))
    searcher.relevance_criteria = searcher._load_relevance_criteria(final_criteria_path) 
    
    logging.info(f"CORE API Dynamic Search Script - Session {session_id}") # Updated log
    if not final_api_key_to_use: # Should not happen with fallback
         logging.critical("CRITICAL: Running without CORE API key - this will likely fail.")


    initial_queries_config = {
        "primary": [
            "Human operator challenges AND communication gaps in Distributed Energy Resource (DER) operations",
            "Human oversight AND operator decision support systems for decentralized energy resource management",
            "AI agent protocols improving manual processes AND human-machine teaming in DER systems",
            "Workflow optimization AND human factors in decentralized energy operations",
            "Addressing communication inefficiencies with AI agent assistance in decentralized energy (DER) operator tasks"
        ],
        "secondary": [
            "Human factors in decentralized energy resource (DER) lifecycle management",
            "Operator communication tools AND protocols for DER coordination",
            "AI agent applications supporting human operators in decentralized energy systems"
        ],
        "tertiary": [
            "Operator decision-making tools for decentralized energy systems",
            "Manual task automation AND augmentation in DER lifecycle (installation, maintenance, operation)",
            "Human intervention strategies for DER fault diagnosis AND system recovery"
        ]
    }
    
    papers_per_query_limit_arg = args.papers_per_query
    relevance_threshold_arg = args.relevance_threshold
    max_new_queries_arg = args.max_new_queries
    max_papers_to_fetch_per_query_arg = args.max_papers_per_query_run
    test_limit_initial_queries_arg = args.test_limit_initial_queries # Get from args

    year_filter = None
    if args.start_year or args.end_year:
        year_filter = (args.start_year, args.end_year)


    searcher.dynamic_search_orchestrator(
        initial_query_dict=initial_queries_config,
        num_dynamic_iterations=args.dynamic_iterations,
        papers_per_query_limit=papers_per_query_limit_arg,
        relevance_threshold_for_analysis=relevance_threshold_arg,
        max_new_queries_per_step=max_new_queries_arg,
        year_range=year_filter,
        max_total_papers_to_fetch_per_query=max_papers_to_fetch_per_query_arg,
        test_mode_limit_initial_queries=test_limit_initial_queries_arg # Pass to orchestrator
    )

if __name__ == "__main__":
    main() 
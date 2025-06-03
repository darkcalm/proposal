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
    "doi", "org", "https", "http", "www", "com", "et", "al",
    # Industry specific stopwords might be added here if needed, e.g. "company", "inc", "llc"
])

class IndustryCoreSearch: # MODIFIED CLASS NAME
    def __init__(
        self,
        api_key: Optional[str] = None,
        iteration: int = 1 
    ):
        self.iteration = iteration
        self.core_api_key = api_key 
        self.base_url = "https://api.core.ac.uk/v3" 
        self.headers = {
            "Accept": "application/json" 
        }
        
        self.workspace_root = Path(__file__).resolve().parent.parent

        # MODIFIED results base directory
        self.results_base_dir = self.workspace_root / "sources" / "4.1.8-industry-search-results"
        self.docs_base_dir = self.workspace_root / "docs" # Summary doc location remains same
        
        self.results_session_dir = self.results_base_dir / f"session-{self.iteration}"
        
        self.results_session_dir.mkdir(parents=True, exist_ok=True)
        
        self.logs_dir = self.results_session_dir / 'logs'
        self.logs_dir.mkdir(parents=True, exist_ok=True)

        self.docs_base_dir.mkdir(parents=True, exist_ok=True)
        
        self._setup_logging()
        self.relevance_criteria = None 
        self.relevance_criteria_path_arg = "<REPLACE_WITH_ACTUAL_PATH_IN_MAIN>"

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

    def _setup_logging(self): # MODIFIED logging setup
        logger = logging.getLogger()
        if logger.hasHandlers():
            logger.handlers.clear()
            
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
        
        session_log_file = self.logs_dir / f'industry_search_log_session{self.iteration}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
        file_handler = logging.FileHandler(session_log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
        tools_log_dir = Path(__file__).resolve().parent 
        script_name = Path(__file__).stem # Will be 4.1.8.4_industry_dynamic_search
        script_log_file = tools_log_dir / f'{script_name}.log' # General log for this specific script
        tools_file_handler = logging.FileHandler(script_log_file) 
        tools_file_handler.setFormatter(formatter)
        logger.addHandler(tools_file_handler)
        logging.info(f"Logging initialized for Industry Focused Search via CORE API - Script: {script_name}")


    def _extract_ngrams(self, text: str, n: int, stopwords: set) -> List[str]:
        if not text:
            return []
        words = [word.lower() for word in text.split() if word.isalnum() and word.lower() not in stopwords and len(word) > 2]
        ngrams = zip(*[words[i:] for i in range(n)])
        return [" ".join(ngram) for ngram in ngrams]

    def _extract_text_from_core_paper(self, paper_data: Dict[str, Any]) -> str:
        title = paper_data.get('title', '') or ""
        abstract = paper_data.get('abstract', '') or ""
        text_content = f"{title} {abstract}".lower()
        return text_content

    def _score_paper_fuzzy(self, paper_data: Dict[str, Any]) -> tuple[float, dict]: # MODIFIED SCORING
        if not self.relevance_criteria:
            logging.error("Relevance criteria not loaded. Cannot score paper.")
            return 0.0, {}

        paper_score = 0.0
        dimension_scores = {}
        text_content = self._extract_text_from_core_paper(paper_data)
        year = paper_data.get('yearPublished')
        if year is None and paper_data.get('publishedDate'):
            try:
                year = int(str(paper_data.get('publishedDate'))[:4])
            except (ValueError, TypeError):
                year = None

        # Citation count and venue quality are not primary drivers for industry relevance from academic papers
        citation_count_original = paper_data.get('citationCount') 
        # citation_count = 0 # Effectively disabled for scoring

        for dim_key, dimension in self.relevance_criteria.get('relevance_dimensions', {}).items():
            dim_score = 0.0 
            dim_weight = dimension.get('weight', 0.0) 
            matched_keywords_in_dim = {}

            if 'subcriteria' in dimension:
                for sub_key, subcrit in dimension['subcriteria'].items():
                    sub_item_score = 0.0 
                    sub_weight = subcrit.get('weight', 0.0) 
                    keywords = subcrit.get('keywords', [])
                    
                    if sub_key == 'publication_year' and year is not None:
                        # Simplified year scoring: boost for very recent, penalize very old, neutral for most.
                        # This is less critical for industry-relevant academic papers than pure academic novelty.
                        year_score_value = 0.5 # Neutral default
                        year_scoring_rules = subcrit.get('scoring', {}) # Keep structure if defined
                        try:
                            year_int = int(year)
                            if "2023-2024" in year_scoring_rules and year_int >= 2023: year_score_value = float(year_scoring_rules.get("2023-2024", 0.7)) # Slight boost for very recent
                            elif "before_2015" in year_scoring_rules and year_int < 2015: year_score_value = float(year_scoring_rules.get("before_2015", 0.3)) # Slight penalization for very old
                            # Other ranges could be neutral or have small adjustments.
                            # For now, only explicit rules or default 0.5
                        except ValueError:
                             logging.warning(f"Could not parse year '{year}' as int for paper {paper_data.get('id', paper_data.get('doi'))}")
                        
                        # Only apply weight if this subcriterion is meant to be used (e.g. weight > 0 in criteria file)
                        # For industry search, one might set the 'publication_year' sub_weight to a low value or 0 in the criteria file.
                        sub_item_score = year_score_value * sub_weight 
                        if year_score_value > 0 and sub_weight > 0: # Only log if it contributes
                            matched_keywords_in_dim[sub_key] = [f"Year: {year} (Norm. Score: {year_score_value}, Weight: {sub_weight})"]
                    
                    elif sub_key == 'citation_count':
                        # Explicitly give zero score contribution for citation count in industry context
                        sub_item_score = 0.0 * sub_weight 
                        # if citation_count_original is not None: # Log if present, but does not score
                        #    matched_keywords_in_dim[sub_key] = [f"Citations: {citation_count_original} (Score Contribution: 0)"]
                    
                    elif sub_key == 'venue_quality':
                        # Explicitly give zero score contribution for venue quality
                        sub_item_score = 0.0 * sub_weight
                        # matched_keywords_in_dim[sub_key] = ["Venue Quality (Score Contribution: 0)"]

                    else: # Keyword-based subcriteria (Primary focus for industry relevance)
                        matched_this_sub = False
                        current_matched_for_sub_list = [] 
                        for kw in keywords:
                            if kw.lower() in text_content: 
                                matched_this_sub = True
                                current_matched_for_sub_list.append(kw)
                        
                        if matched_this_sub:
                            sub_item_score = 1.0 * sub_weight 
                            matched_keywords_in_dim[sub_key] = list(set(current_matched_for_sub_list))
                    
                    dim_score += sub_item_score 
            
            dimension_scores[dim_key] = {
                "score_sum_sub_weighted": round(dim_score, 4), 
                "dimension_weight": dim_weight, 
                "weighted_score": round(dim_score * dim_weight, 4), 
                "matched_keywords_detail": matched_keywords_in_dim
            }
            paper_score += dim_score * dim_weight 
            
        return round(paper_score, 4), dimension_scores

    def search_papers_once(
        self,
        query: str,
        search_identifier: str,
        dynamic_step: int,
        limit: int = 100, 
        year_range: Optional[tuple[Optional[int], Optional[int]]] = None,
        max_total_papers_per_query: int = 200 
    ) -> List[Dict[str, Any]]:
        search_url = f"{self.base_url}/search/works"
        all_papers_for_this_query = []
        current_page = 1
        papers_retrieved_count = 0
        total_hits_for_query = 0 # Initialize

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
                "pageSize": limit, 
                "page": current_page,
                "apiKey": self.core_api_key
            }

            try:
                logging.info(f"Industry Search - Step {dynamic_step} - Query '{search_identifier}' (Page {current_page}): '{params['q'][:100]}...' with pageSize {limit}")
                response = requests.get(search_url, headers=self.headers, params=params, timeout=30)
                time.sleep(3) 
                response.raise_for_status()
                results_data = response.json()
                
                total_hits_for_query = results_data.get('totalHits', 0) # Capture totalHits
                papers_found_raw_this_page = results_data.get('results', [])

                if not papers_found_raw_this_page and current_page == 1: 
                    logging.warning(f"No papers found for industry-focused query: {params['q']}")
                    break 
                
                # Logging first paper structure (can be kept, it's general)
                if papers_found_raw_this_page and current_page == 1:
                    logging.info(f"Structure of the first paper object (keys): {list(papers_found_raw_this_page[0].keys())}")
                    # (Optional: detailed sample logging can be re-enabled if needed)

                processed_papers_for_saving_this_page = []
                for paper_raw in papers_found_raw_this_page:
                    lang_obj = paper_raw.get("language")
                    language_name = lang_obj.get("name") if isinstance(lang_obj, dict) else lang_obj if isinstance(lang_obj, str) else None
                    doc_type_obj = paper_raw.get("documentType")
                    doc_type_name = doc_type_obj.get("name") if isinstance(doc_type_obj, dict) else doc_type_obj if isinstance(doc_type_obj, str) else None
                    
                    paper_to_save = {
                        "id": paper_raw.get("id"), "doi": paper_raw.get("doi"),
                        "title": paper_raw.get("title"), "abstract": paper_raw.get("abstract"),
                        "yearPublished": paper_raw.get("yearPublished"), "publishedDate": paper_raw.get("publishedDate"),
                        "authors": paper_raw.get("authors"), "citationCount": paper_raw.get("citationCount"), # Keep for info, not scoring
                        "downloadUrl": paper_raw.get("downloadUrl"), "publisher": paper_raw.get("publisher"),
                        "journals": paper_raw.get("journals"), "language": language_name,
                        "documentType": doc_type_name, "topics": paper_raw.get("topics")
                    }
                    processed_papers_for_saving_this_page.append(paper_to_save)
                
                all_papers_for_this_query.extend(processed_papers_for_saving_this_page)
                papers_retrieved_count += len(processed_papers_for_saving_this_page)

                logging.info(f"Page {current_page}: Retrieved {len(processed_papers_for_saving_this_page)} papers. Total for query so far: {papers_retrieved_count}/{total_hits_for_query}")

                if not papers_found_raw_this_page or papers_retrieved_count >= total_hits_for_query or papers_retrieved_count >= max_total_papers_per_query:
                    break 

                current_page += 1
                if current_page > 10 and max_total_papers_per_query > 100 : 
                     logging.warning(f"Stopping pagination for query '{search_identifier}' after 10 pages to prevent excessive calls.")
                     break

            except requests.exceptions.Timeout:
                logging.error(f"Timeout on page {current_page} for industry query '{search_identifier}': '{params['q']}'")
                break 
            except requests.exceptions.RequestException as e:
                logging.error(f"Error on page {current_page} for industry query '{search_identifier}': '{params['q']}': {e}")
                if hasattr(e, 'response') and e.response is not None: logging.error(f"Response content: {e.response.text}")
                break 
            except json.JSONDecodeError as e:
                response_text = "N/A"
                if 'response' in locals() and hasattr(response, 'text'): response_text = response.text
                logging.error(f"Error decoding JSON (Page {current_page}) for industry query '{search_identifier}': {e}. Response: {response_text}")
                break 

        if all_papers_for_this_query:
            output_payload_to_save = {
                "totalHitsEncounteredAcrossPages": total_hits_for_query,
                "retrievedCountForThisQuery": papers_retrieved_count,
                "searchIdentifier": search_identifier,
                "originalQuery": query_with_filters, 
                "results": all_papers_for_this_query
            }
            step_results_dir = self.results_session_dir / f"dynamic_step_{dynamic_step}"
            step_results_dir.mkdir(parents=True, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = step_results_dir / f"{search_identifier}_results_{timestamp}.json"
            with open(output_file, 'w') as f:
                json.dump(output_payload_to_save, f, indent=2)
            logging.info(f"Saved {papers_retrieved_count} papers for industry query '{search_identifier}' to {output_file.relative_to(self.workspace_root)}")
        
        return all_papers_for_this_query

    def _generate_queries_from_relevant_papers(
        self, 
        relevant_papers: List[Dict[str, Any]], 
        query_id_to_text_map: Dict[str, str], 
        max_new_queries: int = 5
        ) -> List[str]:
        new_queries_to_run: List[str] = []
        all_terms_with_parent_query = [] 

        if not relevant_papers:
            logging.info("No relevant papers from industry search to generate new queries.")
            return []

        for paper_wrapper in relevant_papers:
            paper_data = paper_wrapper.get('original_data', {})
            parent_query_id = paper_wrapper.get('source_query_id')
            parent_query_text = query_id_to_text_map.get(parent_query_id)

            if not parent_query_text:
                logging.warning(f"Could not find parent query text for ID '{parent_query_id}'. Skipping paper for query gen.")
                continue

            text_content = self._extract_text_from_core_paper(paper_data)
            words = text_content.lower().split() 
            filtered_keywords = [word for word in words if word.isalnum() and word not in STOPWORDS and len(word) > 3]
            for keyword in filtered_keywords: all_terms_with_parent_query.append((keyword, "keyword", parent_query_text))
            bigrams = self._extract_ngrams(text_content, 2, STOPWORDS)
            for bigram in bigrams: all_terms_with_parent_query.append((bigram, "bigram", parent_query_text))
            trigrams = self._extract_ngrams(text_content, 3, STOPWORDS)
            for trigram in trigrams: all_terms_with_parent_query.append((trigram, "trigram", parent_query_text))
            
        if not all_terms_with_parent_query:
            logging.info("No keywords or N-grams extracted from industry-relevant papers for new queries.")
            return []

        parent_query_to_terms: Dict[str, Dict[str, List[str]]] = {}
        for term, term_type, pq_text in all_terms_with_parent_query:
            if pq_text not in parent_query_to_terms: parent_query_to_terms[pq_text] = {"keyword": [], "bigram": [], "trigram": []}
            parent_query_to_terms[pq_text][term_type].append(term)

        generated_query_texts = set(query_id_to_text_map.values()) 

        for parent_q_text, terms_from_children_typed in parent_query_to_terms.items():
            if len(new_queries_to_run) >= max_new_queries: break
            combined_child_terms = [term for term_list in terms_from_children_typed.values() for term in term_list]
            if not combined_child_terms: continue
            term_counts = Counter(combined_child_terms)
            top_child_terms_for_parent = [term for term, count in term_counts.most_common(3)] 

            if top_child_terms_for_parent:
                meaningful_new_terms = [t for t in top_child_terms_for_parent if f'"{t}"'.lower() not in parent_q_text.lower() and t.lower() not in parent_q_text.lower()]
                if meaningful_new_terms:
                    or_part = " OR ".join([f'"{t}"' for t in meaningful_new_terms])
                    potential_new_query = f"({parent_q_text}) AND ({or_part})"
                    if potential_new_query not in generated_query_texts:
                        new_queries_to_run.append(potential_new_query)
                        generated_query_texts.add(potential_new_query)
                        logging.info(f"Generated new industry query (from parent '{parent_q_text[:50]}...'): {potential_new_query}")
        
        if len(new_queries_to_run) < max_new_queries:
            overall_term_counts = Counter(term for term, term_type, pq_text in all_terms_with_parent_query)
            top_overall_terms = [term for term, count in overall_term_counts.most_common(max_new_queries * 2)]
            idx = 0
            while len(new_queries_to_run) < max_new_queries and idx < len(top_overall_terms):
                term_to_try = top_overall_terms[idx]; idx += 1
                base_query_text = next((qtext for qid, qtext in query_id_to_text_map.items() if qid.startswith("initial_primary")), 
                                       next(iter(query_id_to_text_map.values()), None))
                if base_query_text:
                    if f'"{term_to_try}"'.lower() not in base_query_text.lower() and term_to_try.lower() not in base_query_text.lower():
                        potential_new_query = f'({base_query_text}) AND "{term_to_try}"'
                        if potential_new_query not in generated_query_texts:
                            new_queries_to_run.append(potential_new_query); generated_query_texts.add(potential_new_query)
                            logging.info(f"Generated new industry query (fallback with base '{base_query_text[:30]}...'): {potential_new_query}")
                else: 
                    potential_new_query = f'"{term_to_try}"'
                    if potential_new_query not in generated_query_texts:
                        new_queries_to_run.append(potential_new_query); generated_query_texts.add(potential_new_query)
                        logging.info(f"Generated new industry query (absolute fallback): {potential_new_query}")

        logging.info(f"Generated {len(new_queries_to_run)} new industry-focused queries for the next step.")
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
        test_mode_limit_initial_queries: Optional[int] = None 
    ):
        logging.info(f"Starting Industry Focused CORE API dynamic search: {num_dynamic_iterations} iterations, score threshold {relevance_threshold_for_analysis}")
        
        all_papers_scored_unique: Dict[str, Dict[str, Any]] = {} 
        query_id_to_text_map: Dict[str, str] = {} 

        current_queries: List[Dict[str, str]] = []
        query_type_counters = {"primary": 0, "secondary": 0, "tertiary": 0, "custom":0} # Added custom for industry terms

        initial_query_count = 0
        for q_type, queries in initial_query_dict.items():
            if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries:
                logging.info(f"Reached test_mode_limit_initial_queries ({test_mode_limit_initial_queries}), stopping.")
                break
            for query_text in queries:
                if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries: break
                
                actual_q_type = q_type if q_type in query_type_counters else "custom"
                query_id = f"initial_{actual_q_type}_{query_type_counters[actual_q_type]}"
                current_queries.append({"id": query_id, "text": query_text})
                query_id_to_text_map[query_id] = query_text 
                query_type_counters[actual_q_type] += 1
                initial_query_count +=1
            if test_mode_limit_initial_queries is not None and initial_query_count >= test_mode_limit_initial_queries: break
        
        logging.info(f"Prepared {len(current_queries)} initial industry-focused queries (limit: {test_mode_limit_initial_queries}).")

        for dynamic_step in range(num_dynamic_iterations + 1): 
            logging.info(f"--- Industry Search Dynamic Step {dynamic_step} ---")
            if not current_queries:
                logging.info(f"No queries to run in dynamic step {dynamic_step}. Stopping.")
                break

            papers_from_this_step_scored = []
            queries_for_this_step = list(current_queries); current_queries = [] 

            for query_obj in queries_for_this_step:
                query_text, query_id = query_obj["text"], query_obj["id"]
                raw_papers = self.search_papers_once(query_text, query_id, dynamic_step, papers_per_query_limit, year_range, max_total_papers_to_fetch_per_query)

                for paper_data in raw_papers: 
                    core_id, doi = paper_data.get('id'), paper_data.get('doi')
                    unique_id = doi if doi else str(core_id) if core_id else None
                    if not unique_id:
                        logging.warning(f"Skipping paper (no ID): {paper_data.get('title', '[Untitled]')}")
                        continue

                    score, dim_scores = self._score_paper_fuzzy(paper_data)
                    scored_paper = {"original_data": paper_data, "relevance_score": score, "dimension_scores": dim_scores, 
                                    "source_query_id": query_id, "dynamic_step": dynamic_step, "core_id": core_id, "doi": doi}
                    papers_from_this_step_scored.append(scored_paper)
                    if unique_id not in all_papers_scored_unique or score > all_papers_scored_unique[unique_id].get("relevance_score", 0):
                        all_papers_scored_unique[unique_id] = scored_paper
            
            logging.info(f"Step {dynamic_step} (Industry) found {len(papers_from_this_step_scored)} papers. Total unique: {len(all_papers_scored_unique)}")

            if dynamic_step < num_dynamic_iterations:
                relevant_for_next_step = [p for p in papers_from_this_step_scored if p['relevance_score'] >= relevance_threshold_for_analysis]
                logging.info(f"{len(relevant_for_next_step)} papers from step {dynamic_step} met threshold {relevance_threshold_for_analysis} for new query generation.")
                
                new_query_strings = self._generate_queries_from_relevant_papers(relevant_for_next_step, query_id_to_text_map, max_new_queries_per_step)
                
                for idx, q_text in enumerate(new_query_strings):
                    new_q_id = f"dynamic_s{dynamic_step+1}_g{idx}"
                    current_queries.append({"text": q_text, "id": new_q_id, "type": "generated"})
                    query_id_to_text_map[new_q_id] = q_text
                logging.info(f"Generated {len(current_queries)} new industry-focused queries for step {dynamic_step + 1}.")

        final_results_list = list(all_papers_scored_unique.values())
        self._save_consolidated_results(final_results_list, "industry_dynamic_search_complete")
        self._generate_markdown_summary(final_results_list, "industry_dynamic_search_complete", num_dynamic_iterations)
        
        logging.info(f"Industry Focused CORE API Dynamic search completed. Found {len(final_results_list)} unique papers.")
        return all_papers_scored_unique

    def _save_consolidated_results(self, papers_list: List[Dict[str,Any]], stage_name: str):
        output_data = {
            "metadata": {
                "session_id": self.iteration, 
                "timestamp": datetime.now().isoformat(),
                "script_used": f"tools/{Path(__file__).name}", # Will be the new script name
                "search_type": "Industry Focused Search via CORE API",
                "stage": stage_name,
                "relevance_criteria_source": str(self.relevance_criteria_path_arg)
            },
            "summary": {"total_unique_papers_retrieved": len(papers_list)},
            "papers": papers_list
        }
        json_output_file = self.results_session_dir / f"consolidated_{stage_name}_session{self.iteration}.json"
        with open(json_output_file, 'w') as f: json.dump(output_data, f, indent=2)
        logging.info(f"Consolidated JSON for '{stage_name}' (Industry Search) saved to {json_output_file.relative_to(self.workspace_root)}")

    def _generate_markdown_summary(self, papers_list: List[Dict[str,Any]], stage_name: str, num_dynamic_iters_run: int): # MODIFIED SUMMARY
        md_summary_file_path = self.docs_base_dir / f"4.1.8.4-industry-core-search-summary-session-{self.iteration}.md" # MODIFIED filename
        
        json_output_file = self.results_session_dir / f"consolidated_{stage_name}_session{self.iteration}.json"
        json_results_md_path = json_output_file.relative_to(self.workspace_root)

        total_papers = len(papers_list)
        above_0_5_count = sum(1 for p in papers_list if p.get('relevance_score', 0) >= 0.5)
        above_0_3_count = sum(1 for p in papers_list if p.get('relevance_score', 0) >= 0.3)

        with open(md_summary_file_path, 'w') as f:
            f.write(f"# Industry Focused CORE API Search Summary - Session {self.iteration}\n")
            f.write("\n") # Separate newline
            f.write(f"**Completion Timestamp:** {datetime.now().isoformat()}\n")
            f.write(f"**Script Used:** `tools/{Path(__file__).name}`\n")
            f.write(f"**Search Type:** Industry Focused Search via CORE API\n")
            f.write(f"**Relevance Criteria Used:** `{self.relevance_criteria_path_arg}`\n")
            f.write(f"**Number of Dynamic Iterations Configured:** {num_dynamic_iters_run}\n") 
            f.write(f"**Raw Consolidated JSON Results:** `{json_results_md_path}`\n")
            f.write(f"**Individual query JSON files located in:** `{self.results_session_dir.relative_to(self.workspace_root)}/dynamic_step_*/`\n")
            
            f.write(f"## Overall Summary of Results\n")
            f.write(f"- **Total unique papers retrieved:** {total_papers}\n")
            f.write(f"- **Papers with relevance score >= 0.5:** {above_0_5_count}\n")
            f.write(f"- **Papers with relevance score >= 0.3:** {above_0_3_count}\n")
            
            f.write(f"## Notes on Industry Search via CORE API\n")
            f.write("This summary provides an overview of academic papers retrieved using the CORE API, targeted with industry-focused search terms. "
                    "The CORE API primarily indexes academic literature, so results will largely be scholarly articles, pre-prints, and conference papers that align with the industry-oriented queries. "
                    "The scoring was adapted to de-emphasize purely academic metrics (like citation counts) and focus more on keyword relevance to industry topics.\n\n"
                    "This search complements broader industry research which might involve direct industry report searches, company website analysis, etc. "
                    "For detailed information on retrieved items, refer to the consolidated JSON results file and individual query JSON files linked above.\n")

        logging.info(f"Markdown summary for Industry Search saved to {md_summary_file_path.relative_to(self.workspace_root)}")


def main():
    parser = argparse.ArgumentParser(description="Run an industry-focused dynamic search session using the CORE API.") # MODIFIED description
    parser.add_argument("--session_id", type=int, default=1, help="Search session ID. Default: 1")
    parser.add_argument(
        "--relevance_criteria_path", type=str, default=None, 
        help="Path to relevance criteria JSON. Relative to workspace root or absolute. If None, uses a general default."
    )
    parser.add_argument("--dynamic_iterations", type=int, default=1, help="Number of dynamic query iterations. Default: 1 (for shorter industry exploration runs)")
    parser.add_argument("--papers_per_query", type=int, default=15, help="Max papers per query. Default: 15 (for industry exploration)")
    parser.add_argument("--relevance_threshold", type=float, default=0.2, help="Min score for query generation. Default: 0.2 (lower for broader industry exploration)")
    parser.add_argument("--max_new_queries", type=int, default=2, help="Max new queries per step. Default: 2")
    parser.add_argument("--max_papers_per_query_run", type=int, default=100, help="Max total papers per query via pagination. Default: 100")
    parser.add_argument("--test_limit_initial_queries", type=int, default=None, help="Limit initial queries for testing.")
    parser.add_argument("--start_year", type=int, default=None, help="Filter by start year.")
    parser.add_argument("--end_year", type=int, default=None, help="Filter by end year.")
    args = parser.parse_args()

    session_id = args.session_id
    
    # MODIFIED default relevance criteria path and warning
    default_criteria_path = Path(__file__).resolve().parent.parent / "sources" / "4.1.3-relevance-criteria" / "relevance_criteria.json"
    
    if args.relevance_criteria_path:
        temp_path = Path(args.relevance_criteria_path)
        final_criteria_path = Path(__file__).resolve().parent.parent / temp_path if not temp_path.is_absolute() else temp_path
    else:
        final_criteria_path = default_criteria_path
        logging.warning(f"No specific relevance_criteria_path provided. Using general default: {final_criteria_path.relative_to(Path(__file__).resolve().parent.parent)}")
        logging.warning("Consider creating and using a relevance criteria file tailored for industry search for better results.")

    core_api_key_env = os.getenv("CORE_API_KEY") 
    provided_api_key = "FeJVa6KG3ISf8iqN7sZw9RCHBgQPTxW2" # User provided key
    final_api_key_to_use = core_api_key_env if core_api_key_env else provided_api_key

    if not final_api_key_to_use: logging.error("FATAL: CORE_API_KEY not set and no fallback. Exiting.") # Should not happen with fallback
    elif not core_api_key_env and provided_api_key: logging.warning(f"Using provided API key for CORE (CORE_API_KEY env var not set).")
    elif core_api_key_env: logging.info(f"Using CORE_API_KEY from environment variable.")

    searcher = IndustryCoreSearch(api_key=final_api_key_to_use, iteration=session_id)
    searcher.relevance_criteria_path_arg = str(final_criteria_path.relative_to(searcher.workspace_root))
    searcher.relevance_criteria = searcher._load_relevance_criteria(final_criteria_path) 
    
    logging.info(f"Industry Focused CORE API Search Script - Session {session_id}")
    if not final_api_key_to_use: logging.critical("CRITICAL: Running without CORE API key - this will likely fail.")

    # MODIFIED Initial Queries for Industry Focus (examples from docs/4.1.8.3) - SIMPLIFIED FOR EDIT
    initial_queries_config = {
        "operator_tasks_lifecycle": [
            'DER installation technician AND daily tasks',
            'Microgrid operator AND control room workflow',
            'Wind turbine maintenance AND field crew challenges'
        ],
        "communication_coordination": [
            'DER field operations AND communication gap',
            'Utility operator AND DERMS HMI usability issues'
        ],
        "human_augmentation_ai": [
            'AI for DER field service AND benefits',
            'Agent-based assistance AND DER technician safety'
        ],
        "safety_training_human_factors": [
             'DER safety AND incident report',
             'DER operator training AND simulator',
             'Human factors AND DER control room design'
        ]
    }
    
    year_filter = (args.start_year, args.end_year) if args.start_year or args.end_year else None

    searcher.dynamic_search_orchestrator(
        initial_query_dict=initial_queries_config,
        num_dynamic_iterations=args.dynamic_iterations,
        papers_per_query_limit=args.papers_per_query,
        relevance_threshold_for_analysis=args.relevance_threshold,
        max_new_queries_per_step=args.max_new_queries,
        year_range=year_filter,
        max_total_papers_to_fetch_per_query=args.max_papers_per_query_run,
        test_mode_limit_initial_queries=args.test_limit_initial_queries
    )

if __name__ == "__main__":
    main() 
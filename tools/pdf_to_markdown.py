#!/usr/bin/env python3
"""
Convert PDF to markdown format.
"""

import os
from pathlib import Path
import PyPDF2
import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def clean_text(text: str) -> str:
    """Clean and format the text for markdown."""
    # Remove multiple newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Fix common PDF conversion issues
    text = text.replace('ﬁ', 'fi')
    text = text.replace('ﬂ', 'fl')
    
    # Add markdown formatting
    # Convert section headers (assuming they're in ALL CAPS)
    text = re.sub(r'\n([A-Z][A-Z\s]+)\n', r'\n## \1\n', text)
    
    # Convert numbered sections (e.g., "1. Introduction")
    text = re.sub(r'\n(\d+)\.\s+([A-Z][a-zA-Z\s]+)\n', r'\n## \1. \2\n', text)
    
    # Convert subsections (e.g., "3.1. Research questions")
    text = re.sub(r'\n(\d+)\.(\d+)\.\s+([A-Z][a-zA-Z\s]+)\n', r'\n### \1.\2. \3\n', text)
    
    # Convert bullet points
    text = re.sub(r'•\s*', '- ', text)
    
    # Convert numbered lists
    text = re.sub(r'(\d+)\.\s*', r'\1. ', text)
    
    # Fix spacing around headers
    text = re.sub(r'\n##\s+', '\n\n## ', text)
    text = re.sub(r'\n###\s+', '\n\n### ', text)
    
    # Fix spacing around lists
    text = re.sub(r'\n-\s+', '\n\n- ', text)
    text = re.sub(r'\n(\d+)\.\s+', r'\n\n\1. ', text)
    
    # Add title formatting
    if not text.startswith('# '):
        lines = text.split('\n')
        if len(lines) > 0:
            lines[0] = f"# {lines[0]}"
            text = '\n'.join(lines)
    
    return text.strip()

def pdf_to_markdown(pdf_path: str, output_path: str) -> None:
    """Convert PDF file to markdown format."""
    try:
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            # Create PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extract text from each page
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n\n"
            
            # Clean and format the text
            markdown_text = clean_text(text)
            
            # Write to markdown file
            with open(output_path, 'w', encoding='utf-8') as md_file:
                md_file.write(markdown_text)
            
            logger.info(f"Successfully converted {pdf_path} to {output_path}")
            
    except Exception as e:
        logger.error(f"Error converting PDF to markdown: {e}")

def main():
    """Main execution function."""
    # Input and output paths
    pdf_path = "sources/5.3-methodology-papers/A systematic review of methodologies for developing Digital Twins- Insights and recommendations for effective implementation.pdf"
    output_path = "sources/5.3-methodology-papers/A systematic review of methodologies for developing Digital Twins- Insights and recommendations for effective implementation.md"
    
    # Convert PDF to markdown
    pdf_to_markdown(pdf_path, output_path)

if __name__ == "__main__":
    main() 
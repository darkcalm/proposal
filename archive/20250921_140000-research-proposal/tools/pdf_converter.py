import fitz # PyMuPDF
import sys
import os

def pdf_to_markdown(pdf_path, output_path):
    markdown_content = ""
    try:
        doc = fitz.open(pdf_path)
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            # Extract text - simple text extraction without much formatting
            text = page.get_text("text")
            markdown_content += f"\n\n---\n\nPage {page_num + 1}\n\n---\n\n"
            markdown_content += text
        doc.close()
    except Exception as e:
        print(f"Error processing PDF {pdf_path}: {e}")
        return False

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        print(f"Successfully converted {pdf_path} to {output_path}")
        return True
    except Exception as e:
        print(f"Error writing markdown file {output_path}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        print("Usage: python convert_pdf_to_md.py <directory_path>")
        sys.exit(1)

    if not os.path.isdir(target_dir):
        print(f"Error: Directory not found at {target_dir}")
        sys.exit(1)

    for filename in os.listdir(target_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(target_dir, filename)
            markdown_path = os.path.join(target_dir, os.path.splitext(filename)[0] + ".md")

            # Check if a corresponding .tex file exists in the same directory
            tex_path = os.path.join(target_dir, os.path.splitext(filename)[0] + ".tex")
            if os.path.exists(tex_path):
                print(f"Skipping {filename} as .tex source exists in {target_dir}.")
                continue

            # Check if .md file already exists in the same directory
            if os.path.exists(markdown_path):
                 print(f"Skipping {filename} as .md already exists in {target_dir}.")
                 continue

            print(f"Converting {filename}...")
            pdf_to_markdown(pdf_path, markdown_path) 
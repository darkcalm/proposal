#!/bin/bash
# Utility script to compile LaTeX with bibliography (XeLaTeX + Biber)
# Usage: ./latex_compile.sh main.tex

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <main.tex>"
  exit 1
fi

TEXFILE="$1"
BASENAME="${TEXFILE%.tex}"

# Clean up auxiliary files
rm -f "$BASENAME.aux" "$BASENAME.bbl" "$BASENAME.bcf" "$BASENAME.blg" "$BASENAME.log" "$BASENAME.out" "$BASENAME.run.xml" "$BASENAME.toc"

# Compile sequence
xelatex "$TEXFILE"
biber "$BASENAME"
xelatex "$TEXFILE"
xelatex "$TEXFILE"

echo "Compilation complete. Output: $BASENAME.pdf" 
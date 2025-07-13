#!/usr/bin/env python3
"""
Script to fix publication parsing issues by extracting correct data from BibTeX entries.
Version 2: More robust approach using manual parsing.
"""

import os
import re
import glob
from pathlib import Path

def extract_bibtex_field(content, field_name):
    """Extract a specific field from BibTeX content using manual parsing."""
    # Find the field pattern
    pattern = rf'{field_name}\s*=\s*\{{'
    match = re.search(pattern, content, re.IGNORECASE)
    if not match:
        return None
    
    start_pos = match.end() - 1  # Position of the opening brace
    brace_count = 0
    pos = start_pos
    
    # Find the matching closing brace
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                # Extract the content between braces
                field_content = content[start_pos + 1:pos].strip()
                # Clean up the content
                field_content = re.sub(r'\s+', ' ', field_content)
                return field_content
        pos += 1
    
    return None

def extract_bibtex_data(content):
    """Extract title, authors, and venue from BibTeX entry."""
    # Find the BibTeX entry
    bibtex_start = content.find('@')
    if bibtex_start == -1:
        return None, None, None
    
    # Find the opening brace after the entry type
    brace_start = content.find('{', bibtex_start)
    if brace_start == -1:
        return None, None, None
    
    # Find the closing brace for the entire entry
    brace_count = 0
    pos = brace_start
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                break
        pos += 1
    
    if pos >= len(content):
        return None, None, None
    
    # Extract the BibTeX content
    bibtex_content = content[brace_start + 1:pos]
    
    # Extract fields
    title = extract_bibtex_field(bibtex_content, 'title')
    authors = extract_bibtex_field(bibtex_content, 'author')
    
    # Try journal first, then booktitle
    venue = extract_bibtex_field(bibtex_content, 'journal')
    if not venue:
        venue = extract_bibtex_field(bibtex_content, 'booktitle')
    
    return title, authors, venue

def fix_publication_file(filepath):
    """Fix a single publication file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract correct data from BibTeX
    title, authors, venue = extract_bibtex_data(content)
    
    if not title or not authors:
        print(f"Warning: Could not extract data from {filepath}")
        return False
    
    # Update front matter
    # Replace title
    content = re.sub(
        r'title:\s*"[^"]*"',
        f'title: "{title}"',
        content
    )
    
    # Replace authors
    content = re.sub(
        r'authors:\s*"[^"]*"',
        f'authors: "{authors}"',
        content
    )
    
    # Replace venue if we have it
    if venue:
        content = re.sub(
            r'venue:\s*"[^"]*"',
            f'venue: "{venue}"',
            content
        )
    
    # Write back to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def main():
    """Main function to fix all publication files."""
    publication_files = glob.glob('_publications/*.md')
    
    fixed_count = 0
    total_count = len(publication_files)
    
    for filepath in publication_files:
        if fix_publication_file(filepath):
            fixed_count += 1
            print(f"Fixed: {filepath}")
        else:
            print(f"Failed to fix: {filepath}")
    
    print(f"\nFixed {fixed_count} out of {total_count} files")

if __name__ == "__main__":
    main() 
import os
import re
from bs4 import BeautifulSoup

# Usage: python extract_theses_from_html.py theses-original.html _theses

def extract_theses(html_path, output_dir):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    os.makedirs(output_dir, exist_ok=True)
    for li in soup.find_all('li'):
        award = ''
        text = li.get_text(' ', strip=True)
        # Remove [PDF] and similar
        text = re.sub(r'\[PDF\]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        # Extract PDF URL if present
        pdf_url = ''
        a_tag = li.find('a', href=True)
        if a_tag:
            pdf_url = a_tag['href']
        # Extract author (before first period)
        author = text.split('.', 1)[0].strip()
        # Extract title (between first and second period)
        title = ''
        thesis_type = ''
        year = ''
        if '.' in text:
            rest = text.split('.', 1)[1].strip()
            # Title is before next period
            if '.' in rest:
                title = rest.split('.', 1)[0].strip()
                after_title = rest.split('.', 1)[1].strip()
            else:
                title = rest
                after_title = ''
            # Extract thesis type and year: <thesis_type>, <year>.
            m = re.search(r'([^.]+),\s*(\d{4})\.?', after_title)
            if m:
                thesis_type = m.group(1).strip()
                year = m.group(2)
            # Extract award from <b> tag if present
            b_tag = li.find('b')
            if b_tag:
                award = b_tag.get_text(strip=True)
        # Compose markdown
        md = f'''---
layout: thesis
author: "{author}"
title: "{title}"
type: "{thesis_type}"
year: {year}
pdf_url: "{pdf_url}"
award: "{award}"
---
'''
        # Create a safe filename
        safe_title = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:50]
        filename = f"{year}-{safe_title}.md"
        out_path = os.path.join(output_dir, filename)
        with open(out_path, 'w', encoding='utf-8') as out:
            out.write(md)
        print(f"Wrote {out_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) not in (2, 3):
        print("Usage: python extract_theses_from_html.py <input.html> [output_dir]")
        sys.exit(1)
    input_html = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) == 3 else '_theses'
    extract_theses(input_html, output_dir)

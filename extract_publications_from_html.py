import os
import re
from bs4 import BeautifulSoup

def extract_publications(html_path, output_dir):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Find all year headers and their following <ol>
    for h3 in soup.find_all('h3'):
        year = h3.get_text(strip=True)
        ol = h3.find_next_sibling('ol')
        if not ol:
            continue
        for li in ol.find_all('li', recursive=False):
            # Extract authors, title, venue, pages, pdf_url
            text = li.get_text(' ', strip=True)
            # Try to extract BibTeX from the following <div> (if present)
            bibtex = ''
            bib_div = li.find_next('div', class_='papercite_bibtex')
            if bib_div:
                code = bib_div.find('code')
                if code:
                    bibtex = code.get_text(strip=True)
            # Extract main link URL (first <a> tag's href)
            pdf_url = ''
            pdf_link = li.find('a', href=True)
            if pdf_link:
                pdf_url = pdf_link['href']
            # Extract title (from BibTeX if possible)
            title = ''
            authors = ''
            venue = ''
            pages = ''
            if bibtex:
                m = re.search(r'title\s*=\s*[{\"](.+?)[}\"]', bibtex, re.DOTALL)
                if m:
                    title = m.group(1).replace('\n', ' ').strip()
                m = re.search(r'author\s*=\s*[{\"](.+?)[}\"]', bibtex, re.DOTALL)
                if m:
                    authors = m.group(1).replace('\n', ' ').strip()
                m = re.search(r'booktitle\s*=\s*[{\"](.+?)[}\"]', bibtex, re.DOTALL)
                if not m:
                    m = re.search(r'journal\s*=\s*[{\"](.+?)[}\"]', bibtex, re.DOTALL)
                if m:
                    venue = m.group(1).replace('\n', ' ').strip()
                m = re.search(r'pages\s*=\s*[{\"](.+?)[}\"]', bibtex, re.DOTALL)
                if m:
                    pages = m.group(1).replace('\n', ' ').strip()
            # Fallbacks
            if not title:
                # Try to extract title from text (after authors)
                parts = text.split('.')
                if len(parts) > 1:
                    title = parts[1].strip()
            if not authors:
                authors = text.split('.')[0].strip()
            # Compose markdown
            md = f"""---
layout: publication
title: "{title}"
authors: "{authors}"
venue: "{venue}"
year: {year}
pages: "{pages}"
pdf_url: "{pdf_url}"
---


{{% raw %}}
{bibtex}
{{% endraw %}}
"""
            # Create a filename
            safe_title = re.sub(r'[^a-zA-Z0-9]+', '-', title.lower()).strip('-')[:50]
            filename = f"{year}-{safe_title}.md"
            out_path = os.path.join(output_dir, filename)
            with open(out_path, 'w', encoding='utf-8') as out:
                out.write(md)
            print(f"Wrote {out_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python extract_publications_from_html.py <input.html> <output_dir>")
        sys.exit(1)
    extract_publications(sys.argv[1], sys.argv[2])

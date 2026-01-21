import os
import re
from bs4 import BeautifulSoup
import bibtexparser

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
            # Extract text for fallback parsing
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
            doi_url = ''
            slide_url = ''
            for a in li.find_all('a', href=True):
                link_text = a.get_text(strip=True)
                href = a['href']
                if '[DOI]' in link_text:
                    doi_url = href
                elif '[Slides]' in link_text:
                    slide_url = href
                elif not pdf_url:
                    pdf_url = href
            # Extract fields
            title = ''
            authors = ''
            venue = ''
            pages = ''
            if bibtex:
                try:
                    bib_db = bibtexparser.loads(bibtex)
                    if bib_db.entries:
                        entry = bib_db.entries[0]
                        title = entry.get('title', '').replace('\n', ' ').replace('{', '').replace('}', '').strip()
                        authors = entry.get('author', '').replace('\n', ' ').replace(' and ', ', ').strip()
                        venue = entry.get('booktitle', entry.get('journal', '')).replace('\n', ' ').strip()
                        pages = entry.get('pages', '').replace('\n', ' ').strip()
                except Exception as e:
                    print(f"BibTeX parse error: {e}")
            # Fallbacks
            if not title:
                # Try to extract title from text (after authors)
                parts = text.split('.')
                if len(parts) > 1:
                    title = parts[1].strip()
            if not authors:
                authors = text.split('.')[0].strip()
            # Extract award/note from <b> tag if present
            award = ''
            b_tag = li.find('b')
            if b_tag:
                award = b_tag.get_text(strip=True)
                if award.endswith('.'):
                    award = award[:-1]
            # Compose markdown
            md = f"""---
layout: publication
title: "{title}"
authors: "{authors}"
venue: "{venue}"
year: {year}
pages: "{pages}"
pdf_url: "{pdf_url}"
doi_url: "{doi_url}"
slide_url: "{slide_url}"
award: "{award}"
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

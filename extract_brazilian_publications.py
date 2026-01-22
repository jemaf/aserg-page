
import os
import re
from bs4 import BeautifulSoup

# Usage: python extract_brazilian_publications.py pubs-original-br.html

def extract_publications_br(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

        output_dir = extract_publications_br.output_dir
        os.makedirs(output_dir, exist_ok=True)
        for h4 in soup.find_all('h4'):
            year = h4.get_text(strip=True)
            ol = h4.find_next_sibling('ol')
            if not ol:
                continue
            for li in ol.find_all('li', recursive=False):
                # PDF URL
                pdf_url = ''
                a_tag = li.find('a', href=True)
                if a_tag:
                    pdf_url = a_tag['href']
                # Main text (remove PDF icon and tags)
                text = li.get_text(' ', strip=True)
                # Remove [PDF] and similar
                text = re.sub(r'\[PDF\]', '', text)
                # Remove extra whitespace
                text = re.sub(r'\s+', ' ', text).strip()
                # Extract authors, title, venue, pages, year in order
                authors = ''
                title = ''
                venue = ''
                pages = ''
                year_extracted = ''
                # Split by period
                parts = [p.strip() for p in text.split('.') if p.strip()]
                if len(parts) >= 3:
                    authors = parts[0]
                    title = parts[1]
                    # The rest is venue, pages, year (comma separated)
                    rest = '.'.join(parts[2:])
                    # Split by commas
                    rest_parts = [p.strip() for p in rest.split(',') if p.strip()]
                    # Venue: everything up to the last two comma-separated parts
                    if len(rest_parts) >= 3:
                        venue = ', '.join(rest_parts[:-2])
                        pages = rest_parts[-2]
                        # Try to extract year from last part
                        year_match = re.search(r'(\d{4})', rest_parts[-1])
                        if year_match:
                            year_extracted = year_match.group(1)
                    elif len(rest_parts) == 2:
                        venue = rest_parts[0]
                        pages = ''
                        year_match = re.search(r'(\d{4})', rest_parts[1])
                        if year_match:
                            year_extracted = year_match.group(1)
                    elif len(rest_parts) == 1:
                        venue = rest_parts[0]
                        pages = ''
                # Use extracted year if found
                if year_extracted:
                    year = year_extracted
                # Compose markdown
                md = f'''---
layout: publication
title: "{title}"
authors: "{authors}"
venue: "{venue}"
year: {year}
pages: "{pages}"
pdf_url: "{pdf_url}"
language: "portuguese"
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
        print("Usage: python extract_brazilian_publications.py <input.html> [output_dir]")
        sys.exit(1)
    input_html = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) == 3 else 'brazilian_publications_md'
    extract_publications_br.output_dir = output_dir
    extract_publications_br(input_html)

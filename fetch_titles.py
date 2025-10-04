#!/usr/bin/python3

import yaml
import requests
import re
from bs4 import BeautifulSoup

INPUT_FILE = '_data/papers.yml'
OUTPUT_FILE = '_data/fetched_titles.yml'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

def clean_title(title):
    return re.sub(r'\s*[\|•\-—]\s[^|•—\-]{2,}$', '', title).strip()

def fetch_title(url):
    print(f"\nFetching {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=8, allow_redirects=True)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string.strip() if soup.title else "No title"
        print(f"\t[OK] {title}")
        return clean_title(title)
    except Exception as e:
        print(f"\t[ERR] {e}")
        return f"Error: {type(e).__name__}"

with open(INPUT_FILE, 'r') as f:
    papers = yaml.safe_load(f)

with open(OUTPUT_FILE, 'r') as f:
    titles = yaml.safe_load(f)

urls = set()
for pub in papers.get('pubs', []):
    urls.update(u for u in pub.get('media', []))

for url in urls:
    if url not in titles:
        titles[url] = fetch_title(url)

with open(OUTPUT_FILE, 'w') as f:
    yaml.dump(titles, f, allow_unicode=True, sort_keys=True, default_flow_style=False)
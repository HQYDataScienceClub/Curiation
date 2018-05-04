#!/env/venv/bin/python3

"""ManningBooks.py
"""

import json
import os
import re
import requests
from bs4 import BeautifulSoup


# 0. Get url content
url = "https://www.manning.com/books/practical-data-science-with-r"
soup = BeautifulSoup(requests.get(url).text, 'html.parser')


# 1. Parse Product Info
title = soup.find("div", class_="product-title").text.strip()
authors = soup.find("div", class_="product-authorship").contents[0].strip()
info = [c.text.strip() for c in soup.find("div", class_="product-info").find("ul").find_all("li")]


# 2. Parse Chapters
chapters = []
for c in soup.find_all("div", class_=re.compile("^sect1 available")):  # TODO: regex: starts with "sect1 available..."
    chapters.append(c.find("h2", id=re.compile("^chapter")))


# 3. Parse Chapter Sections
sections = []
for section in soup.find_all("div", class_=["sect2"]):
    section_clean = section.text.strip()
    sections.append(section_clean)


# 4. Parse Panels
panels = {}
for panel in soup.find_all("div", class_="product-section-panel"):
    p_name = panel.find("div", class_="panel-heading").text
    p_urls = [url.get("href") for url in panel.find_all("a", href=True)]
    panels[p_name] = p_urls


# 5. Save parsed content to file
if not os.path.exists('data'):
    os.makedirs('data')

file_name = os.path.join('data', 'elements.json')
with open(file_name, 'w') as f:
    json.dump({title: []}, f, indent=4)

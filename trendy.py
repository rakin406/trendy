#!/usr/bin/env python3
"""
Check if github repo is trending.
Usage: ./trendy.py <repo>
Example: ./trendy.py trendy
"""

import sys
import requests
from bs4 import BeautifulSoup

URL = "https://github.com/trending"
PAGE = requests.get(URL)

# Get repository name
if len(sys.argv) > 1:
    REPO = sys.argv[1]
else:
    print("Please supply repository name.")
    sys.exit(1)

soup = BeautifulSoup(PAGE.content, "lxml")

# Search all repository links
repo_links = soup.find_all("a")
found = False
for link in repo_links:
    # Check if repository name matches
    repo_name = link.text
    if repo_name.find(REPO) != -1:
        found = True
        break

# Print outcome
if found is True:
    print("Repository is trending!")
else:
    print("Not found.")

#!/usr/bin/env python3
"""
Check if github repo is trending, works with all date ranges.
Usage: ./trendy.py <repo>
Example: ./trendy.py trendy
"""

import sys
import requests
from bs4 import BeautifulSoup

# Get repository name
if len(sys.argv) > 1:
    REPO = sys.argv[1]
else:
    print("Please supply repository name.")
    sys.exit(1)

# All date ranges(today, this week and this month)
URLS = [
    "https://github.com/trending?since=daily",
    "https://github.com/trending?since=weekly",
    "https://github.com/trending?since=monthly",
]

found = False

for url in URLS:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")

    # Search all repository links
    repo_links = soup.find_all("a")
    for link in repo_links:
        # Check if repository name matches
        repo_name = link.text
        if repo_name.find(REPO) != -1:
            if found is False:
                found = True

            # Print outcome with date range
            if url == URLS[0]:
                print("Repository trending today.")
            elif url == URLS[1]:
                print("Repository trending this week.")
            else:
                print("Repository trending this month.")

            break

if found is False:
    print("Not found.")

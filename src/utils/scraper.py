import urllib.request
import re
import csv

from bs4 import BeautifulSoup
import pandas as pd

def scrape_for_wiki_anchors(url, output):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")

    def wiki_anchors(href):
        return href and re.compile("/wiki/").search(href)

    important_anchors = soup.find_all(href=wiki_anchors)

    anchor_list = []
    for a in important_anchors:
        anchor_list.append(a.text)

    with open(output, "w") as f:
        for a in anchor_list:
            f.write(a)
            f.write(',')

    return True

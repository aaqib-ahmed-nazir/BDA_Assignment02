#!/usr/bin/env python
import sys
import re

WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin:
    # splitting input line into article_id and section_text
    article_id, _, _, section_text = line.strip().split(',', 3)

    # extracting words from section_text and printing them with article_id
    for word in WORD_RE.findall(section_text.lower()):
        print(f'{article_id},{word}:1')
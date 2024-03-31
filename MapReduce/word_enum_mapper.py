#!/usr/bin/env python
import sys
import re

WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin:
    # splitting input line into article_id and section_text
    article_id, _, _, section_text = line.strip().split(',', 3)

    # Extract words from section_text and print them with article_id
    words = set(WORD_RE.findall(section_text.lower()))
    for word in words:
        print(f'{word}:{article_id}')

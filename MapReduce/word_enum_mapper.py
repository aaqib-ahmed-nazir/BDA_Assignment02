#!/usr/bin/env python
import sys
import re

WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin:
    # Assuming the line format is: article_id,title,section_title,section_text
    article_id, _, _, section_text = line.strip().split(',', 3)
    words = set(WORD_RE.findall(section_text.lower()))  # Use set for uniqueness
    for word in words:
        print(f'{word}:{article_id}')

#!/usr/bin/env python
import sys
import re

WORD_RE = re.compile(r"[\w']+")

for line in sys.stdin:
    article_id, _, _, section_text = line.strip().split(',', 3)
    for word in WORD_RE.findall(section_text.lower()):
        print(f'{article_id},{word}:1')
#!/usr/bin/env python
import sys

current_word = None
documents = set()

for line in sys.stdin:
    word, doc_id = line.strip().split(':')
    if word != current_word:
        if current_word:
            print(f'{current_word}:{len(documents)}')
        current_word = word
        documents = set()
    documents.add(doc_id)

# Don't forget the last word
if current_word == word:
    print(f'{current_word}:{len(documents)}')

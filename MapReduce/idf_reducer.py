#!/usr/bin/env python
import sys

current_word = None
documents = set()

for line in sys.stdin:
    # split the input from mapper
    word, doc_id = line.strip().split(':')

    # if the word is different from the current word
    if word != current_word:
        if current_word:
            print(f'{current_word}:{len(documents)}')
        current_word = word
        documents = set()

    # add the document to the set
    documents.add(doc_id)
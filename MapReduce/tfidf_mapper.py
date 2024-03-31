#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()

    # distinguish TF from DF based on the line format
    if ',' in line:
        article_id, word, tf_count = line.split(',')
        print(f'TF\t{article_id},{word},{tf_count}')
    else:
        word, df_count = line.split(':')
        print(f'DF\t{word}:{df_count}')

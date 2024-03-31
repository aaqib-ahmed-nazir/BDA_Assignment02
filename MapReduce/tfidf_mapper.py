#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()

    # Distinguish TF from DF based on the line format
    if ',' in line:  # TF format: article_id,word,count
        article_id, word, tf_count = line.split(',')
        # print(f'{word}\tTF:{article_id},{tf_count}')
        print(f'TF\t{article_id},{word},{tf_count}')
    else:  # DF word:count
        word, df_count = line.split(':')
        print(f'DF\t{word}:{df_count}')

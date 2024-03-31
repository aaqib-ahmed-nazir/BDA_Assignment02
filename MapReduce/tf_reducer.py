#!/usr/bin/env python
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, count = line.split(':', 1)
    count = int(count)
    
    if key == current_key:
        current_count += count
    else:
        if current_key:
            # Outputting previous key's count
            article_id, word = current_key.split(',', 1)
            print(f'{article_id},{word},{current_count}')
        current_key = key
        current_count = count

# Outputting the last key's count if there was at least one line of input
if current_key:
    article_id, word = current_key.split(',', 1)
    print(f'{article_id},{word},{current_count}')
#!/usr/bin/env python
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    # splitting input line into key and count
    key, count = line.strip().split(':', 1)
    count = int(count)
    
    # if the key is different from the current key
    if key == current_key:
        current_count += count
    else:
        if current_key:
            # outputting previous key's count
            article_id, word = current_key.split(',', 1)
            print(f'{article_id},{word},{current_count}')
        
        # updating current key and count
        current_key = key
        current_count = count

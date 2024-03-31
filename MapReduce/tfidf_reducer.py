#!/usr/bin/env python
import sys

tf_dict = {}  # Format: {('article_id', 'word'): TF}
df_dict = {}  # Format: {'word': DF}
weight_dict = {}  # Format: {('article_id', 'word'): TF-IDF}

for line in sys.stdin:
    line_type, data = line.strip().split('\t', 1)

    if line_type == 'DF':
        word, df = data.split(':', 1)
        df_dict[word] = int(df)
    elif line_type == 'TF':
        article_id, word, tf = data.split(',', 2)
        key = (article_id, word)
        tf_dict[key] = int(tf)

# After collecting all TF and DF values, calculate TF-IDF for each word in each document
for (article_id, word), tf in tf_dict.items():
    df = df_dict.get(word, 1)  # Default to 1 to avoid division by zero
    tf_idf = tf / df  # Using TF/IDF formula as per your requirement
    weight_dict[(article_id, word)] = tf_idf

# calculate the sparse vectors for each article
article_vectors = {}
for (article_id, word), tf_idf in weight_dict.items():
    if article_id not in article_vectors:
        article_vectors[article_id] = {}
    article_vectors[article_id][word] = tf_idf

# Output the sparse vectors
for article_id, vector in article_vectors.items():
    print(f'{article_id}:{vector}')


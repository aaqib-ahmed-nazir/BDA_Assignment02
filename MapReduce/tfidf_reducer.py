#!/usr/bin/env python
import sys

query = "world history is not the same as historical anarchism"

tf_dict = {}  # Format: {('article_id', 'word'): TF}
df_dict = {}  # Format: {'word': DF}
weight_dict = {}  # Format: {('article_id', 'word'): TF-IDF}
article_vectors = {}
query_vector = {}
similarities = {}

# Collect all TF and DF values
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
for (article_id, word), tf_idf in weight_dict.items():
    if article_id not in article_vectors:
        article_vectors[article_id] = {}
    article_vectors[article_id][word] = tf_idf

# calculate the sparse vector for the query
for term in query.split():
    df = df_dict.get(term, 1)  # Fallback to 1 if DF is not found
    query_vector[term] = 1 / df

# calculate the cosine similarity between the query vector and each article vector
for article_id, vector in article_vectors.items():
    similarity = 0
    for word, weight in query_vector.items():
        similarity += weight * vector.get(word, 0)

    # save similarity score in dict
    similarities[article_id] = similarity

# print the top 5 articles with the highest similarity scores
for article_id, score in sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f'Document {article_id}:{score}')
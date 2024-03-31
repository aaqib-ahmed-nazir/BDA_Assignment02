
# Hadoop MapReduce Naive Search Engine

This repository aims to develop a basic search engine utilizing Hadoop's MapReduce framework to index and process extensive text corpora efficiently. The dataset used for this project is a subset of the English Wikipedia dump, totaling 5.2 GB in size. The project focuses on implementing a naive search algorithm to address challenges in information.


## Dependencies:
To run the Hadoop MapReduce Search Engine, you'll need the following dependencies:

#### Apache Hadoop [(install)](https://hadoop.apache.org/releases.html)

#### Python [(install)](https://www.python.org/downloads/)

#### NLTK [(install)](https://www.nltk.org/)

#### pandas [(install)](https://pandas.pydata.org/docs/getting_started/install.html)

#### numpy [(install)](https://numpy.org/)

#### langdetect [(install)](https://pypi.org/project/langdetect/)

Ensure you have these software and libraries installed on your system before proceeding.




## Features

- Efficient Indexing: Our solution utilizes MapReduce tasks to efficiently analyze the entire corpus and generate unique word IDs, calculate Inverse Document Frequency (IDF), and create a consolidated vocabulary.
- Vectorized Representation: The Indexer component computes a machine-readable representation of the entire document corpus using TF/IDF (Term Frequency-Inverse Document Frequency) weighting, stored as a tuple of (document ID, vector representation).
- Relevance Analysis: The Ranker Engine generates a vectorized representation for user queries and conducts relevance analysis by calculating the relevance function between the query and each document. This enables the retrieval of sorted lists of relevant documents based on relevance scores.


## How to Use

-  Data Preprocessing: Preprocess the dataset by removing stopwords, lemmatizing English words, and splitting it into chunks for efficient processing.

-  Indexing: Run MapReduce tasks for Word Enumeration, Document Count, and Vocabulary creation to establish the index.

-  Query Processing: Process user queries by vectorizing the query, calculating relevance scores, and retrieving relevant documents.

-  Content Extraction: Extract relevant content from the text corpus based on the provided document IDs.


## Why Choose Our Solution

-  Scalability: Our solution is built on Hadoop's MapReduce framework, making it highly scalable and capable of handling large datasets with ease.

-  Accuracy: By employing TF/IDF weighting and relevance analysis, we ensure that search results are accurate and relevant to user queries.

-  Modularity: The project is modular and extensible, allowing for easy integration of additional features or optimizations in the future.
## Usage

1. **Setup:**
   - Clone the repository from [GitHub](https://github.com/aaqib-ahmed-nazir/BDA_Assignment02).
   - Install and configure Hadoop. Refer to the Hadoop documentation for instructions.
   - Ensure all dependencies, including NLTK and pandas, are installed.

2. **Data Preprocessing:**
   - Prepare dataset in CSV format with a text column.
   - Use provided Python scripts for cleaning, stopword removal, and lemmatization.
   - Split dataset into smaller chunks if necessary.

3. **Indexing:**
   - Run MapReduce tasks for word enumeration and document count.
   - Consolidate results into a vocabulary data structure.

4. **Vectorized Representation:**
   - Compute TF/IDF representations for documents using MapReduce.
   - Store TF/IDF representations with document IDs.

5. **Querying:**
   - Construct query with keywords or phrases.
   - Clean query text and calculate TF/IDF values.
   - Compare query vector with document vectors.

6. **Retrieval:**
   - Sort documents based on relevance scores.
   - Retrieve top-ranked documents matching the query.

7. **Integration:**
   - Integrate search engine into application using APIs.
   - Customize functionality as needed.

8. **Maintenance:**
   - Regularly update index and document representations.
   - Monitor performance and optimize resource usage.

Utilize the Hadoop MapReduce Search Engine for efficient indexing, querying, and retrieval of information from large text corpora.

## Team:

Meet the dedicated individuals who contributed to this project:

- **Ammar Khasif:** Check out Ammar's work on [GitHub](https://github.com/ammar-kashif).
- **Arhum Khan:** Explore Arhum's contributions on [GitHub](https://github.com/Arhum-Khan10).
- **Aaqib Ahmed Nazir:** Discover Aaqib's projects on [GitHub](https://github.com/aaqib-ahmed-nazir)

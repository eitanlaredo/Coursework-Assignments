# Coursework & Assignments

A collection of homework assignments and course projects covering core data science and computer science topics.

## Contents

### [Algorithms & Data Structures](./algorithms-and-data-structures)
Implementations of fundamental data structures and algorithms in Python.
- Linked lists and linked list intersection
- Skip list
- Binomial heaps
- Push-relabel max flow

### [Supervised Machine Learning](./supervised-ml)
Classification and regression using standard ML techniques.
- KNN and polynomial regression with scikit-learn
- CNN for MNIST digit classification

### [Unsupervised Machine Learning](./unsupervised-ml)
Clustering, association rules, and dimensionality reduction.
- [Apriori](./unsupervised-ml/apriori) — Association rule mining
- [K-Means](./unsupervised-ml/kmeans) — K-means clustering
- [Dimensionality Reduction](./unsupervised-ml/dim_reduction) — PCA and Kernel PCA

### [Natural Language Processing](./natural-language-processing)
Text representation, classification, and language modeling.
- [Text Representation](./natural-language-processing/text-representation) — One-hot, BoW, TF-IDF, Word2Vec, FastText, GloVe
- [TF-IDF & Word2Vec](./natural-language-processing/tfidf-word2vec) — TF-IDF from scratch and Word2Vec with t-SNE visualization on a quotes corpus
- [N-gram Autocomplete](./natural-language-processing/ngram) — N-gram language model for text autocompletion
- [Newsgroup Classification](./natural-language-processing/newsgroup-classification) — Text classification on the 20 Newsgroups dataset

## Tools & Libraries

Python · Jupyter Notebooks · Pandas · NumPy · scikit-learn · NLTK · Gensim · TensorFlow/Keras · Matplotlib · Seaborn

## Data Files

Some datasets exceed GitHub's 100 MB file size limit and are excluded via `.gitignore`:
- `natural-language-processing/tfidf-word2vec/quotes.csv`
- `natural-language-processing/ngram/en_US.twitter.txt`
### NLP Usage
This project integrates Natural Language Processing (NLP) to analyze customer reviews before clustering.  
The main steps include:

1. **Text Preprocessing**
   - Lowercasing all text
   - Removing special characters, numbers, and punctuation
   - Stopword removal using NLTK
   - Stemming words with PorterStemmer

2. **Feature Extraction**
   - Using **TF-IDF (Term Frequency – Inverse Document Frequency)** to convert reviews into numerical vectors
   - Limiting to the top 100 most informative features

3. **Clustering**
   - Applying algorithms (K-Means, DBSCAN, Hierarchical) on TF-IDF vectors
   - Comparing models using silhouette scores
   - Identifying representative keywords for each cluster

These NLP steps transform unstructured text into structured data, enabling effective clustering and insights from customer reviews.

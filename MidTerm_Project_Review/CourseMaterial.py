import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load the dataset
data = pd.read_csv("CourseMaterial.csv")

# Relevant document IDs for the given query (example)
relevant_documents = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Define a function to retrieve documents based on a query (example function)
def retrieve_documents(query):
    # Example: retrieve documents based on the query using some IR system
    retrieved_documents = data[data['description'].str.contains(query, case=False)]['material_id'].tolist()
    return retrieved_documents

# Define a function to calculate precision, recall, and F1-score
def calculate_metrics(retrieved_documents, relevant_documents):
    # Calculate true positives, false positives, and false negatives
    true_positives = len(set(retrieved_documents) & set(relevant_documents))
    false_positives = len(retrieved_documents) - true_positives
    false_negatives = len(relevant_documents) - true_positives

    # Calculate precision
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0

    # Calculate recall
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else 0

    # Calculate F1-score
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    return precision, recall, f1

# Example query
query = "information retrieval"

# Example of retrieving documents based on the query
retrieved_docs = retrieve_documents(query)

# Calculate metrics
precision, recall, f1 = calculate_metrics(retrieved_docs, relevant_documents)

# Print the 
print("\nMetrics for CourseMaterial.csv:\n")
print("Precision  :    ", precision)
print("Recall     :    ", recall)
print("F1-score   :    ", f1)
print()

import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load the dataset
data = pd.read_csv("SingleQA.csv")

# Define a function to calculate precision, recall, and F1-score
def calculate_metrics(retrieved_docs, relevant_documents):
    # Calculate true positives, false positives, and false negatives
    true_positives = sum([1 for doc_id in retrieved_docs if doc_id in relevant_documents])
    false_positives = len(retrieved_docs) - true_positives
    false_negatives = len(relevant_documents) - true_positives

    # Calculate precision
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) != 0 else 0

    # Calculate recall
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) != 0 else 0

    # Calculate F1-score
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

    return precision, recall, f1

# Example retrieved documents and relevant documents (replace with actual data)
#  Example list of retrieved document IDs
retrieved_docs = [8, 12, 16, 20, 24, 28, 32, 36, 40,
44, 48, 52, 56, 60, 64, 68, 72, 76, 80,
84, 88, 92, 96]
# Example list of relevant document IDs
relevant_documents = [1, 88, 40, 92, 52, 30, 95, 25, 8, 91, 11, 48, 63, 31, 39, 100, 49, 27, 87, 16, 64, 12, 69, 73, 50, 93, 20, 70, 72, 44, 76, 56, 53, 18, 2, 59, 45, 37, 80, 61, 96, 62, 29, 6, 57, 19, 34, 3, 15, 90, 42, 13, 68, 84, 33, 22, 65, 81, 5, 24, 94, 82, 7, 23, 4, 8, 60, 36]  

# Calculate metrics
precision, recall, f1 = calculate_metrics(retrieved_docs, relevant_documents)

# Print the results
print("\nUpdated Metrics for singleQA.csv:\n")
print("Precision  :", precision)
print("Recall     :", recall)
print("F1-score   :", f1)
print()

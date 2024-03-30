import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

# Load the dataset
data = pd.read_csv("MCQ.csv")

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
# Example list of retrieved document ID
retrieved_docs = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
55, 60, 65, 70, 75, 80, 85, 90, 95, 1009]
# Example list of relevant document IDs
relevant_documents = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  

# Calculate metrics
precision, recall, f1 = calculate_metrics(retrieved_docs, relevant_documents)

# Print the results
print("\nMetrics for MCQ.csv:\n")
print("Precision  :", precision)
print("Recall     :", recall)
print("F1-score   :", f1)
print()

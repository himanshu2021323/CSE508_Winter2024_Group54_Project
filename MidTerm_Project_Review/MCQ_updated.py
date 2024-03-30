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
55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
# Example list of relevant document IDs
relevant_documents = [52, 98, 22, 69, 66, 80, 94, 47, 29, 40, 74, 24, 5, 73, 8, 51, 99, 2, 67, 12, 7, 19, 59, 6, 46, 26, 71, 96, 45, 76, 27, 89, 1, 90, 48, 82, 43, 44, 77, 14, 31, 83, 33, 93, 72, 86, 79, 100, 92, 15, 62, 78, 3, 23, 65, 34, 84, 37, 70, 16, 50, 28, 53, 49, 54, 36, 10, 56, 64, 88, 91, 25, 60, 68, 21, 57, 30, 95, 4, 97, 85, 18, 20, 35, 55]  

# Calculate metrics
precision, recall, f1 = calculate_metrics(retrieved_docs, relevant_documents)

# Print the results
print("\nUpdated Metrics for MCQ.csv:\n")
print("Precision  :", precision)
print("Recall     :", recall)
print("F1-score   :", f1)
print()

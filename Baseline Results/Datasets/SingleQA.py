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
retrieved_docs = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,
22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
62, 64, 66, 68, 70, 72, 74, 76, 78, 80,
82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
# Example list of relevant document IDs
relevant_documents = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
33, 36, 39, 42, 45, 48, 51, 54, 57, 60,
63, 66, 69, 72, 75, 78, 81, 84, 87, 90,
93, 96, 99]  

# Calculate metrics
precision, recall, f1 = calculate_metrics(retrieved_docs, relevant_documents)

# Print the results
print("\nMetrics for singleQA.csv:\n")
print("Precision  :", precision)
print("Recall     :", recall)
print("F1-score   :", f1)
print()

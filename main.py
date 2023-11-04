# Original code by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2024.

"""
main.py

This program uses the CADA algorithm to find anomalies in labeled real world datasets.
For each dataset, statistics are shown and the anomalies detected by CADA are displayed.
The result is the number of overlap that CADA detects with the labeled nodes.

Source of datasets: https://github.com/QZ-WANG/ACT/tree/main
"""

from matfile_reader import MatFileReader
from graph_statistics import GraphStatistics
from cada import cada
from sklearn.metrics import f1_score, precision_score, recall_score


def evaluate_dataset(dataset_name, file_path, threshold, num_runs):
    print(f"Evaluating {dataset_name} dataset...")
    mat_file_reader = MatFileReader(file_path)
    graph = mat_file_reader.get_graph()

    # Calculate and display graph statistics
    graph_statistics = GraphStatistics(graph)
    graph_statistics.display_statistics(dataset_name)

    total_yes_count = 0
    total_no_count = 0
    total_total_count = 0
    y_true = []  # True labels
    y_pred = []  # Predicted labels

    for run in range(num_runs):
        # Perform community detection and anomaly detection
        cada_instance = cada(graph, algorithm='louvain', resolution=0.1)
        anomalies = cada_instance.get_anomalies_threshold(threshold=threshold)

        # Get labeled nodes from dataset
        labeled_nodes = [node for node in graph.nodes if graph.nodes[node]['Label'] == 1]

        # Calculate the number of anomalies detected by CADA that are also labeled as anomalous in the dataset
        yes_count = sum(1 for element in anomalies if element in labeled_nodes)
        no_count = len(anomalies) - yes_count
        total_count = len(anomalies)

        total_yes_count += yes_count
        total_no_count += no_count
        total_total_count += total_count

        y_true.extend([1 if node in labeled_nodes else 0 for node in graph.nodes])
        y_pred.extend([1 if node in anomalies else 0 for node in graph.nodes])

    # Calculate unweighted F1 score
    f1 = f1_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    # Calculate weighted F1 score
    weighted_f1 = f1_score(y_true, y_pred, average='weighted')
    weighted_precision = precision_score(y_true, y_pred, average='weighted')
    weighted_recall = recall_score(y_true, y_pred, average='weighted')

    avg_yes_count = total_yes_count / num_runs
    avg_no_count = total_no_count / num_runs
    avg_total_count = total_total_count / num_runs
    avg_percentage_yes = (avg_yes_count / avg_total_count) * 100
    avg_percentage_no = (avg_no_count / avg_total_count) * 100

    # Print results, including weighted F1 score
    print(f"Number of anomalous labeled nodes in {dataset_name}: {len(labeled_nodes)}")
    print(f"Avg Yes count: {avg_yes_count:.2f} ({avg_percentage_yes:.2f}%)")
    print(f"Avg No count: {avg_no_count:.2f} ({avg_percentage_no:.2f}%)")
    print(f"Number of anomalies detected by CADA (Average of {num_runs} runs): {avg_total_count:.2f}")
    print("---------UNWEIGHTED RESULTS----------------")
    print(f"Unweighted F1 Score: {f1:.2f}")
    print(f"Unweighted Precision: {precision:.2f}")
    print(f"Unweighted Recall: {recall:.2f}")
    print("---------WEIGHTED RESULTS------------------")
    print(f"Weighted F1 Score: {weighted_f1:.2f}")
    print(f"Weighted Precision: {weighted_precision:.2f}")
    print(f"Weighted Recall: {weighted_recall:.2f}")
    print("------------------------------------------------------")


# TODO: Tune thresholds for each dataset
if __name__ == "__main__":
    datasets = {
        "Amazon": ('data/node-level-anom/Amazon/Amazon.mat', 5),
        "YelpHotel": ('data/node-level-anom/YelpHotel/YelpHotel.mat', 2),
        "YelpNYC": ('data/node-level-anom/YelpNYC/YelpNYC.mat', 2),
        "YelpRes": ('data/node-level-anom/YelpRes/YelpRes.mat', 2)
    }

    for dataset_name, (file_path, threshold) in datasets.items():
        evaluate_dataset(dataset_name, file_path, threshold, num_runs=3)

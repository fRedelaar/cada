# Original code by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2023.

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


def evaluate_dataset(dataset_name, file_path, threshold):
    print(f"Evaluating {dataset_name} dataset...")
    mat_file_reader = MatFileReader(file_path)
    graph = mat_file_reader.get_graph()

    # Calculate and display graph statistics
    graph_statistics = GraphStatistics(graph)
    graph_statistics.display_statistics(dataset_name)

    # Perform community detection and anomaly detection
    cada_instance = cada(graph, algorithm='louvain', resolution=0.1)
    anomalies = cada_instance.get_anomalies_threshold(threshold=threshold)

    # Get labeled nodes from dataset
    labeled_nodes = [node for node in graph.nodes if graph.nodes[node]['Label'] == 1]

    # Calculate the number of anomalies detected by CADA that are also labeled as anomalous in the dataset
    yes_count = sum(1 for element in anomalies if element in labeled_nodes)
    no_count = len(anomalies) - yes_count
    total_count = len(anomalies)
    percentage_yes = (yes_count / total_count) * 100
    percentage_no = (no_count / total_count) * 100

    # Print results
    # The yes count is the number of anomalies detected by CADA that are also labeled as anomalous in the dataset
    print(f"Number of anomalous labeled nodes in {dataset_name}: {len(labeled_nodes)}")
    print(f"Yes count: {yes_count} ({percentage_yes:.2f}%)")
    print(f"No count: {no_count} ({percentage_no:.2f}%)")
    print("Anomalies detected by CADA:", anomalies)
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
        evaluate_dataset(dataset_name, file_path, threshold)

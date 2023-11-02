# Original code by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2023.

"""
graph_statistics.py

This module provides a class for calculating and displaying graph statistics.
"""

import networkx as nx
import matplotlib.pyplot as plt

class GraphStatistics:
    def __init__(self, graph):
        self.graph = graph

    def display_statistics(self, dataset_name):
        # Calculate and display graph statistics
        num_nodes = len(self.graph.nodes)
        num_edges = len(self.graph.edges)
        density = nx.density(self.graph)
        average_clustering = nx.average_clustering(self.graph)
        degree_histogram = nx.degree_histogram(self.graph)

        print(f"Number of nodes: {num_nodes}")
        print(f"Number of edges: {num_edges}")
        print(f"Graph density: {density}")
        print(f"Average clustering coefficient: {average_clustering}")

        # Plot histogram showing the distribution of node labels (0 or 1)
        label_values = [self.graph.nodes[node]['Label'] for node in self.graph.nodes]

        # Count the occurrences of 0 and 1
        count_0 = label_values.count(0)
        count_1 = label_values.count(1)

        # Display the histogram
        labels = [0, 1]
        counts = [count_0, count_1]

        plt.bar(labels, counts, tick_label=labels)
        plt.xlabel('Label Value')
        plt.ylabel('Frequency of nodes')
        plt.title(f'Distribution of Label Values - {dataset_name}')

        # Display the count numbers above the bars
        for i, count in enumerate(counts):
            plt.text(labels[i], count, str(count), ha='center', va='bottom')

        plt.show()

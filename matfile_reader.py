# Original code by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2024.

"""
matfile_reader.py

This module provides a class for reading in matlab files and converting them to networkx graphs.
"""

from scipy.io import loadmat
import networkx as nx
from scipy.sparse import csc_matrix

class MatFileReader:
    def __init__(self, file_path):
        self.data = loadmat(file_path)

    def get_graph(self):
        # Extract the 'Network' data and create a graph
        network_matrix = self.data['Network']
        network_matrix = csc_matrix(network_matrix)
        graph = nx.Graph(network_matrix)

        # Extract the 'Label' data
        label_data = self.data['Label'].flatten()

        # Add 'Label' attribute to graph nodes
        for node, label in zip(graph.nodes, label_data):
            graph.nodes[node]['Label'] = label

        # Extract the 'Attributes' data
        attributes_data = self.data['Attributes']

        # Add 'Attributes' attribute to graph nodes
        for node, attributes in zip(graph.nodes, attributes_data):
            graph.nodes[node]['Attributes'] = attributes

        return graph

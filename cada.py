# Source: https://github.com/thomashelling/cada
# Modified by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# (Implemented LPA and the Leiden algorithms)
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2024.

"""
cada.py

This module was written originally by Thomas Helling et al. This module contains the CADA algorithm for all four variants.
"""

import numpy as np
import community
import infomap
import networkx as nx
import leidenalg as la
import igraph as ig

class cada():
    def __init__(self, graph, algorithm='leiden', resolution=0.1):
        # First do community detection
        if algorithm == 'louvain':
            partition = community.best_partition(graph, resolution=resolution)

        elif algorithm == 'infomap':
            partition = self.run_infomap(graph)

        elif algorithm == 'label_propagation':
            partition = self.run_label_propagation(graph)

        elif algorithm == 'leiden':
            partition = self.run_leiden(graph, resolution=resolution)

        else:
            raise ValueError("Invalid algorithm. Choose 'louvain', 'infomap', 'label_propagation' or 'leiden'.")

        anom_score = {}
        for node in graph.nodes():
            comms = {}
            for neighbor in graph.neighbors(node):
                if neighbor != node:
                    if partition[neighbor] not in comms:
                        comms[partition[neighbor]] = 0

                    comms[partition[neighbor]] += 1

            if len(comms) > 0:
                comms = np.array(list(comms.values()))
                max_com = np.max(comms)
                comms = comms / max_com
                anom_score[node] = np.sum(comms)

        self.anomaly_scores = sorted(anom_score.items(), key=lambda x: x[1])[::-1]

    def run_infomap(self, graph):
        """
        Runs Infomap with infomap package
        """
        infomapSimple = infomap.Infomap("--two-level --silent")

        for e in graph.edges():
            infomapSimple.addLink(int(e[0]), int(e[1]))

        infomapSimple.run()

        partition = {}
        for node in infomapSimple.iterTree():
            if node.isLeaf():
                partition[node.physicalId] = node.moduleIndex()

        return partition

    def run_label_propagation(self, graph):
        """
        Runs Label Propagation Algorithm with NetworkX package
        """
        partition = nx.algorithms.community.label_propagation.label_propagation_communities(graph)
        partition = {node: comm_index for comm_index, community in enumerate(partition) for node in community}
        return partition

    def run_leiden(self, graph, resolution):
        """
        Runs Leiden Algorithm with leidenalg
        """
        if isinstance(graph, nx.Graph):
            # Convert networkx graph to igraph
            graph = ig.Graph.TupleList(graph.edges(), directed=False)

        partition = la.find_partition(graph, la.ModularityVertexPartition)
        return dict(zip(graph.vs.indices, partition.membership))

    def get_anomaly_scores(self, nr_anomalies=None):
        """
        Returns tuple (node, anomaly_score) for either nr_anomalies or all
        """
        if nr_anomalies:
            return self.anomaly_scores[:nr_anomalies]
        else:
            return self.anomaly_scores

    def get_top_anomalies(self, nr_anomalies=100):
        """
        Returns the highest scoring anomalies
        """
        anomalies = [anomaly[0] for anomaly in self.anomaly_scores[:nr_anomalies]]
        return anomalies

    def get_anomalies_threshold(self, threshold):
        """
        Returns anomalies that are above a certain threshold.
        """
        anomalies = [anomaly[0] for anomaly in self.anomaly_scores if anomaly[1] > threshold]
        return anomalies
# Original code by Thomas Helling
# Source: https://github.com/thomashelling/cada
# Modified by Felicia Redelaar (s1958410) and Louka Wijne (s2034697) for SNACS
# SNACS: Social Network Analysis for Computer Scientists
# Leiden University, 2023 - 2024.

import numpy as np
import community
import infomap

class cada():
    def __init__(self, graph, algorithm='louvain', resolution=0.1):
        # First do community detection
        if algorithm == 'louvain':
            partition = community.best_partition(graph, resolution=resolution)

            # Version for Louvain
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
                    # print('Anomaly score., ', anom_score[node], 'Node', node)

        else:
            partition = self.run_infomap(graph)

            # Altered version for Infomap
            anom_score = {}
            for node in graph.nodes():
                comms = {}
                for neighbor in graph.neighbors(node):
                    if neighbor != node:
                        neighbor_key = int(neighbor)  # Convert neighbor to the appropriate type
                        if neighbor_key in partition:
                            if partition[neighbor_key] not in comms:
                                comms[partition[neighbor_key]] = 0

                            comms[partition[neighbor_key]] += 1

                if len(comms) > 0:
                    comms = np.array(list(comms.values()))
                    max_com = np.max(comms)
                    comms = comms / max_com
                    anom_score[node] = np.sum(comms)
                    # print('Anomaly score., ', anom_score[node], 'Node', node)

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
        anomalies = []
        for anomaly in self.anomaly_scores[:nr_anomalies]:
            anomalies.append(anomaly[0])

        return anomalies

    def get_anomalies_threshold(self, threshold):
        """
        Returns anomalies that are above a certain threshold.
        """
        anomalies = []

        for anomaly in self.anomaly_scores:
            if anomaly[1] > threshold:
                anomalies.append(anomaly[0])
            else:
                break

        return anomalies

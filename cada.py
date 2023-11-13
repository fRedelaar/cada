import numpy as np
import community
import infomap
import networkx as nx

class cada():
    def __init__(self, graph, algorithm='louvain', resolution=0.1, weight_attribute='Attributes'):
        # First do community detection
        if algorithm == 'louvain':
            partition = community.best_partition(graph, resolution=resolution, weight=weight_attribute)

        elif algorithm == 'infomap':
            partition = self.run_infomap(graph)

        elif algorithm == 'label_propagation':
            partition = self.run_label_propagation(graph)

        else:
            raise ValueError("Invalid algorithm. Choose 'louvain', 'infomap', or 'label_propagation'.")

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
        Runs Label Propagation Algorithm with NetworkX
        """
        partition = nx.algorithms.community.label_propagation.label_propagation_communities(graph)
        partition = {node: comm_index for comm_index, community in enumerate(partition) for node in community}
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
        anomalies = [anomaly[0] for anomaly in self.anomaly_scores[:nr_anomalies]]
        return anomalies

    def get_anomalies_threshold(self, threshold):
        """
        Returns anomalies that are above a certain threshold.
        """
        anomalies = [anomaly[0] for anomaly in self.anomaly_scores if anomaly[1] > threshold]
        return anomalies

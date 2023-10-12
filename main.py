import networkx as nx
from cada import cada


# Initialize an empty graph
graph = nx.Graph()

# Read the data from file
with open('data/small-test-data/medium.tsv', 'r') as file:
    for line in file:
        edge = line.strip().split('\t')
        if len(edge) == 2:
            source, target = edge
            graph.add_edge(source, target)


# Specify the algorithm and resolution
algorithm = 'louvain'  # Infomap is also supported by cada module
resolution = 0.1

# Create an instance of 'cada' with the graph
cada_instance = cada(graph, algorithm=algorithm, resolution=resolution)

# Method 1: Get the top N anomalies
top_anomalies = cada_instance.get_top_anomalies(nr_anomalies=10)  # Can be changed..

# Method 2: Get anomalies above a certain threshold
threshold = 0.5  # Should be tuned or set based on paper (?)
anomalies_above_threshold = cada_instance.get_anomalies_threshold(threshold)

# # Method 3: Get all anomalies (sorted by score)
# all_anomalies = cada_instance.get_anomaly_scores()

# Print or use the list of anomalies as needed
print("Top Anomalies:", top_anomalies)
print("Anomalies Above Threshold:", anomalies_above_threshold)
# print("All Anomalies:", all_anomalies)
# print("Length of all anomalies:", len(all_anomalies))

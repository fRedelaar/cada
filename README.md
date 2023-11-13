# Node Anomaly Detection project for SNACS
This repository contains code for the Social Network Analysis for Computer Scientists (SNACS) 2023/2024 project at Leiden University. 
For this project, we have used the CADA algorithm [1] to detect node anomalies in labelled real world networks. 
Furthermore, we have implemented a third out-of-the-box community detection algorithm, namely ... . 


The code in this repository is based on the code from the original CADA repository, which can be found [here](https://github.com/thomashelling/cada).


## Getting Started
To get started and use the code in this repository, you need to have Python 3.9 or higher installed, since this is a requirement of NetworkX. 

### Installation
To install the required packages, run the following command in the root directory of this repository:
```
pip install -r requirements.txt
```
## To do
- [x] Read and process data
- [x] Calculate graph statistics
- [x] Setup evaluation framework
- [x] Implement (weighted) F1-score
- [x] Tune threshold parameter for the 4 datasets
- [ ] Get results of (un)weighted F1 for CADA for the 4 datasets
  - [x] Louvain
  - [x] Infomap
  - [x] LPA
- [x] Add third community detection algorithm - LPA
- [ ] Add weighted/unweighted option

## Authors of SNACS project
- Louka Wijne (s2034697)
- Felicia Redelaar (s1958410)


# CADA (Original repository)
Community-aware detection of anomalies [1]

This is the code for detecting node anomalies in networks with NetworkX by including community structure from two out-of-the-box community detection algorithms: (1) Louvain [2], and (2) Infomap [3]. The algorithm is described <a href="https://link.springer.com/chapter/10.1007/978-3-030-05411-3_20">here</a>. 

For (1), Python package <a href="https://github.com/taynaud/python-louvain">Python-Louvain</a> is used. 

For (2), Python package <a href="https://pypi.org/project/infomap/">Infomap</a> is used.

[1] Helling, T.J., Scholtes, J. C., Takes, F.W. A community-aware approach for identifying node anomalies in complex networks. In Proceedings of the 7th International Conference on Complex Networks, CI, pages 244–255. Springer, 2019.

[2] Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment10008(10), 6 (2008)

[3] Rosvall, M., Bergstrom, C.: Maps of random walks on complex networks reveal community structure. Proceedings of National Academy of Sciences,105(4), 1118–1123 (2008)

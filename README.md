# Node Anomaly Detection project for SNACS
This repository contains code for the Social Network Analysis for Computer Scientists (SNACS) 2023/2024 project at Leiden University. 
For this project, we have used the CADA algorithm [1] to detect node anomalies in labelled real world networks. The CADA algorithm uses two out-of-the-box community detection algorithms, namely Louvain [2], and Infomap [3].
For this project, we have forked the CADA algorithm and we have implemented a third and fourth out-of-the-box community detection algorithm, namely the Label Propagation algorithm (LPA) [4, 5], and the Leiden algorithm [6].


The code in this repository is based on the code from the original CADA repository, which can be found [here](https://github.com/thomashelling/cada).


## Getting Started
To get started and use the code in this repository, you need to have Python 3.9 or higher installed, since this is a requirement of NetworkX. 

### Installation
To install the required packages, run the following commands in the root directory of this repository:

```
python -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
```

### Running the experiments
Adjust the wanted CADA algorithm in main.py on line 38 and cada.py on line 15. Do not forget to adjust the thresholds accordingly to Table 1, in main.py lines 96-99. Run the experiments using the following command:

```
python main.py
```
This will generate statistics for each network, and run the experiments. 


## Parameters used for datasets
|        | Amazon | YelpHotel | YelpNYC | YelpRes |
|--------|--------|-----------|---------|---------|
| CADA_L | 5.0    | 3.5       | 3.5     | 3       |
| CADA_I | 3.25   | 1.75      | 4.75    | 2.75    |
| CADA_LPA | 1.25  | 2.5       | 1.5     | 1.75    |
| CADA_LEI | 6.5   | 7.25      | 9       | 7.5     |

Table: Threshold table for each **CADA** variant

## Authors of SNACS project
- Louka Wijne (s2034697)
- Felicia Redelaar (s1958410)


# References
For Louvain, Python package <a href="https://github.com/taynaud/python-louvain">Python-Louvain</a> is used. 

For Infomap, Python package <a href="https://pypi.org/project/infomap/">Infomap</a> is used.

For LPA, Python package <a href="https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.community.label_propagation.label_propagation_communities.html">NetworkX</a> is used.

For Leiden, Python package <a href="https://pypi.org/project/leidenalg/">leidenalg</a> is used.

[1] Helling, T.J., Scholtes, J. C., Takes, F.W. A community-aware approach for identifying node anomalies in complex networks. In Proceedings of the 7th International Conference on Complex Networks, CI, pages 244–255. Springer, 2019.

[2] Blondel, V.D., Guillaume, J.L., Lambiotte, R., Lefebvre, E.: Fast unfolding of communities in large networks. Journal of Statistical Mechanics: Theory and Experiment10008(10), 6 (2008)

[3] Rosvall, M., Bergstrom, C.: Maps of random walks on complex networks reveal community structure. Proceedings of National Academy of Sciences,105(4), 1118–1123 (2008)

[4] Usha Nandini Raghavan, Réka Albert, and Soundar Kumara. 2007. Near linear time algorithm to detect community structures in large-scale networks. Physical review E 76, 3 (2007)

[5] Xiaojin Zhu and Zoubin Ghahramani. 2002. Learning from labeled and unlabeled data with label propagation. (2002)

[6]  Traag, V. A., Waltman, L., and van Eck, N. J. From Louvain to Leiden: guaranteeing well-connected communities. Scientific Reports 9, 1 (mar 2019)


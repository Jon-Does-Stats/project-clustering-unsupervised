## Primary project objective

- Create a tool that ingests tabular data files of various formats and conducts unsupervised clustering using the k-means algorithm. Two or three variable datasets are currently supported. The stand-alone tool outputs the coordinate values for the calculated centroids, a membership list for each, and a visual representation of the resulting clusters for two-variable datasets.

## Primary language

- Python

## Highlighted visualizations
- (three images below) Centroid and membership visualization for demonstration for the first example dataset, `aggregation.csv`. Here, user has set K = 5, 7, and 9. Each color represents a cluster, and each cluster has a centroid represented with an 'X' symbol.  See the repository's output folder for centroid locations (filename syntax of `agg_K_equal_<.value>_clusters.csv`) and membership lists (filename syntax of `agg_K_equal_<.value>_points.csv`).

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/agg_K_equal_5_plot.png" width=675>

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/agg_K_equal_7_plot.png" width=675>

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/agg_K_equal_9_plot.png" width=675>

- (three images below) Centroid and membership visualization for demonstration for the second example dataset, `s1.txt`. Here, user has set K = 10, 15, and 20 Each color represents a cluster, and each cluster has a centroid represented with an 'X' symbol.  See the repository's output folder for centroid locations (filename syntax of `s1_K_equal_<.value>_clusters.csv`) and membership lists (filename syntax of `s1_K_equal_<.value>_points.csv`).

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/s1_K_equal_10_plot.png" width=675>

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/s1_K_equal_15_plot.png" width=675>

<img src="https://raw.githubusercontent.com/Jon-Does-Stats/project-clustering-unsupervised/main/figures/s1_K_equal_20_plot.png" width=675>



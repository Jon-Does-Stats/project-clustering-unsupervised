import os
from libs.MyKmean import MyKmeans
from libs.MyKmean import save_clust_points_img
from libs.MyKmean import save_clust_points_csv

# output directory
if not os.path.isdir("./output/"):
    os.mkdir("./output/")

if not os.path.isdir("./figures/"):
    os.mkdir("./figures/")

# NOTE: MAY NEED TO CLEAR OUT OUTPUT PNGS
def main():
    chosen_k = [10, 15, 20]
    output_prefix = "s1"
    instance = MyKmeans(k=1)
    instance.read_xy_from_file(file_path="./data/s1.txt", delimiter="\t")
    for k in chosen_k:
        instance.k = k
     #   instance.generate_points()
        instance.assign_random_clust_number()
        instance.initialize_centroids()
        flag_terminate = False
        while not flag_terminate:
            instance.assign_clust_number()
            flag_terminate = instance.update_centroid()
        fp_prefix0 = "./output/"
        fp_prefix1 = "_K_equal_"
        fp_prefix2 = "./figures/"
	fp_suffix1 = "_plot.png"
        fp_suffix2 = "_points.csv"
        fp_suffix3 = "_clusters.csv"
        fp1 = fp_prefix2 + output_prefix + fp_prefix1 + str(k) + fp_suffix1
        fp2 = fp_prefix0 + output_prefix + fp_prefix1 + str(k) + fp_suffix2
        fp3 = fp_prefix0 + output_prefix + fp_prefix1 + str(k) + fp_suffix3
        save_clust_points_img(instance, fp1)
        save_clust_points_csv(instance, point_file_path = fp2, clust_file_path = fp3)

    output_prefix = "agg"
    chosen_k = [5, 7, 9]
    instance = MyKmeans(k=k)
    instance.read_xy_from_file(file_path="./data/aggregation.csv", delimiter=",")
    for k in chosen_k:
        instance.k = k
      #  instance.generate_points()
        instance.assign_random_clust_number()
        instance.initialize_centroids()
        flag_terminate = False
        while not flag_terminate:
            instance.assign_clust_number()
            flag_terminate = instance.update_centroid()
        fp_prefix0 = "./output/"
        fp_prefix1 = "_K_equal_"
        fp_suffix1 = "_plot.png"
        fp_suffix2 = "_points.csv"
        fp_suffix3 = "_clusters.csv"
        fp1 = fp_prefix0 + output_prefix + fp_prefix1 + str(k) + fp_suffix1
        fp2 = fp_prefix0 + output_prefix + fp_prefix1 + str(k) + fp_suffix2
        fp3 = fp_prefix0 + output_prefix + fp_prefix1 + str(k) + fp_suffix3
        save_clust_points_img(instance, fp1)
        save_clust_points_csv(instance, point_file_path = fp2, clust_file_path = fp3)

if __name__ == "__main__":
    main()


##############################################
############ K MEANS ADVANTAGES ##############

# it is an easy-to-understand, fairly easy-to-implement algorithm.

# it scaled well from 10 to 750 to 2500 points, and from 5 to 20 clusters.

# the process visualizes well, aiding in understanding.

##############################################
########## K MEANS DISADVANTAGES #############

# We have to choose K, and how do we really know the underlying data's properties?

# multiple runs on the same dataset don't result in identical outputs, meaning that the cluster locations are
# sensitive to initial values.

# The algorithm seems to want to make equal sized clusters. I can't be sure if its the way the data was generated,
# but it seems like in all my output plots, the clusters are near equal size and density with each other.

# The algorithm as I have written it is not very fast. It takes a minute or two to run with only a 500-2500 pts. I have
# personally had geospatial datasets with 100,000+ observations.

# The algorithm only works with numerical data.
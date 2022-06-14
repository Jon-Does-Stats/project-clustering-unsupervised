import sys, csv
import numpy as np
from matplotlib import pyplot as plt
from random import sample, shuffle
from .Utility import get_rand_pt, check_same_coordinate
from .Point import pt

class MyKmeans:
    def __init__(self, k, num_points=10, dimension=2, lower_bound=(0, 0), upper_bound=(10, 10)):
        self.k = k
        self.num_points = num_points
        self.dim = dimension
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.points = list()
        self.centroids = dict()

    def set_parameters(self):
        k = input("Set k, number of clusters. s to skip.")
        num_points = input("Set number of points. s to skip.")
        dimension = input("Set dimension. s to skip.")
        lower_bound = input("Set lower bound with tuple. s to skip.")
        upper_bound = input("Set upper bound with tuple. s to skip.")

        if not k == "s":
            self.k = int(k)

        if not num_points == "s":
            self.num_points = int(num_points)

        if not dimension == "s":
            self.dim = int(dimension)

        if not lower_bound == "s":
            self.lower_bound = lower_bound

        if not upper_bound == "s":
            self.upper_bound = upper_bound


    def generate_points(self):
        arg1 = self.num_points
        arg2 = self.dim
        arg3 = self.lower_bound
        arg4 = self.upper_bound

        self.points = get_rand_pt(num_points = arg1, dimension = arg2, lower_bound = arg3, upper_bound = arg4)
        print("{n} points of dimension {dim} stored in points".format(n=arg1, dim=arg2))

    def initialize_centroids(self):
        starts = sample(self.points, self.k)

        for i in range(self.k):
            starting_point = starts[i]

            if self.dim == 2:
                point = [starting_point[0], starting_point[1]]
            else:
                point = [starting_point[0], starting_point[1], starting_point[2]]
            center = pt(*point)
            self.centroids[i + 1] = center
        print("centroids initialized at: {}".format(self.centroids))

    def assign_random_clust_number(self):
        for point in self.points:
            point.clust_id = sample(range(1, self.k + 1), 1)
        print("random cluster id between 1 to {k} assigned to each point in points".format(k=self.k))

    def assign_clust_number(self):
        """Assign the nearest centroid's cluster id to each point in points.
        - min_dist is initialized at extreme value so centroid 1's cluster
          id is always assigned to each point to start.
        - distances are then calculated to each centroid 2 to k.
        - during that process, if any centroid is closer to point
          than a previous centroid, its cluster id is newly assigned to the
          point, overwriting the previous.
        - at the end of the loop, each point is assigned the cluster
          id of the nearest centroid.
        """
        for point in self.points:
            min_dist = sys.maxsize
            for i in self.centroids:
                dist = point.calc_distance(self.centroids[i])
                if min_dist > dist:
                    min_dist = dist
                    point.clust_id = i
        print("nearest centroid's cluster id assigned to each point")

    def update_centroid(self):
        flag_all_same_coordinate = True

        for i in self.centroids:
            ref_centroid = self.centroids[i]
            ref_clust_id = i
            x_coord_sum = 0
            y_coord_sum = 0
            z_coord_sum = 0
            point_count = 0

            for point in self.points:
                if self.dim == 2:
                    if point.clust_id == ref_clust_id:
                        point_count += 1
                        x_coord_sum += point.x
                        y_coord_sum += point.y
                else:
                    if point.clust_id == ref_clust_id:
                        point_count += 1
                        x_coord_sum += point.x
                        y_coord_sum += point.y
                        z_coord_sum += point.z

            if point_count > 0:
                if self.dim == 2:
                    point = [x_coord_sum / point_count, y_coord_sum / point_count]
                    center = pt(*point)
                    self.centroids[i] = center
                    flag_all_same_coordinate = check_same_coordinate(center, ref_centroid)
                else:
                    point = [x_coord_sum / point_count, y_coord_sum / point_count, z_coord_sum / point_count]
                    center = pt(*point)
                    self.centroids[i] = center
                    flag_all_same_coordinate = check_same_coordinate(center, ref_centroid)
        return flag_all_same_coordinate

    def read_xy_from_file(self, file_path = "../data/s1.txt", delimiter = "\t"):
        self.points = list()
        f = open(file_path, "r")
        lines = list()
        line = True
        for line in f.readlines():
            lines.append(line.strip().split(delimiter))
        f.close()
        x_min = 1e100
        y_min = 1e100
        x_max = -1e100
        y_max = -1e100

        for pair in lines:
            x = float(pair[0])
            y = float(pair[1])
            if x < x_min:
                x_min = x
            if x > x_max:
                x_max = x
            if y < y_min:
                y_min = y
            if y > y_max:
                y_max = x
            point = [x, y]
            classobj = pt(*point)
            self.points.append(classobj)
        lb = (x_min,y_min)
        ub = (x_max,y_max)
        self.lower_bound = lb
        self.upper_bound = ub
        self.num_points = len(self.points)
        return print("{} points read from file." .format(self.points))



def plot_clust_points(mykmean, pt_size=100, centroid_size=200, pt_marker="o", centroid_marker="x"):
    # create a color map object based on a rainbow colormap
    cmap = plt.cm.get_cmap("rainbow", mykmean.k)
     # randomize color index list
    idx_sh = list(range(mykmean.k))
    shuffle(idx_sh)
     # assign a color for points and centroids by cluster
    for i in mykmean.points:
         color = np.array(cmap(idx_sh[i.clust_id - 1])).reshape(1, -1)
         plt.scatter(i.x, i.y, c=color, marker=pt_marker, s=pt_size)

    for i in mykmean.centroids:
        pt = mykmean.centroids[i]
        pt.clust_id = i
        color = np.array(cmap(idx_sh[pt.clust_id - 1])).reshape(1, -1)
        plt.scatter(pt.x, pt.y, c=color, marker=centroid_marker, s=centroid_size)
    plt.show()



def save_clust_points_img(mykmean, out_file_path, pt_size = 100, centroid_size = 200, pt_marker = "o", centroid_marker= "x", pt_alpha = 0.5, centroid_alpha = 1):
    """
    :param mykmean: MyKmeans' instance (MyKmeans)
    :param out_file_path: output file path (string)
    :param pt_size: point size (integer)
    :param centroid_size: centroid point size (integer
    :param pt_marker: point marker type defined under matplotlib.markers (string/integer)
    :param centroid_marker: centroid marker type defined under matplotlib.markers (string/integer)
    :return: None
    """
    # create a color map object based on a rainbow colormap
    cmap = plt.cm.get_cmap("rainbow", mykmean.k)
    # randomize color index list
    idx_sh = list(range(mykmean.k))
    shuffle(idx_sh)
    # assign a color for points and centroids by cluster
    for i in mykmean.points:
        plt.scatter(i.x, i.y, c=[cmap(idx_sh[i.clust_id - 1])], marker=pt_marker, s=pt_size, alpha=pt_alpha)

    for i in mykmean.centroids:
        pt = mykmean.centroids[i]
        pt.clust_id = i
        plt.scatter(pt.x, pt.y, c=[cmap(idx_sh[pt.clust_id - 1])], marker=centroid_marker, s=centroid_size, alpha = centroid_alpha)
    plt.savefig(out_file_path)
    plt.clf()



def save_clust_points_csv(mykmean, point_file_path, clust_file_path):
    f = open(point_file_path, 'w')
    header = ["id", "x", "y", "cluster"]
    data = [ ]
    id = 1
    for point in mykmean.points:
        line = [id, point.x, point.y, point.clust_id]
        data.append(line)
        id += 1
    with open(point_file_path, "w", encoding="UTF8", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

    g = open(clust_file_path, 'w')
    header = ["cluster", "centroid_x", "centroid_y"]
    data = [ ]
    for i in mykmean.centroids:
        clust = mykmean.centroids[i]
        line = [i, clust.x, clust.y]
        data.append(line)
    with open(clust_file_path, "w", encoding="UTF8", newline='') as g:
        writer = csv.writer(g)
        writer.writerow(header)
        writer.writerows(data)

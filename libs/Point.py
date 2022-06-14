import math


class pt:

    def __init__(self, x, y, z=None, clust_id=-1):
        self.x = x
        self.y = y
        self.z = z
        self.clust_id = clust_id  # CLUSTER ID HERE
        if z is None:
            self.dim = 2
        else:
            self.dim = 3

    def __repr__(self):
        if self.dim == 3:
            return "(" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ")"
        elif self.dim == 2:
            return "(" + str(self.x) + ", " + str(self.y) + ")"
        else:
            return "dim error"

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z

    def print_coords(self):
        if self.dim == 3:
            print("({x}, {y}, {z}) \nCluster: {cluster}".format(x=self.x, y=self.y, z=self.z, cluster=self.clust_id))
        elif self.dim == 2:
            print("({x}, {y}) \nCluster: {cluster}".format(x=self.x, y=self.y, cluster=self.clust_id))
        else:
            print("Dimension error!")

    def print_dim(self):
        print(self.dim)

    def calc_distance(self, other_point):
        if isinstance(other_point, pt) == False:
            print("ERROR! Object supplied to calc_distance() is not of the proper class <pt>")
        else:
            if self.dim == 2:
                if other_point.dim == 2:
                    x2 = other_point.x
                    y2 = other_point.y
                    try:
                        distance = math.sqrt(((x2 - self.x) ** 2) + ((y2 - self.y) ** 2))
                    except Exception as e:
                        return print("error type:{} \nerror message:{}".format(type(e), e))
                    distance = math.sqrt(((x2 - self.x) ** 2) + ((y2 - self.y) ** 2))
                else:
                    return print("ERROR! Comparison point does not have same coordinate dimensions.")

            if self.dim == 3:
                if other_point.dim == 3:
                    x2 = other_point.x
                    y2 = other_point.y
                    z2 = other_point.z
                    try:
                        distance = math.sqrt(((x2 - self.x) ** 2) + ((y2 - self.y) ** 2) + ((z2 - self.z) ** 2))
                    except Exception as e:
                        return print("error type:{} \nerror message:{}".format(type(e), e))
                    distance = math.sqrt(((x2 - self.x) ** 2) + ((y2 - self.y) ** 2) + ((z2 - self.z) ** 2))
                else:
                    return print("ERROR! Comparison point does not have same coordinate dimensions.")
            return distance
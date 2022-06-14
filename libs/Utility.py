import random
from .Point import pt

def get_rand_pt(num_points=10, dimension=2, lower_bound=(0, 0), upper_bound=(10, 10)):
    pt_list = list()

    if dimension == 2:
        for i in range(num_points):
            x_var = random.uniform(lower_bound[0], upper_bound[0])
            y_var = random.uniform(lower_bound[1], upper_bound[1])
            point = [x_var, y_var]
            obj = pt(*point)
            pt_list.append(obj)

        return pt_list

    elif dimension == 3:
        try:
            z_var = random.uniform(lower_bound[2], upper_bound[2])

        except Exception as e:
            return print("Error, did you provide coordinates with 3 dimensions?  \nerror message:{}".format(e))

        for i in range(num_points):
            x_var = random.uniform(lower_bound[0], upper_bound[0])
            y_var = random.uniform(lower_bound[1], upper_bound[1])
            z_var = random.uniform(lower_bound[2], upper_bound[2])
            point = [x_var, y_var, z_var]
            obj = pt(*point)
            obj.dim = 3
            pt_list.append(obj)
        return pt_list

    else:
        return print("Dimension problem. Function supports only dim = 2 or 3.")


def check_same_coordinate(point1, point2):
        check_dist = point1.calc_distance(point2)
        return check_dist == 0
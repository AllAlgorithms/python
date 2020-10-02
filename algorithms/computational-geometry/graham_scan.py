'''
Layout: algorithms
Title : Graham Scan Algorithm
Author: RadientBrain
'''


from random import randint
import matplotlib.pyplot as plt


def orientation(m, n, o):
    val = ((n[1]-m[1])*(o[0]-n[0])) - ((o[1]-n[1])*(n[0]-m[0]))
    if val > 0:
        return 1
    elif val < 0:
        return -1
    else:   
        return 0

def distance(m, n):
    return (n[0]-m[0])**2 + (n[1]-m[1])**2

def Sorting_with_bubble(coordinates, b):
    for coord_ith in range(len(coordinates)):
        for j in range(len(coordinates)-coord_ith-1):
            if (orientation(b, coordinates[j], coordinates[j+1]) > 0) or (orientation(b, coordinates[j], coordinates[j+1])==0 and (distance(b, coordinates[j]) > distance(b, coordinates[j+1]))):
                temp = coordinates[j+1]
                coordinates[j+1] = coordinates[j]
                coordinates[j] = temp

    return coordinates


def Convex_hull_through_graham(coordinates):
    b = min(coordinates, key= lambda coord: (coord[1], coord[0]))
    coord_ith = coordinates.index(b)
    coordinates[coord_ith]=coordinates[0]
    coordinates[0] = b
    coordinates = [b] + Sorting_with_bubble(coordinates[1:], b)
    size_triplet = [coordinates[0], coordinates[1], coordinates[2]]
    for coord_ith in range(3, len(coordinates)):
        while len(size_triplet)>=3 and orientation(size_triplet[-2], size_triplet[-1], coordinates[coord_ith]) >= 0:
            size_triplet.pop()            
        size_triplet.append(coordinates[coord_ith])
    return size_triplet+[size_triplet[0]]


def random_points(n=30):
    coordinates = [(randint(0, n), randint(0, n)) for _ in range(n)]
    print (coordinates)
    return coordinates


if __name__ == "__main__":
    coordinates = random_points(120)

    X = [coord[0] for coord in coordinates]
    Y = [coord[1] for coord in coordinates]
    plt.plot(X, Y, '.b')

    boundary_poly = Convex_hull_through_graham(coordinates)

    X = [coord[0] for coord in boundary_poly]
    Y = [coord[1] for coord in boundary_poly]
    plt.plot(X, Y, '-og')

    plt.show()
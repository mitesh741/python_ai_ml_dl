
from time import time
import numpy as np
import matplotlib.path as mpltPath
import random
import copy
import cv2

list_of_rects = []
rect = []
flag = False
image = cv2.imread("/home/mitesh/Pictures/6.jpg")

list_of_rects = [[(2,3), (4,3), (4,1), (2,1)], [(5, 7), (7,7), (7, 5), (1,5)], [(7,3),(9,3),(9,1),(7,1)] ]

# index = -1

# def is_inside_polygon(x,y):
#     for j in range(len(list_of_rects)):
#         verts = list_of_rects[j]
#         path = mpltPath.Path(verts)
#         inside2 = path.contains_points([[x,y]])
#         if True == inside2:
#             return inside2, j
#         elif j == (len(list_of_rects) - 1):
#             return inside2, j
        
# flag, index =  is_inside_polygon(4,6)

# (x,y) = list_of_rects[0][1]

centroid_x  = 0 
centroid_y  = 0 

list_of_centroids = []
for k in range(len(list_of_rects)):
    for l in range(4):
        (x,y) = list_of_rects[k][l]
        print("(x,y) = {}, {}".format(x,y))
        centroid_x = centroid_x + x 
        centroid_y = centroid_y + y
    centroid = (centroid_x / 4, centroid_y / 4)
    list_of_centroids.insert(k, centroid)
    (centroid_x, centroid_y) = (0, 0)
    print("\n")

# print("list of centroids  = {}".format(list_of_centroids))

for l in range(len(list_of_centroids)):
    print(list_of_centroids[l])

# if True == flag:
#     print(" Point is in polygon index = {}".format(index))
# else:
#     print("Point is not in any polgon")

cv2.imshow("Output", image)
cv2.waitKey(0)


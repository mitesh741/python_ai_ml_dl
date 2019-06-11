# import random
# import copy

# list_of_rects = []
# rect = []

# for i in range(2):
#     for j in range(4):  
#         rect.insert(0, (random.randint(1,101),random.randint(1,101)))
#     list_of_rects.append(copy.deepcopy(rect))
#     rect.clear()
# print("list of rects")
# print(list_of_rects)

# print(list_of_rects[0])


import random
import copy

list_of_rects = []
rect = []
tup = None

for i in range(2): # Number of Rects
    for j in range(4):   # Four coodinates of each rect
        rect.insert(0, (random.randint(1,101),random.randint(1,101))) # add Each coordinates
    list_of_rects.append(copy.deepcopy(rect))
    tup = (list_of_rects[i] , 'green')
    list_of_rects[i] = tup
    rect.clear()

print(list_of_rects)
print("\n")
for j in range(2):
    for k in range(4):  
        list_of_rects[j] = (list_of_rects[0][0], 'red')
    rect.clear()

print(list_of_rects)





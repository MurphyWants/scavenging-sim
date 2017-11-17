import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

''' Salem's Code '''

myMap = {1: 'Hive', 2: 'Breeze', 3: 'Water', 4: 'Food', 5: 'Scent', 6: 'None'}

a = np.array([[3, 2, 1], [4, 5, 2], [5, 4, 3]])

v1 = a[1]
v2 = a[2]

print("Let's print the vectors in the matrix:")
for v in a:
    print(v)

print("Let's print the meaning of the numerical representations")
for v in a:
    for s in v:
        print(myMap.get(s)),
    print('')

def genarr():
    size_arr = random.randrange(10,100)
    size_arr2 = random.randrange(10,100)
    sampl = [None] * size_arr


    for x in range(size_arr):
        sampl[x] = np.random.random_integers(1, high=6, size=size_arr2)

    sampl = np.asarray(sampl)
    return sampl


''' Jon's Code '''

def arrToPlot (ar):
    myMapColors = {'Hive': 'Yellow', 'Breeze': 'Grey',
                   'Water': 'Blue', 'Food': 'Brown', 'Scent': 'Green', 'None': 'White'}

    out_list = []
    for x in range(len(ar)):
        for y in range(len(ar[0])):
            out_list.append(patches.Rectangle((x,y), 1,1, color=myMapColors[myMap[ar[x][y]]], fill=myMapColors[myMap[ar[x][y]]]))

    ax = plt.gca(aspect='equal')
    ax.cla()
    ax.set_xlim((0,len(ar)))
    ax.set_ylim((0,len(ar[0])))

    for rect in out_list:
        ax.add_artist(rect)

    plt.show()

arrToPlot(a)

b = np.array([[1,2,3,4,5], [4,5,4,4,5], [3,3,3,3,3]])

arrToPlot(b)

c = np.array([[1,3,5,4,5], [3,3,6,5,6], [6,2,2,6,2], [1,2,3,3,5], [6,3,4,1,2]])

arrToPlot(c)

arrToPlot(genarr())

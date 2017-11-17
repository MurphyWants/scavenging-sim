import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

''' Salem's Code '''

myMap = {1: 'Hive', 2: 'Breeze', 3: 'Water', 4: 'Food', 5: 'Scent'}

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

''' Jon's Code '''

myMapColors = {'Hive': 'Yellow', 'Breeze': 'Grey',
               'Water': 'Blue', 'Food': 'Brown', 'Scent': 'Green'}

out_list = []
for x in range(len(a)):
    for y in range(len(a[0])):
        out_list.append(patches.Rectangle((x,y), 1,1, color=myMapColors[myMap[a[x][y]]], fill=myMapColors[myMap[a[x][y]]]))

ax = plt.gca(aspect='equal')
ax.cla()
ax.set_xlim((0,len(a)))
ax.set_ylim((0,len(a[0])))

for rect in out_list:
    ax.add_artist(rect)

plt.show()

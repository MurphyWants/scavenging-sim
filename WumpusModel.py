import numpy as np

myMap = {1 : 'Hive', 2 : 'Breeze', 3 : 'Water', 4 : 'Food', 5 : 'Scent' }

a = np.array([[3,2,1], [4,5,2], [5,4,3]])

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
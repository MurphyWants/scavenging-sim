import map_class as wum
import random

a = wum.Wumpus(f=70,w=6,b=3, l=100, h=150)
for x in range(10000):
    x_coord = random.randrange(0, a.get_length())
    y_coord = random.randrange(0, a.get_height())
    a.get_map_data(x_coord, y_coord)
a.get_map_data(1,3)
a.get_map_data(2,3)
a.get_map_data(2,4)
a.get_map_data(3,4)
a.get_map_data(3,5)
a.get_map_data(4,5)
a.get_map_data(4,6)
a.get_map_data(5,6)
a.print_all()
a.graph()

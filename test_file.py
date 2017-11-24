import map_class as wum

a = wum.Wumpus(f=3,w=2,b=3, l=15, h=15)
a.get_map_data(1,3)
a.get_map_data(2,3)
a.get_map_data(2,4)
a.get_map_data(3,4)
a.get_map_data(3,5)
a.get_map_data(4,5)
a.get_map_data(4,6)
a.get_map_data(5,6)
a.print_all()

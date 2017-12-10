import map_class as wum
import random
import sim_class as sim

a = wum.Wumpus(f=5,w=3,b=1, l=10, h=10)
a.print_all()
s = sim.Simulation(a, bot_number=50)
s.make_graph()
s.generate_random_heatmap(100000)
s.scatter_bots()
s.make_graph()

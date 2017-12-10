import map_class as wum
import random
import sim_class as sim
from Search_Template import foraging_template as ft

class test_functor:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def get_number(self):
        self.count = self.count+1
        return self.count

    def get_name(self):
        return self.name

a = wum.Wumpus(f=5,w=3,b=0, l=10, h=10)
s = sim.Simulation(a, bot_number=10)
save = test_functor("test1")
s.run(ft, Save=False, Show=True)

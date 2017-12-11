import map_class as wum
import random
import sim_class as sim
from Search_Template import foraging_template as ft
import math

import sys
import os

name = sys.argv[1]
length = int(sys.argv[2])
height = int(sys.argv [3])


class test_functor:
    def __init__(self, name):
        self.name = name
        self.count = 0
        if not os.path.exists(name):
            os.makedirs(name)

        fig1_str = name+"/fig1/"
        fig2_str = name+"/fig2/"
        fig3_str = name+"/fig3/"
        fig4_str = name+"/fig4/"
        if not os.path.exists(fig1_str):
            os.makedirs(fig1_str)
        if not os.path.exists(fig2_str):
            os.makedirs(fig2_str)
        if not os.path.exists(fig3_str):
            os.makedirs(fig3_str)
        if not os.path.exists(fig4_str):
            os.makedirs(fig4_str)

    def get_number(self):
        self.count = self.count+1
        return self.count

    def get_name(self):
        return self.name

a = wum.Wumpus(f=int(math.floor(length/2)), b=0, l=length, h=height)
s = sim.Simulation(a, bot_number=10)
save = test_functor(name)
s.run(ft, Save=save, Show=False)

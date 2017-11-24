import numpy
import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import map_class as wum
import bot_class as bot

class Simulation:
    def __init__(self, wumpus_class=None, bot_number=1):
        if wumpus_class == None:
            self.__Wumpus_Map = wum.Wumpus()
        else:
            self.__Wumpus_Map = wumpus_class

        self.__bot_arr = []
        '''self.__bot_arr = [bot.bot_class(self.__Wumpus_Map)] * bot_number'''
        for x in range(bot_number):
            self.__bot_arr.append(bot.bot_class(self.__Wumpus_Map, x))

    def get_bot_arr(self):
        return self.__bot_arr
    def get_wumpus_map(self):
        return self.__Wumpus_Map

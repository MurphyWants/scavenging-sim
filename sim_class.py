import numpy
import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import map_class as wum
import bot_class as bot

class Simulation:
    '''
        Private Variables:
        ====================================================================
        __Wumpus_Map: The wumpus map class
        __bot_arr:    An array of bots

        Functions:
        ====================================================================
        init:           Constructor
        get_bot_arr:    Returns the array of bots
        get_wumpus_map: Returns the wumpus map class
    '''
    def __init__(self, wumpus_class=None, bot_number=1):
        if wumpus_class == None:
            self.__Wumpus_Map = wum.Wumpus()
        else:
            self.__Wumpus_Map = wumpus_class

        self.__bot_arr = []
        for x in range(bot_number):
            self.__bot_arr.append(bot.bot_class(self.__Wumpus_Map, x))

    def get_bot_arr(self):
        return self.__bot_arr
    def get_wumpus_map(self):
        return self.__Wumpus_Map

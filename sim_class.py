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
        init:             Constructor
        get_bot_arr:      Returns the array of bots
        get_wumpus_map:   Returns the wumpus map class
        generate_bot_map: Generates a map of all locations of bots by id
        make_graph:       Graphs heatmap, regular map, bot map, distribution map
        graph:            plt.show()
        run:              Runs the simulation with the given foraging method and search method
    '''
    def __init__(self, wumpus_class=None, bot_number=1):
        if wumpus_class == None:
            self.__Wumpus_Map = wum.Wumpus()
        else:
            self.__Wumpus_Map = wumpus_class

        self.__bot_arr = []
        for x in range(bot_number):
            self.__bot_arr.append(bot.bot_class(self.__Wumpus_Map, x+1))

        self.__hive = bot.bot_class(wumpus_class, "Hive")

    def get_bot_arr(self):
        return self.__bot_arr

    def get_wumpus_map(self):
        return self.__Wumpus_Map

    def generate_bot_map(self):
        m = numpy.zeros((self.__Wumpus_Map.get_length(), self.__Wumpus_Map.get_height()), dtype=object)
        distribution = self.__Wumpus_Map.get_empty_map()
        for bot in self.__bot_arr:
            coord  = bot.get_loc()
            bot_id = bot.get_id()
            if m[coord[0]][coord[1]] == 0:
                m[coord[0]][coord[1]] = [bot_id]
                distribution[coord[0]][coord[1]] = 1
            else:
                m[coord[0]][coord[1]].append(bot_id)
                distribution[coord[0]][coord[1]] = distribution[coord[0]][coord[1]] + 1
        return m, distribution

    def make_graph(self, Save=False, Show=True):
        fig1, ax1, fig2, ax2 = self.__Wumpus_Map.graph(show=False)
        bot_map,distribution = self.generate_bot_map()
        fig3 = plt.figure(3)
        ax3  = fig3.add_subplot(111)
        ax3.set_title("Bot Distribution")
        ax3.imshow(distribution, cmap='hot')
        '''
        Todo: Plot m, map of bots
        '''
        plot_map = []
        num_map = {0: 'None', 1: 'Hive', 2: 'Breeze', 3: 'Water',
                   4: 'Food', 5: 'Scent', 6: 'None-2', 7: 'Blockade'}
        num_map_colors = {'Hive': 'Yellow', 'Breeze': 'Grey', 'Water': 'Blue',
                          'Food': 'Brown', 'Scent': 'Green', 'None': 'White', 'Blockade': 'Black', 'None-2' : 'Black'}
        for x in range(self.__Wumpus_Map.get_length()):
            for y in range(self.__Wumpus_Map.get_height()):
                map_data = self.__hive.known_map_get(x,y)
                plot_map.append(patches.Rectangle((x,y), 1,1, color=num_map_colors[num_map[map_data]], fill=num_map_colors[num_map[map_data]]))

        fig4 = plt.figure(4)
        ax4 = fig4.add_subplot(111)
        ax4.set_title("Hive Map")
        ax4.set_ylim(self.__Wumpus_Map.get_height())
        ax4.set_xlim(self.__Wumpus_Map.get_length())

        plot_map2 = plot_map[:]
        for rect in plot_map2:
            ax4.add_patch(rect)


        if not(Save==False):
            base_str = Save.get_name() + "/"
            count = Save.get_number()
            fig1_str = base_str+"fig1/"+str(count)
            fig2_str = base_str+"fig2/"+str(count)
            fig3_str = base_str+"fig3/"+str(count)
            fig4_str = base_str+"fig4/"+str(count)

            fig1.savefig(fig1_str)
            fig2.savefig(fig2_str)
            fig3.savefig(fig3_str)
            fig4.savefig(fig4_str)
        if Show:
            plt.show()
        fig1.clf()
        fig2.clf()
        fig3.clf()
        fig4.clf()

    def run(self, foraging_method, Save=False, Show=True):

        method = foraging_method(self.__bot_arr)

        while True:
                self.__hive = method.run(self.__bot_arr, self.__Wumpus_Map, self.__hive)
                if Save:
                    self.make_graph(Save=Save, Show=Show)
                else:
                    self.make_graph(Show=Show)
        return 0

    def generate_random_heatmap(self, count=None):
        if count == None:
            count = random.randint(100, 100000)

        for x in range(count):
            x_coord = random.randrange(0, self.__Wumpus_Map.get_length())
            y_coord = random.randrange(0, self.__Wumpus_Map.get_height())
            self.__Wumpus_Map.get_map_data(x_coord, y_coord)

    def scatter_bots(self):
        for b in self.__bot_arr:
            x_coord = random.randrange(0, self.__Wumpus_Map.get_length())
            y_coord = random.randrange(0, self.__Wumpus_Map.get_height())
            b.set_loc(x_coord, y_coord)

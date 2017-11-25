import numpy
import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Wumpus:
    '''
    Private Variables:
    ====================================================================
    __length:     Length of the map, initialized at init, default is 10
    __height:     Height of the map, initialized at init, default is 10
    __empty_map:  An empty matrix of length and height, used for making more maps of same size
    __heat_map:   Heat map used for to see which nodes are more traveled
    __map:        The actual map to be generated

    Constant Variables:
    ====================================================================
    num_map:        The map is made of numbers, this map converts the numbers to the proper names
    num_map_colors: Converts the graph map to the proper colors

    Maps:
    ====================================================================
    Num | Name     | Color  | Purpose
    ----|----------|--------|------------------------------------------
    0   | None     | White  | Empty Space, Starting
    1   | Hive     | Yellow | Starting Place for the bots
    2   | Breeze   | Grey   | Indicates there is a water source nearby
    3   | Water    | Blue   | Water source, breezes around it
    4   | Food     | Brown  | Food source, scent around it
    5   | Scent    | Green  | Indicates there is a food source nearby
    6   | None     | White  | Empty Space, Known Empty Space
    7   | Blockade | Black  | Full space that can't be filled

    Functions:
    ====================================================================
    init:           Constructor
    get_length:     Returns map length
    get_height:     Returns map height
    generate_map:   Generates a map
    get_empty_map:  Returns a matrix of 0's of size length*height
    get_heat_map:   Returns the heatmap
    get_map_data:   Given an x,y coord, returns whats on the map
    get_hive:       Returns the hive (starting) coords
    print_all:      Prints out a bunch of info, useful for testing
    graph:          Draws the graph of the map, draws the heatmap
    reset_heat_map: Resets the heatmap to an empty matrix
    '''

    num_map = {0: 'None', 1: 'Hive', 2: 'Breeze', 3: 'Water',
               4: 'Food', 5: 'Scent', 6: 'None', 7: 'Blockade'}
    num_map_colors = {'Hive': 'Yellow', 'Breeze': 'Grey', 'Water': 'Blue',
                      'Food': 'Brown', 'Scent': 'Green', 'None': 'White', 'Blockade': 'Black'}
    def __init__(self, l=10, h=10, m=None, f=1, w=1, b=0):
        '''
        l: Length
        h: Height
        m: Map, could be used to pass a static map
        f: Food spots for generating map
        w: Water spots for generating map
        b: Blockades
        '''
        if m == None:
            self.__length = l
            self.__height = h
            self.__empty_map = self.get_empty_map()
            self.__heat_map = self.get_empty_map()
            self.__map = self.get_empty_map()
            self.generate_map(food=f, water=w,blockade=b)
            self.map_to_plot()

        else:
            self.__length = len(m)
            self.__height = len(m[0])
            self.__empty_map = self.get_empty_map()
            self.__heat_map = self.get_empty_map()
            self.__map = m

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def generate_map(self, food=0, water=0, blockade=0):
        '''
            l:        length of the map, default is 0
            h:        height of the map, default is 0
            in_class: if this function is part of the class, default is False
            food:     amount of food spots in the map, default is 0
            water:    amount of food spots in the map, default is 0
            blockade: amount of blocked spots in the map, default is 0
        '''
        length = self.get_length()
        height = self.get_height()
        total_space = length * height

        if ((5*food) + (5*water) + blockade + 1) > total_space:
            print "\nERROR: Can't generate map, to many objects \n"
            print "\nFood spots: ", food, " | Max Spaces: ", food*5
            print "\nWater spots: ", water, " | Max Spaces: ", water*5
            print "\nBlockades: ", blockade
            print "\nHive: 1"
            print "\nTotal number of spaces: ", ((5*food) + (5*water) + blockade + 1)
            print "\nTotal number of available spaces: ", total_space, "\n"
            return 1

        '''
            Set Hive Start
        '''
        x_coord = random.randrange(0, self.get_length()-1)
        y_coord = random.randrange(0, self.get_height()-1)
        '''print "Setting Hive: ", x_coord, ",", y_coord, "\n"'''
        self.__map[x_coord][y_coord] = 1
        self.__map_hive = (x_coord,y_coord)
        '''
            Generate Food Spots
        '''
        f = food
        if f == 0:
            f = random.randrange(1, math.ceil(math.sqrt(total_space)))

        for count in range(f):
            '''print "\n Trying Count: ", count+1, "\n"'''
            satisfied = False
            while not satisfied:
                x_coord = random.randrange(0, self.get_length()-1)
                y_coord = random.randrange(0, self.get_height()-1)
                map_data = [0]*5
                map_data[0] = self.get_map_data(x_coord, y_coord, heatmap=False, isprint=False)
                '''print "Trying coords: ", x_coord, ",", y_coord, "| Map Data: ", map_data[0], "\n"'''
                '''
                    Array setup: Checking the coord and the surrounding  spots

                        1
                    2   0   3
                        4
                '''
                if map_data[0]==0:
                    map_data[1] = self.get_map_data(x_coord, y_coord-1, heatmap=False, isprint=False)
                    map_data[2] = self.get_map_data(x_coord-1, y_coord, heatmap=False, isprint=False)
                    map_data[3] = self.get_map_data(x_coord+1, y_coord, heatmap=False, isprint=False)
                    map_data[4] = self.get_map_data(x_coord, y_coord+1, heatmap=False, isprint=False)
                    usable = 0
                    for d in map_data:
                        if (d == False) or (d == 0) or (d == 6):
                            usable += 1
                    if usable == 5:
                        '''print "This is usable:\nHive: ", x_coord, ", ", y_coord, "\n"'''
                        self.__map[x_coord][y_coord] = 4
                        if map_data[1]==0:
                            '''print "1: ", x_coord, ", ", y_coord-1, "\n"'''
                            self.__map[x_coord][y_coord-1] = 5
                        if map_data[2]==0:
                            '''print "2: ", x_coord-1, ", ", y_coord, "\n"'''
                            self.__map[x_coord-1][y_coord] = 5
                        if map_data[3]==0:
                            '''print "3: ", x_coord+1, ", ", y_coord, "\n"'''
                            self.__map[x_coord+1][y_coord] = 5
                        if map_data[4]==0:
                            '''print "1: ", x_coord, ", ", y_coord+1, "\n"'''
                            self.__map[x_coord][y_coord+1] = 5
                        satisfied = True



        '''
            Generate Water Spots (pretty much similar to food)
        '''
        w = water
        if w == 0:
            w = random.randrange(1, math.ceil(math.sqrt(total_space)))

        for count in range(w):
            '''print "\n Trying Count: ", count+1, "\n"'''
            satisfied = False
            while not satisfied:
                x_coord = random.randrange(0, self.get_length()-1)
                y_coord = random.randrange(0, self.get_height()-1)
                map_data = [0]*5
                map_data[0] = self.get_map_data(x_coord, y_coord, heatmap=False, isprint=False)
                '''print "Trying coords: ", x_coord, ",", y_coord, "| Map Data: ", map_data[0], "\n"'''
                '''
                    Array setup: Checking the coord and the surrounding  spots

                        1
                    2   0   3
                        4
                '''
                if map_data[0]==0:
                    map_data[1] = self.get_map_data(x_coord, y_coord-1, heatmap=False, isprint=False)
                    map_data[2] = self.get_map_data(x_coord-1, y_coord, heatmap=False, isprint=False)
                    map_data[3] = self.get_map_data(x_coord+1, y_coord, heatmap=False, isprint=False)
                    map_data[4] = self.get_map_data(x_coord, y_coord+1, heatmap=False, isprint=False)
                    usable = 0
                    for d in map_data:
                        if (d == False) or (d == 0) or (d == 6):
                            usable += 1
                    if usable == 5:
                        '''print "This is usable:\nHive: ", x_coord, ", ", y_coord, "\n"'''
                        self.__map[x_coord][y_coord] = 3
                        if map_data[1]==0:
                            '''print "1: ", x_coord, ", ", y_coord-1, "\n"'''
                            self.__map[x_coord][y_coord-1] = 2
                        if map_data[2]==0:
                            '''print "2: ", x_coord-1, ", ", y_coord, "\n"'''
                            self.__map[x_coord-1][y_coord] = 2
                        if map_data[3]==0:
                            '''print "3: ", x_coord+1, ", ", y_coord, "\n"'''
                            self.__map[x_coord+1][y_coord] = 2
                        if map_data[4]==0:
                            '''print "1: ", x_coord, ", ", y_coord+1, "\n"'''
                            self.__map[x_coord][y_coord+1] = 2
                        satisfied = True

        '''
            Generate Blockades
        '''
        for b in range(blockade):
            satisfied = False
            while not satisfied:
                x_coord = random.randrange(0, self.get_length()-1)
                y_coord = random.randrange(0, self.get_height()-1)
                map_data = self.get_map_data(x_coord, y_coord, heatmap=False, isprint=False)
                if map_data == 0:
                    self.__map[x_coord][y_coord] = 7
                    satisfied = True
        return 0

    def get_empty_map(self):
        '''
            Returns the empty map, if we need to make another copy for any reason
        '''
        return numpy.zeros((self.get_length(), self.get_height()))
        ''', dtype=object)'''

    def get_heat_map(self):
        '''
            Returns the heatmap, used for graphing
        '''
        return self.__heat_map

    def get_map_data(self, x, y, heatmap=True, isprint=False):
        '''
            Given an x,y coordinate: Returns the value on the map (1-7)
            Heatmap (default True):  If True, increases the value on the heatmap
            isprint (default False): If True, will print the coord trying and an error message if it is out of bounds
        '''
        if isprint:
            print "get_map_data: ", x, ",", y, "\n", self.get_length(), ",", self.get_height(), "\n"
        if (x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height()):
            if isprint:
                print "\nERROR: Out of Bounds\n"
                print "\nRequest: ", x, ",", y
                print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
                print "(x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height())\n"
                print (x<0) ,"\t", (x>=self.get_length()) ,"\t", (y<0) ,"\t", (y>=self.get_height()), "\n"
            return False
        if heatmap == True:
            self.__heat_map[x][y] += 1
        return self.__map[x][y]

    def get_hive(self):
        '''
            Getter for the hive, returns as a tuple
        '''
        return self.__map_hive

    def map_to_plot(self):
        '''
            Takes the generated map and makes it into rectangles
        '''
        self.__plot_map = []
        for x in range(self.get_length()):
            for y in range(self.get_height()):
                map_data = self.get_map_data(x,y,heatmap=False)
                self.__plot_map.append(patches.Rectangle((x,y), 1,1, color=self.num_map_colors[self.num_map[map_data]], fill=self.num_map_colors[self.num_map[map_data]]))

    def print_all(self):
        '''
            Prints a whole bunch of info, useful for testing
        '''
        '''print dir(self)
        for x in vars(self):
            print "\n", x'''
        print "Height ", self.get_height(), " |Length: ", self.get_length(), "\nEmpty Map:\n", self.get_empty_map(), "\nHeat Map:\n", self.get_heat_map(), "\nMap:\n", self.__map

    def graph(self, show=True):
        '''
            Graphs the map of rectangles
            Graphs the heatmap

            If show is true, it will show the graphs

            Returns the figures and axes
        '''
        fig = plt.figure(1)
        ax1 = fig.add_subplot(111)
        ax1.set_title("Map")
        for rect in self.__plot_map:
            ax1.add_patch(rect)
        ax1.set_ylim(self.get_height())
        ax1.set_xlim(self.get_length())

        fig2 = plt.figure(2)
        ax2 = fig2.add_subplot(111)
        ax2.set_title("Heatmap")
        ax2.imshow(self.get_heat_map(), cmap='hot')
        if show:
            plt.show()
        return fig, ax1, fig2, ax2

    def reset_heat_map(self):
        '''
            Resets the heatmap to all 0's
        '''
        self.__heat_map = self.get_empty_map()

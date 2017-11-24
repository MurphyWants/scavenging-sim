import numpy
import math


class Wumpus:
    '''
    Private Variables:
    ====================================================================
    __length:     Length of the map, initialized at init, default is 10
    __height:     Height of the map, initialized at init, default is 10
    __empty_map:  An empty matrix of length and height, used for making more maps of same size
    __heap_map:   Heat map used for to see which nodes are more traveled
    __map:        The actual map to be generated
    __static_map: A static copy of the map for refrence

    Constant Variables:
    ====================================================================
    num_map:        The map is made of numbers, this map converts the numbers to the proper names
    num_map_colors: Converts the graph map to the proper colors

    Maps:
    ====================================================================
    Num | Name     | Color  | Purpose
    ----|----------|--------|------------------------------------------
    1   | Hive     | Yellow | Starting Place for the bots
    2   | Breeze   | Grey   | Indicates there is a water source nearby
    3   | Water    | Blue   | Water source, breezes around it
    4   | Food     | Brown  | Food source, scent around it
    5   | Scent    | Green  | Indicates there is a food source nearby
    6   | None     | White  | Empty Space
    7   | Blockade | Black  | Full space that can't be filled
    '''

    num_map = {1: 'Hive', 2: 'Breeze', 3: 'Water',
               4: 'Food', 5: 'Scent', 6: 'None', 7: 'Blockade'}
    num_map_colors = {'Hive': 'Yellow', 'Breeze': 'Grey', 'Water': 'Blue',
                      'Food': 'Brown', 'Scent': 'Green', 'None': 'White', 'Blockade': 'Black'}
    def __init__(self, l=10, h=15, m=None):
        '''
        l: Length
        h: Height
        m: Map, could be used to pass a static map
        '''
        if m == None:
            self.__length = l
            self.__height = h
            self.__empty_map = self.get_empty_map()
            self.__heat_map = self.get_empty_map()
            self.__map = self.generate_map(in_class=True)
            self.__static_map = self.__map
        else:
            self.__length = len(m)
            self.__height = len(m[0])
            self.__empty_map = self.get_empty_map()
            self.__heat_map = self.get_empty_map()
            self.__map = m
            self.__static_map = __map

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def generate_map(self, l=0, h=0, in_class=False, food=0, water=0, blockade=0):
        '''
            l:        length of the map, default is 0
            h:        height of the map, default is 0
            in_class: if this function is part of the class, default is false
            food:     amount of food spots in the map, default is 0
            water:    amount of food spots in the map, default is 0
            blockade: amount of blocked spots in the map, default is 0
        '''
        if in_class == True:
            length = self.get_length()
            height = self.get_height()
            total_space = length * height
            m = self.get_empty_map()

            if ((5*food) + (5*water) + blockade + 1) > total_space:
                print "\nERROR: Can't generate map, to many objects \n"
                print "\nFood spots: ", food, " | Max Spaces: ", food*5
                print "\nWater spots: ", water, " | Max Spaces: ", water*5
                print "\nBlockades: ", blockade
                print "\nHive: 1"
                print "\nTotal number of spaces: ", ((5*food) + (5*water) + blockade + 1)
                print "\nTotal number of available spaces: ", total_space, "\n"
                return m

        else:
            m = numpy.zeros((h, l))
        return m

    def get_empty_map(self):
        '''
            Returns the empty map, if we need to make another copy for any reason
        '''
        return numpy.zeros((self.__height, self.__length))

    def get_heap_map(self):
        '''
            Returns the heatmap, used for graphing
        '''
        return self.__heap_map

    def get_map_data(self, x, y, heatmap=True):
        '''
            Given an x,y coordinate: Returns the value on the map (1-7)
            Heatmap (default true):  If true, increases the value on the heatmap
        '''
        if (x<0) or (x>self.get_length()) or (y<0) or (y>self.get_height()):
            print "\nERROR: Out of Bounds\n"
            print "\nRequest: ", x, ",", y
            print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
            print "(x<0) or (x>self.get_length()) or (y<0) or (y<self.get_height())\n"
            print (x<0) , (x>self.get_length()) , (y<0) , (y<self.get_height()), "\n"
            return False
        if heatmap == True:
            self.__heat_map[x][y] += 1
        return self.__map[x][y]

    def print_all(self):
        print dir(self)
        for x in vars(self):
            print "\n", x
        print "Height ", self.get_height(), " |Length: ", self.get_length(), "\nEmpty Map:\n", self.get_empty_map(), "\nHeat Map:\n", self.__heat_map, "\nMap:\n", self.__map

import numpy

class Wumpus:
    '''
    Variables:
    ====================================================================
    __length:     Length of the map, initialized at init, default is 10
    __height:     Height of the map, initialized at init, default is 10
    __empty_map:  An empty matrix of length and height, used for making more maps of same size
    __heap_map:   Heat map used for to see which nodes are more traveled
    __map:        The actual map to be generated
    __static_map: A static copy of the map for refrence
    '''
    def __init__(self, l=10, h=10, m=None):
        '''
        l: Length
        h: Height
        m: Map, could be used to pass a static map
        '''
        if m == None:
            self.__length = l
            self.__height = h
            self.__empty_map = numpy.zeros(shape(__length, __height))
            self.__heat_map = __empty_map
            self.__map = self.generate_map()
            self.__static_map = __map
        else:
            self.__length = len(m)
            self.__height = len(m[0])
            self.__empty_map = numpy.zeros(shape(__length, __height))
            self.__heat_map = __empty_map
            self.__map = m
            self.__static_map = __map

    def get_length(self):
        return self.__length
    def get_height(self):
        return self.__height
    def generate_map(self, l=0, h=0):
        '''
        Do stuff
        '''
        m = None
        return m
    def get_empty_map(self):
        return self.__empty_map

import numpy
class bot_class:
    '''
        Private Variables:
        ====================================================================
        __length:      The length of the map, from the wun class
        __height:      The height of the map, from the wum class
        __known_map:   Starting as an empty map, as the bot moves around it will mark what it knows on the map
        __guessed_map: Starting as an empty map, as the bot moves around it will mark what it guesses on the map
        __location_x:  Current location x coord
        __location_y:  Current location y coord
        __id:          The bot id, given at birth
        __task:        Current Task

        Functions:
        ====================================================================
        init:          Constructor
        get_length:    Returns the length of the map
        get_height:    Returns the height of the map
        guess_map_set: Given an x and y coord and a value, sets the x,y coord to the value
        guess_map_get: Given an x,y coord, returns the value on the guessed map or false for out of bounds
        known_map_set: Given an x and y coord and a val, sets the x,y coord to the value
        known_map_get: Given an x,y coord, returns the value on the guessed map or false for out of bounds
        get_loc:       Returns a tuple x,y coord of the current location
        set_loc:       Given an x,y coord, sets the location to the value
        get_id:        Returns the bot id
        set_task:      Sets the current bot task
        get_task:      Returns the current task
        set_sub_task:  Sets the sub task
        get_sub_task:  Gets the sub task
    '''
    def __init__ (self, wum, bot_id):
        '''
            Constructor, needs a wumpus class and a bot_id
        '''
        self.__length = wum.get_length()
        self.__height = wum.get_height()
        self.__known_map = wum.get_empty_map()
        self.__guessed_map = wum.get_empty_map()
        self.__location_x, self.__location_y = wum.get_hive()
        self.__id = bot_id
        self.__task = "None"
        self.__sub_task = "None"

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def guess_map_set(self, x, y, val, isprint=False):
        '''
            Given an x,y coord and a value it sets the x,y coord to the value and returns True
                or the x,y coord is out of bounds and returns False

            isprint (default: False): if True and the x,y coord is out of bounds, it will print error info
        '''
        if (x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height()):
            if isprint:
                print "\nERROR: Out of Bounds\n"
                print "\nRequest: ", x, ",", y
                print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
                print "(x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height())\n"
                print (x<0) ,"\t", (x>=self.get_length()) ,"\t", (y<0) ,"\t", (y>=self.get_height()), "\n"
            return False
        self.__guessed_map[x][y] = val
        return True

    def guess_map_get(self, x, y, isprint=False):
        '''
            Given an x,y coord it will return the value at x,y, or false if it is out of bounds

            isprint (default: False): is True and the x,y coord is out of bounds, it will print error info
        '''
        if (x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height()):
            if isprint:
                print "\nERROR: Out of Bounds\n"
                print "\nRequest: ", x, ",", y
                print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
                print "(x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height())\n"
                print (x<0) ,"\t", (x>=self.get_length()) ,"\t", (y<0) ,"\t", (y>=self.get_height()), "\n"
            return False
        return self.__guessed_map[x][y]

    def known_map_set(self, x, y, val, isprint=False):
        '''
            Given an x,y coord and a value it sets the x,y coord to the value and returns True
                or the x,y coord is out of bounds and returns False

            isprint (default: False): if True and the x,y coord is out of bounds, it will print error info
        '''
        if (x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height()):
            if isprint:
                print "\nERROR: Out of Bounds\n"
                print "\nRequest: ", x, ",", y
                print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
                print "(x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height())\n"
                print (x<0) ,"\t", (x>=self.get_length()) ,"\t", (y<0) ,"\t", (y>=self.get_height()), "\n"
            return False
        self.__known_map[x][y] = val
        return True

    def known_map_get(self, x, y, isprint=False):
        '''
            Given an x,y coord it will return the value at x,y, or false if it is out of bounds

            isprint (default: False): is True and the x,y coord is out of bounds, it will print error info
        '''
        if (x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height()):
            if isprint:
                print "\nERROR: Out of Bounds\n"
                print "\nRequest: ", x, ",", y
                print "\nBounds: (0,0) - ", self.get_length(), ",", self.get_height(), "\n"
                print "(x<0) or (x>=self.get_length()) or (y<0) or (y>=self.get_height())\n"
                print (x<0) ,"\t", (x>=self.get_length()) ,"\t", (y<0) ,"\t", (y>=self.get_height()), "\n"
            return False
        return self.__known_map[x][y]

    def get_loc(self):
        return self.__location_x, self.__location_y

    def set_loc(self, x, y):
        '''
            Given an x,y coord, sets the bot as the x,y coord
        '''
        self.__location_x = x
        self.__location_y = y

    def get_id(self):
        return self.__id

    def set_task(self, task):
        self.__task = task

    def get_task(self):
        return self.__task

    def set_sub_task(self, task):
        self.__sub_task = task

    def get_sub_task(self):
        return self.__sub_task

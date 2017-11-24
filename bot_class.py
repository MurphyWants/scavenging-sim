import numpy
class bot_class:
    def __init__ (self, wum, id):
        self.__length = wum.get_length()
        self.__height = wum.get_height()
        self.__known_map = wum.get_empty_map()
        self.__guessed_map = wum.get_empty_map()
        self.__location_x, self.__location_y = wum.get_hive()
        self.__id = id

    def get_length(self):
        return self.__length

    def get_height(self):
        return self.__height

    def guess_map_set(self, x, y, val, isprint=False):
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

    def guess_map_get(self, x, y, isrint=False):
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
        self.__location_x = x
        self.__location_y = y

    def get_id(self):
        return self.__id

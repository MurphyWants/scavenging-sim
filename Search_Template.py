import bot_class as bot
import math
import random
import sys

class foraging_template:
    '''
        Init: Give each bot a main task and a sub task
        Run: For each bot, do their task and their subtask

        Tasks:
            Search: Searches the map, reports back
            Collect: Being told where things are, go collect them and return
    '''
    def __init__(self, bots):
        self.__bot_num = len(bots)
        self.__num_scavengage = int(math.floor(self.__bot_num/2))
        self.__num_collect = int(math.floor(self.__bot_num/2))

        if not((self.__num_scavengage + self.__num_collect) == self.__bot_num):
            self.__num_scavengage =  self.__num_scavengage + 1

        '''
            There should be half of the bots scavenging, half of the bots collecting
            If there is an odd number, half +1 are scavenging
        '''

        for i in range(self.__num_scavengage):
            bots[i].set_task("Scavenge")

        for i in range(self.__num_collect):
            bots[i+self.__num_scavengage].set_task("Collect")


        return None

    def run(self, bots, wum, hive):
        if hive == None:
            hive  = bot.bot_class(wum, "Hive")

        length = wum.get_length()
        height = wum.get_height()

        for i in range(self.__bot_num):
            '''current_bot = bots[i]'''
            if bots[i].get_task() == "Scavenge":
                '''
                    The bot task is scavenging
                '''
                if bots[i].get_sub_task() == "None":
                    '''
                        Bot does not have a destination
                        Choose a random x,y coord and go there
                    '''
                    x_coord = random.randrange(0, length-1)
                    y_coord = random.randrange(0, height-1)
                    original_coords = (x_coord, y_coord)
                    while not (bots[i].known_map_get(x_coord, y_coord) == 0):
                        y_coord = y_coord + 1
                        if (y_coord > (height -1)):
                            y_coord = 0
                            x_coord = x_coord + 1
                        if (x_coord > (length - 1)):
                            x_coord = 0
                            y_coord = 0
                        if original_coords == (x_coord, y_coord):
                            print "\nEverything found\n"
                            sys.exit(0)
                    if bool(random.getrandbits(1)):
                        '''
                            Random True/False
                        '''
                        bots[i].set_sub_task(('X', (x_coord, y_coord), 'S'))
                    else:
                        bots[i].set_sub_task(('Y', (x_coord, y_coord), 'S'))

                else:
                    coord = bots[i].get_sub_task()[1]
                    if (coord == bots[i].get_loc()):
                        if (bots[i].get_sub_task()[2] == 'S'):
                            '''
                                At the Point we were going to Scavenge to
                                Setting task as heading back to hive
                            '''
                            if bool(random.getrandbits(1)):
                                bots[i].set_sub_task(('X', wum.get_hive(), 'H'))
                            else:
                                bots[i].set_sub_task(('Y', wum.get_hive(), 'H'))
                        else:
                            '''
                                Heading back to the hive and we are there
                            '''
                            for x in range(length):
                                for y in range(height):
                                    info = bots[i].known_map_get(x,y)
                                    if not(info == 0):
                                        hive.known_map_set(x,y, info)

                            for x in range(length):
                                for y in range(height):
                                    bots[i].known_map_set(x,y, hive.known_map_get(x,y))
                            bots[i].set_sub_task("None")

                    if (bots[i].get_sub_task()[0] == 'X'):
                        if (bots[i].get_loc()[0] < coord[0]):
                            bots[i].set_loc((bots[i].get_loc()[0] +1), (bots[i].get_loc()[1]))
                            x_coord, y_coord = bots[i].get_loc()
                            bots[i].known_map_set(x_coord, y_coord, wum.get_map_data(x_coord, y_coord))

                        if (bots[i].get_loc()[0] > coord[0]):
                            bots[i].set_loc((bots[i].get_loc()[0] - 1), (bots[i].get_loc()[1]))
                            x_coord, y_coord = bots[i].get_loc()
                            bots[i].known_map_set(x_coord, y_coord, wum.get_map_data(x_coord, y_coord))

                        else:
                            bots[i].set_sub_task(('Y', bots[i].get_sub_task()[1], bots[i].get_sub_task()[2]))

                    if (bots[i].get_sub_task()[0] == 'Y'):
                        if (bots[i].get_loc()[1] < coord[1]):
                            bots[i].set_loc((bots[i].get_loc()[0]), (bots[i].get_loc()[1]+1))
                            x_coord, y_coord = bots[i].get_loc()
                            bots[i].known_map_set(x_coord, y_coord, wum.get_map_data(x_coord, y_coord))

                        if (bots[i].get_loc()[0] > coord[0]):
                            bots[i].set_loc((bots[i].get_loc()[0]), (bots[i].get_loc()[1] -1))
                            x_coord, y_coord = bots[i].get_loc()
                            bots[i].known_map_set(x_coord, y_coord, wum.get_map_data(x_coord, y_coord))

                        else:
                            bots[i].set_sub_task(('X', bots[i].get_sub_task()[1], bots[i].get_sub_task()[2]))

            if bots[i].get_task() == "Collect":
                return 0
        return 0

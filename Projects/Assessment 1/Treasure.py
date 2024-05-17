'''
File: Treasure.py
Description: holds treasure class which allows itself to be buried in an island
Author: Roy Vallecera
ID: 110319378
Username: valry014
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import random


class Treasure:
    def __init__(self):
        self.__location = []

    # buries treasure on island
    def bury_treasure(self, island):
        # finds available postions of the island
        grid = island.get_grid()
        # finds areas the treasure cannot be buried such as hazards and starting point
        hazrds = island.get_hazards()
        middle = island.find_middle()
        pos_locations = len(grid) - 1
        buried = False
        # loops until valid positon is
        while buried == False:
            index = random.randint(0, pos_locations)
            loc = grid[index]
            if loc not in hazrds and loc != middle:
                buried = True
        self.__location = loc

    # getter for treasure attribute
    def get_location(self):
        return self.__location

'''
File: Pirate.py
Description: holds the pirate class responsible for naking valid moves on an island and drinking when neccessary
Author: Roy Vallecera
ID: 110319378
Username: valry014
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Pirate:
    def __init__(self):
        self.__explored = []
        self.__currennt_location = []
        self.__thirst = 0
        self.__hazards_hidden = []
        self.__island = []

    def start_position(self, island):
        # calls upon the island class find middle method to determine staring position, hazards and determine boundaries it can move using the grid
        position = island.find_middle()
        self.set_current_location(position)
        self.__hazards_hidden = island.get_hazards()
        self.__island = island.get_grid()
        self.__explored.append(position)

    # changing the x axis of the curret location by -1 to move up in the island
    def move_north(self):
        # increasing thirst as action is being made
        self.__thirst += 1
        location = self.__currennt_location
        # using the current location and changing its x value to move it on the list
        location[0] -= 1
        # checks if the new location co-ordinate exists on the map
        if location not in self.__island:
            # if  not in island not a valid move and thirst is reverted as no action taken
            self.__thirst -= 1
            print('Cannot move out of island, pirate not moved')
            # inverse action to axis change is made as it is out of bounds of the island
            location[0] += 1
            self.set_current_location(location)
        # checks if pirate is attemptint to move to a hazard position and reverting changes made to location
        elif location in self.__hazards_hidden:
            print('hazzard area, character not moved')
            print('thirst increases')
            location[0] += 1
            self.set_current_location(location)
        else:
            print('Character moved North!')
            # pirate makes move and is set to new positon
            self.set_current_location(location)
            self.set_current_location(location)
            self.__explored.append(location)

    # copy and paste of move north with appropriate changes made to the axis modifiers
    def move_south(self):
        self.__thirst += 1
        location = self.__currennt_location
        location[0] += 1
        if location not in self.__island:
            self.__thirst -= 1
            print('Cannot move out of island, pirate not moved')
            location[0] -= 1
            self.set_current_location(location)
        elif location in self.__hazards_hidden:
            print('hazzard area, character not moved')
            print('thirst increases')
            location[0] -= 1
            self.set_current_location(location)
        else:
            print('Character moved South!')
            self.set_current_location(location)
            self.__explored.append(location)

    # copy and paste of move north with appropriate changes made to the axis modifiers
    def move_east(self):
        self.__thirst += 1
        location = self.__currennt_location
        location[1] += 1
        if location not in self.__island:
            self.__thirst -= 1
            print('Cannot move out of island, pirate not moved')
            location[1] -= 1
            self.set_current_location(location)
        elif location in self.__hazards_hidden:
            print('hazzard area, character not moved')
            print('thirst increases')
            location[1] -= 1
            self.set_current_location(location)
        else:
            print('Character moved East!')
            self.set_current_location(location)
            self.__explored.append(location)

    # copy and paste of move north with appropriate changes made to the axis modifiers
    def move_west(self):
        self.__thirst += 1
        location = self.__currennt_location
        location[1] -= 1
        if location not in self.__island:
            self.__thirst -= 1
            print('Cannot move out of island, pirate not moved')
            location[1] += 1
            self.set_current_location(location)
        elif location in self.__hazards_hidden:
            print('hazzard area, character not moved')
            print('thirst increases')
            location[1] += 1
            self.set_current_location(location)
        else:
            print('Character moved West!')
            self.set_current_location(location)
            self.__explored.append(location)

    # Pirates must drink grog to move if they are too thirsty, sets thirsts back down to 0

    def drink_grog(self):
        self.set_thirst(0)

    # getters and setters for pirate attributes
    def get_current_location(self):
        return self.__currennt_location

    def set_current_location(self, location):
        self.__currennt_location = location

    def get_explored(self):
        return self.__explored

    def get_thirst(self):
        return self.__thirst

    def set_thirst(self, grog_levels):
        self.__thirst = grog_levels

    def set_hazards_hidden(self, hazards):
        self.__hazards_hidden = hazards

'''
File: Island.py
Description: holds the island class which forms and displays island and its contents
Author: Roy Vallecera
ID: 110319378
Username: valry014
This is my own work as defined by the University's Academic Misconduct Policy.
'''


import random
import colorama
from colorama import Back, Fore, Style

colorama.init(autoreset=True)


class Island:
    def __init__(self):
        self.__rows = 0
        self.__columns = 0
        self.__grid = []
        self.__treasure = []
        self.__density = 0
        self.__hazards = []
        self.__pirate_location = []
        self.__ex_areas = []

    def island_diff(self):
        print('Difficulties: ')
        print('|1|Arrrd, |2|Arrrd..rrr, |3|Very Arrrrd ')
        print('')
        # Input selection for difficulty and validation of correct input
        diff = input('Please selecet a difficulty: ')
        while diff not in ['1', '2', '3']:
            diff = input('Please enter 1, 2, or 3 for difficulty: ')

        # setting island attributes based on difficulty set
        if diff == '1':
            print('Arrrd difficulty has been selected')
            print('')
            self.set_rows(10)
            self.set_columns(10)
            # calling form_grid function to make use of attributes
            self.form_grid()
            self.set_density(10)
            self.place_hazards()
            # all pirates start at the middle of the island
            start = self.find_middle()
            self.__pirate_location.append(start)
            print('-----------------------------------------------------------')
            print('')

        # setting island attributes based on difficulty set (format copied from first difficulty)
        elif diff == '2':
            print('Arrrd..rrr difficulty has been selected')
            print('')
            self.set_rows(20)
            self.set_columns(10)
            self.form_grid()
            self.set_density(20)
            self.place_hazards()
            # all pirates start at the middle of the island
            start = self.find_middle()
            self.__pirate_location.append(start)
            print('-----------------------------------------------------------')
            print('')

        # setting island attributes based on difficulty set (format copied from first difficulty)
        elif diff == '3':
            print('Very Arrrrd difficulty has been selected')
            print('')
            self.set_rows(30)
            self.set_columns(30)
            self.form_grid()
            self.set_density(35)
            self.place_hazards()
            # all pirates start at the middle of the island
            start = self.find_middle()
            self.__pirate_location.append(start)
            print('-----------------------------------------------------------')
            print('')

    # creating a grid based on the number of rows and columns, rows dictating x position and columns dictating y postion
    def form_grid(self):
        # for every row a new list is created
        for x in range(self.__rows):
            # for every column a new list created within a row
            for y in range(self.__columns):
                position = [x, y]
                self.__grid.append(position)

    # main display for island
    def print_island_display(self):
        # index accesses items in the grid and moves along as per rows and columns attributes used to create island grid
        index = 0
        # symbols that are outputted to the island display
        status = ['.', '*', 'w', 'P']
        for r in range(self.__rows):
            for c in range(self.__columns):
                # checks to see if grid[index] is in a particular list which should be displayed differently
                if self.__grid[index] == self.__pirate_location:
                    print(Fore.YELLOW + " ".join(status[3]), end=' ')
                    index += 1
                elif self.__grid[index] in self.__hazards:
                    print(Fore.RED + " ".join(status[2]),  end=' ')
                    index += 1
                elif self.__grid[index] in self.__ex_areas:
                    print(Fore.GREEN + " ".join(status[1]),  end=' ')
                    index += 1
                # if not in explored list or hazrd list island location is unexplored
                else:
                    print(Fore.BLACK + " ".join(status[0]),  end=' ')
                    index += 1
            print("")

    # Acknowledges pirates moves and updates island accordingly
    def move_pirate(self, pirate, explored):
        p_location = pirate.get_current_location()
        self.__pirate_location = p_location
        self.__ex_areas = explored

    def place_hazards(self):
        # sets hazards to no entries so that the specified density is not exceeded from previous entries
        self.__hazards = []
        start = self.find_middle()
        start_index = self.__grid.index(start)
        existing_hazards = [start_index]
        # since len starts counting at 1 and list indexes start at 0 we have to - 1
        pos_locations = len(self.__grid) - 1
        for x in range(self.__density):
            location = random.randint(0, pos_locations)
            # validation that hazards cannot occupy the same position on the grid by ensuring the index used is not already existing in the existing hazards list.
            while location in existing_hazards:
                location = random.randint(0, pos_locations)
            existing_hazards.append(location)
            self.__hazards.append(self.__grid[location])

    # finds middle of the island as this is the starting point for the pirate and this location should not house any hazards or treasures
    def find_middle(self):
        position = []
        # set to integer as a positon with a decimal doesn not exist in the grid
        start_x = int(self.__rows / 2)
        start_y = int(self.__columns / 2)
        position = [start_x, start_y]
        return position

    # Preparing getters and setters for potential use

    def get_grid(self):
        return self.__grid

    def get_ex_areas(self):
        return self.__ex_areas

    def get_un_areas(self):
        return self.__ex_areas

    def get_rows(self):
        return self.__rows

    def get_columns(self):
        return self.__columns

    def get_hazards(self):
        return self.__hazards

    def get_treasure(self):
        return self.__treasure

    def set_ex_areas(self, areas):
        self.__ex_areas = areas

    def set_rows(self, row):
        self.__rows = int(row)

    def set_columns(self, columns):
        self.__columns = int(columns)

    def set_treasure(self, location):
        self.__treasure = location

    def set_density(self, percentage):
        percentage = float(percentage/100)
        # set to integer as a positon with a decimal doesn not exist in the grid
        self.__density = int((len(self.__grid) * percentage))

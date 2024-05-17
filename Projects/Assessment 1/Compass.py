'''
File: Compass.py
Description: holds Compass class which allows gives hints to player based on player location
Author: Roy Vallecera
ID: 110319378
Username: valry014
This is my own work as defined by the University's Academic Misconduct Policy.
'''


class Compass:
    # instantiate  a location (a list with 2 nuumbers representy x and y co-ordinates) as the point the player is hinted clues for
    # in this case the treasure location, as this is what the player is trying to find
    def __init__(self, treasure_loc):
        self.__treasure = treasure_loc

    def find_treasure(self, player):
        # the number for each x position and each y position dictates 1 movement respectively
        # by adding the numbers of each x and y positon together we can compare 2 locations and how far they are with moves
        player_pos = player[0] + player[1]
        treasure_pos = self.__treasure[0] + self.__treasure[1]
        # the treasures location may be smaller than the players location as a sum of their x and y values but would still have a numerical difference
        # this numerical difference shows how far each location is from one another
        treasure_bigger = treasure_pos - player_pos
        treasure_smaller = player_pos - treasure_pos
        # the right subtraction is called for after checking which  position has a larger sum of their x and y values
        if treasure_pos > player_pos and treasure_bigger <= 3:
            print('Hotter, the treasure is close by')
        elif treasure_pos > player_pos and treasure_bigger <= 6:
            print('Warmer, you are in the vacinity')
        elif treasure_pos > player_pos and treasure_bigger >= 7:
            print('Colder, the treasure eludes you')
        elif player_pos > treasure_pos and treasure_smaller <= 3:
            print('Hotter, the treasure is close by')
        elif player_pos > treasure_pos and treasure_smaller <= 6:
            print('Warmer, you are in the vacinity')
        elif player_pos > treasure_pos and treasure_smaller >= 7:
            print('Colder, the treasure eludes you')

# • Colder – The player is 7 or more space away from treasure.
# • Warmer – The player is between 3 and 7 spaces.
# • Hotter – The player is 3 or less spaces away.

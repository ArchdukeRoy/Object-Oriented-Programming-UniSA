'''
File: Assessment 1.py
Description: Holds all code making use of the other classes to make a pirate treasure hunting game
Author: Roy Vallecera
ID: 110319378
Username: valry014
This is my own work as defined by the University's Academic Misconduct Policy.
'''

# PLEASE HAVE COLORAMA INSTALLED

# imports classes onto 1 file
import copy
from Island import Island
from Pirate import Pirate
from Treasure import Treasure
from Compass import Compass

# metho to call copy and paste of hud display taking the only 2 changing variables of the hud as the 2 parameters


def print_hud(turn, thirst):
    print('Turn:', turn, end=' | ')
    print('Thirsty level: ', thirst, '/10', sep='')
    print('|W|North, |A|West, |S|South, |D|East, |E|Drink, |C|Compass')
    print('-----------------------------------------------------------')


# function for a print statement that includes the goal of the game and the explanations of valid user inputs
def print_instructions():
    instructions = """
    -----------------------------------------------------------
    Arrrr me hearties I see you've made it to treasure island.
    It is your job to find the buried treasure by navigating
    this island.

    'P' marks where the pirate currently is.
    '*' marks where the pirate has been.
    'w' marks where water is.
    '.' marks any unexplored areas

    Hazards occupy the island, they cannot be passed through
    and trying to pass them whill use up a turn and increase
    your thirsty levels.

    'W' or 'North' will move you up
    'S' or 'South' will move you down
    'D' or 'East' will move you to the right
    'A' or 'West' will move you left

    Watch out for getting too thirsty and keep an eye out on
    your thirsty levels. Get too thirsty and you'll become
    immobilised, unable to anything until you have a drink.

    'E' or 'Drink' makes you drink, quenching your thirst

    It can be hard to find the treasure blindly. Make use of
    your compass to give you clues of where it might be.
    
    'C' or 'Compass' will give you a clue to the treasure
    -----------------------------------------------------------
    """
    print(instructions)


trasure_island = Island()
first_mate = Pirate()
treasure_chest = Treasure()

# title screen for player
print('-----------------------------------------------------------')
print('')
print('WELCOME TO TREASURE ISLAND')
print('')
print('-----------------------------------------------------------')

game = True

while game == True:
    # print statment to show user possible options
    print('')
    print('Options:')
    print('|1|Begin game, |2|Show instructions, |3|Quit game')
    print('')
    query = input('Please select an option: ')
    # validation loop that accepts only query 1 or 3
    # choosing instructions will display instructions but will return you to options menu
    while query not in ['1', '3']:
        if query == '2':
            print_instructions()
        print('Options:')
        print('|1|Begin game, |2|Show instructions, |3|Quit game')
        query = input('Please select an option (1, 2 or 3): ')
        print('')
    # choosing to quit game breaks loop after goodbye message
    if query == '3':
        print('-----------------------------------------------------------')
        print('')
        print('THANK YOU FOR PLAYING')
        print('')
        print('-----------------------------------------------------------')
        print('')
        break
    # print statments for visual appeal the procceeding to game initialization
    elif query == '1':
        print('')
        print('-----------------------------------------------------------')
        print('')
    # initializes game
    # creates island based on difficulty
    trasure_island.island_diff()
    # finds starting location based on island
    first_mate.start_position(trasure_island)
    # assigns treasure to location on the map
    treasure_chest.bury_treasure(trasure_island)
    # creates a copy of starting position ands saves it a list of explored locations
    explored = copy.deepcopy(first_mate.get_current_location())
    all_explored = []
    all_explored.append(explored)
    # acknowledges pirate movement
    trasure_island.move_pirate(first_mate, all_explored)
    trasure_island.print_island_display()
    # returns the location of treasure
    treasure_loc = treasure_chest.get_location()
    # compass is instantiated based on treasure location
    p_compass = Compass(treasure_loc)
    # turn is reset back to 0 at the start of every game
    turn = 0
    # resets pirates thirst to 0 at the start of every new game
    first_mate.drink_grog()
    # sets two variables responible for the conidions of the game to be run
    t_location = treasure_chest.get_location()
    pirate_pos = first_mate.get_current_location()
    # thirst not set yet, but by default and at start it is at 0
    print_hud(turn, 0)
    # game loop
    while pirate_pos != t_location:
        thirst = first_mate.get_thirst()
        # players are forced to drink if pirate is too thirsty
        while thirst == 10:
            print('Too thirsty to do anything, have a drink!!')
            trasure_island.print_island_display()
            print_hud(turn, thirst)
            drink = input('Action:')
            # accounts for user input being cappital letters
            drink = drink.lower()
            if drink == 'e':
                first_mate.drink_grog()
                thirst = first_mate.get_thirst()
                print('Thirst quenched!')
                trasure_island.print_island_display()
                print_hud(turn, thirst)
            else:
                print('E to DRINK!!!')
        command = input('Action: ')
        # accounts for user input being cappital letters
        command = command.lower()
        print('')
        # an if, elif, else statment that only accepts valid commands
        # wasd are the movement commands, copy and pasted with the directions set accordingly

        # as display shows the key and command name user input for single key and full comman name accepted
        if command == 'w' or command == 'north':
            # pirate moves
            first_mate.move_north()
            # copies location to explored locations
            explored = copy.deepcopy(first_mate.get_current_location())
            if explored not in all_explored:
                all_explored.append(explored)
            # island acknowlges movement
            trasure_island.move_pirate(first_mate, all_explored)
            # island display is printed
            trasure_island.print_island_display()
            # turn  has passed and turn counter increased
            turn += 1
        elif command == 's' or command == 'south':
            first_mate.move_south()
            explored = copy.deepcopy(first_mate.get_current_location())
            if explored not in all_explored:
                all_explored.append(explored)
            trasure_island.move_pirate(first_mate, all_explored)
            trasure_island.print_island_display()
            turn += 1
        elif command == 'd' or command == 'east':
            first_mate.move_east()
            explored = copy.deepcopy(first_mate.get_current_location())
            if explored not in all_explored:
                all_explored.append(explored)
            trasure_island.move_pirate(first_mate, all_explored)
            trasure_island.print_island_display()
            turn += 1
        elif command == 'a' or command == 'west':
            first_mate.move_west()
            explored = copy.deepcopy(first_mate.get_current_location())
            if explored not in all_explored:
                all_explored.append(explored)
            trasure_island.move_pirate(first_mate, all_explored)
            trasure_island.print_island_display()
            turn += 1
        elif command == 'e' or command == 'drink':
            first_mate.drink_grog()
            thirst = first_mate.get_thirst()
            print('Thirst quenched!')
            trasure_island.print_island_display()
        elif command == 'c' or command == 'compass':
            # the compass uses the pirates location as a paramaeter to determine how far it is from the treasure
            current_location = first_mate.get_current_location()
            # calling compass' only function
            p_compass.find_treasure(current_location)
            trasure_island.print_island_display()
        else:
            # if valid command not entered  error statment printed and turn and thirst not increased
            print('Please enter a valid command')
            trasure_island.print_island_display()

        # TESTING TO FIND TREASURE LOCATION INTENTIONALLY LEFT IN IN FOR MARKERS
        # h = treasure_chest.get_location()
        # print(h)
        # p = first_mate.get_current_location()
        # print(p)

        # print statement for the HUD of the game
        print_hud(turn, thirst)
        print('')
    # user notification treasure has been found
    print('TREASURE HAS BEEN FOUND!!')
    print('It took you', turn, 'turns')
    print('')
    print('-----------------------------------------------------------')
    # break or continue loop as per user
    ending = input('Would you like to keep playing: |Y|N| ')
    while ending.lower() not in ['y', 'n']:
        ending = input('Would you like to keep playing: |Y|N| ')
    # Goodbye message and sets game contidion to false breaking the game loop
    if ending.lower() == 'n':
        print('-----------------------------------------------------------')
        print('')
        print('THANK YOU FOR PLAYING')
        print('')
        print('-----------------------------------------------------------')
        print('')
        game = False
    # print statement acknoledging new game before reinitializing game state
    else:
        print('-----------------------------------------------------------')
        print('')
        print('NEW GAME')
        print('')
        print('-----------------------------------------------------------')

"""
A bike would not be anything without a cyclist to accompany it. We should create this class
which can ride the bike. Again, we will need attributes which define this class.
1. An attribute to represent the name of a cyclist.
2. An attribute for age.
3. An attribute for weight as this is a big factor in cycling.
4. An attribute for proficiency. I.e., Mountain, Road, Racer, Leisure.
5. An attribute which shows if they are or are not wearing protective gear. This can be
set to false for now.
"""


class Cylist:
    def __init__(self, name, age, weight, proficiency_type):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__proficiency_type = proficiency_type
        self.__protective_gear = False

    def acceleerate(self):
        print(self.__name, 'is accelerating')

    def turn(self, direction):
        print(self.__name, 'is turning', direction)

    def brakes(self):
        print('Braking')

    def change_protective_gear(self):
        self.__protective_gear = not self.__protective_gear
        if self.__protective_gear:
            print('Protective gear has been put on')
        else:
            print('Protective gear has been taken off')

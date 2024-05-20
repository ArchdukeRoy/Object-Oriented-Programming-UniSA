"""
Classes are needed to represent a few real-world objects. Write a class which represents a
bike. The bike should have some attributes which define it.
• An attribute which represents what type of bike it is. I.e., Mountain Bike, Electric Bike,
Road Bike, etc.
• An attribute which is the maximum gears this bike may have. Most bikes start with 6
gears.
• An attribute which represents the gear which is currently being used. To make things
simple, we can start this at 1.
"""


class Bike:
    def __init__(self, type, max_gears):
        self.__type = type
        self.__max_gears = max_gears
        self.__current_gear = 1

    # takes a boolean as a parameter to change gears
    def change_gears(self, change):
        if change and self.__current_gear != self.__max_gears:
            self.__current_gear += 1
            print('gear has increased to', self.__current_gear)
        elif not change and self.__current_gear != 1:
            self.__current_gear -= 1
            print('gear has decreased to', self.__current_gear)
        else:
            print('gear has not been changed')

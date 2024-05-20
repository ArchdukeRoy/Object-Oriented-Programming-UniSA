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

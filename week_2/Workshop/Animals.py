"""
You have been assigned to create several classes for different animals. These animals include
cats, sheep, snakes, mice, and cows. Each animal has a set of properties that define them.
They also have a set of behaviours that perform operations. Each animal requires a
constructor.
The system should provide a simple and structured way to manage animals in a
programmatic manner. It allows us to simulate animals and monitor their different
behaviours. This demonstrates the use of object-oriented programming in Python to
model and manage different types of animals with distinct characteristics and
behaviours.

CLasses:
Snake
Cat
Sheep
Mouse
Cow
"""


class Snake:
    def __init__(self, name, nickname, cry):
        self.__name = name
        self.__nickname = nickname
        self.__cry = cry

    # TODO complete print statement
    def cry(self):
        pass

    # TODO complete print statement
    def coil(self):
        pass

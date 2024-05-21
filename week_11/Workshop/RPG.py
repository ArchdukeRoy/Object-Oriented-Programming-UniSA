"""
Create a program which allows for the creation of three different types of roles in a role playing
game: Mage, Warrior, and Rogue. Each character has their own set of values which allow them
to attack in different ways. 

Classes:
Mage
Warrior
Rogue
BattleMage
BladeMaster
ShadowCaster
"""
import random

class Mage:
    def __init__(self, magic_attribute):
        self.__damage = 50
        self.__magic_attribute = magic_attribute
        
    def attack(self):
        damage = self.__damage * (self.__magic_attribute/10)
        return damage
    
class Warrior:
    def __init__(self, strength):
        self.__damage = 50
        self.__strength = strength
   
    def attack(self):
        damage = self.__damage + self.__strength
        return damage
    
class Rogue:
    def __init__(self):
        self.__damage = 50
        self.__crit = 10

    def attack(self):      
        crit_check = random.randint(1, 100)
        if crit_check <= self.__crit:
            damage = self.__damage**2
            return damage
        else:
            return self.__damage
    
class BattleMage(Mage,Warrior):
    pass

class BladeMaster(Warrior,Rogue):
    pass

class ShadowCaster(Mage,Rogue):
    pass
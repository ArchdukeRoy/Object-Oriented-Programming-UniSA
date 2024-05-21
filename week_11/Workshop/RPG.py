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
    def __init__(self,magic_attribute,strength):
        Mage.__init__(self,magic_attribute)
        Warrior.__init__(self,strength)
           
    def attack(self):
        return Mage.attack(self)+Warrior.attack(self)
        

class BladeMaster(Warrior,Rogue):
    def __init__(self,strength):
        Warrior.__init__(self, strength)
        Rogue.__init__(self)
    
    def attack(self):
        return Warrior.attack(self)+Rogue.attack(self)

class ShadowCaster(Mage,Rogue):
    def __init__(self,magic_attribute):
        Mage.__init__(self,magic_attribute)
        Rogue.__init__(self)
        
    def attack(self):
        return Mage.attack(self)+Rogue.attack(self) 
    
#TEST CODE   
# shadow_caster=ShadowCaster(10)   
# print("ShadowCaster:", shadow_caster.attack())

# blade_master = BladeMaster(20)
# print("BladeMaster:", blade_master.attack())

# battle_mage = BattleMage(10, 20)   
# print("BattleMage", battle_mage.attack())
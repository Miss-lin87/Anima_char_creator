from attribut_functions import get_value_auto as gva

class Empty_character:
    def __init__(self,char):
        self.lv = gva(char, "Level")
        self.Block = gva(char, "Block")
        self.dodge = gva(char, "Dodge")
        self.attack = gva(char, "Attack")
        self.armor = gva(char, "Armor")
        self.weapons = gva (char, "Weapon")

class Characters():
  char1 = Empty_character("char1")
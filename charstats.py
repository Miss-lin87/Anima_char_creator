import weapons
import armor

class Character:
    def __init__(self,lv,defe,dodge,attack,armor,weapons):
        self.lv = int(lv)
        self.defe= int(defe)
        self.dodge = int(dodge)
        self.attack = int(attack)
        self.armor = armor
        self.weapons = weapons

char1 = Character(2,40,80,25,armor.Half_plate,weapons.club)
char2 = Character(4,60,100,80,armor.Leather,weapons.short_sword)
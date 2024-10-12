emptydic = {
    "level":0,
    "defence":0,
    "dodge":0,
    "attack":0,
    "armor":"",
    "weapon":""
}

import armor
import weapons

char1 = {
    "level":2,
    "defence":40,
    "dodge":80,
    "attack":25,
    "armor": armor.Half_plate,
    "weapon": weapons.club
    }

char2 = {
    "level":4,
    "defence":60,
    "dodge":100,
    "attack":65,
    "armor":armor.Leather,
    "weapon": weapons.short_sword
}



def copy():
    new={}
    new = emptydic.copy()
    f = open("test.txt")
    f.write, str(new, "a")
    f.close
    print (new)

copy()

import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from dice import openroll10 as iD10

from attribut_functions import get_value_auto as gva

def attribute_roll(char="", attri=""):
    if char=="" or attri == "": char, attri=autofill(char,attri)
    stat = gva(char,attri)
    roll = iD10()
    if roll > stat:
        dif = abs(stat-roll)
        # print(roll) #for testing
        # print(stat) #for testing
        return ("You failed with a difference of " + str(dif))
    else:
        dif = abs(roll-stat)
        # print(roll) # for testing
        # print(stat) #for testing
        return ("You succedd with a difference of " + str(dif))
    
def autofill(char="", attri=""):
    if char == "" and attri =="": char = input("What character? "); attri = input("What attribute? "); return char, attri
    elif char == "" and attri !="": char = input("What charater? "); return char, attri
    elif char !="" and attri =="": attri = input("What attribute? "); return char, attri
    else: return char, attri


print(attribute_roll("","Power"))
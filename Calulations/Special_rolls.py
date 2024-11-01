import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

from dice import openroll10 as iD10
from Functions.Call_functions import autofill
from Functions.attribut_functions import get_value_auto as gva


def attribute_roll(char="", attri=""):
    """This is used to roll a D10 against attribute and return the win of fail level"""
    if char=="" or attri == "": char, attri=autofill(char,attri)
    stat = gva(char,attri)
    roll = iD10()
    if roll > stat:
        dif = abs(stat-roll)
        # print(roll) # for testing
        # print(stat) # for testing
        return ("You failed with a difference of " + str(dif))
    else:
        dif = abs(roll-stat)
        # print(roll) # for testing
        # print(stat) # for testing
        return ("You succedd with a difference of " + str(dif))
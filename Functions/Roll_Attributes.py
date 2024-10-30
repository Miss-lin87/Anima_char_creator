import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

import dice as D

def menu_text():
    """This brings up the text of the menu and gives you choses to pick. the selection is made with just numbers"""
    print("Please make a selection:\n"
          "1. Method one\n"
          "2. Method two\n"
          "3. Method three\n"
          "4. Exit\n")
    slect = input("Make a selection")
    return str(slect)
    
def selection(slect):
    """This function only works in tandom with the menu function. This one calls the specific functions based on choice"""
    if slect == "1": return method_one()
    elif slect == "2": return method_two()
    elif slect == "3": return method_thre()
    elif slect == "4": return
    else: print("Wrong selection made. Please try again "); return selection()

# This is the first method of rolling stats. It Rolls stats 8 times, rerolling 1,2 and 3.
# Then replaces the lowest number rolled with a 10.
def method_one():
    """This is the first metod of rolling stats. Were the lowest number is replaced with a 10 and 1-3 is ignored"""
    rolls = []
    x = 8
    while x > 0:
        roll = D.otherdice(10)
        if roll in range(4,10): x -= 1; rolls.append(roll); remove_low(rolls)
        else: continue
    else: return rolls

def remove_low(rolls):
    """This function will sort the list. The pop the lowest value and add a 10"""
    sortR = sorted(rolls)
    sortR.pop(0)
    sortR.append(10)
    return sortR
# end of the functions to roll metod one

# This is the start of method two for rolling stats. 
# You roll 2d10 and take the highest roll. This is done 8 times
def method_two():
    """This method rolls 2d10 and keeps the higher of the two. Adds them to a list and returns the list"""
    rolls = []
    x = 8
    while x > 0:
        roll1 = D.otherdice(10)
        roll2 = D.otherdice(10)
        if roll1 > roll2: x -=1; rolls.append(roll1)
        else: x-= 1; rolls.append(roll2)
    return rolls
# This is the end of the secound method for rolling stats

# Begining of method 3 for rolling stats.
# This is the simplest method. Just roll 1d10 8 times and add it to a list
def method_thre():
    """This function rolls stats with just 1d10 8 times"""
    rolls = []
    x = 8
    while x > 0:
        roll = D.otherdice(10)
        rolls.append(roll)
        x -= 1
    return rolls
# This marks the end of the therd way to roll stats.

# this will be the main function to call to bring up the menue.
# Will do it in one call instead of nested calls
def menu():
    rolls = selection(menu_text())
    return rolls
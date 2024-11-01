from pathlib import Path
import shutil
import Functions.attribut_functions as AF
import Calulations.attrib_lib as AL
import Functions.Roll_Attributes as roll_attri

def char_pick(char=""):
    """This is called to let the player pick a character"""
    if char == "": char = input("What charaeter is being uppdated? ")
    else: char == char

def contin():
    """This is just used for contuniuation question"""
    x = input("What to continue to the next skill? J/N "); x = x.capitalize()
    if x == "J":
        return True
    elif x == "N":
        return False
    else: print("try again"); return contin()

def uppdate_list(char="", cont=False):
    """This is used to uppdate the list of attributes. If cont is true then it will ask continue after every stat"""
    if char == "": char = input("What character is being uppdated? ")
    else: char == char
    for x in AL.Attributes:
            print("The stat is: " + str(x) + " : " + str(AF.get_value_auto(char,x)))
            AF.new_value(char,x)
            if cont == True: contin()
    else: return

def New_Char():
    """This created a new blank character y copying the blank txt file and naming it whatever the input is. Will return the name of the character"""
    name = input("Please pick a name for the new Character ")
    path = Path(".\\Characters\\" + name + "_attrib.txt")
    test = (path.is_file())
    if test == False:
        sorce = ".\\Characters\\empty_attrib.txt"
        shutil.copy(sorce, "Characters\\" + name + "_attrib.txt")
        print("Characater has been created")
        question_roll = input("Do you want to roll stats now (Y/N)? "); question_roll = question_roll.capitalize()
        if question_roll == "Y": roll_attributes(name); return name
        else: return name
    else:
        option = input("Character already excist; pick an option \n 1. New Character \n 2. Exit \n")
        if option == "1": return New_Char()
        elif option == "2": return
        else: ValueError

def roll_attributes(char):
    """This rolls stats in 1 of 3 methods. Return the stats and then lets the player assign them to the character selecte"""
    rolls = roll_attri.menu()
    for x in AL.Attributes:
        print(rolls)
        selection = int(input("Please pick one of the numbers to assign to: " + str(x) + " "))
        AF.new_value(char,x,selection)
        rolls.remove(selection)
    print("The allocation of stats is completed. These are the new stats: ")
    for x in AL.Attributes:
        skill = AF.look_skill(char,x)
        print(skill)

def find_type(attri):
    """This is ment to find out if the attribute called is a grupe or a specific attribute. Not for use yet"""
    if attri in AL.All_Skills: return attri
    else:
        x = AF.find_type(attri)
        return x
from pathlib import Path
import shutil
import attribut_functions as AF
import Calulations.attrib_lib as AL
import Functions.Roll_Attributes as roll_attri

def char_pick(char=""):
    if char == "": char = input("What charaeter is being uppdated? ")
    else: char == char

def contin():
    x = input("What to continue to the next skill? J/N "); x = x.capitalize()
    if x == "J":
        return True
    elif x == "N":
        return False
    else: print("try again"); return contin()

def uppdate_list(char=""):
    if char == "": char = input("What character is being uppdated? ")
    else: char == char
    cont = True
    for x in AL.Attributes:
        if cont == True:
            print("The stat is: " + str(x) + " : " + str(AF.get_value_auto(char,x)))
            AF.new_value(char,x)
            cont = contin()
        else: return

def New_Char():
    name = input("Please pick a name for the new Character ")
    path = Path(".\\Characters\\" + name + "_attrib.txt")
    test = (path.is_file())
    if test == False:
        sorce = ".\\Characters\\empty_attrib.txt"
        shutil.copy(sorce, "Characters\\" + name + "_attrib.txt")
        print("Characater has been created")
    else:
        option = input("Character already excist; pick an option \n 1. New Character \n 2. Exit \n")
        if option == "1": return New_Char()
        elif option == "2": return
        else: ValueError

def roll_attributes(char):
    rolls = roll_attri.menu()
    skills_list = []
    for x in AL.Attributes:
        print(rolls)
        selection = int(input("Please pick one of the numbers to assign to: " + str(x) + " "))
        AF.new_value(char,x,selection)
        rolls.remove(selection)
    print("The allocation of stats is completed. These are the new stats: ")
    for x in AL.Attributes:
        skill = AF.look_skill(char,x)
        print(skill)

roll_attributes("char1")
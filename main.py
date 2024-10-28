from pathlib import Path
import shutil
import attribut_functions as AF
import char_uppdate as Cupp
import time

char = "None"

def menu():
    """This is the text for the inital menu"""
    global char
    print("Please select an option:\n"
          "The currently selected character is: " + str(char) + "\n"
          "1. Create new character\n"
          "2. Change the selected character\n"
          "3. Change all Attributes of existing character\n"
          "4. Change specific Attribute of existing character\n"
          "5. Export character to PDF\n"
          "6. Exit")
    select = input("Selection: ")
    return select

def selection(select):
    """This will take the input from the menue and actually do stuff with it"""
    global char
    if select == "1": sleep(0.25); char = Cupp.New_Char(); return_menu(2)
    elif select == "2": sleep(0.25); char = input("Change it to what character? "); return_menu(0.75)
    elif select == "3": sleep(0.25); Cupp.uppdate_list(char=char); return_menu(1)
    elif select == "4": sleep(0.25); AF.new_value(char=char); return_menu(1)
    elif select == "5": sleep(0.25); print("Not yet working"); time.sleep(0.75); selection(menu())
    elif select == "6": return
    else: ValueError

def return_menu(sec):
    """Function to return to the menue with a slight delay of X secounds"""
    print("The operation has finished. Returning to menu\n")
    time.sleep(sec)
    selection(menu())

def sleep(x):
    """Faster way to sleep the console for the inputed amount secounds"""
    time.sleep(x)

selection(menu())
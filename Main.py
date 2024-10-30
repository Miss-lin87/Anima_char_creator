from pathlib import Path
import shutil
import attribut_functions as AF
import char_uppdate as Cupp

def menu():
    print("Please select an option:\n"
          "1. Create new character\n"
          "2. Change all stat of existing character\n"
          "3. Change specific stat of existing character\n"
          "4. Export character to PDF\n"
          "5. Exit")
    select = input("Selection: ")
    return select

def selection(select):
    if select == "1": Cupp.New_Char()
    elif select == "2": Cupp.uppdate_list()
    elif select == "3": AF.new_value()
    elif select == "4": return
    elif select == "5": return
    else: ValueError

selection(menu())
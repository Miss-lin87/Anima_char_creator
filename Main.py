from pathlib import Path
import shutil

def New_Char():
    name = input("Please pick a name for the new Character ")
    path = Path(".\Characters\\" + name + "_attrib.txt")
    test = (path.is_file())
    if test == False:
        print("working")
        sorce =   ".\Characters\empty_attrib.txt"
        shutil.copy(sorce, "Characters/" + name + "_attrib.txt")
        print("File has been copied")
    else:
        option = input("Character already excist; pick a new name or exit? ")
        if option == "new name":
            New_Char()
        else:
            StopIteration
    

New_Char()
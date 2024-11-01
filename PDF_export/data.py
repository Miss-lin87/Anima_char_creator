from Functions.attribut_functions import get_value_auto as gva
from Functions.Call_functions import get_attri_modifier as get_mod

def Attributes_data(char):
    Attributes_data = [
        ["Attributes", "Base", "Actual", "Bonus"],
        ["Agility", gva(char,"Agility"),"", get_mod(str(gva(char,"Agility")))],
        ["Constitution", gva(char,"Constitution"),"",get_mod(str(gva(char,"Constitution")))],
        ["Dexterity", gva(char,"Dexterity"),"",get_mod(str(gva(char,"Dexterity")))],
        ["Strength", gva(char,"Strength"),"",get_mod(str(gva(char,"Strength")))],
        ["Inteligence", gva(char,"Inteligence"),"",get_mod(str(gva(char,"Inteligence")))],
        ["Perception", gva(char,"Perception"),"",get_mod(str(gva(char,"Perception")))],
        [  "Power", gva(char,"Power"),"",get_mod(str(gva(char,"Power")))],
        ["Wilpower", gva(char,"Willpower"),"",get_mod(str(gva(char,"Willpower")))]
    ]
    return Attributes_data
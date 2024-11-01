import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

All_Skills = ["Skills","Attributes","Stuff","Level","Other"]
Skills = {
# Skills_Athletics
"Acrobatics":5, "Athleticism":6, "Climb":7, "Jump":8, "Ride":9, "Swim":10,
# Skills_Vigor
"Composure":13, "Feats of str":14, "Withstand pain":15,
# Skills_Perception
"Notice":18, "Sertch":19, "Track":20,
# Skills_Intellectual
"Animals":23, "Appraisal":24, "Herbal lore":25, "History":26, "Magic appraisal":27, "Medicine":28, "Memorize":29, "Navigation":30, "Occult":31, "Sciences":32,
# Skills_Subterfuge
"Disguise":35, "Hide":36, "Lock picking":37, "Poisons":38, "Theft":39, "Trap lore":40, "Stealth":41,
# Skills_Creative 
"Art":44, "Dance":45, "Forging":46, "Music":47, "Slight of hand":48
}
Attributes = {"Agility": 51,"Constitution": 52, "Dexterity": 53,"Strength": 54, "Inteligence": 55, "Perception": 56, "Power": 57, "Willpower": 58}
Combat_skills = {"Attack": 61, "Block": 62, "Dodge": 63, "Initiative": 64}
Stuff = {"Weapon": 67, "Armor": 68}
Level = {"Level" : 1}
Other = {"Max life": 0, "Current life": 0} # need fixing later when posible

# test for attribute Modifiers
Mods = {"1":-30, "2":-20, "3":-10, "4":-5, "5":0, "6":5, "7":5,
        "8":10, "9":10, "10":15, "11":20, "12":20, "13": 25, "14":25,
        "15":30, "16":35, "17":35, "18":40, "19":40, "20":45}
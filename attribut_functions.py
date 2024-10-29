import fileinput
import sys
from pathlib import Path
from Calulations.attrib_lib import Skills, Attributes as attr, Combat_skills as comb_skills, Stuff as stuff, Other
from Functions.Call_functions import autofill

# this will start the process to replace the value of a skill. First get the character name, then the skill name and last the new value
def new_value(char="", raw_skill=""):
    if char=="" or raw_skill=="": char, raw_skill = autofill(char=char, attri=raw_skill)
    raw_value = input("What is the new value of the skill? ")
    stat_type = find_type(raw_skill)
    number = stat_type[raw_skill]
    file = str(Path.cwd()) + "\Characters\\" + char + "_attrib.txt"
    open_file = open(file, "r+")
    read_line = open_file.readlines()
    value = read_line[number]
    old_skill = value.strip()
    skill_name = raw_skill + " : "
    new_skill = skill_name + raw_value
    open_file.close()
    replace(file,old_skill,new_skill)
    print("Skill changed to " + look_skill(char, raw_skill))

def replace(file,target_skill,new_skill):
    for line in fileinput.input(file, inplace=1):
        if target_skill in line:
            line = line.replace(target_skill,new_skill)
        sys.stdout.write(line)

def look_skill(char,raw_skill):
    # select_skill = raw_skill
    stat_type = find_type(raw_skill)
    skill_number = stat_type[raw_skill]
    file = open((str(Path.cwd()) + "\Characters\\" + char + "_attrib.txt"), "r")
    read_line = file.readlines()
    output = read_line[skill_number]
    file.close()
    return output

def get_value_auto(char="", attri=""):
    if char=="" or attri=="": char, attri = autofill(char=char,attri=attri)
    stat_type = find_type(attri)
    value_number = stat_type[attri]
    file = open((str(Path.cwd()) + "\Characters\\" + char + "_attrib.txt"), "r")
    read_line = file.readlines()
    output_value = read_line[value_number]
    output_value = output_value.strip(attri + " : ")
    value = output_value.strip()
    return int(value)

def find_type(select_stat):
    if select_stat in Skills: stat_type = Skills; return stat_type
    elif select_stat in attr: stat_type = attr; return stat_type
    elif select_stat in stuff: stat_type = stuff; return stat_type
    elif select_stat in Other: stat_type = Other; return stat_type
    else: stat_type = comb_skills; return stat_type
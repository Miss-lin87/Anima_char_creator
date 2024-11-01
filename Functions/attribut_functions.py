import sys, os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), "..")))

import fileinput
from pathlib import Path
from Calulations.attrib_lib import Skills, Attributes as attr, Combat_skills as comb_skills, Stuff as stuff, Other, Level as lv
from Functions.Call_functions import autofill

def new_value(char="", raw_skill="", raw_value=""):
    """this will start the process to replace the value of a skill. First get the character name, then the skill name and last the new value"""
    if char=="" or raw_skill=="": char, raw_skill = autofill(char=char, attri=raw_skill)
    if raw_value=="": raw_value = input("What is the new value of the skill? ")
    else: raw_value = raw_value
    file = get_file(char)
    old_skill, new_skill = skill_names(raw_skill,char,raw_value)
    replace(file,old_skill,new_skill)
    return ("Skill changed to " + look_skill(char, raw_skill))

def replace(file,target_skill,new_skill):
    """Specific function to just replace an old value with a new one. Do not call unless needed"""
    for line in fileinput.input(file, inplace=1):
        if target_skill in line:
            line = line.replace(target_skill,new_skill)
        sys.stdout.write(line)

def look_skill(char,raw_skill):
    """Used to just look up the skill of a speicific skill. Usefull for looking something up without changing it"""
    stat_type = find_type(raw_skill)
    skill_number = stat_type[raw_skill]
    open_file = open(get_file(char), "r+")
    read_line = open_file.readlines()
    output = read_line[skill_number].strip("\n")
    open_file.close()
    return output

def get_value_auto(char="", attri=""):
    """This will automaticaly get the value of a specific skill from a character when called"""
    if char=="" or attri=="": char, attri = autofill(char=char,attri=attri)
    stat_type = find_type(attri)
    value_number = stat_type[attri]
    open_file = open(get_file(char), "r+")
    read_line = open_file.readlines()
    output_value = read_line[value_number]
    output_value = output_value.strip(attri + " : ")
    value = output_value.strip()
    return int(value)

def find_type(select_stat):
    """Used to find the type of skill is being called and return its specific name"""
    if select_stat in Skills: stat_type = Skills; return stat_type
    elif select_stat in attr: stat_type = attr; return stat_type
    elif select_stat in stuff: stat_type = stuff; return stat_type
    elif select_stat in lv: stat_type = lv; return stat_type
    elif select_stat in Other: stat_type = Other; return stat_type
    else: stat_type = comb_skills; return stat_type

def skill_names(raw_skill, char, raw_value):
    """Find the name of a skille as well as the skills value"""
    stat_type = find_type(raw_skill)
    number = stat_type[raw_skill]
    open_file = open(get_file(char), "r+")
    read_line = open_file.readlines()
    value = read_line[number]
    old_skill = value.strip()
    skill_name = raw_skill + " : "
    new_skill = str(skill_name) + str(raw_value)
    open_file.close()
    return old_skill, new_skill

def get_file(char):
    """defines the file with tha corret pathway. Used to make the main code a bit shorter"""
    file = str(Path.cwd()) + "\\Characters\\" + char + "_attrib.txt"
    return file

# def calculate_mod(char="",attri=""):


import fileinput
import sys
from attrib_lib import Skills, Attributes as attr, Combat_skills as comb_skills, Stuff as stuff

# this will start the process to replace the value of a skill. First get the character name, then the skill name and last the new value
def new_value():
    char = input("Pick the character? ")
    raw_skill = input("What skill has a new value? ")
    raw_value = input("What is the new value of the skill? ")
    number = Skills[raw_skill]
    file = char + "_attrib.txt"
    open_file = open(file, "r+")
    read_line = open_file.readlines()
    value = read_line[number]
    old_skill = value.strip()
    skill_name = raw_skill +" : "
    print(skill_name)
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
    select_skill = raw_skill
    skill_number = Skills[select_skill]
    file = open(char + "_attrib.txt", "r")
    read_line = file.readlines()
    output = read_line[skill_number]
    file.close()
    return output

def get_value():
    char = input("Please select the character? ")
    select_stat = input("Please select the stat? ")
    stat_type = find_type(select_stat)
    value_number = stat_type[select_stat]
    file = open(char + "_attrib.txt", "r")
    read_line = file.readlines()
    output_value = read_line[value_number]
    output_value = output_value.strip(select_stat + ": ")
    value = output_value.strip()
    return value

def get_value_auto(char, select_stat):
    stat_type = find_type(select_stat)
    value_number = stat_type[select_stat]
    file = open(char + "_attrib.txt", "r")
    read_line = file.readlines()
    output_value = read_line[value_number]
    output_value = output_value.strip(select_stat + ": ")
    value = output_value.strip()
    return value

def find_type(select_stat):
    if select_stat in Skills:
        stat_type = Skills
        return stat_type
    elif select_stat in attr:
        stat_type = attr
        return stat_type
    elif select_stat in stuff:
        stat_type = stuff
        return stat_type
    else:
        stat_type = comb_skills
        return stat_type
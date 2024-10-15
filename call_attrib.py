from attrib_lib import Skills

def get_skill():
    select = input("what skill to call? ")
    number = Skills[select]
    print("position is" + str(number))
    char = input("what Characters skill? ")
    file = open(char + "_attrib.txt", "r")
    skill = file.readlines()
    y = skill[number]
    print(y)
    f = int(y[-5:])
    return f
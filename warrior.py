def level_up():
    global level
    global level_dif
    level_pre = level
    level += int(input("number of levels increseed"))
    level_dif = level - level_pre

def innate_bonus():
    global Feats_of_sth
    global Wear_armor
    Feats_of_sth =+ (level_dif*5)
    Wear_armor =+ (level_dif*5)

def level_attack():
    levelif = level_dif
    global attack
    while levelif > 0:
        if attack < 50:
            attack += 5
            levelif += -1
        else:
            break

def level_defence():
    levelif = level_dif
    global defence
    while levelif >0:
        if defence <50:
            defence += 5
            levelif += -1
        else:
            break

import char
defence = char.char1["defence"]
level_dif = int(0)
level = char.char1["level"]
attack = char.char1["attack"]
Feats_of_sth = char.char1["Feats_of_sth"]
Wear_armor = char.char1["Wear_armor"]

level_up()
level_defence()
innate_bonus()
print("Current level is " + str(level))
print("current attack is " + str(attack))
print("current defence is " + str(defence))
print("current wear armor is " + str(Wear_armor))
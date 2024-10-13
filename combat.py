# initiate comabt
# calculate to hit etc

import dice
import charstats
import mathfunktions as math

roll = dice.rolldice
char = charstats

def attack():
    x = char.char1.attack + roll(100)
    # print("the attack roll is " + str(x))
    y = char.char2.defe + roll(100)
    # print("the defence roll is " + str(y))
    W_type = charstats.char1.weapons.prim_attack
    # print("the wepon type is " + str(W_type))
    AT = charstats.char2.armor.__getattribute__(W_type)
    # print("the armor rating is " + str(AT))
    combat_result = x-y
    # print("the result on the tabel is " + str(combat_result))
    combat_final = (math.flatten(combat_result))-((AT-1)*10)
    # print("the final combat result is " + str(combat_final))
    damage = charstats.char1.weapons.damage
    # print("the damage is " + str(damage))
    total_damage = damage * (combat_final/100)
    # print("the final damage is " + str(total_damage))
    return total_damage

print(attack())
# initiate comabt
# calculate to hit etc

import dice
import charstats
import weapons


def attack():
    x = charstats.char1.get("attack") + Rolldice(100)
    y = charstats.char2.get("defence") + Rolldice(100)
    h = charstats.char1.get("weapon")
    z = charstats.char2.get("armor")

   # if x-y > 0:

    return x, y, h

print(dice.openroll(100,90))
# initiate comabt
# calculate to hit etc

from dice import rolldice
import charstats
import weapons as weapons


def attack(x):
    x = charstats.char1.get("attack") + rolldice(100)
    y = charstats.char2.get("defence") + rolldice(100)
    h = charstats.char1.get("weapon")
    z = charstats.char2.get("armor")

   # if x-y > 0:

    return x

x=0
print(attack(x))
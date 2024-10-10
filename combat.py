# initiate comabt
# calculate to hit etc

from dice import Rolldice
import charstats
import weapons

x = charstats.char1.get("attack")
y = charstats.char2.get("defence")
print(x+Rolldice(50))

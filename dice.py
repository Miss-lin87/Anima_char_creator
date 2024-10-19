from random import randint as random

def roll():
        x = input("what number of sides to roll? ")
        x = int(x)
        return(rolldice(x))

def rolldice(select):
        if select == 10:
                return openroll10(10)
        elif select == 100:
                return openroll100(100,90,3)
        else:
                return otherdice(select)

def otherdice(dice):
        return random(1,dice)

def openroll100(dice, dice_target, dice_min):
        dice_target = dice_target
        dice_min = dice_min # -3 if skill enough
        total = random(1,dice)
        # print("total ", str(total)) # just for testing
        if total >= dice_target and dice_target != dice:
                # print("target " + str(dice_target)) # just for testing
                dice_target += 1
                return total + openroll100(dice, dice_target)
        elif total <= dice_min:
                print("the roll is a faliure")
                return total
        else:
                return total

def openroll10():
        roll= random(1,10)
        if roll == 10:
                # print(roll) # for testing the code
                return (roll+3)
        elif roll == 1:
                # print(roll) # for testing the code
                return (roll-3)
        else:
                # print(roll) # for testing the code
                return roll
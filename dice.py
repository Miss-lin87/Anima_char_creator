from random import randint as random


def Rolldice(dice):
        return random(1, dice)

def openroll(dice, dice_target):
        dice_target = dice_target
        total = random(1, dice)
        # print("total ", str(total)) just for testing
        if total >= dice_target and dice_target != dice:
                # print("target " + str(dice_target)) just for testing
                dice_target += 1
                return total + openroll(dice, dice_target)
                
        else:
                return total

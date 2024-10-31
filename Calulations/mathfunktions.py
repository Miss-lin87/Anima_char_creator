import math

def flatten(number):
    """Used to round the number inputed into the closest devider of 10"""
    if number > 9 and number < 100:
        number = int(str(number)[:1])
        number = int(number*10)
        return number
    elif number > 100:
        number = int(str(number)[:2])
        number = int(number*10)
        return number
    else:
        return 0
import math

def test(number):
    if number > 9 and number < 100:
        number = int(str(number)[:1])
        number = int(number*10)
        return number
    elif number > 100:
        number = int(str(number)[:2])
        number = int(number*10)
        return number
    else:
        return number
    
print(test(256))

import random

number1 = 0
number2 = random.randint(10,99)
number3 = random.randint(10,99)
number4 = random.randint(10,99)

def getToken(number1, number2, number3, number4):
    return "{} - {} - {} - {}".format(number1, number2, number3, number4)

def getActivation(number1, number2, number3, number4):
    number = [number1, number2, number3, number4]
    num1 = random.choice(number)
    num2 = random.choice(number)
    num3 = random.choice(number)
    num4 = random.choice(number)
    return "{}{}{}{}".format(num1, num2, num3, num4)
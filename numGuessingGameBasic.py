import random

randNum = random.randint(1,4) #store the random number generated

def sameNum(target, number):
    if target == number:
        result = "Win"
    else:
        result = "Fail"
    return result

guess = int(input("Guess a number between 1-3: "))
print(sameNum(randNum, guess))
import random

randNum = random.randint(1,21) #store the random number generated

at = 1

def sameNum(target, number):
    if target == number:
        result = "Win!"
    elif number > target:
        result = "Too high"
    elif number < target:
        result = "Too low"
    else:
        result = "Fail"
    return result

guess = int(input("Guess a number between 1-20: "))

g = sameNum(randNum, guess)

while g != "Win!":
    if g == "Too high":
        guess = int(input("Too high, try again: "))
    else:
        guess = int(input("Too low, try again: "))
    g = sameNum(randNum, guess)
    at+=1
print(sameNum(randNum, guess) + " It took you " + str(at) + " attempts.")
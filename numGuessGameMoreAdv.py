import random

randNum = random.randint(1,21) #store the random number generated

gNum = 0
score = 5

while gNum < 5:
    guess = int(input("Guess a number between 1-20: "))
    if guess == randNum:
        score-=gNum
        print("You win with score of " + str(score))
    elif guess > randNum:
        print("Too high")
    else:
        print("Too low")
    gNum+=1

if guess == randNum:
    print("Done")
else:
    print("You lose. The random number was " + str(randNum))
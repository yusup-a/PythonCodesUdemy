counter = 1
while counter<11:
    print(counter)
    counter +=1
print('Finished!')

secretNum = 14
userInput = int(input('Guess the secret number from 0 to 20: '))
while userInput != secretNum:
    print('Wrong!')
    userInput = int(input('Guess a number from 0 to 20: '))
print('Perfect! You guessed the secret number.')
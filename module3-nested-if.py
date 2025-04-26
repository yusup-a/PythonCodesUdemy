answerA = input('Do you like travelling? y/n: ')

if answerA == 'y':
    answerB = input('And do you like Asia? y/n: ')
    if answerB == 'y':
        print('Excellent! You can win a ticket to Thailand!')
    else:
        print('Sorry to hear that!')
else:
    print('Sorry to hear that!')
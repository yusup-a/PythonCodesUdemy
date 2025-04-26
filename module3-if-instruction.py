userAge = int(input('What is your age'))
if userAge > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif userAge == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify!')

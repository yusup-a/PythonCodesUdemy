userAge = int(input('What is your age'))
userCountry = input('What is your age')

if userAge < 25 and userCountry == 'Germany': #both conditions needs to be met for it to execute
    print('You can apply for a German student exchange programmes')
else:
    print('Sorry, you do not qualify')

if userCountry == 'Norway' or userCountry == 'Denmark' or userCountry == 'Sweden':
    print('You can apply for a Scandinavian student exchange programmes') #one condition needed to be met
else:
    print('Sorry, you do not qualify')


# Order of priority
# 1. not
# 2. and
# 3. or
import sys

userName = input('What is your name?')

#SystemExit BaseException
if userName == '':
    print('Empty name? I cannot work with that. I am closing the program. Bye!')
    sys.exit()
print('Hello', userName)
print('Let us get started')

programmingLanguages = ["Java", "Python", "C++"]
#print(programmingLanguages[10]) #IndexError (index 10 is not present in the list)

ages = {'Jim':30, 'Pam':28, 'Kevin':33}
#print(ages['Michael']) #KeyError (The key 'Michael' doesn't exist in the ages dictionary)

#type error indicates that the type of data you are trying to use is not correct
#for example
#age = input('What is your age? ')
#print('In 10 years, you will be', age + 10)
# #input function's default return type is string
# so you can not do integer operations with a string

#type error
#for example, you type in a when the program asks for a number

#you will see the more specific exceptions when you get an exception
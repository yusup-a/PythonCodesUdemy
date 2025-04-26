# value = int(input('Enter an integer: '))
# print('The inverse of', value, 'is', 1/value)

#an exception is an event which occurs during the execution of a program that disrupts the normal flow
#python raises an exception when you enter letters for value

#you put code that could raise an exception in the try block
try:
    value = int(input('Enter an integer: '))
    print('The inverse of', value, 'is', 1 / value)
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')
except ZeroDivisionError:
    print('You provided 0 and division by 0 is not possible, sorry')
except:
    print('Something strange happened here, sorry')
#the code in the except block is the code that handles the exception
#to make more except blocks, type except errorName:
#none of the exceptions (errors) can be mentioned more than once
#you can add a general except block that covers other exceptions
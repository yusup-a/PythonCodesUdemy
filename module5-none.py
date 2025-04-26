#functions can do 2 things (it can do both at the same time)
# 1. It can cause some EFFECT (change)
# 2. It can RETURN a meaningful value

print('hello') #only causes effect (1)
length = len('hello')  #only returns a meaningful value (2)

# input does both, it returns the user's input (2)
# it causes an effect by showing text (prompt) (1)
#number = input('What is the number? ')

# print returns nothing literally,
# but it returns the value none
print_return = print('Hello world')
print(print_return)

#none is used to describe a null value or no value at all
#none is NOT ZERO
#none is NOT False
#none is NOT the same as an empty string
#only none can be none


x = None
if x:
    print('None is True')
elif x is False:
    print('None is False')
else:
    print('None is not True, or False, None is just None')

y = None
if y is None:
    print('yes')
if y == None:
    print('it does ')

# none is a value returned implicitly by functions that don't return anything meaningful

def greet():
    print('hello')

#greet() returns None
x = greet()
print(x)
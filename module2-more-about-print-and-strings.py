#len() gives length of a string
print(len('Hello!'))

#Keyword arguments are arguments which you can use at the end of a function invocation
# They are used after ALL the OTHER arguments (they are optional)
print('Hellow, World!', end='.') #keyword arguments/named arguments (default argument for end is \n)
print('Python speaking!')

#Sep argument specifies the separator between values printed to the output
# default argument for sep is a space
name = 'John'
print('Your first name is', name, 'Welcome!', sep='-', end = '=')
#can use both end and sep at the same time

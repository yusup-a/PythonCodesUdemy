userData = ('John','American', 1964)
print(len(userData))

if 'American' in userData:
    print('This person comes from the US!')

for element in userData:
    print(element)

#this makes a new tuple
userData = ('John','American', 1964) + ('teacher','male')
print(userData)

numbers = (0,1) * 10
print(numbers)

#this represent user John and you can really change when and where you were born
userData = ('John','American', 1964)

first = 5
second = 7
fist, second = second, first #this is a tuple
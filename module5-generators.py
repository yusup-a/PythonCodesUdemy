def get_number():
    for i in range(1,4):
        yield i #this makes the function a generator


print(get_number()) #generator object

#generators work by generating certain values one by one
#when you use next when there are no more values available, you get an error
generator = get_number()
print(next(generator))
print(next(generator))
print(next(generator))

for x in get_number():
    print(x)

numbers = list(get_number())
print(numbers)
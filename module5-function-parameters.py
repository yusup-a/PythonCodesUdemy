def get_average(inputNums): #inputNums is a parameter
    sum = 0.0

    for number in inputNums:
        sum+=number
    average = sum / len(inputNums)

    print(average)

# [5.0, 3.5, 7.8, 9.9, 10.0] is an argument
# you need to enter an argument with the correct type (list)
get_average([5.0, 3.5, 7.8, 9.9, 10.0])

def print_letter_count(text, letter):
    counter = 0
    for char in text:
        if char == letter:
            counter+=1
    print('Number of', letter, 'is', counter)

#the order matters!!
# these are called positional arguments since the order matters
print_letter_count('Welcome', 'e')

# named arguments are (parameter name = value
#you can swap the arguments if you use
print_letter_count(text='Welcome', letter='e')
print_letter_count(letter='e', text='Welcome')
# end argument has the default value of a new line character (\n)
# sep argument has the default value of a whitespace character ( )
print('Hello', 'How are you?', end='.', sep='-')
print()

# to add a default value for a parameter,
# do parameterName = (any value)
# in the def line
# parameters with default values MUST be at the end
def print_letter_count(text='This is the default string to search', letter='a'):
    counter = 0
    for char in text:
        if char == letter:
            counter+=1
    print('Number of', letter, 'is', counter)

print_letter_count('How many letters a are here?')
print_letter_count()

# named arguments MUST be at the end
# print_letter_count(letter='a', 'Search here')
print_letter_count('Search here', letter = 'a')
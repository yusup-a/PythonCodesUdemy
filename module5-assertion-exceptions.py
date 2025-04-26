#Assertions are assumptions in our program that should always be true.

#format is this
# assert conditions_that_is_assumed_to_be_always_true, this is executed when the condition is false
def calculate_inverse(number):
    assert (number != 0), 'Got 0 as number!'
    return 1/number

print(calculate_inverse(5))

#print(calculate_inverse(0)) will show AssertionError: Got 0 as number!

#The purpose of assertions are to notify you about bugs during development so you can catch and fix bugs quickly.
# available logical operators
#
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# == equals
# != not equals

password = input('Do you know the secret password?')

if password != '--secret':
    print('not correct')
else:
    print('correct password')

# if 2 == 2.0:
# this will be true since python automatically converts the int to a float
#It immediately exits the function when the return statement happens
#This means that any instruction after the return statement will be IGNORED

def get_average(inputNums): #inputNums is a parameter
    sum = 0.0
    for number in inputNums:
        sum+=number
    average = sum / len(inputNums)
    return average

print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))

average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])
if average > 5.0:
    print('The average is too high!')

def get_average2(inputNums): #inputNums is a parameter
    sum = 0.0
    for number in inputNums:
        sum+=number
    average = sum / len(inputNums)
    return average
    print('Show me!') #this never happens since it is after the return statement

print(get_average2([2]))

def is_first_last_equal(number_list):
    if len(number_list) == 0:
        return #returns None
    if number_list[0] == number_list[-1]:
        return True
    else:
        return False

print(is_first_last_equal([10,20,30,40,10]))
print(is_first_last_equal([10,20,30,40,50]))
print(is_first_last_equal([]))
#we type return by itself when we want to exit a function
# without returning anything meaningful
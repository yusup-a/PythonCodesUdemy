#recursion takes place when a function calls itself
# factorial 3! = 3*2*1 = 6

#iterative function
def get_factorial(num):
    factorial = 1
    for x in range(1,num+1):
        factorial*=x
    return factorial

print(get_factorial(6))

# 1! = 1
# 2! = 2 * 1!
# 3! = 3 * 2!
# 4! = 4 * 3!
# 5! = 5 * 4!

#recursive function
def get_factorial_recursive(num):
    if num <= 1:
        return 1
    return num * get_factorial_recursive(num-1)

print(get_factorial_recursive(6))
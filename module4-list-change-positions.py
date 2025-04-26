#regular way of swapping values of variables

# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping:', first, second)
# temp = first
# first = second
# second = temp
# print('After swapping:', first, second)
#
# #shortcut
# first = input('Enter first number: ')
# second = input('Enter second number: ')
# print('Before swapping:', first, second)
# first, second = second, first
# print('After swapping:', first, second)

#we can use the same logic for lists
top_cities = ['NYC', 'LA', 'Chicago','Houston','Phoenix']
top_cities[0], top_cities[4] = top_cities[4], top_cities[0]
print(top_cities)

top_cities = ['NYC', 'LA', 'Chicago','Houston','Phoenix']
top_cities.sort() #sorted in alphabetical order
print(top_cities)

random_numbers = [2,5,0,-3,4]
random_numbers.sort() #sorted in increasing order (least to greatest)
print(random_numbers)

random_numbers = [2,5,0,-3,4]
random_numbers.sort(reverse=True) #sorted in decreasing order (greatest to least)
print(random_numbers)

top_cities = ['NYC', 'LA', 'Chicago','Houston','Phoenix']
print(sorted(top_cities)) #sorted doesn't change the list
print(top_cities)

#list_name.sort(): sorts the original list
#sorted(list_name): gives back a new, sorted list, keeps the original unchanged (sorting in place)

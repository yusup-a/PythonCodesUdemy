#sequences in python are special datastructures
# that can store more than one value
# and can be browsed sequentially,
# meaning element by element,
# like strings and lists

top_cities = ['NYC', 'LA', 'Chicago','Houston','Phoenix']

#this is good for going through a list
# but you don't have access to the index of the current element
for city in top_cities:
    print('Current city:', city)

# you have access to the index of the current element with this way
for city_index in range(len(top_cities)):
    print('Current index:', city_index, '| Current city:',top_cities[city_index])

spendings = [32.45, 18.65, 23.45, 78.32, 5.23]
sum = 0.0

for spending in spendings:
    sum += spending
print('Money spent:',sum)
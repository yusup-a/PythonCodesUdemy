top_cities = ['NYC', 'LA','Singapore', 'Chicago','Houston','Phoenix']

#When you delete an element, there are no empty holes in the list
del top_cities[2]
print(top_cities)

top_cities = ['NYC', 'LA','Singapore', 'Chicago','Houston','Phoenix']
#Deletes elements from index 3 and forward
del top_cities[3:]
print(top_cities)

top_cities = ['NYC', 'LA','Singapore', 'Chicago','Houston','Phoenix']
#Deletes all the elements
del top_cities[:]
print(top_cities)

# top_cities = ['NYC', 'LA','Singapore', 'Chicago','Houston','Phoenix']
# # This literally Deletes the list top_cities so it gives an ERROR
# del top_cities[]
# print(top_cities)
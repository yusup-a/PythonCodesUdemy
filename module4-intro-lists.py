# A collection in Python is a data type that can store more than one value in a single variable
# lists
# tuples
# dictionaries

#lists are used to store multiple values of the same type, multiple ints, multiple floats, etc.

city1 = 'NYC'
city2 = 'LA'
city3 = 'Chicago'
city4 = 'Houston'
city5 = 'Phoenix'

empty_list = []
top_cities = ['NYC', 'LA', 'Chicago','Houston','Phoenix']
print(top_cities)

#INDEX STARTS AT 0 AND ENDS WITH len(variable)-1
print(top_cities[0])
print(top_cities[4])
print(top_cities[-1]) #gives last element

print(top_cities[0:2])
#[first,second]
# first is inclusive  (included)
# second is exclusive (not included)

# if [2:] it means start from index 2 and get everything after index
print(top_cities[2:])

# if [:3] it means take everything from start up to index 3 not including index 3 (exclusive)
print(top_cities[:3])

# These 2 are the same
print(top_cities)
print(top_cities[:])

# You never get an error when you enter non-existing index when slicing
# If you exceed the boundaries, you will get an empty list
print(top_cities[10:15])

# When you access a single element, you get a string (in this case)
# Slicing gives you a list
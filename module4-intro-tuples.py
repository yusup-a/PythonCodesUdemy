#tuples use ()
empty_tuple = ()

oneElementTupleA = (1,)
oneElementTupleB = 1,

threeElementTuple = 1,2,3
print(threeElementTuple) #prints with parenthesis even when you don't use them

# mutable data can be freely updated anytime you want (lists)
# immutable data can NOT be freely updated anytime you want (tuples)

#this is possible
userData = ('John','American', 1964)
userData = ('Katya','Russian', 1980)
#you can't add or delete elements to a tuple

#you can't change specific elements in a tuple
print(userData)

# Biggest difference between lists and tuples is
# that lists are mutable while tuples are immutable
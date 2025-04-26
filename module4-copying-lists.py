originalName = 'John'
newName = originalName
originalName = 'Mike'
print(originalName,newName)

originalList = [1,2,3]
newList = originalList
originalList[0] = -5
print('Original:', originalList, '\nNew:',newList)
#both originalList and newList both point to the same list stored in memory
# so when you try to modify some of the elements in one of the variables,
# you also modify the elements of the other variable

originalList = [1,2,3]
newList = originalList[:]
originalList[0] = -5
print('Original:', originalList, '\nNew:',newList)
# use slicing to make a separate copy of a list

originalList = [1,2,3]
newList = originalList[:2]
originalList[0] = -5
print('Original:', originalList, '\nNew:',newList)
# you can also slice some parts of another list and make a separate copy
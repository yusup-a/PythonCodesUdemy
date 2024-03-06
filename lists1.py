mfood2 = ['eggs','coffee','apple','cheese cube']
print(mfood2)

#number based list
nos = [4,56,7,11,15]
print(nos)

#mixed based list
mix = [4,11,7,25,"cat","dog","rat"]
print(mix)

#pass a list inside another list
mix2 = [12,2,'egg', 32, 'coffee', nos]
print(mix2)

#create a list from scratch
contact = [] #empty list
contact.append("Gary") #adds "Gary" to the END of the list
contact.append("Gary") #adds "Gary" to the END of the list
print(contact)

#add several items to a list
contact.extend(['Ray','Tia', 3,8,2])

#insert item at index 2 (3rd place)
contact.insert(2, "Molly")
print(contact)

nos2 = [2,7,14,5,26,19,30,14,35]
print(nos2)

nos2.remove(14) #literally removes that specific value (if multiple, it will remove only the first one it sees)
print(nos2)

del nos2[3] #deletes the value in the list at index 3 (4th place)
print(nos2)

rno=  nos2.pop(2) #removes the value at index 2 and stores it into variable rno
print(rno)

print(nos2[0]) #prints the value in the list at index 0  (1st place)
print(nos2[1:4]) #prints the values at index 1 thru index 4-1 (3)

nos2[1] = 6 #changes the value in index 1 (2nd place) to 5
print(nos2)
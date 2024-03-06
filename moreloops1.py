dict1 = {'Japan':'Tokyo', 'China':'Beijing', 'Taiwan':'Tapei', 'South Korea':'Seoul'}

for i in dict1: #prints out all keys
    print(i)

for s,c in dict1.items():
    print(s + "'s capital is " + c)

for b in dict1:
    print(b, dict1[b])

for i in range(21):
    if i % 2 == 0:
        print(i)

for x in range(1,5): #outer loop
    print("CAT")
    for y in range(1,4): #inner loop
        print("DOG")
    print("Over") #final line
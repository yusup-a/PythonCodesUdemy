dict1 = {'Japan':'Tokyo','China':'Beijing','South Korea':'Seoul','North Korea':'Pyongyang','a':3}
#Key is Japan and the value is Tokyo, key is China and value is Beijing, the key is a and the value is 3
print(dict1)
print(len(dict1)) #number of items (key-value pairs)

print(dict1.keys()) #keys
print(dict1.values())#values

dict2 = dict1.copy() #make a copy of dict1
print(dict2)

del dict2['a'] #you only have to delete the key to remove both key and value
print(dict2)

#add new key-value pair
#nameOfDict[key] = value
dict2["HK Sar"] = "Hong Kong" #HK Sar is key and Hong Kong is value
dict2[10] = "bullseye"
print(dict2)

print('a' in dict1) #prints True or False wheter or not the key 'a' is in dict1
print('b' in dict1) #prints True or False wheter or not the key 'b' is in dict1
print('b' not in dict1) #prints True or False wheter or not the key 'b' is NOT in dict1

print(dict2[10]) #prints the value of the key 10
print(dict2["China"]) #prints the value of the key "China"

print(sorted(dict1)) #sorts keys in Alphabetical order
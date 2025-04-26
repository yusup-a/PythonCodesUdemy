#dictionaries are mutable

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'
print(grades)

#one way to change a value for a key (this method is preferred)
grades['Anne'] = 'A'
print(grades)

#another way to change a value for a key
grades.update({'John':'A'})
print(grades)

print(len(grades))

if 'John' in grades:
    print('John got:', grades['John'])

del grades['John']
print(grades)

grades = {}
grades['John'] = 'A-'
grades['Anne'] = 'B'

#prints keys
for el in grades:
    print(el)

#prints keys
for el in grades.keys():
    print(el)

#prints values
for el in grades.values():
    print(el)

#prints values
for el in grades:
    print(grades[el])

#prints both key and value
#FORMAT
# for key, value in dictionaryName.items():
for person, grade in grades.items():
    print(person, 'got', grade)
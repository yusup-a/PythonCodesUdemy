#dictionaries use {}

emails = {
    'Anne Stahl': 'astahl@gmail.com',
    'Peter Small': 'peters@yandex.com',
    'Mark Steel': 'mark@steel.com'
}
#format is key:value(, if multiple key value pairs in dictionary)
# keys can be any type of variables EXCEPT LISTS
# values can be ANY type of variables

#'Mark Steel' is the key for the value 'mark@steel.com'
print(emails['Mark Steel'])

spanishAnimals = {
    'dog':'el perro',
    'cat':'el gato',
    'horse':'el caballo',
    'bird':'el pajaro'
}
print(spanishAnimals['bird'])

#EACH KEY MUST BE UNIQUE

spanishAnimals = {
    'dog':'el perro',
    'cat':'el gato',
    'horse':'el caballo',
    'bird':'el pajaro',
    'bird':'el ave'
}
print(spanishAnimals) #replaces old value (el pajaro) with new value (el ave)

#You can't provide a value for a key
# print(spanishAnimals['el perro'])
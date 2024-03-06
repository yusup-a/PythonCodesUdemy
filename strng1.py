str1 = "Bruh"
str2 = "momento"
str3 = "primo"

print(str1 + str2 + str3) #combines all 3 strings
print(str1 + " " + str2 + " " + str3) #combines all 3 string but with spaces in between them

c = " ".join([str1,str2,str3]) #joins (concatanates) each string togethr and the thing before the .join is in between each string
print(c)

print(len(c)) #tells us the length (number of characters) of a string

print(c[0:12]) #1st num is starting point, 2nd num ends at 2nd num - 1
print(c[:4]) #when theres no 1st num, it starts from the beggining until 2nd num - 1
print(c[5:]) #when theres only 1st num, it starts from 1st num to everything after
print(c[:]) #if theres no 1st or 2nd num, it gives everything

print(c.upper()) #makes all characters uppercase
print(c.lower()) #makes all characters lowercase

print(c.split()) #splits between spaces (whitespace)

print(c.replace("primo", "leon")) #replaces primo of string "c" with leon
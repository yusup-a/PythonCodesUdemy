favBand = 'Green Day'
print(favBand[6])
print(favBand[:6])
#favBand[6] = 'M' #ERROR, you can't change a specific character in a string

text = 'please capitalise me'
textCap = text.upper()
print(textCap)

userNum = input('Please provide a number: ')
if userNum.isnumeric(): #checks if a string ONLY contains numbers
    print('Thank you, that\'s a correct a number!')
else:
    print('Sorry,', userNum, 'is not a number!')

#islower() checks if the string only contains lowercase characters
#isspace() checks if the string only contains white spaces
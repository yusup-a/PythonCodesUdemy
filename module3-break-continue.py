# break means that it immediately exits loop and moves on to next lines of code
# continue means that it escapes the current interation and moves on to the next iteration

while True:
    name = input('Enter name or EXIT to close the program: ')
    if name=='EXIT':
        break
    print('Hello', name)

for i in range(1,21):
    if i % 5 == 0:
        continue
    print(i)
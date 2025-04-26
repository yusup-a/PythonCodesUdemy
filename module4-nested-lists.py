numbers = [1,2,3,4]
countries = ['UK', 'US', 'Germany']
countries = [1, 'UK', 2, 'US'] #not recommended, keep the type of data consistent in a list

cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']] #nested lists
print(cells[0])
print(cells[1])
print(cells[0][0])

for x in cells:
    print('Element:', x)

for x in cells:
    for y in x:
        print('Element:', y)

table = cells
for row in table:
    for cell in row:
        print(cell, '', end='')
    print()

#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5

table2 = [[i for i in range(1,6)] for j in range(4)]

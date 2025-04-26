city1 = ('London', 'UK', 8.98)
city2 = ('Canberra', 'Australia', 0.4)
city3 = ('Algiers', 'Algeria', 3.9)

capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]

for capital in capitals:
    print('Name:', capital[0], ', Country:', capital[1], ', Population:', capital[2])

userData = ('John','American', 1964, [77.0, 78.2, 77.5])
userData[3].append(79.6)
print(userData)
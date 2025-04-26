# numbers = []
# for i in range(1,101):
#     numbers.append(i)
# print(numbers)

#list comprehension
# numbers = [i for i in range(1,101)]
# print(numbers)

# so list comprehension is a list created on the fly when you run
numbers = [i for i in range(1,101) if i % 3 != 0]
print(numbers)
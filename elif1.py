import random

ans1 = "cat"
ans2 = "dog"
ans3 = "goat"
ans4 = "tortoise"
ans5 = "kitten"

print("Select my pet")

ques = input("Which is the most suitable pet to keep in a flat?\n")

choice = random.randint(1,5)

if choice==1:
    answer = ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
else:
    answer = ans5
print(choice)
print(answer)
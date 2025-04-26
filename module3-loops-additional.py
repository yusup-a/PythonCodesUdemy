# loop syntax requires at least one instruction inside the loop's body
# pass is kinda like placeholder, it does nothing functionally

for i in range(11):
    pass

for a in range(1,6):
    for b in range(1,6):
        print(a,'x',b,'=', a*b)

#else branch of a loop is ALWAYS executed exactly once (except when there is a break statement)
i = 2
while i < 5:
    print(i)
    i+=1
else:
    print('else',i)
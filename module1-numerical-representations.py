#underscores in numbers
# 12000300
# 12_000_300
# PYTHON SEES the 2 numbers as same
# You can use underscores to see big numbers better (improves readability)
#scientific notation
# 3e4 = 3E4 = 3 * 10000 = 30000
# 3e-4 = 3E-4 = 3 * 1/10000 = 0.0003
# Python automatically uses scientific notation when printing BIG or small numbers
print(0.000000000000000000000000003)

#octal numbers
# start with 0O or 0o (zero first and then O or o) only numbers from 0 to 7
# rarely used (just recognize them)
print(0o123)

#hex numbers
# start with 0X or 0x (zero first and then X or x)
# only numbers from 0 to 9 and A(10), B(11), C(12), D(13), E(14), F(15)
print(0x123)

#Python automatically converts them to base 10 numbers (decimal)


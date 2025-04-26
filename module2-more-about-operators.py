# + and - operators are binary since they work with two operands or two values

# unary operators 1 operand or 1 value
print(+12) #plus sign optional
print(-2)  #minus is NOT optional

#ORDER OF OPERATORS
# 1. () parenthesis
# 2. **
# 3. *, /, //, or %
# 4. + or -

#Precision of floats are limited

# 2**8 = 256 CORRECT
# 4**3 = 64 INCORRECT
# Python STARTS FROM RIGHT WHEN USING EXPONENTS
# Exponentation operator (**) uses right-sided binding (starts from the right)
print(2**2**3)
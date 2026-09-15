# Program to Demonstrate Operator Precedence


# Assign values to variables
a = 10
b = 5
c = 2


# Calculate expressions using operator precedence
# Multiplication (*) is performed before addition (+)
result1 = a + b * c

# Parentheses () have the highest priority
result2 = (a + b) * c

# Exponentiation (**) has higher priority than multiplication (*) and addition (+)
result3 = a + b * c ** 2


# Display the values of variables
print("a =", a, "b =", b, "c =", c)


# Display the calculated results
print("a + b * c =", result1)
print("(a + b) * c =", result2)
print("a + b * c ** 2 =", result3)
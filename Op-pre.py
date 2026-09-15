# Program to Demonstrate Operator Precedence


# Example 1: Exponentiation
# ** has higher precedence than other arithmetic operators
x = 2 ** 3
print("2 ** 3 =", x)


# Program 1: Parentheses have the highest precedence
x = (10 + 5) * 2
print("(10 + 5) * 2 =", x)


# Program 2: Multiplication is performed before addition
y = 10 + (5 * 2)
print("10 + (5 * 2) =", y)


# Program 3: Multiplication (*) is performed before addition (+)
z = 10 + 2 * 3
print("10 + 2 * 3 =", z)


# Program 4: Division (/) and multiplication (*) are performed
# before addition (+)
a = 10 + 20 / 5 * 2
print("10 + 20 / 5 * 2 =", a)
# Program to Swap Two Numbers Using Temporary Variables

print("--------- Swapping Using Temporary Variables ---------")
print()


# Assign values to variables
a = 10
b = 20


# Display values before swapping
print("Before Swapping:")
print("a =", a)
print("b =", b)


# Swap the values of a and b
# Python allows swapping without an extra variable
a, b = b, a


# Display values after swapping
print("\nAfter Swapping:")
print("a =", a)
print("b =", b)
# Program to calculate power using default arguments

def power(base, exponent=2):
    return base ** exponent

num = int(input("Enter the base number: "))

print("Power =", power(num))
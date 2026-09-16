# Program to calculate factorial using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num =int(input("enter a nummber"))
result =factorial(num)
print("FActorail of",num,"=",result)
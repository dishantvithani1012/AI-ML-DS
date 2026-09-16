a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if a>b:
    if a>c:
        largest = a
    else:
        largest = c
else:
    if b>c:
        largest=b
    else:
        largest=c

print("The Largest value of A B C is :",largest)
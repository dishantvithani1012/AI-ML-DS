# Program to demonstrate break, continue, and pass inside loops
#1.break
print("\n Using brak")
for i in range(1,6):
    if i==3:
        break
    print(i)
#countinue
print("\n Using countinue")
for i in range(1,6):
    if i==3:
        continue
    print(i)
#pass
print("\n Using pass")
for i in range(1,6):
    if i==3:
        pass
    print(i)

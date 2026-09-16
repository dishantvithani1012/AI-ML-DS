#python for loops 
friuts =["apple","banana","cherry"]
for x in friuts:
    print(x)

#looping through a string 
for x in "banana":
    print(x)

#the break statement 
friuts =["apple","banana","cherry"]
for x in friuts:
    print(x)
    if x == "banana" :
        break

#the continue statemnet 

friuts =["apple","banana","cherry"]
for x in friuts:
    if x == "banana":
        continue

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
for x in range(6):
    print(x)

# increment the sequencr with 3
for x in range(2, 30, 3):
    print(x)

#print all numbers from 0 to 5, and print a message
 





#while loop
i = 1
while i < 6:
    print(i)
    i += 1

#the break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=  1

# The continue Statement
i == 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
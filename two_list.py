# Program using zip() and enumerate() to iterate over two lists simultaneously

names = ["Dishant", "Rahul", "Amit", "Raj"]
marks = [85, 78, 92, 88]

for index, (name, mark) in enumerate(zip(names, marks), start=1):
    print(index, name, mark)
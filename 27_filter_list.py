# Program to use lambda functions with map() and filter()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() to find squares
squares = list(map(lambda x: x * x, numbers))

# Using filter() to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Original List:", numbers)
print("Squares using map():", squares)
print("Even numbers using filter():", even_numbers)
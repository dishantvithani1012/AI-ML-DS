# Program to Find the Area and Perimeter of a Rectangle and Circle

import math


# -----------------------------
# Rectangle Dimensions
# -----------------------------

length = 10
width = 5


# -----------------------------
# Circle Radius
# -----------------------------

radius = 7


# -----------------------------
# Rectangle Calculations
# -----------------------------

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)


# -----------------------------
# Circle Calculations
# -----------------------------

circle_area = math.pi * radius * radius
circle_perimeter = 2 * math.pi * radius


# -----------------------------
# Display Rectangle Results
# -----------------------------

print("Rectangle")
print("Length =", length)
print("Width =", width)
print("Area =", rectangle_area)
print("Perimeter =", rectangle_perimeter)


# -----------------------------
# Display Circle Results
# -----------------------------

print("\nCircle")
print("Radius =", radius)
print("Area =", round(circle_area, 2))
print("Perimeter =", round(circle_perimeter, 2))
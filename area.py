import math

# Rectangle

length = float(input("Enter the length of rectangle: "))
width = float(input("Enter the width of rectangle: "))

area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)

print("Area of Rectangle:", area_rectangle)
print("Perimeter of Rectangle:", perimeter_rectangle)

# Circle

radius = float(input("Enter the radius of circle: "))

area_circle = math.pi * radius * radius
perimeter_circle = 2 * math.pi * radius

print("Area of Circle:", area_circle)
print("Perimeter of Circle:", perimeter_circle)
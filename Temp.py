# Program to Convert Celsius Temperature
# into Fahrenheit and Kelvin

# Get temperature in Celsius from the user
celsius = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Convert Celsius to Kelvin
kelvin = celsius + 273.15

# Display the converted temperature
print("Fahrenheit =", fahrenheit)
print("Kelvin =", kelvin)
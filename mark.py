# Student Marks Calculator

name = input("Enter student name: ")

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))

total = maths + python + english
percentage = total / 3

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("\n--- Student Result ---")
print(f"Student Name : {name}")
print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")
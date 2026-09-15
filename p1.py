# ACTIVITY-1: Student Marksheet Program

student_name = input("Enter student name: ")
roll_number = int(input("Enter roll number: "))

english = float(input("Enter English marks: "))
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
computer = float(input("Enter Computer marks: "))
social_science = float(input("Enter Social Science marks: "))

total = english + maths + science + computer + social_science
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n----- STUDENT MARKSHEET -----")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("English:", english)
print("Maths:", maths)
print("Science:", science)
print("Computer:", computer)
print("Social Science:", social_science)
print("Total Marks:", total, "/ 500")
print("Percentage:", percentage, "%")
print("Grade:", grade)
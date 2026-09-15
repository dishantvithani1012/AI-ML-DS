# 2. STUDENT RESULT PROCESSING

def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, subjects):
    return total / subjects


def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "F"


def calculate_result(percentage):
    if percentage >= 40:
        return "Pass"
    else:
        return "Fail"


name = input("Enter student name: ")
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = calculate_total(marks)
percentage = calculate_percentage(total, len(marks))
grade = calculate_grade(percentage)
result = calculate_result(percentage)

print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Total Marks:", total)
print(f"Percentage: {percentage:.2f}%")
print("Grade:", grade)
print("Result:", result)
# Program to demonstrate *args and **kwargs

def student_info(*args, **kwargs):
    print("Subjects:", args)
    print("Student Details:")

    for key, value in kwargs.items():
        print(key, ":", value)


student_info(
    "Python",
    "Java",
    "Database",
    Name="Dishant",
    Course="MCA",
    Semester=1
)
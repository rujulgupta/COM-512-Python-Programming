# Write a Python program to store one student data as a tuple: name, roll number, and marks. Display students who scored above 75
students = [
    ("Rahul", "2024A1R001", 82),
    ("Priya", "2024A1R002", 91),
    ("Amit", "2024A1R003", 65),
    ("Suman", "2024A1R004", 78)
    ]
print("Students scoring above 75: ")
for students in students:
    name, roll_no, marks = students

    if marks > 75:
        print(name, roll_no, marks)
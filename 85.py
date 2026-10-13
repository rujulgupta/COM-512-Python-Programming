# Write a python program to create records of n students. Store each student record as a dictionary containing roll number, name, branch and marks. Store all records in a list and search for a student using roll number. 
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = int(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

search = int(input("Enter roll number to search: "))

for student in students:
    if student["roll"] == search:
        print(student)
        break
else:
    print("Student not found")
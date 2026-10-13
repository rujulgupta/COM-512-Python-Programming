n = int(input("Enter number of students: "))
database = []
for i in range(n):
    roll_no = input("Enter roll number: ")
    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))
    student_record = (roll_no, name , branch, cgpa)
    database.append(student_record)
    print("\n ")
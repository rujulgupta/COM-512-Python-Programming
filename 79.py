# Write a Python program to check whether a given value is present in a tuple. If present, display its position.
a = (10, 20, 30, 40)

x = int(input("Enter value: "))

if x in a:
    print("Position:", a.index(x))
else:
    print("Not found")
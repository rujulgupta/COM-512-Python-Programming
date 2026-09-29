# Write a Python program to store repeated values in a tuple and count how many times a given value appears.
numbers = (10, 20, 10, 30, 10, 40)

search = int(input("Enter number to count:"))
count = 0
for num in numbers:
    if num == search:
        count += 1

print("Occurence: ",count)
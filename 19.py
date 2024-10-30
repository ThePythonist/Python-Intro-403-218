students = ["abolfazl", "peyman", "shayan"]

age = int(input("Enter your age  : "))

if age >= 18:
    name = input("Enter your name : ")
    students.append(name)
else:
    print("You are underage")

print(students)

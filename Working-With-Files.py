# f = open("cars.txt")
# print(f.read()) # string
# print(f.readline())  # string
# print(f.readline())
# print(f.readline())
# print(f.readlines())  # list

# print(f.read())
# print(f.tell())
# f.seek(5)
# print(f.read())

# print(f.read())
# print(f.read())
# print(f.tell())

f = open("names.txt", "w")
# f.write("\nferrari")

names = ["pizza", "kentucky", "french fries", "steak"]
# f.writelines(names)
for i in names:
    f.write(i + "\n")

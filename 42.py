numbers = []
for i in range(3):
    entry = input("Entry : ")

    try:
        entry = int(entry)
        # print("Entry is a number")
        numbers.append(entry)
    except ValueError:
        print("Entry is not a number")

print(numbers)
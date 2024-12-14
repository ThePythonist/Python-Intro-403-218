data = open("words.txt").read().split("\n")
numbers = []

for i in data:
    if i.isdigit() == True:
        numbers.append(i)

print(numbers)

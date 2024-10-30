number = int(input("Enter any number : "))
selection = [124, 136, 948, 512]

if number % 2 == 0 and 99 < number < 1000:
    selection.append(number)
elif number % 2 == 0 and -99 > number > -1000:
    selection.append(number)

selection.sort()
print(selection)

data = open("words.txt").readlines()

five_letters = []

for i in data:
    if len(i) == 5:
        five_letters += [i]

print(five_letters)

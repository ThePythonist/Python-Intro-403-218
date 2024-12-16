data = open("words.txt").readlines()

five_letters = []

for i in data:
    if len(i) == 6:
        five_letters += [i]

new = open("fivelleters.txt", "w")
new.writelines(five_letters)

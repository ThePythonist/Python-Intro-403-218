data = open("words.txt").readlines()

# az in estefade nemikonim !
# for i in data:
#     f = open("reversedwords.txt", "a")
#     f.write(i[::-1])


# solution 1
# new_data = []
# for i in data:
#     new_data.append(i[::-1])
#
# open("reversedwords.txt", "w").writelines(new_data)


# solution 2
new_data = []
for i in data:
    new_data.append(i[::-1])

output = "".join(new_data)

open("reversedwords.txt", "w").write(output)

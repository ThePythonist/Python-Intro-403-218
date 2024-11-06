items = ["Yazd", 10, 12, "Tehran", 15, True, 10.5, "Tabriz"]
strings = []

for i in items:
    if type(i) == str:
        strings.append(i)

print(strings)
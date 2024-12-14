def f1(file):
    data = file.readlines()
    new_data = []
    for i in data:
        new_data.append(i[:-1])

    print(new_data)


def f2(file):
    data = file.read().split("\n")
    print(data)


file = open("words.txt")
f2(file)

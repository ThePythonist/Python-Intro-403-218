def longest1(file):
    data = file.readlines()
    longest = max(data, key=len)
    print(longest)
    print(len(longest))


def longest2(file):
    data = file.readlines()
    longest = sorted(data, key=len)[-1]
    print(longest)
    print(len(longest))


def longest3(file):
    data = file.readlines()
    longest = max(data, key=len)
    max_len = len(longest)
    for i in data:
        if len(i) == max_len:
            print(i)


f = open("words.txt")
# longest1(f)
# print("-" * 100)
# f.seek(0)
# longest2(f)
longest3(f)

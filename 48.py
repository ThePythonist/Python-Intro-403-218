# def func(word):
#     characters = {}
#
#     for i in range(len(word)):
#         characters.setdefault(i, word[i])
#
#     print(characters)
#
#
# func("python")


def func(word):
    indexes = range(len(word))

    characters = dict(zip(indexes, word))
    print(characters)


func("python")

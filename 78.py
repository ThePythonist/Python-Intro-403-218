# data = open("words.txt").readlines()
#
# inglist = []
#
# for i in data:
#     if i[-4:-1] == "ing":
#         inglist.append(i)
#
# print(inglist)

data = open("words.txt").readlines()


def has_sub(item):
    # return True if item[-4:] == "ing\n" else False
    return True if item[-4:-1] == "ing" else False


sublist = list(filter(has_sub, data))
print(sublist)

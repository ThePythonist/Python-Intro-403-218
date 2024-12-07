# data = open("words.txt").readlines()
#
# sublist = []
#
# for i in data:
#     if i[:3] == "sub":
#         sublist.append(i)
#
# print(sublist)

data = open("words.txt").readlines()


def has_sub(item):
    return True if item[:3] == "sub" else False


sublist = list(filter(has_sub, data))
print(sublist)

def has_duplicate1(word):
    chars = []
    for i in word:
        if i not in chars:
            chars.append(i)
        else:
            return True
    else:
        return False


def has_duplicate2(word):
    if len(set(word)) == len(word):
        return False
    else:
        return True


# print(has_duplicate1("ilia"))
print(has_duplicate2("arman"))

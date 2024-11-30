def is_binary(number):
    for i in number:
        if i not in ["0", "1"]:
            return False
    else:
        return True


print(list(filter(is_binary, ["24", "101", "1011", "256", "100"])))

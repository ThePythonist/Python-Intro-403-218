def find_longest1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    maxl_len = max(lengths)

    for i in text:
        if len(i) == maxl_len:
            print(i)


# ============================================================================

def find_longest2(text):
    text = text.split()
    text.sort(key=len)
    print(text)


# ============================================================================

def find_longest3(text):
    text = text.split()
    print(max(text, key=len))


# ============================================================================

find_longest3("python is a good programming language")

word = input("Enter any word : ")
words = ("nan", "wow", "mom")

if word == word[::-1]:
    # words = words + (word,)
    words += (word,)


print(words)

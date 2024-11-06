# entry = input("Type something : ")
#
# while entry != "exit":
#     print(entry)
#     entry = input("Type something : ")
# else:
#     print("Entry has turned into exit")

# ===================================================

# flag = True
#
# while flag == True:
#     entry = input("Type something : ")
#     print(entry)
#     if entry == "exit":
#         # break # be in ravesh else ejra nemishe
#         flag = False  # be in ravesh else ejra mishe
# else:
#     print("The flag has turned into false")

# ===================================================

flag = 1

while flag:
    entry = input("Type something : ")
    print(entry)
    if entry == "exit":
        flag = 0  # be in ravesh else ejra mishe
else:
    print("The flag has turned into false")

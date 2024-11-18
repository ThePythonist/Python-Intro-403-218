# def greetings(name):
#     print("Hello", name)
#
#
# greetings(input("Enter your name : "))

def greetings(name):
    return "Hello " + name


# print(greetings(input("Enter your name : ")))

names = ["ahmad", "mina", "milad", "keyhan"]
for i in names:
    print(greetings(i))

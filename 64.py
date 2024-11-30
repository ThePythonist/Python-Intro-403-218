a = int(input("Enter a : "))
b = int(input("Enter b : "))
print((lambda x, y: "equal" if x == y else x if x > y else y)(a, b))

# if x == y:
#     print("equal")
# else:
#     if x > y :
#         print(x)
#     else:
#         print(y)

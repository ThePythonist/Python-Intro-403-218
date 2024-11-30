def is_binary(number):
    for i in number:
        if i not in ["0", "1"]:
            return False
    else:
        return True


# binary : 0,1
# decimal : 0,1,2,3....9
# hexadecimal : 0,1,2,3,...9,a,b,c,d,e,f

items = ["1011", "256", "1010", "64", "1000", "16", "1111"]

for i in items:
    print(is_binary(i))

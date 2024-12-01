pn = input("Enter phone number : ")

if len(pn) == 11:
    if pn[:2] == "09":
        pn = pn.replace("0", "+98", 1)
        print(pn)
    else:
        print("Invalid phone number")
else:
    print("Invalid phone number")

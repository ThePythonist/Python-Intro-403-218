from customlogs import make_log

numbers = []

while True:
    entry = input("Entry : ")
    if entry == "exit":
        break
    try:
        entry = float(entry)
        if str(entry)[-2:] == ".0":
            numbers.append(int(entry))
        else:
            numbers.append(entry)
    except ValueError:
        # print("Entry is not a number")
        make_log("info", f"Entry was a not a number. Entry : {entry}")
        pass

print(numbers)

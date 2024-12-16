number = int(input("How many files ? "))
suffix = input("Which type of file ? ")

for i in range(number):
    open(f"{i + 1}.{suffix}", "w")

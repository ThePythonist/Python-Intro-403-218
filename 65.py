x = int(input("Enter any number : "))
print((lambda number: True if number == sum([i for i in range(1, number) if number % i == 0]) else False)(x))

number = int(input("Enter any number : "))
divisors = []  # shomarande ha

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# print("Divisors :", divisors)

# if len(divisors) == 2:
if divisors == [1, number]: # tartib inja mohem ast
    print("Aval ast")
else:
    print("Aval nist")

number = int(input("Enter any number : "))
divisors = []  # shomarande ha

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print("Divisors :", divisors)

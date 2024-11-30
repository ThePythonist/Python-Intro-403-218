# def is_prime(number):
#     divisors = [i for i in range(1, number + 1) if number % i == 0]
#     print("Aval ast") if len(divisors) == 2 else print("Aval nist")
#
#
# x = int(input("Enter any number : "))
# is_prime(x)

def is_prime(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return "Aval ast" if len(divisors) == 2 else "Aval nist"


x = int(input("Enter any number : "))
print(is_prime(x))

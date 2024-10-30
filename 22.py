print("AX^2 + B^X + C")

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("No roots available")
elif delta == 0:
    x = (-b) / (2 * a)
    print("X :", x)
else:
    x1 = ((-b) + (delta ** 0.5)) / (2 * a)
    x2 = ((-b) - (delta ** 0.5)) / (2 * a)
    print("X1 :", x1)
    print("X2 :", x2)

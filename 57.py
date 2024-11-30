def is_number(entry):
    if type(entry) in [int, float]:
        even_or_odd(entry)
    else:
        print("Entry is not a number")


def even_or_odd(number):
    if number % 2 == 0:
        print("Entry is even")
    else:
        print("Entry is odd")


is_number("tehran")

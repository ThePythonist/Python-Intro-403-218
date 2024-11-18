def adder1(number):
    digits = []
    for i in str(number):
        digits.append(int(i))

    print(sum(digits))


def adder2(number):
    summation = 0
    for i in str(number):
        summation += int(i)

    print(summation)


# adder1(67567)
adder2(459219)

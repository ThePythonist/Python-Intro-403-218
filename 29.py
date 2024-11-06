# numbers = [24, 11, 15, 16, 18, 19, 21]
# evens = []
#
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#
# print(evens)


numbers = [24, 11, 15, 16, 18, 19, 21]
evens = [i for i in numbers if i % 2 == 0]
print(evens)

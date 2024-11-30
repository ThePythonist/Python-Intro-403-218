def func(x):
    return [i for i in range(1, x + 1) if x % i == 0]


m = list(map(func, [10, 15, 21, 7]))
print(m)

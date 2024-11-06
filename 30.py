items = [
    10, True,
    2.5, 2.8,
    15, 20,
    "Tokyo", "Paris",
    "New York", 12
]

for i in items:
    # if type(i) is int or type(i) is float:
    if type(i) in [int, float]:
        print(i)

items = [10, 15, ["Tokyo", "Moscow"], 1.5, True, "Paris", 6]
print(list(filter(lambda x: type(x) in [int, float], items)))

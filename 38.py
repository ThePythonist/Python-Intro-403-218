items = [
    "coffee", "packet",
    "coffee", "coffee",
    "spoon", "packet",
    "milk", "milk"
]

unique_items = []

for i in items:
    if i not in unique_items:
        unique_items.append(i)

print(unique_items)

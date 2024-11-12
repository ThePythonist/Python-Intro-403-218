scores = {
    "riazi": 18,
    "zaban": 20,
    "farsi": 14,
    "arabi": 7,
    "shimi": 17,
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": passed")
    else:
        print(k, ": failed")

average = sum(scores.values()) / len(scores)
print("Moadel :", average)

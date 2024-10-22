# 1 - Tuple

# t = ("Pedram", 2, 3, "Ali", 5, 10.5, 20.37)
# print(t)
# print(type(t))

# t = (10, 20, 30, 40)

# print(t[0])
# print(t[-1])

# t[0] = 50
# print(t)

# names = ("taha", "arian", "taha", "sara", "sara")
# print(names)

# t1 = (10, 20, 30)
# t2 = (40, 50, 60)
# print(t2+t1)
# print(t1 + 4)
# print(t1*3)

# names = ("iran", "germany", "turkey", "france", "italy", "italy", "france", "italy")
# print(names.count("france"))
# print(names.index("germany"))

# =========================================================================================

# 2 - Set

# s = {1, 2, 3}

# print(s)
# print(type(s))

# print(s[0])

# s[-1] = 4
# print(s)

# items = {"tehran", "paris", "tokyo", "istanbul"}
# print(items)

# items = {10, 20, 30, 10, 40, 10, 50}
# print(items)

# s1 = {100, 200, 300}
# s2 = {-50, -60, -30}
# print(s1 + s2)

# names = {
#     "michael jackson",
#     "lady gaga",
#     "george michael",
#     "billie eilish",
# }

# names.add("adele")
# print(names)

# names.remove("lady gaga")
# print(names)

# del names[-1]
# print(names)

# s1 = {10, 20, 30}
# s2 = {0.5, 2.25, 4.73}
# print(s1.union(s2))

# =========================================================================================

# 3 - List

# items = [10, 20, 10, 30, 10, 40]
# print(items)
# print(type(items))

# print(items[-1])
# items[-1] = 50
# print(items)

# print(items + [60, 70, 90])

# names = ["james", "kirk", "zayn", "lars", "jason"]
# names.append("robert")
# print(names)

# names.insert(2, "robert")
# print(names)

# names.remove("jason")
# print(names)

# names.sort()
# print(names)

# numbers = [40, 30, 10.25, 10.06, 20]
# numbers.sort()
# print(numbers)

# =========================================================================================

# 4 - Dictionary

# d = {"name": "michael", "job": "singer", "city": "la", "age": 40}
# print(d)
# print(type(d))

# info = {"club": "bayern munich", "manager": "kompany", "stadium": "alianz arena"}
# print(info)
# print(info["club"])


# info = {"club": "bayern munich", "manager": "kompany", "stadium": "alianz arena", "manager": "flick"}
# print(info)

d1 = {"city": "tehran", "country": "iran", "population": 9616000}
d2 = {"district": "north", "area code": "021"}

# print(d1+d2)

# d1.setdefault("mayor", "zakani")
# print(d1)

# d1.pop("country")
# print(d1)

# d1.popitem()
# print(d1)

# d1.update(d2)
# print(d1)

# d1.update({"city": "yazd"})
# print(d1)

# d1.setdefault("city", "yazd")
# print(d1)

# print(d1.keys())
# print(list(d1.keys()))
# print(list(d1.keys())[0])


# print(d1.values())
# print(list(d1.values()))
# print(list(d1.values())[0])


# print(d1.items())
# print(list(d1.items()))
# print(list(d1.items())[0])

# =========================================================================================

# lst = [
#     (["tehran", "tabriz"], {"name": "saeed", "age": 23}),
#     (("new york", "texas"), ["madagascar", "dubai", 45, 10.5]),
#     (("pen", "paper"), ("mouse", "keyboard")),
#     12,
# ]

# =========================================================================================


info = {
    "name": "bayern munich",
    "league": "bundesliga",
    "rival": "dortmund",
    "stadium": "alianz arena"
}

key = input("Search for any key : ")

# if key in info:
#     print("Found :", info[key])
# else:
#     print("Key not found")

try:
    print("Found :", info[key])
except KeyError:
    print("Key not found")

# pythons = ["alireza", "hanieh", "kian", "shayan"]
# icdls = ["mitra", "kian", "aria", "hanieh", "alireza", "parsa"]
# common = []
#
# for i in icdls:
#     if i in pythons:
#         print(i)

# =====================================================================

pythons = ["alireza", "hanieh", "kian", "shayan"]
icdls = ["mitra", "kian", "aria", "hanieh", "alireza", "parsa"]
common = []

for i in pythons:
    for j in icdls:
        if i == j:  # n * m bar ejra mishe
            print(i)

people = {
    "mina": 20,
    "shayan": 27,
    "meysam": 30,
    "hananeh": 24,
    "taha": 30,
}

maxage = max(people.values())

for i in people:
    if people[i] == maxage:
        print(i)
        # break # agar khastim faghat 1 nafar entekhab shavad

def send_message(person):
    msg = f"""
Moshtarake gerami {person}
basteye {people[person]} shoma roo be etmam ast
lotfan nesbat be kharid ya tamdid basteye khod
eghdam namayid.
"""
    print(msg)


people = {
    "09399445646": "10 rooze 10 gig",
    "09306643738": "1 rooze 2 gig",
    "09367140284": "60 rooze 15 gig"
}

for i in people:
    send_message(i)

mamad_scores = {
    "riazi": (18, 3),
    "zaban": (17, 2),
    "farsi": (15, 1),
    "arabi": (12, 1),
    "shimi": (20, 2),
}

armin_scores = {
    "riazi": (15, 3),
    "zaban": (20, 2),
    "farsi": (14, 1),
    "arabi": (7, 1),
    "shimi": (17, 2),
}


def pass_or_fail(scores):
    for k, v in scores.items():
        if v[0] >= 10:
            print(k, ": passed")
        else:
            print(k, ": failed")


def show_grade(scores):
    nomarat = []
    zarayeb = []

    for i in scores.values():
        zarayeb.append(i[1])
        nomarat.append(i[0] * i[1])

    grade = sum(nomarat) / sum(zarayeb)
    print(grade)


show_grade(armin_scores)

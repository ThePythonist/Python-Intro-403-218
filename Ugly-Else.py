scores = [19, 16, 8, 17, 20]

for i in scores:
    if i >= 10:
        pass
    else:
        print("You cannot graduate!")
        break
else:  # Agar for break nashavad, else ejra mishavad
    print("Congratulations you graduated!")

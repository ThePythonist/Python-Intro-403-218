data = open("words.txt").read().split("\n")
newdata = open("onelinewords.txt", "w")
newdata.writelines(data)

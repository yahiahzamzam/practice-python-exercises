with open("txt.txt", "r", encoding="utf-8") as f:
    names = {}
    for line in f:
        name = line.strip()
        if name in names:

            names[name] += 1
        else:
            names[name] = 1
print(names)

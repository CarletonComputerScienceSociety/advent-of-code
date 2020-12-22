data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [0, 0]

allergens = {}
words = {}
for i, value in enumerate(data):
    line = value.split("(contains ")

    be = []
    for word in line[1][:-1].split(", "):
        if word not in allergens:
            allergens[word] = 0
        allergens[word] += 1
        be.append(word)

    for word in line[0].split(" "):
        if word == "":
            continue
        if word not in words:
            words[word] = [[], 0]

        words[word][0] += be
        words[word][1] += 1


inert = []
for k, v in words.items():
    can_be = True
    for allergen in list(set(v[0])):
        if v[0].count(allergen) == allergens[allergen]:
            can_be = False

    if can_be:
        count += v[1]
        inert.append(k)

print(count)

allergens = {}
words = {}
for i, value in enumerate(data):

    line = value.split("(contains ")

    begin = line[0]
    begin = " " + begin
    for bad in inert:
        begin = begin.replace(f" {bad}", "")
    be = []
    for word in line[1][:-1].split(", "):
        if word not in allergens:
            allergens[word] = 0
        allergens[word] += 1
        be.append(word)

    for word in line[0].split(" "):
        if word == "" or word in inert:
            continue
        if word not in words:
            words[word] = [[], 0]

        words[word][0] += be
        words[word][1] += 1

for k, v in words.items():
    can_be = False
    for allergen in list(set(v[0])):
        if v[0].count(allergen) == allergens[allergen]:
            can_be = True
            print(k, allergen)

    if can_be:
        count += v[1]

# I did the rest by hand at this point

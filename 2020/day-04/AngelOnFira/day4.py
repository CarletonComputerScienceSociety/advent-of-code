data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]

# map_in = {}
# for i, line in enumerate(data):
#     for j, character in enumerate(line):
#         map_in[(j, i)] = character

passports = []
curr = {}

for i, line in enumerate(data):

    if line == "":
        passports.append(curr)
        curr = {}
        continue

    broken = line.split()
    for item in broken:
        curr[item.split(":")[0]] = item.split(":")[1]

passports.append(curr)

valid = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# for passport in passports:
#     print(passport)

for passport in passports:
    good = True
    for item in valid:
        if item not in passport:
            good = False

    for k, v in passport.items():
        if k == "byr":
            if (int(v) < 1920 or int(v) > 2002) or len(v) != 4:
                good = False
        if k == "iyr":
            if (int(v) < 2010 or int(v) > 2020) or len(v) != 4:
                good = False
        if k == "eyr":
            if (int(v) < 2020 or int(v) > 2030) or len(v) != 4:
                good = False
        if k == "hgt":
            if v[-2:] == "cm":
                if int(v[:-2]) < 150 or int(v[:-2]) > 193:
                    good = False
            elif v[-2:] == "in":
                if int(v[:-2]) < 59 or int(v[:-2]) > 76:
                    good = False
            else:
                good = False
        if k == "hcl":
            if v[0] == "#" and len(v) == 7:
                for character in v[1:]:
                    # print (character)
                    if not character in "1234567890abcdef":
                        # print("sdf")
                        good = False
            else:
                good = False
        if k == "ecl":
            if not v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                good = False
        if k == "pid":
            # print(len(v))
            if len(v) == 9:
                for char in v:
                    if not char in "0123456789":
                        good = False
            else:
                good = False

    if good:
        counter += 1
print(counter)

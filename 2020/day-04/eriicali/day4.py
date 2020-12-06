currentPassport = []
allPassports = []
firstScreening = []

hclValidChars = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"}
eclValid = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

numValidPassports = 0

file = open("day_4_input.txt", "r")

for line in file.readlines():
    if line == "\n":
        allPassports.append(currentPassport)
        currentPassport = []
    else:
        passportData = line.strip().split(" ")
        currentPassport += passportData

allPassports.append(currentPassport)

for passport in allPassports:
    requiredFields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False}
    passportDict = {}
    if len(passport) == 7:
        for field in passport:
            requiredFields[field[0:3]] = True
            passportDict[field[0:3]] = field[4:]
        if not requiredFields["cid"]:
            firstScreening.append(passportDict)
    elif len(passport) == 8:
        for field in passport:
            requiredFields[field[0:3]] = True
            passportDict[field[0:3]] = field[4:]
        firstScreening.append(passportDict)

for passportDict in firstScreening:
    if not 1920 <= int(passportDict["byr"]) <= 2002:
        continue
    if not 2010 <= int(passportDict["iyr"]) <= 2020:
        continue
    if not 2020 <= int(passportDict["eyr"]) <= 2030:
        continue
    if passportDict["hgt"][-2:] == "cm":
        if not 150 <= int(passportDict["hgt"][:-2]) <= 193:
            continue
    elif passportDict["hgt"][-2:] == "in":
        if not 59 <= int(passportDict["hgt"][:-2]) <= 76:
            continue
    else:
        continue
    if not passportDict["hcl"][0] == "#" or not len(passportDict["hcl"]) == 7:
        continue
    else:
        for char in passportDict["hcl"][1:]:
            if char not in hclValidChars:
                continue
    if passportDict["ecl"] not in eclValid:
        continue
    if not len(passportDict["pid"]) == 9:
        continue
    numValidPassports += 1

print(numValidPassports)

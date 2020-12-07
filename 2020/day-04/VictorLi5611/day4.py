passports = []
current = ""
with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if line == "":
            passports.append(current.strip())
            current = ""
        else:
            current += " " + line
passports.append(current.strip())


def valid_passport(p, part2=False):
    req = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    for y in req:
        if y in p.keys() and p[y]:
            continue
        else:
            return False
    if not part2:
        return True
    if not (1920 <= int(p["byr"]) <= 2002):
        return False
    if not (2010 <= int(p["iyr"]) <= 2020):
        return False
    if not (2020 <= int(p["eyr"]) <= 2030):
        return False
    hgt = p["hgt"]
    if hgt[-2:] not in ("cm", "in"):
        return False
    if hgt[-2:] == "cm":
        if not (150 <= int(hgt[:-2]) <= 193):
            return False
    if hgt[-2:] == "in":
        if not (59 <= int(hgt[:-2]) <= 76):
            return False
    hcl = p["hcl"]
    if not hcl[0] == "#" or not hcl[1:].isalnum():
        return False
    if p["ecl"] not in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return False
    if not len(p["pid"]) == 9 or not p["pid"].isnumeric():
        return False

    return True


part1 = 0
part2 = 0
for p in passports:
    keys = (x.split(":")[0] for x in p.split())
    items = (x.split(":")[1] for x in p.split())
    p = dict(zip(keys, items))
    if valid_passport(p, part2=False):
        part1 += 1
    if valid_passport(p, part2=True):
        part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)

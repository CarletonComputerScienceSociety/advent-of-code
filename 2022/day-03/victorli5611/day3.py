data = []
with open("day3.txt") as f:
    data = [x.strip() for x in f.readlines()]

rucksacks = []
shared = []

for rucksack_raw in data:
    first, second = (
        rucksack_raw[0 : len(rucksack_raw) // 2],
        rucksack_raw[len(rucksack_raw) // 2 :],
    )
    rucksacks.append((first, second))
    first_set = set(first)
    second_set = set(second)
    shared.append(next(x for x in (first_set & second_set)))

pass
part1 = 0
for s in shared:
    part1 += " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s)

print(part1)
#####################################
data = []
with open("day3.txt") as f:
    data = [x.strip() for x in f.readlines()]

rucksacks = []

shared = []

for n in range(0, len(data), 3):
    first_set = set(data[n])
    second_set = set(data[n + 1])
    third_set = set(data[n + 2])
    shared.append(next(x for x in (first_set & second_set & third_set)))

pass
part2 = 0
for s in shared:
    part2 += " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(s)

print(part2)

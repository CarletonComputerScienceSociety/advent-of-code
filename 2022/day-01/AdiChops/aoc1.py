data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]

num_total = 3
current_elf = 0
elves = []
for i, line in enumerate(data):
    if line == "":
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)

max_total = 0
mindex = 0
top_elves = 0

# alternatively could sort and take first 3, but 3O(n) is probably faster than O(nlogn)
for i in range(num_total):
    for j, elf in enumerate(elves):
        if elf > max_total:
            max_total = elf
            mindex = j
    top_elves += max_total
    max_total = 0
    del elves[mindex]

print(top_elves)
import re
import itertools

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [0, 0]

memory = {}
mask = ""

for i, value in enumerate(data):
    if value.startswith("mask ="):
        mask_str = value.split(" = ")
        mask = mask_str[1]

    else:
        groups = re.search(r'mem\[(\d+)\] = (\d+)', value)
        location = int(groups.group(1))
        value = int(groups.group(2))

        this_loc = ""

        binary = '{0:036b}'.format(location)
        perms = []

        for i in range(36):
            if mask[i] == "X":
                this_loc += "0"
                perms.append(pow(2, 36 - i-1))
            elif mask[i] == "1":
                this_loc += "1"
            else:
                this_loc += binary[i]

        new_loc = int(this_loc, 2)

        for i in range(len(perms) + 1):
            for comb in itertools.combinations(perms, i):
                memory[new_loc + sum(comb)] = value

for v in memory.values():
    count += int(v)

print(count)

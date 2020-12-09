import re
import datetime
import string

alphabet_lower = string.ascii_lowercase

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [0, 0]

# map_in = {}
# for i, line in enumerate(data):
#     for j, character in enumerate(line):
#         map_in[(j, i)] = character

preamble = []
for i in range(25):
    preamble.append(int(data[i]))

num = 15353384

for index in range(len(data)):
    counter = index
    total = 0
    found = []
    while total < num:
        total += int(data[counter])
        found.append(int(data[counter]))

        if total == num:
            print(min(found) + max(found))

        counter += 1

    # i = int(data[index])
    # found = False
    # for j in preamble:
    #     for k in preamble:
    #         if j + k == i:
    #             found = True
    #             break

    #     if found:
    #         break

    # if found == False:
    #     print(i)

    # preamble.append(i)
    # preamble.pop(0)

    # groups = re.search(r'', line)
    # first = groups.group(1)
    # second = groups.group(2)
    # third = groups.group(3)

print(count)

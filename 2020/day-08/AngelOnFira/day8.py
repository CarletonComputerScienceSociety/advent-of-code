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

index = 0
accu = 0
last = 0


rules = {}
ids = []
first = ""

seen = {}

for i in range(len(data)):
    if data[i][0] == 'j':
        data[i] = data[i].replace("jmp", "nop")

        counter = 0
        accu = 0
        last = 0
        found = True
        index = 0
        # print(data)
        while index < len(data):
            if counter > 100000:
                found = False
                break
            counter += 1

            # print(accu)
            # print(data[index])
            seen[index] = 1
            instruction = data[index].split(" ")

            if instruction[0] == "nop":
                pass
            if instruction[0] == "acc":
                last = accu
                accu += int(instruction[1])
            if instruction[0] == "jmp":
                index += int(instruction[1]) - 1

            index += 1

        if found:
            break

        data[i] = data[i].replace("nop", "jmp")

print(last)
print(accu)

# groups = re.search(r'', line)
# first = groups.group(1)
# second = groups.group(2)
# third = groups.group(3)

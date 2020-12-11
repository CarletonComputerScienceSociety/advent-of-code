import re
import datetime
import string

alphabet_lower = string.ascii_lowercase

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [0, 0]

map_old = []
for i, lines in enumerate(data):
    line = []
    for j, character in enumerate(lines):
        line.append(character)
    map_old.append(line)


# print(map_old)

adj = [
    [-1, 0],
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
]

while 1:
    map_new = []
    for y in range(len(data)):
        line_new = []
        for x in range(len(data[0])):
            pound = 0
            l = 0
            curr = map_old[y][x]
            for ray in adj:
                pos = [y, x]
                while True:
                    pos[0] += ray[0]
                    pos[1] += ray[1]

                    if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(data) or pos[1] >= len(data[0]):
                        break
                    if map_old[pos[0]][pos[1]] == "#":
                        pound += 1
                        break
                    elif map_old[pos[0]][pos[1]] == "L":
                        l += 1
                        break

            if curr == "L":
                if pound == 0:
                    line_new.append("#")
                else:
                    line_new.append("L")

            elif curr == "#":
                if pound >= 5:
                    line_new.append("L")
                else:
                    line_new.append("#")

            else:
                line_new.append(".")

        map_new.append(line_new)

    count2 = 0
    for line in map_new:
        for char in line:
            count2 += 1 if char == "#" else 0

    print(count2)

    map_old = map_new

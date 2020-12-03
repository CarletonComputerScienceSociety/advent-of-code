data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]

map_in = {}

for i, line in enumerate(data):
    for j, character in enumerate(line):
        map_in[(j, i)] = character

counter2 = [0, 0, 0, 0, 0]

for i in range(int((len(data)))):
    # print(i)
    # if map_in[(i * 3 % len(data[0]), i)] == "#":
    if map_in[(i % len(data[0]), i)] == "#":
        counter2[0] += 1

    if map_in[((i * 3) % len(data[0]), i)] == "#":
        counter2[1] += 1

    if map_in[((i * 5) % len(data[0]), i)] == "#":
        counter2[2] += 1

    if map_in[((i * 7) % len(data[0]), i)] == "#":
        counter2[3] += 1

    if i < len(data) / 2:
        if map_in[(i % len(data[0]), i * 2)] == "#":
            counter2[4] += 1

print(counter2)
print(counter2[0] * counter2[1]*counter2[2]*counter2[3]*counter2[4])

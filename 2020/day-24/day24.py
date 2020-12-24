data = [line.strip() for line in open("input.txt", 'r')]

count = 0

grid = {}
out = {}

for line in data:
    i = 0
    pos = [0, 0]

    while True:
        this_char = line[i]
        lookahead = ""
        if i < len(line) - 1:
            lookahead = line[i + 1]

        if this_char + lookahead in ["se", "sw", "nw", "ne"]:
            string = this_char + lookahead
            i += 1
            if string == "se":
                pos[0] += 1
                pos[1] += 1
            if string == "sw":
                pos[0] += 1
                pos[1] += -1
            if string == "ne":
                pos[0] += -1
                pos[1] += 1
            if string == "nw":
                pos[0] += -1
                pos[1] += -1

        else:
            if this_char == "e":
                pos[0] += 0
                pos[1] += 2
            if this_char == "w":
                pos[0] += 0
                pos[1] += -2

        i = i + 1
        if i >= len(line):
            break
    if tuple(pos) not in out:
        out[tuple(pos)] = 0
    out[tuple(pos)] += 1

for k, v in out.items():
    if v % 2 == 1:
        count += 1

print(count)

adj = [
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1],
    [0, -2],
    [0, 2],
    [0, 0],
]

old = out
for i in range(100):
    new_map = {}
    for k, v in old.items():
        for neigh in adj:
            tile = False
            nx = k[0] + neigh[0]
            ny = k[1] + neigh[1]

            if (nx, ny) in old:
                tile = old[(nx, ny)] % 2 == 1

            black = 0
            for adjacent in adj[:-1]:
                posx = k[0] + neigh[0] + adjacent[0]
                posy = k[1] + neigh[1] + adjacent[1]
                if (posx, posy) in old and old[(posx, posy)] % 2 == 1:
                    black += 1
            if tile:
                if black == 0 or black > 2:
                    pass
                else:
                    new_map[(nx, ny)] = 1

            else:
                if black == 2:
                    new_map[(nx, ny)] = 1

    old = new_map
print(i + 1, len(old))

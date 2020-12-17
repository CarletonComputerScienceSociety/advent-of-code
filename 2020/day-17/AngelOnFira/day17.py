data = [line.strip() for line in open("input.txt", 'r')]

count = 0

grid_in = {}
for y, line in enumerate(data):
    for x, character in enumerate(line):
        grid_in[(x, y, 0, 0)] = character

last_grid = grid_in

curr_grid = {}
for i in range(6):
    curr_grid = {}

    min_x = min([pos[0] for pos in last_grid.keys()]) - 1
    max_x = max([pos[0] for pos in last_grid.keys()]) + 2
    min_y = min([pos[1] for pos in last_grid.keys()]) - 1
    max_y = max([pos[1] for pos in last_grid.keys()]) + 2
    min_z = min([pos[2] for pos in last_grid.keys()]) - 1
    max_z = max([pos[2] for pos in last_grid.keys()]) + 2
    min_w = min([pos[3] for pos in last_grid.keys()]) - 1
    max_w = max([pos[3] for pos in last_grid.keys()]) + 2

    for w in range(min_w, max_w):
        for z in range(min_z, max_z):
            for y in range(min_y, max_y):
                for x in range(min_x, max_x):

                    if (x, y, z, w) in last_grid:
                        self_cell = last_grid[(x, y, z, w)]
                    else:
                        self_cell = "."

                    active = 0
                    for xk in range(-1, 2):
                        for yk in range(-1, 2):
                            for zk in range(-1, 2):
                                for wk in range(-1, 2):
                                    if xk == yk == zk == wk == 0:
                                        continue
                                    if (x + xk, y + yk, z + zk, w + wk) in last_grid:
                                        cell = last_grid[(
                                            x + xk, y + yk, z + zk, w + wk)]
                                        if cell == "#":
                                            active += 1

                    if self_cell == ".":
                        if active == 3:
                            curr_grid[(x, y, z, w)] = "#"
                        else:
                            curr_grid[(x, y, z, w)] = "."
                    if self_cell == "#":
                        if 2 <= active <= 3:
                            curr_grid[(x, y, z, w)] = "#"
                        else:
                            curr_grid[(x, y, z, w)] = "."

    last_grid = curr_grid

for value in curr_grid.values():
    if value == "#":
        count += 1

count

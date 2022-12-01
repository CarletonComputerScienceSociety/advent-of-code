from aoc import AOC, Position, griditer
from math import prod

aoc = AOC(year=2021, day=9)
height_map = aoc.load().digits_by_line()
d = height_map

Position.set_limits(range(len(height_map[0])), range(len(height_map)))

# Part 1

aoc.p1(
    sum(
        height_map[y][x] + 1
        for x, y in griditer(height_map)
        if all(
            height_map[y][x] < height_map[a.y][a.x] for a in Position(x, y).adjacent()
        )
    )
)

visited = set()
basins = []

for x, y in griditer(height_map):
    p = Position(x, y)
    if p in visited or height_map[p.y][p.x] == 9:
        continue

    q = [p]
    basin = set([p])
    while q:
        p = q.pop()
        visited.add(p)

        for adj in p.adjacent(diagonal=False):
            if adj in visited or height_map[adj.y][adj.x] == 9:
                continue
            basin.add(adj)
            q.append(adj)
    basins.append(len(basin))

aoc.p2(prod(sorted(basins)[-3:]))


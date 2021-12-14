from aoc import AOC, Drop, Regex, Numbers, griditer, stringifygrid

aoc = AOC(year=2021, day=13)
data = aoc.load()

chunks = data.chunk(
    [
        Numbers(),
        Drop(1),
        Regex(r"fold along (x|y)=(\d+)"),
    ]
)

coords = set([(x, y) for [x, y] in chunks[0]])
folds = [(axis, line) for [axis, line] in chunks[1]]


def retrieve_grid():
    width = max([x for x, _ in coords]) + 1
    height = max([y for _, y in coords]) + 1

    grid = []
    for y in range(height):
        grid.append([])
        for x in range(width):
            grid[y].append("#" if (x, y) in coords else ".")

    return grid


def fold(grid, folds):
    for axis, line in folds:
        if axis == "y":
            for i, y in enumerate(range(line + 1, len(grid))):
                for x in range(len(grid[y])):
                    if grid[y][x] == "#":
                        grid[line - i - 1][x] = "#"
            grid = [row for index, row in enumerate(grid) if index < line]
        else:
            for i, x in enumerate(range(line + 1, len(grid[0]))):
                for y in range(len(grid)):
                    if grid[y][x] == "#":
                        grid[y][line - i - 1] = "#"
            grid = [
                [col for index, col in enumerate(row) if index < line] for row in grid
            ]

    return grid


# Part 1

grid = retrieve_grid()
grid = fold(grid, folds[:1])
aoc.p1(sum(1 for x, y in griditer(grid) if grid[y][x] == "#"))

# Part 2

grid = retrieve_grid()
grid = fold(grid, folds)
aoc.p2(stringifygrid(grid))


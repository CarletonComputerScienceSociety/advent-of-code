from aoc import AOC, Position, griditer

aoc = AOC(year=2021, day=11)
data = aoc.load()
Position.set_limits(x=range(10), y=range(10))

octos = data.digits_by_line()

def clear_flashed(octos):
    # Reset octos that have flashed to 0
    for x, y in griditer(octos):
        if octos[y][x] > 9:
            octos[y][x] = 0

def step(octos):
    # Start with incremeneting every octo
    needs_increment = [(x, y) for x, y in griditer(octos)]
    flashed = set()

    while needs_increment:
        x, y = needs_increment.pop()
        octos[y][x] += 1
        if octos[y][x] > 9 and (x, y) not in flashed:
            # When an octo's energy exceeds 9, it flashes and increments those surrounding
            flashed.add((x, y))
            for adj in Position(x, y).adjacent():
                if adj.tuple not in flashed:
                    # Octo's can only flash once in a step, so skip if they've already flashed
                    needs_increment.append(adj.tuple)

    clear_flashed(octos)
    return octos, len(flashed)


# Part 1

total = 0
for _ in range(100):
    octos, flash_count = step(octos)
    total += flash_count

aoc.p1(total)

# Part 2

octos = data.digits_by_line()

flash_count = 0
step_count = 0
while flash_count != 100:
    octos, flash_count = step(octos)
    step_count += 1

aoc.p2(step_count)


from aoc import AOC

aoc = AOC(year=2021, day=7)
data = aoc.load()

crabs = data.nums()

# Part 1

aoc.p1(min(sum(abs(c - i) for c in crabs) for i in range(max(crabs))))

# Part 2

aoc.p2(
    min(
        sum((abs(c - i) * (abs(c - i) + 1)) // 2 for c in crabs)
        for i in range(max(crabs))
    )
)


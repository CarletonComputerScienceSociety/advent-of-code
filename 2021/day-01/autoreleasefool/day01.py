from aoc import AOC, sliding_window


aoc = AOC(year=2021, day=1)
series = aoc.load().numbers()


# Part 1

increments = sum(1 for x in range(len(series) - 1) if series[x] < series[x + 1])
aoc.p1(increments)

# Part 2

series = sliding_window(series, 3)
increments = sum(
    1 for i in range(1, len(series)) if sum(series[i - 1]) < sum(series[i])
)
aoc.p2(increments)

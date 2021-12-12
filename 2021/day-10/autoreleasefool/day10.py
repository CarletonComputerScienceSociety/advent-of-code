from aoc import AOC

aoc = AOC(year=2021, day=10)
data = aoc.load()

# Part 1

open_close = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">",
}

close_open = {v: k for k, v in open_close.items()}

values = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

incomplete = []

total_score = 0
for line in data.lines():
    has_error = False
    stack = []
    for c in line:
        if c in close_open:
            last = stack.pop()
            if last != close_open[c]:
                has_error = True
                total_score += values[c]
        else:
            stack.append(c)

    if not has_error:
        incomplete.append(stack)

aoc.p1(total_score)

# Part 2

values = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

scores = []
for stack in incomplete:
    scores.append(0)
    while stack:
        c = stack.pop()
        matching = open_close[c]

        scores[-1] *= 5
        scores[-1] += values[matching]

aoc.p2(sorted(scores)[len(scores) // 2])


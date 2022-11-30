import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    return puzzle_input


def part1(puzzle_input):
    counter = 0
    for line in puzzle_input:
        counter += int(line) // 3 - 2 

    return counter

def part2(puzzle_input):
    output = []
    i = 0
    p = []
    for line in puzzle_input:
        p.append(int(line))
        output.append(0)
    while (p[i] > 0 and i <= len(puzzle_input)-1):
        p[i] = int(p[i]) // 3 - 2
        if (p[i] <= 0):
            p[i] = 0
        output[i] += p[i]
        i += 1
        if (i >= len(p)):
            i = 0
    return sum(output)
puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

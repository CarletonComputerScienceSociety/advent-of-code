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
    pass


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

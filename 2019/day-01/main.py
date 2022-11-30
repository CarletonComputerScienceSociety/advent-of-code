import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")

    return puzzle_input


def part1(puzzle_input):
    sum = 0
    for line in puzzle_input:
        sum += int(line) // 3 - 2
    return sum

def recur(fuel, fuelSum):
    if fuel <= 0:
        return fuelSum
    fuel = fuel // 3 - 2
    fuelSum += fuel
    recur(fuel, fuelSum)

def part2(puzzle_input):
    sum = 0
    for line in puzzle_input:
        fuelSum = recur(int(line), 0)
        sum += fuelSum
    return sum

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

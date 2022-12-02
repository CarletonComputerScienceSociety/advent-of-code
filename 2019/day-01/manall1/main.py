import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")

    return puzzle_input


def part1(puzzle_input):
    fuel = 0
    for line in puzzle_input:
        fuel += int(line)//3 - 2
    return fuel

def part2(puzzle_input):
    final_fuel = 0
    #fuel = 0
    for line in puzzle_input:
        total = 0
        fuel = int(line)
        while fuel >= 0:
            fuel = (fuel // 3) - 2
            if (fuel<=0):
                break
            total+=fuel
        final_fuel+=total

    return final_fuel


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

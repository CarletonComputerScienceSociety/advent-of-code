import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")

    return puzzle_input


def part1(puzzle_input):
    counter=0
    for line in puzzle_input:
        counter+= int(line)//3-2
    return counter


def part2(puzzle_input):
    total_fuel=0
    for line in puzzle_input:
        counter=0
        fuel=int(line)
        while (fuel>0):
            fuel=fuel//3-2
            if (fuel<=0):
                break
            counter+=fuel
        total_fuel+=counter
    return total_fuel


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))
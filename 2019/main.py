import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")

    return puzzle_input


def part1(puzzle_input):
    counter = 0
    for line in puzzle_input:
        counter += int(line) //3-2
    
    return counter


def part2(puzzle_input):
    total_counter = 0
    for line in puzzle_input:
        mini_total_counter = 0
        line_counter = int(line)
        while line_counter > 0:
            line_counter = (line_counter//3)-2
            if line_counter < 0:
                break
            mini_total_counter += line_counter
        total_counter += mini_total_counter

    return total_counter



puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

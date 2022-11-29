import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")
    puzzle_input = puzzle_input[0].split(", ")
    return puzzle_input


def part1(puzzle_input):
    # Set the initial start position
    position = (0, 0)
    direction = 0

    # Move based on the instructions
    for instruction in puzzle_input:
        # Turn based on the first letter of the instruction
        if instruction[0] == "R":
            direction += 1
        elif instruction[0] == "L":
            direction -= 1

        # Make sure direction is between 0 and 3
        direction %= 4

        # Move
        if direction == 0:
            position = (position[0], position[1] + int(instruction[1:]))
        elif direction == 1:
            position = (position[0] + int(instruction[1:]), position[1])
        elif direction == 2:
            position = (position[0], position[1] - int(instruction[1:]))
        elif direction == 3:
            position = (position[0] - int(instruction[1:]), position[1])

    # Return the final position in terms of blocks away
    return abs(position[0]) + abs(position[1])


def part2(puzzle_input):
    # Set the initial start position
    position = (0, 0)
    direction = 0

    # Keep track of all visited positions
    visited = set()

    # Move based on the instructions
    for instruction in puzzle_input:
        # Turn based on the first letter of the instruction
        if instruction[0] == "R":
            direction += 1
        elif instruction[0] == "L":
            direction -= 1

        # Make sure direction is between 0 and 3
        direction %= 4

        # Move
        if direction == 0:
            for i in range(int(instruction[1:])):
                position = (position[0], position[1] + 1)
                if position in visited:
                    return abs(position[0]) + abs(position[1])
                visited.add(position)
        elif direction == 1:
            for i in range(int(instruction[1:])):
                position = (position[0] + 1, position[1])
                if position in visited:
                    return abs(position[0]) + abs(position[1])
                visited.add(position)
        elif direction == 2:
            for i in range(int(instruction[1:])):
                position = (position[0], position[1] - 1)
                if position in visited:
                    return abs(position[0]) + abs(position[1])
                visited.add(position)
        elif direction == 3:
            for i in range(int(instruction[1:])):
                position = (position[0] - 1, position[1])
                if position in visited:
                    return abs(position[0]) + abs(position[1])
                visited.add(position)

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))

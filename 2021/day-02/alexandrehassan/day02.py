"""
For problem statement:
    https://adventofcode.com/2021/day/2
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from Common import get_lines, time_function


def part1(lines: list) -> int:
    x_position, y_position = 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            y_position -= distance
        elif instruction == "down":
            y_position += distance
        elif instruction == "forward":
            x_position += distance
        else:
            print("Something went wrong")
    return x_position * y_position


def part2(lines: list) -> int:
    x_position, y_position, aim = 0, 0, 0
    for line in lines:
        instruction = line.split(" ")[0]
        distance = int(line.split(" ")[1])
        if instruction == "up":
            aim -= distance
        elif instruction == "down":
            aim += distance
        elif instruction == "forward":
            x_position += distance
            y_position += aim * distance
        else:
            print("Something went wrong")
    return x_position * y_position


def main():
    lines = get_lines("Inputs/Day02.txt")
    # Part 1: 1989265
    print(f"Part 1: {part1(lines)}")
    # Part 2: 2089174012
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0007306340010836721s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0008213049988262355s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

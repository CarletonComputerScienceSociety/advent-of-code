"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from Common import get_lines, time_function


def calculate(bytes: list, CO2: bool) -> int:
    count_1 = 0
    to_remove = '1'
    index = 0

    while True:
        count_1 = len(
            list(filter(lambda x: x[index] == '1', bytes)))
        to_remove = '0' if CO2 != (count_1 >= len(bytes)/2) else '1'

        bytes = list(
            filter(lambda x: x[index] == to_remove, bytes))

        if len(bytes) == 1:
            return int(bytes[0], 2)
        index += 1


def flip_bit(string: str) -> int:
    return int(string.replace('1', '2').replace('0', '1').replace('2', '0'), 2)


def part1(lines: list) -> int:
    num_lines = len(lines)
    count_1 = [0] * len(lines[0])

    for line in lines:
        for index, value in enumerate(line):
            count_1[index] += int(value)

    gamma = ""
    for count in count_1:
        gamma += '0' if count >= int(num_lines/2) else '1'
    return int(gamma, 2) * flip_bit(gamma)


def part2(lines: list) -> int:
    return calculate(lines, CO2=True) * calculate(lines, CO2=False)


def main():
    lines = get_lines("Inputs/Day03.txt")
    # Part 1: 3633500
    print(f"Part 1: {part1(lines)}")
    # Part 2: 4550283
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0010945069999999998s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0007929939999999999s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

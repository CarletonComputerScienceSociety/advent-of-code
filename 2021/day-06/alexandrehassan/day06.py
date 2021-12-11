"""
For problem statement:
    https://adventofcode.com/2021/day/6
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from typing import DefaultDict
from Common import get_lines, time_function


def setup(lines: list) -> DefaultDict:
    input = lines[0].split(',')
    input = list(map(int, input))
    fish = DefaultDict(int)
    for f in input:
        fish[f] += 1
    return fish


def calculate_fish(lines: list, days: int) -> int:
    fishes = setup(lines)
    for _ in range(days):
        babies = fishes[0]
        fishes[0] = 0
        for i in range(8):
            fishes[i] = fishes[i + 1]
            fishes[i + 1] = 0
        fishes[8] = babies
        fishes[6] += babies

    return sum(fishes.values())


def part1(lines: list) -> int:
    return calculate_fish(lines, 80)


def part2(lines: list) -> int:
    return calculate_fish(lines, 256)


def main():
    lines = get_lines("Inputs/Day06.txt")
    # Part 1: 351092
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1595330616005
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.00012867999999999997s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.00030791799999999996s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

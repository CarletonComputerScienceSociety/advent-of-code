"""
    For problem statement:
        https://adventofcode.com/2021/day/5
    @author: Alexandre Hassan
    https://github.com/alexandrehassan/AdventOfCode2021
    """
from typing import DefaultDict
from Common import get_lines, time_function
import re


class Vent:
    def __init__(self, input: str):
        line = re.split(',| ->', input)
        self.x1, self.y1, self.x2, self.y2 = int(
            line[0]), int(line[1]), int(line[2]), int(line[3])
        self.isVertical = self.x1 == self.x2
        self.isHorizontal = self.y1 == self.y2
        if self.isHorizontal or self.isVertical:
            self.order()
        else:
            self.order_diagonal()

    @property
    def slope(self) -> int:
        if self.x2 - self.x1 > 0 and self.y2 - self.y1 > 0 or \
                self.x2 - self.x1 < 0 and self.y2 - self.y1 < 0:
            return 1
        else:
            return -1

    def part1_valid(self) -> bool:
        return self.isHorizontal or self.isVertical

    def order(self) -> int:
        if self.x1 > self.x2 or self.y1 > self.y2:
            self.x1, self.y1, self.x2, self.y2 =\
                self.x2, self.y2, self.x1, self.y1

    def order_diagonal(self):
        if self.x1 > self.x2:
            self.x1, self.y1, self.x2, self.y2 =\
                self.x2, self.y2, self.x1, self.y1

    def get_coords(self):
        if self.isVertical:
            for i in range(self.y1, self.y2 + 1):
                yield (i, self.x1)
        elif self.isHorizontal:
            for i in range(self.x1, self.x2+1):
                yield (self.y1, i)
        else:
            b = self.y1 - (self.slope * self.x1)
            x_range = abs(self.x2 - self.x1)
            for i in range(x_range+1):
                x = self.x1 + i
                yield (self.slope * x + b, x)

    def __str__(self) -> str:
        return f"{self.x1},{self.y1}->{self.x2},{self.y2}"


def get_num_dangers(lines: list, part1: bool) -> int:
    vents = [Vent(i) for i in lines]
    grid = DefaultDict(int)
    if part1:
        vents = list(filter(lambda x: x.part1_valid(), vents))
    for vent in vents:
        for coord in vent.get_coords():
            grid[coord] += 1
    return sum(1 for i in grid.values() if i >= 2)


def part1(lines: list):
    return get_num_dangers(lines, part1=True)


def part2(lines: list):
    return get_num_dangers(lines, part1=False)


def main():
    lines = get_lines("Inputs/Day05.txt")
    # Part 1: 7468
    print(f"Part 1: {part1(lines)}")
    # Part 2: 22364
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.049304637000000005s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.098618044s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

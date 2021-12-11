"""
For problem statement:
    https://adventofcode.com/2021/day/7
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from Common import get_lines, time_function
from statistics import mean, median


def triangular_sequence(num: int) -> int:
    return num * (num + 1) // 2


def calc(num: int, toCheck: list) -> int:
    return sum(list(map(lambda x: triangular_sequence(abs(x - num)), toCheck)))


def part1(lines: list) -> int:
    # Credit to the subreddit for pointing out that part 1 can be found
    # with the median of the list
    lines = list(map(int, (lines[0].split(","))))
    med = int(median(lines))
    return sum(list(map(lambda x: abs(x - med), lines)))


def part2(lines: list) -> int:
    # Credit to the subreddit for pointing out that part 1 can be found
    # with the mean +-1 of the list
    lines = list(map(int, (lines[0].split(","))))
    avg = round(mean(lines))
    return min([int(calc(avg - 1, lines)), int(calc(avg, lines)),
                int(calc(avg + 1, lines))])


def main():
    lines = get_lines("Inputs/Day07.txt")
    # Part 1: 351092
    print(f"Part 1: {part1(lines)}")
    # Part 2: 104149091
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.0002950209999999842s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0011027729999999992s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

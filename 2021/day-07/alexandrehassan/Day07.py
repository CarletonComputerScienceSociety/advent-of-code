"""
For problem statement:
    https://adventofcode.com/2021/day/3
@author: Alexandre Hassan
"""
from timeit import timeit
from statistics import mean, median


def get_lines(filename: str) -> list:
    with open(filename) as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    return lines


def time_function(func, iterations=100) -> int:
    return timeit(func, number=iterations) / 100


def sequence(num: int) -> int:
    return num * (num + 1) // 2


def calc(num: int, toCheck: list) -> int:
    return sum(list(map(lambda x: sequence(abs(x - num)), toCheck)))


def part1(lines: list) -> int:
    # Credit to the subreddit for pointing out that part 1 can be found
    # with the median of the list
    pos = list(map(int, (lines[0].split(","))))
    med = int(median(pos))
    return sum(list(map(lambda x: abs(x - med), pos)))


def part2(lines: list) -> int:
    # Credit to the subreddit for pointing out that part 1 can be found
    # with the mean +-1 of the list
    pos = list(map(int, (lines[0].split(","))))
    avg = round(mean(pos))
    return min([int(calc(avg, pos)), int(calc(avg + 1, pos)),
                int(calc(avg - 1, pos))])


def test():
    lines = get_lines("Inputs/Day07_sample.txt")

    result = part1(lines)
    print(f"Part 1 sample: {result}")
    assert(result == 37)

    result = part2(lines)
    print(f"Part 2 sample: {result}")
    assert(result == 168)

    lines = get_lines("Inputs/Day07.txt")
    result = part1(lines)
    print(f"Part 1: {result}")
    assert(result == 364898)

    result = part2(lines)
    print(f"Part 2: {result}")
    assert(result == 104149091)

    # Part 1: 0.0002950209999999842s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.0011027729999999992s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


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
    test()

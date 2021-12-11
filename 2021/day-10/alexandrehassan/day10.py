"""
For problem statement:
    https://adventofcode.com/2021/day/10
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from collections import deque
from Common import get_lines, time_function


def check_line(line: str, part1=True) -> int:
    pairs = {"(": ")", "{": "}", "<": ">", "[": "]"}
    closings = {"}": 1197, "]": 57, ">": 25137, ")": 3}
    queue = deque()
    for char in line:
        if char in pairs.keys():
            queue.append(char)
        elif char in closings.keys():
            if pairs[queue.pop()] != char:
                return closings[char] if part1 else 0

    if part1:
        return 0
    to_add = ""
    while len(queue) > 0:
        to_add += pairs[queue.pop()]
    return get_score(to_add)


def get_score(to_add: str) -> int:
    scoring = {"}": 3, "]": 2, ">": 4, ")": 1}
    score = 0
    for char in to_add:
        score = score * 5 + scoring[char]
    return score


def part1(lines: list) -> int:
    score = 0
    for line in lines:
        score += check_line(line)

    return score


def part2(lines: list) -> int:
    score = []
    for line in lines:
        sc = check_line(line, part1=False)
        if sc != 0:
            score.append(sc)
    score.sort()
    return score[len(score)//2]


def main():
    lines = get_lines("Inputs/Day10.txt")
    # Part 1: 166191
    print(f"Part 1: {part1(lines)}")
    # # Part 2: 1152088313
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.00098471s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.001091627s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

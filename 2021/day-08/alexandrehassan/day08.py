"""
For problem statement:
    https://adventofcode.com/2021/day/8
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from typing import DefaultDict
from Common import get_lines, time_function


def string_sort(string: str):
    return ''.join(sorted(string))


def string_differences(a: str, b: str) -> str:
    if len(a) > len(b):
        return string_sort(''.join(set(a) - set(b)))
    else:
        return string_sort(''.join(set(b) - set(a)))


def string_similarities(a: str, b: str) -> str:
    a = set(a)
    b = set(b)
    if len(a) > len(b):
        return string_sort(''.join(a.intersection(b)))
    else:
        return string_sort(''.join(b.intersection(a)))


class Proccessed_line:
    def __init__(self, inputs: list, outputs: list) -> None:
        self.outputs = [string_sort(i) for i in outputs]
        self.inputs = [string_sort(i) for i in inputs]


def process_line(line: str) -> Proccessed_line:
    raw = line.split(" | ")
    return Proccessed_line(raw[0].split(" "), raw[1].split(" "))


def solve(processed: Proccessed_line) -> DefaultDict[int, str]:
    five_characters = set()
    six_characters = set()
    segments = DefaultDict(str)
    known_values = DefaultDict(str)
    for value in processed.inputs:
        length = len(value)
        if length == 2:
            known_values["1"] = value
        elif length == 3:
            known_values["7"] = value
        elif length == 4:
            known_values["4"] = value
        elif length == 7:
            known_values["8"] = value
        elif length == 5:
            five_characters.add(value)
        elif length == 6:
            six_characters.add(value)

    segments[1] = string_differences(known_values["1"], known_values["7"])
    temp = known_values["4"] + segments[1]
    for num in six_characters:
        if len(string_differences(num, temp)) == 1:
            known_values["9"] = num
            six_characters.remove(num)
            break

    for num in five_characters:
        if len(string_differences(num, known_values["9"])) != 1:
            known_values["2"] = num
            five_characters.remove(num)
            break

    temp = string_differences(known_values["9"], known_values["7"])
    for num in six_characters:
        if len(string_differences(num, temp)) == 3:
            known_values["6"] = num
        else:
            known_values["0"] = num

    segments[3] = string_differences(known_values["8"], known_values["6"])

    for num in five_characters:
        if segments[3] in num:
            known_values["3"] = num
        else:
            known_values["5"] = num
    return known_values


def get_output_num(raw_line: str) -> int:
    processed = process_line(raw_line)
    known_values = solve(processed)
    out = ""
    keys = list(known_values.keys())
    values = list(known_values.values())
    for output in processed.outputs:
        out += keys[values.index(output)]
    return int(out)


def part1(lines: list) -> int:
    output_values = []
    for line in lines:
        output_values.extend(line.split(" | ")[1].split(" "))
    return sum(len(x) in [2, 3, 4, 7] for x in output_values)


def part2(lines: list) -> int:
    return sum(get_output_num(line) for line in lines)


def main():
    lines = get_lines("Inputs/Day08.txt")
    # Part 1: 504
    print(f"Part 1: {part1(lines)}")
    # Part 2: 1073431
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.00021447399999999998s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.005627696000000001s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

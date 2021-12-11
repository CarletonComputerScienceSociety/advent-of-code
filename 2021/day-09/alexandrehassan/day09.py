"""
For problem statement:
    https://adventofcode.com/2021/day/9
@author: Alexandre Hassan
https://github.com/alexandrehassan/AdventOfCode2021
"""
from typing import Generator
from Common import get_lines, time_function


def product_largest_3(nums: list) -> list:
    nums.sort(reverse=True)

    return nums[0] * nums[1] * nums[2]


def get_adjacent_points(row: int, col: int, num_lines: int, num_col: int) -> list:
    adjacent_points = []

    if row > 0:
        adjacent_points.append((row - 1, col))
    if row < num_lines - 1:
        adjacent_points.append((row + 1, col))
    if col > 0:
        adjacent_points.append((row, col - 1))
    if col < num_col - 1:
        adjacent_points.append((row, col + 1))

    return adjacent_points


def get_neighbors(row: int, col: int, grid: list) -> list:
    neighbors = set()
    value = grid[row][col]
    adjacent_points = get_adjacent_points(row, col, len(grid), len(grid[0]))

    for adj in adjacent_points:
        adj_value = grid[adj[0]][adj[1]]
        if adj_value > value and adj_value != 9:
            neighbors.add(adj)

    return neighbors


def is_low_point(row: int, col: int, grid: list) -> bool:
    adjacent_points = get_adjacent_points(row, col, len(grid), len(grid[0]))

    for adj_row, adj_col in adjacent_points:
        if grid[adj_row][adj_col] <= grid[row][col]:
            return False

    return True


def find_lowpoints(grid: list) -> list:
    low_points = {}

    for row, line in enumerate(grid):
        for col in range(len(line)):
            if is_low_point(row, col, grid):
                low_points[(row, col)] = get_neighbors(row, col, grid)

    return low_points


def get_basin_size(grid: list, low_points: set):
    basin = low_points
    to_check = low_points.copy()
    checked = set()

    while len(to_check) > 0:
        current = to_check.pop()
        neighbors = get_neighbors(*current, grid)
        to_check.update(neighbors)
        basin.update(neighbors)
        checked.add(current)
        to_check = set(filter(lambda x: x not in checked, to_check))
    return len(basin) + 1


def get_grid(lines: list) -> list:
    grid = []

    for line in lines:
        grid.append(list(map(int, (list(line)))))

    return grid


def part1(lines: list) -> int:
    grid = get_grid(lines)
    low_points = find_lowpoints(grid)
    risk_level = 0

    for row, line in low_points.keys():
        risk_level += grid[row][line] + 1

    return risk_level


def part2(lines: list) -> int:
    basin_sizes = []
    grid = list(get_grid(lines))
    low_points = find_lowpoints(grid)

    for low_point in low_points.keys():
        basin_sizes.append(get_basin_size(grid, low_points[low_point]))

    return product_largest_3(basin_sizes)


def main():
    lines = get_lines("Inputs/Day09.txt")
    global num_col
    global num_lines

    # Part 1:
    print(f"Part 1: {part1(lines)}")
    # Part 2:
    print(f"Part 2: {part2(lines)}")

    # Part 1: 0.02289861800149083s
    print(f"Part 1: {time_function(lambda: part1(lines))}s")
    # Part 2: 0.056208234000951054s
    print(f"Part 2: {time_function(lambda: part2(lines))}s")


if __name__ == "__main__":
    main()

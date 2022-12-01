from aoc import AOC
from collections import defaultdict
from math import floor, sqrt

aoc = AOC(year=2021, day=5)
data = aoc.load()

# Part 1


def draw_cardinal_line(x1, y1, x2, y2, board):
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            board[(x, y)] += 1


board = defaultdict(int)
for coords in data.numbers_by_line():
    [x1, y1, x2, y2] = coords
    if x1 == x2 or y1 == y2:
        draw_cardinal_line(x1, y1, x2, y2, board)

overlapping = sum(1 for x in board if board[x] > 1)
aoc.p1(overlapping)

# Part 2


def draw_diagonal_line(x1, y1, x2, y2, board):
    dx, dy = (x2 - x1) / abs(x2 - x1), (y2 - y1) / abs(y2 - y1)
    x, y = x1, y1
    while True:
        board[(x, y)] += 1
        x, y = x + dx, y + dy

        if (x, y) == (x2 + dx, y2 + dy):
            break


board = defaultdict(int)
for coords in data.numbers_by_line():
    [x1, y1, x2, y2] = coords
    if x1 == x2 or y1 == y2:
        draw_cardinal_line(x1, y1, x2, y2, board)
    else:
        draw_diagonal_line(x1, y1, x2, y2, board)

overlapping = sum(1 for x in board if board[x] > 1)
aoc.p2(overlapping)


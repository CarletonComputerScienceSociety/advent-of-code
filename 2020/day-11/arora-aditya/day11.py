from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *
import copy


DAY = 11
setup(DAY)
lines = read_file(DAY)

dirs = [(0,1), (1,0), (0,-1), (-1,0)]
octs = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

R = -1
C = -1

# Part 1
##################################################
def access(grid, i, j):
    if i >= R or j >= C or i < 0 or j < 0:
        return ""
    else:
        return grid[i][j]

def occupy(grid):
    final = [g[:] for g in grid]
    for i in range(R):
        for j in range(C):
            empty = 0
            full = 0
            total = 0
            for di, dj in octs:
                if access(grid, i+di, j+dj) == "L":
                    empty += 1
                    total += 1
                elif access(grid, i+di, j+dj) == "#":
                    full += 1
                    total += 1
            if empty == total and grid[i][j] == "L":
                final[i][j] = "#"
            elif full >= 4 and grid[i][j] == "#":
                final[i][j] = "L"
    return final

def pg(grid):
    list(map(print, grid))
    print("")

def count(grid):
    k = 0
    for i in grid:
        k += i.count("#")
    return k

def part1(lines: List[str]) -> int:
    global R
    global C
    i = 0
    grid = list(map(list, lines))
    R = len(grid)
    C = len(grid[0])
    # pg(grid)
    ne = occupy(grid)
    while ",".join(map(str, ne)) != ",".join(map(str, grid)):
        grid = ne
        # pg(grid)
        ne = occupy(grid)
        i += 1
    
    return count(grid)

submit(1, part1(lines))


# Part 2
##################################################
def occupy2(grid):
    final = [g[:] for g in grid]
    for i in range(R):
        for j in range(C):
            cur = grid[i][j]
            neighbours = []

            for di, dj in octs:
                for k in range(1, 10000):
                    nex = access(grid, i+di*k, j+dj*k)
                    if nex != ".":
                        neighbours.append(nex)
                        break

            if cur == "L" and neighbours.count("#") == 0:
                final[i][j] = "#"
            
            if cur == "#" and neighbours.count("#") >= 5:
                final[i][j] = "L"
    return final


def part2(lines: List[str]) -> int:
    global R
    global C
    i = 0
    grid = list(map(list, lines))
    R = len(grid)
    C = len(grid[0])
    ne = occupy2(grid)
    while ",".join(map(str, ne)) != ",".join(map(str, grid)):
        grid = ne
        ne = occupy2(grid)

    return count(grid)

submit(2, part2(lines))


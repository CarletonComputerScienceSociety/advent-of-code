from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *
from pprint import pprint as pp
import numpy as np


DAY = 17
setup(DAY)
lines = read_file(DAY)

cubes = [
    (-1, -1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (-1, 0, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (-1, 1, -1),
    (-1, 1, 0),
    (-1, 1, 1),
    (0, -1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (0, 0, -1),
    (0, 0, 1),
    (0, 1, -1),
    (0, 1, 0),
    (0, 1, 1),
    (1, -1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (1, 0, -1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, -1),
    (1, 1, 0),
    (1, 1, 1),
]

quads = [
    (-1, -1, -1, -1),
    (-1, -1, -1, 0),
    (-1, -1, -1, 1),
    (-1, -1, 0, -1),
    (-1, -1, 0, 0),
    (-1, -1, 0, 1),
    (-1, -1, 1, -1),
    (-1, -1, 1, 0),
    (-1, -1, 1, 1),
    (-1, 0, -1, -1),
    (-1, 0, -1, 0),
    (-1, 0, -1, 1),
    (-1, 0, 0, -1),
    (-1, 0, 0, 0),
    (-1, 0, 0, 1),
    (-1, 0, 1, -1),
    (-1, 0, 1, 0),
    (-1, 0, 1, 1),
    (-1, 1, -1, -1),
    (-1, 1, -1, 0),
    (-1, 1, -1, 1),
    (-1, 1, 0, -1),
    (-1, 1, 0, 0),
    (-1, 1, 0, 1),
    (-1, 1, 1, -1),
    (-1, 1, 1, 0),
    (-1, 1, 1, 1),
    (0, -1, -1, -1),
    (0, -1, -1, 0),
    (0, -1, -1, 1),
    (0, -1, 0, -1),
    (0, -1, 0, 0),
    (0, -1, 0, 1),
    (0, -1, 1, -1),
    (0, -1, 1, 0),
    (0, -1, 1, 1),
    (0, 0, -1, -1),
    (0, 0, -1, 0),
    (0, 0, -1, 1),
    (0, 0, 0, -1),
    # (0, 0, 0, 0),
    (0, 0, 0, 1),
    (0, 0, 1, -1),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 1, -1, -1),
    (0, 1, -1, 0),
    (0, 1, -1, 1),
    (0, 1, 0, -1),
    (0, 1, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 1, -1),
    (0, 1, 1, 0),
    (0, 1, 1, 1),
    (1, -1, -1, -1),
    (1, -1, -1, 0),
    (1, -1, -1, 1),
    (1, -1, 0, -1),
    (1, -1, 0, 0),
    (1, -1, 0, 1),
    (1, -1, 1, -1),
    (1, -1, 1, 0),
    (1, -1, 1, 1),
    (1, 0, -1, -1),
    (1, 0, -1, 0),
    (1, 0, -1, 1),
    (1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 0, 0, 1),
    (1, 0, 1, -1),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 1, -1, -1),
    (1, 1, -1, 0),
    (1, 1, -1, 1),
    (1, 1, 0, -1),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 1, 1, -1),
    (1, 1, 1, 0),
    (1, 1, 1, 1),
]


# Part 1
##################################################
def parse_lines(lines):
    g = set()
    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == '#':
                g.add((x, y, 0))
    return g

def bounds(g):
    res = []
    for d in range(3):
        lo = min(x[d] for x in g) - 1
        hi = max(x[d] for x in g) + 2
        res.append((lo, hi))
    return res

def get_count(g, x, y, z):
    return len(set(neighbors(x, y, z)) & g)


def get_next(g):
    ne = set()
    xr, yr, zr = bounds(g)
    for x in range(*xr):
        for y in range(*yr):
            for z in range(*zr):
                n = get_count(g, x, y, z)
                if (x, y, z) in g:
                    if n >=2 and n <= 3:
                        ne.add((x, y, z))
                else:
                    if n == 3:
                        ne.add((x, y, z))
    return ne

def neighbors(x, y, z):
    for dx, dy, dz in cubes:
        yield (dx + x, dy + y, dz + z)

def part1(lines: List[str]) -> int:
    g = parse_lines(lines)

    for i in range(6):
        g = get_next(g)
    return len(g)

submit(1, part1(lines), True)


# Part 2
##################################################
def bounds2(g):
    res = []
    for d in range(4):
        lo = min(x[d] for x in g) - 1
        hi = max(x[d] for x in g) + 2
        res.append((lo, hi))
    return res

def neighbors2(x, y, z, w):
    for dx, dy, dz, dw in quads:
        yield (dx + x, dy + y, dz + z, dw + w)

def get_next2(g):
    ne = set()
    xr, yr, zr, wr = bounds2(g)
    for x in range(*xr):
        for y in range(*yr):
            for z in range(*zr):
                for w in range(*wr):
                    n = get_count2(g, x, y, z, w)
                    if (x, y, z, w) in g:
                        if n in [2,3]:
                            ne.add((x, y, z, w))
                    else:
                        if n == 3:
                            ne.add((x, y, z, w))
    return ne

def get_count2(g, x, y, z, w):
    return len(set(neighbors2(x, y, z, w)) & g)

def parse_lines2(lines):
    g = set()
    for x, l in enumerate(lines):
        for y, c in enumerate(l):
            if c == '#':
                g.add((x, y, 0, 0))
    return g

def part2(lines: List[str]) -> int:
    g = parse_lines2(lines)

    for i in range(6):
        g = get_next2(g)

    return len(g)

submit(2, part2(lines), True)



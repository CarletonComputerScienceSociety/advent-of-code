from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 3
setup(DAY)
file = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

x = 0
y = 0
R = len(file)
C = len(file[0])
count = 0
while x != R - 1:
    x += 1
    y += 3
    y = y % C
    row = file[x]
    if row[y] == "#":
        count += 1

ans = count

submit(1, ans)


# Part 2
##################################################
ans = float("inf")

def get_count(right, down):
    x = 0
    y = 0
    R = len(file)
    C = len(file[0])
    count = 0
    while x + down < R:
        x += down
        y += right
        y = y % C
        row = file[x]
        if row[y] == "#":
            count += 1
    return count

x1 = get_count(1, 1)
x2 = get_count(3, 1)
x3 = get_count(5, 1)
x4 = get_count(7, 1)
x5 = get_count(1, 2)

ans = x1 * x2 * x3 * x4 * x5

submit(2, ans)

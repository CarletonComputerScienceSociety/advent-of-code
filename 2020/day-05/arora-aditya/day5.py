from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
import sys
from helper.submit.submit import *
from utils import *


DAY = 5
setup(DAY)
file = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

R = 128
C = 8

def get_seat(s):
    u_bound = (0, R - 1)
    l_bound = (0, C - 1)
    for char in s:
        l, u = u_bound
        mid = (l + u)//2
        lr, ur = l_bound
        midr = (lr + ur)//2
        if char == "F":
            u_bound = (l, mid)
        elif char == "B":
            u_bound = (mid+1, u)
        elif char == "L":
            l_bound = (lr, midr)
        elif char == "R":
            l_bound = (midr+1, ur)
    x, x1 = u_bound
    if x != x1:
        sys.exit(1)
    y, y1 = l_bound
    if y != y1:
        sys.exit(1)
    
    return x, y

ma = -1        
for line in file:
    x, y = get_seat(line)
    ma = max(ma, x*8 + y)


ans = ma


submit(1, ans)


# Part 2
##################################################
ans = float("inf")

se = set()


for line in file:
    x, y = get_seat(line)
    se.add(x*8 + y)
    
ans = list(set(range(min(se), max(se)+1)) - se)[0]


submit(2, ans)

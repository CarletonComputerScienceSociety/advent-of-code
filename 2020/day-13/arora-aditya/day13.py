from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 13
setup(DAY)
lines = read_file(DAY)

buses = []

# Part 1
##################################################
def part1(lines: List[str]) -> int:
    global t
    global buses
    t = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != "x"]
    next_times = []
    ans = [float('inf'), None]
    for b in buses:
        m = (((t//b)*b))
        if m < t:
            m += b
        m -= t
        if m < ans[0]:
            ans = [m, b]
    return ans[0] * ans[1]

# submit(1, part1(lines))


# Part 2
##################################################
# def part2(lines: List[str]) -> int:
#     b = []
#     for i, x in enumerate(lines[1].split(",")):
#         if x != "x":
#             b.append([i, int(x)])
# 
#     s = 1000
#     xs = set()
#     while True:
#         i, x = b[0]
#         xs = set([x*j - i for j in range(s)])
#         for i, x in b[1:]:
#             a = set([x*j - i for j in range(s//2 - 1, s)])
#             xs &= a
#             if len(xs) == 0:
#                 break
#         if len(xs) >= 1:
#             return min(xs)
#         else:
#             s *= 2

from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def part2(lines: List[str]) -> int:
    remainders = []
    divisors   = []
    for i, x in enumerate(lines[1].split(',')):
        if x != "x":
            x = int(x)
            remainders.append(x-i)
            divisors.append(x)
    return chinese_remainder(divisors, remainders)

submit(2, part2(lines))



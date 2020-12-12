from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from math import ceil
from helper.submit.submit import *
from utils import *


DAY = 12
setup(DAY)
lines = read_file(DAY)

F = "E"

# E N
e = 0
n = 0

def process(dir, count):
    if dir == "N":
        return 0, count
    elif dir == "S":
        return 0, -1 * count
    elif dir == "E":
        return count, 0
    elif dir == "W":
        return -1*count , 0

order = list("NESW")

def move(line):
    global F
    global e
    global n
    dir, count = line[0], int(line[1:])
    if dir in set("NEWS"):
        de, dn = process(dir, count)
        e += de
        n += dn
    elif dir == "F":
        de, dn = process(F, count)
        e += de
        n += dn
    elif dir == "L":
        if count % 90 != 0:
            sys.exit(1)
        for i in range(ceil(count/90)):
            F = order[order.index(F)-1]
    elif dir == "R":
        if count % 90 != 0:
            sys.exit(1)
        for i in range(ceil(count/90)):
            F = order[(order.index(F)+1)%len(order)]
            
        

# Part 1
##################################################
def part1(lines: List[str]) -> int:
    for line in lines:
        move(line)
    return abs(e) + abs(n)

submit(1, part1(lines))


# Part 2
##################################################
e = 0
n = 0
we = 10
wn = 1

def move2(line):
    global F
    global e
    global n
    global we
    global wn
    dir, count = line[0], int(line[1:])
    if dir in set("NEWS"):
        de, dn = process(dir, count)
        we += de
        wn += dn
    elif dir == "F":
        de, dn = process(F, count)
        for i in range(count):
            e += we
            n += wn
    elif dir == "L":
        if count % 90 != 0:
            sys.exit(1)
        count = count % 360
        for i in range(ceil(count/90)):
            we, wn = -wn, we
    elif dir == "R":
        if count % 90 != 0:
            sys.exit(1)
        count = count % 360
        for i in range(ceil(count/90)):
                we, wn = wn, -we


def part2(lines: List[str]) -> int:
    for line in lines:
        move2(line)
    return abs(e) + abs(n)

# part2(lines)
submit(2, part2(lines))



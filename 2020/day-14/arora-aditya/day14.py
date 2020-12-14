from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from itertools import product
from helper.submit.submit import *
from utils import *

import sys


DAY = 14
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def apply(m, v):
    if m == "X":
        return v
    if m == "1":
        return "1"
    if m == "0":
        return "0"
    sys.exit(1)

def part1(lines: List[str]) -> int:
    mem = {}
    for line in lines:
        if line.startswith("mask = "):
            mask = line[len("mask = "):]
            print(mask)
        else:
            index = int(line[line.index("[") + 1:line.index("]")])
            value = int(line[line.index("=") + 1:])
            value = bin(value)[2:]
            value = "0" * (len(mask) - len(value)) + value
            result = ""
            for i in range(len(mask)):
                result += apply(mask[i], value[i])
            mem[index] = int(result, 2)
    return sum(mem.values())
                
        

submit(1, part1(lines))


# Part 2
##################################################
def mask_addr(mask, index):
    addrn = [None]*36
    for i, (m, a) in enumerate(zip(mask, index)):
        if m == "0":
            addrn[i] = a
        elif m == "1":
            addrn[i] = "1"
        else:
            addrn[i] = "X"
    return "".join(addrn)
        

def part2(lines: List[str]) -> int:
    mem = {}
    for line in lines:
        if line.startswith("mask = "):
            mask = line[len("mask = "):]
        else:
            index = int(line[line.index("[") + 1:line.index("]")])
            index = bin(index)[2:]
            index = "0" * (len(mask) - len(index)) + index

            value = int(line[line.index("=") + 1:])
                
            addr = mask_addr(mask, index)
            addr_ft = addr.replace("X", "{}") 
            for i in product("01", repeat=addr.count("X")):
                a = int(addr_ft.format(*i),2)
                mem[a] = value

        
    return sum(mem.values())


submit(2, part2(lines))



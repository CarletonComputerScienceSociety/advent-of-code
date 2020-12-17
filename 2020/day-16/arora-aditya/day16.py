from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *
from pprint import pprint as pp


DAY = 16
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def get_invalids(di, nums):
    invalids = []
    for num in nums:
        flag = False
        for x in di.values():
            if num in x:
                flag = True
                break
        if not flag:
            invalids.append(num)
    return invalids

def part1(lines: List[str]) -> int:
    i = 0
    line = lines[i]
    di = defaultdict(set)
    while len(line) != 0:
        i += 1
        name, ranges = line.split(": ")
        for r in ranges.split(" or "):
            l, u = r.split("-")
            x = set(range(int(l), int(u)+1))
            di[name] |= x
        line = lines[i]
    
    
    i += 5
    asa = []
    # print(lines[i-1])
    for j in range(i, len(lines)):
        # print(lines[j])
        asa.extend(get_invalids(di, map(int, lines[j].split(",")))) 
    # print(asa)
    return sum(asa)

submit(1, part1(lines))


# Part 2
##################################################
def is_invalid(di, nums):
    invalids = []
    for num in nums:
        flag = False
        for x in di.values():
            if num in x:
                flag = True
                break
        if not flag:
            invalids.append(num)
    return len(invalids) != 0

def part2(lines: List[str]) -> int:
    i = 0
    line = lines[i]
    di = defaultdict(set)
    while len(line) != 0:
        i += 1
        name, ranges = line.split(": ")
        for r in ranges.split(" or "):
            l, u = r.split("-")
            x = set(range(int(l), int(u)+1))
            di[name] |= x
        line = lines[i]
    
    
    i += 5
    asa = []
    
    my_ticket = list(map(int, lines[i-3].split(",")))
    L = len(my_ticket)

    keys = list(di.keys())
    opts = [set(keys) for i in range(L)]

    for j in range(i, len(lines)):
        nums = list(map(int, lines[j].split(",")))
        if not is_invalid(di, nums):
            for i in range(L):
                for k in range(len(keys)):
                    key = keys[k]
                    if nums[i] not in di[key]:
                        opts[i].remove(key)
    
    opts_sorted = []
    for o in range(len(opts)):
        opts_sorted.append([o, opts[o]])
    
    opts_sorted.sort(key=lambda x: len(x[1]))
    
    
    mappings = dict()
    i = dict()
    for o in opts_sorted:
        if len(o[1]) == 1:
            for x in opts_sorted:
                if x != o:
                    x[1] -= o[1]
            mappings[list(o[1])[0]] = o[0]
        
    ans = 1
    for k in range(len(keys)):
        key = keys[k]
        if key.startswith("departure"):
            ans *= my_ticket[mappings[key]]
    
    
    return ans

submit(2, part2(lines))



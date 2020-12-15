from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 15
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def get_next(nums, di):
    if len(di[nums[-1]]) == 1:
        return 0
    return di[nums[-1]][-1] - di[nums[-1]][-2]

def part1(lines: List[str]) -> int:
    nums = list(map(int, lines[0].split(",")))
    di = defaultdict(list)
    for i in range(len(nums)):
        di[nums[i]].append(i+1)
    
    turn = 2020
    i = len(nums) + 1
    while i < turn + 1:
        nums.append(get_next(nums, di))
        di[nums[-1]].append(i)
        i += 1
    
    return nums[-1]    
    

# submit(1, part1(lines), True)


# Part 2
##################################################
def get_next(nums, di):
    if len(di[nums[-1]]) == 1:
        return 0
    return di[nums[-1]][-1] - di[nums[-1]][-2]

def part2(lines: List[str]) -> int:
    nums = list(map(int, lines[0].split(",")))
    di = defaultdict(list)
    for i in range(len(nums)):
        di[nums[i]].append(i+1)
    
    turn = 30000000
    i = len(nums) + 1
    while i < turn + 1:
        nums.append(get_next(nums, di))
        di[nums[-1]].append(i)
        i += 1
    
    return nums[-1]   

submit(2, part2(lines), True)



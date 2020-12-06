from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 6
setup(DAY)
file = read_file(DAY)


# Part 1
##################################################
ans = float('inf')
ct = 0

def count_for_group(lines):
    chars = "".join(lines)
    return len(set(chars))

j = 0
done = False
for i in range(len(file)):
    done = False
    line = file[i]
    if line == "":
        x = count_for_group(file[j:i])
        ct += x
        j = i + 1
        done = True

if not done:
    x = count_for_group(file[j:i])
    ct += x
    j = i + 1


ans = ct
submit(1, ans)


# Part 2
##################################################
ans = float("inf")

ct = 0

def count_for_group2(lines):
    chars = "".join(lines)
    ct = 0
    for char in set(chars):
        flag = True
        for line in lines:
            if char not in line:
                flag = False
                break
        if flag:
            ct += 1
    return ct

j = 0
done = False
for i in range(len(file)):
    done = False
    line = file[i]
    if line == "":
        x = count_for_group2(file[j:i])
        ct += x
        j = i + 1
        done = True

if not done:
    x = count_for_group2(file[j:i])
    ct += x
    j = i + 1


ans = ct



submit(2, ans)

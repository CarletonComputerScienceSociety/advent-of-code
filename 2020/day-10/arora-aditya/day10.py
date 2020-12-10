from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 10
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

nums = []
for line in lines:
    nums.append(int(line))
    
START = 0
sor = list(sorted(nums))

T = 0
O = 0
sor = [0] + sor
sor = sor + [max(nums) + 3]

for i in range(len(sor)-1):
    if sor[i+1] - sor[i] == 3:
        T += 1
    elif sor[i+1] - sor[i] == 1:
        O += 1

ans = O * T

submit(1, ans)


# Part 2
##################################################
ans = float("inf")

dp = [0 for i in range(len(sor))]
dp[-1] = 1
for i in range(len(sor)-2, -1, -1):
    su = 0
    for j in range(i+1,len(sor)):
        if sor[j] - sor[i]<=3:
            su += dp[j]
        else:
            break
    dp[i] = su

ans = dp[0]


submit(2, ans)

from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 9
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {} # val : index
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return True
        prevMap[n] = i
    return False

nums = []
for line in lines:
    nums.append(int(line))
    
for i in range(25, len(nums)):
    if not twoSum(nums[i-25: i], nums[i]):
        ans = nums[i]
        break


submit(1, ans)


# Part 2
##################################################

dp = [0]*(len(nums)+1)
for i in range(len(nums)):
    dp[i+1] = dp[i] + nums[i]

done = False
N = len(nums)
for j in range(N):
    for i in range(N):
        if dp[i] - dp[j] == ans:
            arr = nums[j:i]
            ans = min(arr) + max(arr)
            done = True
            break
    if done:
        break
    



submit(2, ans)

from typing import List, Dict, Set
from collections import defaultdict
from collections import Counter
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 2
setup(DAY)
file = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

count = 0
for line in file:
    line = line.strip()
    mi, line = line.split('-')
    ma, lcolon, st = line.split(' ')
    mi = int(mi)
    ma = int(ma)
    lcolon = lcolon[:-1]
    c = Counter(st)
    if c[lcolon] > ma or c[lcolon] < mi:
        pass
    else:
        count += 1

ans = count

submit(1, ans)


# Part 2
##################################################
ans = float("inf")

count = 0
for line in file:
    line = line.strip()
    mi, line = line.split('-')
    ma, lcolon, st = line.split(' ')
    mi = int(mi)
    ma = int(ma)
    lcolon = lcolon[:-1]
    if st[mi-1] == lcolon and st[ma-1] != lcolon:
        count += 1
    elif st[mi-1] != lcolon and st[ma-1] == lcolon:
        count += 1
    else:
        pass

ans = count

submit(2, ans)

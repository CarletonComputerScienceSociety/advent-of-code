from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *
import sys


DAY = 8
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

acc = 0

seen = set()
values = [acc]

N = 0
J = 1
A = 2

def parse_line(line):
    i, num = line.split(' ')
    if i == "jmp":
        i = J
    elif i == "acc":
        i = A
    elif i == "nop":
        i = N
    else:
        print("F")
        sys.exit(1)
    return i, int(num)
    print(line)

pines = []
for line in lines:
    pines.append(parse_line(line))

idx = 0
while True:
    i, n = pines[idx]
    if idx in seen:
        break
    
    seen.add(idx)
    values.append(idx)
    if i == A:
        acc += n
        idx += 1
    elif i == J:
        idx += n
    elif i == N:
        pass
        idx += 1
    else:
        print("F")
        sys.exit(1)


ans = acc


# submit(1, ans)


# Part 2
##################################################
ans = float("inf")

def does_loop(ps):
    print(ps)
    accc = 0

    seen = set()
    values = [accc]
    
    idx = 0
    while idx < len(ps):
        i, n = ps[idx]
        if idx in seen:
            return True, -1
        
        seen.add(idx)
        values.append(idx)
        if i == A:
            accc += n
            idx += 1
        elif i == J:
            idx += n
        elif i == N:
            pass
            idx += 1
        else:
            print("F")
            sys.exit(1)

    return False, accc

for j in range(len(pines)):
    i, n = pines[j]
    if i == J:
        k, ans = does_loop(pines[:j] + [(N, n)] + pines[j+1:])
        if not k:
            break


submit(2, ans)

from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from pprint import pprint as pp
import sys
from math import *
from helper.submit.submit import *
from utils import *


DAY = 18
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
def split(part):
    k = []
    for p in part.split("+"):
        k.append(p.split("*"))

def get_matching_brackets(line):
    di = {}
    st = []
    L = len(line)
    for i in range(L):
        l = line[i]
        if l == "(":
            st.append(i)
        elif l == ")":
            di[st.pop()] = i
    if len(st) != 0:
        sys.exit(1)
    # print(st, di)
    return di
    

def get_ans(line):
    # print("L", line)
    split = line.split(" ")
    bs = get_matching_brackets(line)
    # print("B", bs)
    L = len(line)
    S = len(split)
    ops = {"+", "*"}
    j = 0
    i = 0
    a = 0
    O = ""
    while i < S:
        s = split[i]
        if s.startswith("("):
            # print("H", s, j, bs)
            att = get_ans(line[j+1:bs[j]])
            if O == "":
                a = att
            elif O == "+":
                a += att
            elif O == "*":
                a *= att
            i += line[j+1:bs[j]].count(" ") + 1
            j += len(line[j+1:bs[j]]) + 3
        elif s in ops:
            # print("O", s)
            j += 2
            i += 1
            O = s
        else:
            k = int(s)
            j += len(s) + 1
            # print("N", k)
            i += 1
            if O == "":
                a = k
            elif O == "+":
                a += k
            elif O == "*":
                a *= k
    return a
            
        

def part1(lines: List[str]) -> int:
    ans = sum(map(get_ans, lines))
    return ans

submit(1, part1(lines))


# Part 2
##################################################
class new_ops(int):
    def __mul__(self, b):
        return new_ops(int(self) + b)
    def __sub__(self, b):
        return new_ops(int(self) * b)
    
    
def get_ans2(line):
    e = re.sub(r"(\d+)", r"a(\1)", line)
    e = e.replace("*", "-")
    e = e.replace("+", "*")
    return eval(e, {}, {"a": new_ops})

def part2(lines: List[str]) -> int:
    ans = sum(map(get_ans2, lines))
    return ans

submit(2, part2(lines))



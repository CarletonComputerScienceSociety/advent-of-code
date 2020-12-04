from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *


DAY = 4
setup(DAY)
file = read_file(DAY)


# Part 1
##################################################
ans = float("inf")

def is_valid(x):
    return len(required_keys - set(x.keys())) == 0
        

def parse_line(y):
    di = dict()
    for i in y.split(" "):
        key, val = i.split(":")
        di[key] = val
    return di


required_keys = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
])

count = 0

x = dict()
done = False
for line in file:
    if line == "":
        if is_valid(x):
            count += 1
        x = dict()
        done = True
    else:
        done = False
        x.update(parse_line(line))

if not done:
    if is_valid(x):
        count += 1

ans = count

submit(1, ans)


# Part 2
##################################################
ans = float("inf")

def is_valid(x):
    if len(required_keys - set(x.keys())) == 0:
        byr = int(x.get("byr"))
        if byr < 1920 or byr > 2002:
            return False

        iyr = int(x.get("iyr"))
        if iyr < 2010 or iyr > 2020:
            return False
        
        eyr = int(x.get("eyr"))
        if eyr < 2020 or eyr > 2030:
            return False
        
        pid = x.get("pid")
        if len(pid) != 9:
            return False
        
        ecl = x.get("ecl")
        if ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth",}:
            return False
        
        hcl = x.get("hcl")
        if hcl[0] != "#" or any([not x.isalnum() for x in hcl[1:]]):
            return False
        
        hgt = x.get("hgt")
        n, uni = hgt[:-2], hgt[-2:] 
        try:
            n = int(n)
        except:
            return False
        if uni == "in":
            if n < 59 or n > 76: 
                return False
        elif uni == "cm":
            if n < 150 or n > 193: 
                return False
        else:
            return False
    else:
        return False
    return True

def parse_line(y):
    di = dict()
    for i in y.split(" "):
        key, val = i.split(":")
        di[key] = val
    return di


required_keys = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
])

count = 0

x = dict()
done = False
for line in file:
    if line == "":
        if is_valid(x):
            count += 1
        x = dict()
        done = True
    else:
        done = False
        x.update(parse_line(line))

if not done:
    if is_valid(x):
        count += 1

ans = count

submit(2, ans)

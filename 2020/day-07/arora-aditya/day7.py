from typing import List, Dict, Set
from collections import *
from functools import lru_cache
from math import log10
from helper.submit.submit import *
from utils import *
from pprint import pprint as pp


DAY = 7
setup(DAY)
lines = read_file(DAY)


# Part 1
##################################################
ans = float("inf")
di = dict()

def parse_bag(bag):
    bag = bag.split(' ')
    if bag[0] == 'no':
        return None
    else:
        return int(bag[0]), ' '.join(bag[1:3])

def parse_container(bag):
    bag = bag.split(' ')
    return ' '.join(bag[:2])

def parse_line(line):
    line = line[:-1]
    split = line.split(" contain ")
    key = parse_container(split[0])
    di[key] = []
    for s in split[1:]:
        for bag in s.split(", "):
            di[key].append(parse_bag(bag))
    

for line in lines:
    parse_line(line)

counter = 0
uniques = dict()
for key in di:
    if key not in uniques:
        uniques[key] = counter
        counter += 1

GOLD = "shiny gold"

def find_parents(childs):
    se = set()
    for key in di:
        for children in di[key]:
            if children is not None and children[1] in childs:
                se.add(key)
                break
    return se

gg = set()
prev = find_parents({GOLD})
gg |= prev
while len(prev) != 0:
    prev = find_parents(prev)
    gg |= prev

    
ans = len(gg)

submit(1, ans)


# Part 2
##################################################
ans = float("inf")

def get_bags_for_parent(parent):
    count = 0
    for b in di[parent]:
        if b is not None:
            ct, bag = b
            count += ct*(1 + get_bags_for_parent(bag))
    return count

ans = get_bags_for_parent(GOLD)


submit(2, ans)

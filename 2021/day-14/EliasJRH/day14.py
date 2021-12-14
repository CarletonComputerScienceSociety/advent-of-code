import copy
import math

inf = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

lines = inf.split("\n")

pairs = {}

occurs = {}
tempOccurs = {}
letters = {}

template = list(lines[0])

for line in range(2, len(lines)):
    lines[line] = lines[line].split(" ")
    pairs[lines[line][0]] = lines[line][2]

for par in range(len(template) - 1):
    curPair = template[par] + template[par + 1]
    if curPair not in occurs:
        occurs[curPair] = 0
    occurs[curPair] += 1

def solve(ran):

    global pairs
    global occurs
    global tempOccurs
    global letters
    global template

    for x in range(ran):
        for key in occurs:
            match = pairs[key]

            backPair = key[0] + match
            frontPair = match + key[1]

            if backPair not in tempOccurs:
                tempOccurs[backPair] = 0
            tempOccurs[backPair] += occurs[key]

            if frontPair not in tempOccurs:
                tempOccurs[frontPair] = 0
            tempOccurs[frontPair] += occurs[key]

        occurs = copy.deepcopy(tempOccurs)
        tempOccurs = {}

    for key in occurs:
        for char in key:
            if char not in letters:
                letters[char] = 0
            letters[char] += occurs[key]

    print(math.ceil((max(letters.values()) - min(letters.values())) / 2))

solve(10)
solve(40)

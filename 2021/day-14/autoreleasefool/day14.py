from collections import defaultdict
from typing import Counter
from aoc import AOC, Drop, Regex, String

aoc = AOC(year=2021, day=14)
data = aoc.load()

chunks = data.chunk([
    String(1),
    Drop(1),
    Regex(r"(\w+) -> (\w+)")
])

polymer = chunks[0][0]
rules = {k: v for k, v in chunks[1]}

# Part 1

for _ in range(10):
    # Build polymer iteratively
    next_polymer = ""
    for a, b in zip(polymer[:-1], polymer[1:]):
        next_polymer += f"{a}{rules[a + b]}"
    polymer = next_polymer + polymer[-1]

counter = Counter(polymer)
aoc.p1(max(counter.values()) - min(counter.values()))

# Part 2

template = chunks[0][0]
last_character = template[-1]

# Count occurrences of each pair in the template
polymer = defaultdict(int)
for a, b in zip(template[:-1], template[1:]):
    polymer[(a, b)] += 1

for _ in range(40):
    # Count occurrences of pairs instead of constructing the string
    next_polymer = defaultdict(int)
    for a, b in polymer.keys():
        inserted = rules[a + b]
        next_polymer[(a, inserted)] += polymer[(a, b)]
        next_polymer[(inserted, b)] += polymer[(a, b)]
    polymer = next_polymer

counter = defaultdict(int)
for (a, _), occurrences in polymer.items():
    counter[a] += occurrences
counter[last_character] += 1

aoc.p2(max(counter.values()) - min(counter.values()))


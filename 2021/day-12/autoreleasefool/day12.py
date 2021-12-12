from collections import defaultdict
from typing import Set
from aoc import AOC

aoc = AOC(year=2021, day=12)
data = aoc.load()

connections = defaultdict(set)
small_caves = set()

for a, b in data.parse(r"(.*)-(.*)"):
    connections[a].add(b)
    connections[b].add(a)

    if a.upper() != a:
        small_caves.add(a)
    if b.upper() != b:
        small_caves.add(b)


def search(cave: str, path: Set[str], can_visit_small_cave_twice: bool):
    if cave == 'end':
        return 1

    paths = 0
    for connection in connections[cave]:
        if connection == 'start':
            continue
        elif connection not in small_caves:
            paths += search(connection, set(list(path) + [connection]), can_visit_small_cave_twice)
        elif connection not in path:
            paths += search(connection, set(list(path) + [connection]), can_visit_small_cave_twice)
        elif can_visit_small_cave_twice:
            paths += search(connection, set(list(path) + [connection]), False)
    return paths

aoc.p1(search('start', set(['start']), False))
aoc.p2(search('start', set(['start']), True))


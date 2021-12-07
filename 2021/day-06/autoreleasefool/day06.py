from aoc import AOC

aoc = AOC(year=2021, day=6)
data = aoc.load()

# Part 1

fish = data.nums()
for _ in range(80):
    nfish = []
    for f in fish:
        if f == 0:
            nfish.append(6)
            nfish.append(8)
        else:
            nfish.append(f - 1)
    fish = nfish

aoc.p1(len(fish))

# Part 2

fish = [0] * 9

for f in data.nums():
    fish[f] += 1

for _ in range(256):
    nfish = [0] * 9
    for i, f in enumerate(fish[1:]):
        nfish[i] = f
    nfish[6] += fish[0]
    nfish[8] = fish[0]
    fish = nfish

aoc.p2(sum(fish))


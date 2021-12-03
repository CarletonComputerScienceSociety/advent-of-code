from aoc import AOC

aoc = AOC(year=2021, day=3)
data = aoc.load()

# Part 1

def most_common_bit(bitstrings, position):
    bits = {0: 0, 1: 0}
    for b in bitstrings:
        bits[int(b[position])] += 1

    return 0 if bits[0] > bits[1] else 1

gamma = ""
for position in range(data.line_length):
    gamma += str(most_common_bit(data.lines(), position))

epsilon = "".join(["0" if g == "1" else "1" for g in gamma])

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

aoc.p1(gamma * epsilon)

# Part 2

def least_common_bit(bitstrings, position):
    bits = {0: 0, 1: 0}
    for b in bitstrings:
        bits[int(b[position])] += 1

    return 1 if bits[1] < bits[0] else 0


def reduce(bitstrings, position, bit_extractor):
    reduced = []
    comparator = str(bit_extractor(bitstrings, position))
    reduced = [b for b in bitstrings if b[position] == comparator]
    if len(reduced) == 1:
        return int(reduced[0], 2)
    else:
        return reduce(reduced, position + 1, bit_extractor)


oxygen = reduce(data.lines(), 0, most_common_bit)
co = reduce(data.lines(), 0, least_common_bit)

aoc.p2(oxygen * co)
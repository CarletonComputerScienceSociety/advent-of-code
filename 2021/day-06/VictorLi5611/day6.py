from collections import Counter
data = [line.strip() for line in open("input.txt", 'r')]

nums = list(map(int, data[0].split(",")))
cums = Counter(nums)
def evolves(cnums):
    out = Counter()
    for k, v in cnums.items():
        if k > 0:
            out[k - 1] += v
        else:
            out[6] += v
            out[8] += v
    return out

for i in range(80):
    cums = evolves(cums)
print(sum(cums.values()))

nums = list(map(int, data[0].split(",")))
cums = Counter(nums)


for i in range(256):
    cums = evolves(cums)
print(sum(cums.values()))

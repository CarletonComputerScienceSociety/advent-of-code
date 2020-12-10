data = [int(line.strip()) for line in open("input.txt", 'r')]


def solve1(data):
    data.append(0)
    data.append(max(data)+3)
    data.sort()
    ones = 0
    threes = 0
    for a, b in zip(data, data[1:]):
        if b-a == 1:
            ones +=1
        elif b-a == 3:
            threes += 1
    return ones * threes

memo = {}
def solve2(adapters, start, goal):
    k = (len(adapters), start)
    if k in memo:
        return memo[k]
    ways = 0
    
    if goal - start <= 3:
        ways += 1
    if not adapters:
        return ways
    if adapters[0] - start <= 3:
        ways += solve2(adapters[1:], adapters[0], goal)
    ways += solve2(adapters[1:], start, goal)
    memo[k] = ways
    return ways

print(solve1(data))
print(solve2(sorted(data), 0, max(data) + 3))


def reader() -> list[str]:
    res = []
    with open('input', 'r') as f:
        lines = f.readlines()
        res = [l.strip('\n') for l in lines ]
    return res

def part1(input: list[str]) -> int:
    greatest = 0
    current = 0
    for line in input:
        if line == '':
            if current > greatest:
                greatest = current
            current = 0
            continue
        current += int(line)
    if current > greatest:
        greatest = current
        
    return greatest

def part2(input: list[str]) -> int:
    totals = []
    current = 0
    for line in input:
        if line == '':
            totals.append(current)
            current = 0
            continue
        current += int(line)
    totals.sort()
    return totals[-1] + totals[-2] + totals[-3]

input = reader()
p1 = part1(input)
p2 = part2(input)

print(f"Part 1 = {p1}")
print(f"Part 2 = {p2}")


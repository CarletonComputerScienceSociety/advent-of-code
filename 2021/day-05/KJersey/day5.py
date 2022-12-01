data = [line.strip() for line in open("day5.txt", 'r')]

size = 1000
counter = 0

grid = []

for _ in range(size):
    row = []
    for _ in range(size):
        row.append(0)

    grid.append(row)

for line in data:
    start, end = line.split(" -> ")
    x1, y1 = list(map(lambda x: int(x), start.split(',')))
    x2, y2 = list(map(lambda x: int(x),   end.split(',')))

    if x1 == x2:
        s = min(y1, y2)
        e = max(y1, y2)
        for i in range(s, e + 1):
            grid[i][x1] += 1
    elif y1 == y2:
        s = min(x1, x2)
        e = max(x1, x2)
        for i in range(s, e + 1):
            grid[y1][i] += 1
    elif (x2 > x1 and y2 > y1) or (x1 > x2 and y1 > y2):
        for i in range(abs(x2 - x1) + 1):
            grid[min(y1, y2) + i][min(x1, x2) + i] += 1
    else:
        for i in range(abs(x2 - x1) + 1):
            grid[max(y1, y2) - i][min(x1, x2) + i] += 1


for i in range(size):
    for j in range(size):
        if grid[i][j] >= 2:
            counter += 1

print(counter)
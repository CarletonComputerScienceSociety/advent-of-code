data = [line.strip() for line in open("day13.txt", 'r')]

coords = []
folds = []

max_x = 0
max_y = 0

def printGrid():
    for j in range(max_y):
        for i in range(max_x):
            print("#", end = '') if grid[j][i] else print(" ", end = '')
        print()

def foldGrid(axis, n):
    global max_x
    global max_y
    len_x = max_x - 1
    len_y = max_y - 1
    if axis == "x":
        for y in range(len_y):
            for x in range(len_x - n):
                grid[y][x] = grid[y][x] or grid[y][len_x - x]
        max_x = len_x // 2
    else:
        for y in range(len_y - n):
            for x in range(len_x):
                grid[y][x] = grid[y][x] or grid[len_y - y][x]
        max_y = len_y // 2

def countGrid():
    count = 0
    for row in grid:
        for c in row:
            if c:
                count += 1

    return count

for line in data:
    if line == '':
        continue
    
    try:
        x, y = line.split(',')
        x = int(x)
        y = int(y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        coords.append((x, y))
    except:
        axis, n = line.split('=')
        folds.append((axis[-1], int(n)))

max_x = 0
max_y = 0

for axis, n in folds:
    if axis == "x":
        max_x = max(max_x, 2 * n + 1)
    else:
        max_y = max(max_y, 2 * n + 1)

grid = [[False for _ in range(max_x)] for _ in range(max_y)] 

for x, y in coords:
    grid[y][x] = True

for axis, n in folds:
    foldGrid(axis, n)

printGrid()
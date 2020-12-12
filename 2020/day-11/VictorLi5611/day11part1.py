data = [line.strip() for line in open("input.txt", 'r')]

def state(grid):
    row, col = len(grid), len(grid[0])
    newGrid = [[grid[x][y] for y in range(col)] for x in range(row)]
    changeHappen = False
    for x in range(row):
        for y in range(col):
            if grid[x][y] == '.':
                continue

            adj = 0
          
            adj += x and y and grid[x-1][y-1] == '#'
            adj += x and grid[x-1][y] == '#'
            adj += x and y + 1 < col and grid[x-1][y+1] == '#'
            adj += y and grid[x][y-1] == '#'
            adj += y + 1 < col and grid[x][y+1] == '#'
            adj += x + 1 < row and y and grid[x+1][y-1] == '#'
            adj += x + 1 < row and grid[x+1][y] == '#'
            adj += x + 1 < row and y + 1 < col and grid[x+1][y+1] == '#'
            
            if grid[x][y] == 'L' and adj == 0:
                changeHappen = True
                newGrid[x][y] = '#'
            elif grid[x][y] == '#' and adj >= 4:
                changeHappen = True
                newGrid[x][y] = 'L'
    return newGrid, changeHappen

changeHappen = True
while changeHappen:
    data, changeHappen = state(data)

total = 0
for row in data:
    total += row.count('#')
print(total)

data = [line.strip() for line in open("input.txt", 'r')]

def canSee(grid, row, col, diagRight, diagUp):
    #if it reaches the end of the grid or empty chair, stop
    if (row < 0) or (row == len(grid)) or (col < 0) or (col == len(grid[0])) or (grid[row][col] == 'L'):
        return 0
    #if it reaches a chair, change
    if grid[row][col] == '#':
        return 1
    return canSee(grid, row + diagRight, col + diagUp, diagRight, diagUp)

def state(grid):
    row, col = len(grid), len(grid[0])
    newGrid = [[grid[x][y] for y in range(col)] for x in range(row)]
    changeHappen = False
    for x in range(row):
        for y in range(col):
            if grid[x][y] == '.':
                continue

            adj = 0
            adj += canSee(grid, x-1, y-1, -1, -1)
            adj += canSee(grid, x-1, y  , -1,  0)
            adj += canSee(grid, x-1, y+1, -1,  1)
            adj += canSee(grid, x  , y-1,  0, -1)
            adj += canSee(grid, x  , y+1,  0,  1)
            adj += canSee(grid, x+1, y-1,  1, -1)
            adj += canSee(grid, x+1, y  ,  1,  0)
            adj += canSee(grid, x+1, y+1,  1,  1)
            
            if grid[x][y] == 'L' and adj == 0:
                changeHappen = True
                newGrid[x][y] = '#'
            elif grid[x][y] == '#' and adj >= 5:
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

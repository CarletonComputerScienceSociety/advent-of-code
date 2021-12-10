import math
data = [[int(y) for y in x] for x in open('input.txt').read().strip().split('\n')]
#https://www.geeksforgeeks.org/flood-fill-algorithm/
#https://www.freecodecamp.org/news/flood-fill-algorithm-explained/

def part1(data):
    ans = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            if x > 0 and data[x][y] >= data[x-1][y]:
                continue
            if x < len(data) - 1 and data[x][y] >= data[x+1][y]:
                continue
            if y > 0 and data[x][y] >= data[x][y-1]:
                continue
            if y < len(data[0]) - 1 and data[x][y] >= data[x][y+1]:
                continue
            ans += data[x][y] + 1
    print(ans)

def part2(data):
    nextTo = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rowSize = len(data)
    colSize = len(data[0])
    def floodfill(row, col):
        height = data[row][col]
        if height == 9:
            return 0
        data[row][col] = 9
        size = 1
        for rowDif, colDif in nextTo:
            if 0 <= row + rowDif < rowSize and 0 <= col + colDif < colSize:
                size += floodfill(row + rowDif, col + colDif)
        return size

    basinSize = []
    for r in range(rowSize):
        for c in range(colSize):
            if data[r][c] != 9:
                basinSize.append(floodfill(r, c))

    print(math.prod(sorted(basinSize)[-3:]))
part1(data)
part2(data)

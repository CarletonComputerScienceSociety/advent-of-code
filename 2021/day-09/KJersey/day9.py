data = [line.strip() for line in open("day9.txt", 'r')]

#Code shamelessly ~~stolen~~ copied from https://lvngd.com/blog/flood-fill-algorithm-python/

def flood_recursive(matrix, start_x, start_y):
    width = len(matrix)
    height = len(matrix[0])
    def fill(x,y):
        if matrix[x][y] == 9:
            return 0
        #if the square is not the new color
        else:
            #update the color of the current square to the replacement color
            matrix[x][y] = 9
            neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            count = 1
            for n in neighbors:
                if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                    count += fill(n[0],n[1])
            return count
    #pick a random starting point
    return fill(start_x, start_y)

counter = 0

tubes = []

lows = []

for line in data:
    row = []
    for c in line:
        row.append(int(c))
    tubes.append(row)

for c1, v1 in enumerate(tubes):
    for c2, v2 in enumerate(tubes[c1]):
        if (c1 == 0 or v2 < tubes[c1 - 1][c2]) and (c1 == len(tubes) - 1 or v2 < tubes[c1 + 1][c2]) and (c2 == 0 or v2 < tubes[c1][c2 - 1]) and (c2 == len(tubes[c1]) - 1 or v2 < tubes[c1][c2 + 1]):
            lows.append([c1, c2])
            counter += v2 + 1

print(counter)

counter = 0

m = []

for low in lows:
    m.append(flood_recursive(tubes[:], low[0], low[1]))

m.sort()
m.reverse()

print(m[0] * m[1] * m[2])
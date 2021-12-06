# file is currently part 1, uncomment lines 32 - 53 for part 2

points = {}

file = open("day5.txt")

for line in file:
    x1 = int(line.strip().split(" -> ")[0].split(",")[0])
    y1 = int(line.strip().split(" -> ")[0].split(",")[1])
    x2 = int(line.strip().split(" -> ")[1].split(",")[0])
    y2 = int(line.strip().split(" -> ")[1].split(",")[1])
    
    largerX = max(x1, x2)
    smallerX = min(x1, x2)
    largerY = max(y1, y2)
    smallerY = min(y1, y2)

    if x1 == x2:
        while smallerY <= largerY:
            if (x1, smallerY) not in points:
                points[(x1, smallerY)] = 1
            else:
                points[(x1, smallerY)] += 1
            smallerY += 1
    elif y1 == y2:
        while smallerX <= largerX:
            if (smallerX, y1) not in points:
                points[(smallerX, y1)] = 1
            else:
                points[(smallerX, y1)] += 1
            smallerX += 1
    ''' elif x1 < x2:
        while x1 <= x2:
            if (x1, y1) not in points:
                points[(x1, y1)] = 1
            else:
                points[(x1, y1)] += 1
            x1 += 1
            if y1 < y2:
                y1 += 1
            else:
                y1 -= 1
    elif x2 < x1:
        while x2 <= x1:
            if (x2, y2) not in points:
                points[(x2, y2)] = 1
            else:
                points[(x2, y2)] += 1
            x2 += 1
            if y2 < y1:
                y2 += 1
            else:
                y2 -= 1 '''

numDangerSpots = 0

for point in points:
    if points[point] >= 2:
        numDangerSpots += 1

print(numDangerSpots)

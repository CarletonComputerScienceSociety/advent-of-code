inf = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

coords = []

for line in inf.split("\n"):
    line = line.split(" ")
    coords.append([line[0], line[2]])

#key is coordinate
#value is number of times its hit
spots = {}

for coord in coords:
    x1 = int(coord[0].split(",")[0])
    x2 = int(coord[1].split(",")[0])
    y1 = int(coord[0].split(",")[1])
    y2 = int(coord[1].split(",")[1])
    if x1 == x2:
        for x in range(max(y2,y1) - min(y2,y1) + 1):
            if (x1, min(y1, y2) + x) not in spots:
                spots[(x1, min(y1, y2) + x)] = 0
            spots[(x1, min(y1, y2) + x)] += 1
    elif y1 == y2:
        for x in range(max(x2,x1) - min(x2,x1) + 1):
            if (min(x1, x2) + x, y1) not in spots:
                spots[(min(x1, x2) + x, y1)] = 0
            spots[(min(x1, x2) + x, y1)] += 1
    elif (max(x1,x2) - min(x1,x2) == max(y1,y2) - min(y1,y2)):
        
        for x in range(max(x1,x2) - min(x1,x2) + 1):
            #going right and up
            if x1 < x2 and y1 < y2:
                if (x1 + x, y1 + x) not in spots:
                    spots[(x1 + x, y1 + x)] = 0
                spots[(x1 + x, y1 + x)] += 1
                #right and down
            elif x1 < x2 and y1 > y2:
                if (x1 + x, y1 - x) not in spots:
                    spots[(x1 + x, y1 - x)] = 0
                spots[(x1 + x, y1 - x)] += 1
                #left and up
            elif x1 > x2 and y1 < y2:
                if (x1 - x, y1 + x) not in spots:
                    spots[(x1 - x, y1 + x)] = 0
                spots[(x1 - x, y1 + x)] += 1
                #left and down
            elif x1 > x2 and y1 > y2:
                if (x1 - x, y1 - x) not in spots:
                    spots[(x1 - x, y1 - x)] = 0
                spots[(x1 - x, y1 - x)] += 1
            

count = 0

for key in spots:
    if spots[key] >= 2:
        count += 1

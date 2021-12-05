from collections import Counter

data = [line.strip() for line in open("input.txt", 'r')]

def part1(data):
    pts = []
    for line in data:
        x1=int(line.split()[0].split(",")[0])
        y1=int(line.split()[0].split(",")[1])

        x2=int(line.split()[2].split(",")[0])
        y2=int(line.split()[2].split(",")[1])
        if x1==x2 or y1==y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                for y in range(min(y1,y2),max(y1,y2)+1):
                    pts.append((x,y))

    print(len([x for (x,y) in Counter(pts).items() if y>1]))

def part2(data):
    pts = []
    for line in data:
        x1=int(line.split()[0].split(",")[0])
        y1=int(line.split()[0].split(",")[1])

        x2=int(line.split()[2].split(",")[0])
        y2=int(line.split()[2].split(",")[1])
        
        overx = 1 if x2>x1 else -1
        overy = 1 if y2>y1 else -1
        if x1 == x2:
            overx = 0
        if y1 == y2:
            overy = 0
        pts.append((x1,y1))
        while x1 != x2 or y1 != y2:
            x1 += overx
            y1 += overy
            pts.append((x1,y1))

    print(len([x for (x,y) in Counter(pts).items() if y>1]))

part1(data)
part2(data)

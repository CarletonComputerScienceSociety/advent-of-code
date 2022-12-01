inf = """input"""
inf2 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

inf = inf.split("\n")
inf2 = inf2.split("\n")

coords = []
instructions = []

for line in inf2:
    if len(line) > 0 and line[0].isnumeric():
        line = line.split(",")
        coords.append([int(line[0]), int(line[1])])
    elif len(line) > 0:
        line = line.split(" ")
        line[2] = line[2].split("=")
        instructions.append((line[2][0], int(line[2][1])))

for count, instruction in enumerate(instructions):
    curr_set = set({})
    if instruction[0] == 'y':
        for coord in range(len(coords)):
            if coords[coord][1] >= instruction[1]:
                coords[coord][1] = abs(coords[coord][1] - instruction[1] - instruction[1])
            curr_set.add((coords[coord][0], coords[coord][1]))
    elif instruction[0] == 'x':
        for coord in range(len(coords)):
            if coords[coord][0] >= instruction[1]:
                coords[coord][0] = abs(coords[coord][0] - instruction[1] - instruction[1])
            curr_set.add((coords[coord][0], coords[coord][1]))
    coords = []
    for coord in curr_set:
        coords.append([coord[0], coord[1]])
    if count == 0:
        print(len(coords))

maxX = 0
maxY = 0

for coord in coords:
    if coord[0] > maxX:
        maxX = coord[0]
    if coord[1] > maxY:
        maxY = coord[1]

for row in range(maxY + 1):
    for col in range(maxX + 1):
        if [col, row] in coords:
            print("#", end="")
        else:
            print(" ", end="")
    print("")


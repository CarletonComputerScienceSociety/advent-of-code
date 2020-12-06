file = open("day_3_input.txt", "r")

forestMap = [line.strip() for line in file.readlines()]


def countTrees(run, rise):
    x = 0
    y = 0
    numTrees = 0
    while y < len(forestMap):
        if x >= len(forestMap[0]):
            x = x - len(forestMap[0])
        if forestMap[y][x] == "#":
            numTrees += 1
        x += run
        y += rise
    return numTrees


print(countTrees(3, 1) * countTrees(1, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))

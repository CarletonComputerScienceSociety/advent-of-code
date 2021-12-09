inf2 = """input"""

inf = """2199943210
3987894921
9856789892
8767896789
9899965678"""

inf = inf.split("\n")

# inf2 = inf2.split("\n")

low = []

def solve1():
    
    for rowNum in range(len(inf)):
        for columnNum in range(len(inf[rowNum])):
            curr = int(inf[rowNum][columnNum])
            if rowNum - 1 >= 0 and int(inf[rowNum - 1][columnNum]) <= curr:
                continue
            if columnNum - 1 >= 0 and int(inf[rowNum][columnNum - 1]) <= curr:
                continue
            if rowNum + 1 < len(inf) and int(inf[rowNum + 1][columnNum]) <= curr:
                continue
            if columnNum + 1 < len(inf[rowNum]) and int(inf[rowNum][columnNum + 1]) <= curr:
                continue
            low.append([curr, (rowNum, columnNum)])

    sum = 0

    for num in low:
        sum += num[0] + 1

    return sum

all_searched = set({})

def bfs(rowNum, columnNum):
    toSearch = [(rowNum, columnNum)]
    size = 0
    searched = set({(rowNum, columnNum)})
    while len(toSearch) != 0:
        size += 1
        currRow = toSearch[0][0]
        currCol = toSearch[0][1]
        currInt = int(inf[currRow][currCol])
        del toSearch[0]
        if currRow - 1 >= 0 and int(inf[currRow - 1][currCol]) < 9 and int(inf[currRow - 1][currCol]) > currInt and (currRow - 1, currCol) not in searched:
            toSearch.append((currRow - 1, currCol))
            searched.add((currRow - 1, currCol))
        if currCol - 1 >= 0 and int(inf[currRow][currCol - 1]) < 9 and int(inf[currRow][currCol - 1]) > currInt and (currRow, currCol - 1) not in searched:
            toSearch.append((currRow, currCol - 1))
            searched.add((currRow, currCol - 1))
        if currRow + 1 < len(inf) and int(inf[currRow + 1][currCol]) < 9 and int(inf[currRow + 1][currCol]) > currInt and (currRow + 1, currCol) not in searched:
            toSearch.append((currRow + 1, currCol))
            searched.add((currRow + 1, currCol))
        if currCol + 1 < len(inf[currRow]) and int(inf[currRow][currCol + 1]) < 9 and int(inf[currRow][currCol + 1]) > currInt and (currRow, currCol + 1) not in searched:
            toSearch.append((currRow, currCol + 1))
            searched.add((currRow, currCol + 1))

    return size

# print(low)

def solve2():
    biggest = []

    for num in low:
        if len(biggest) < 3:
            biggest.append(bfs(num[1][0], num[1][1]))
        else:
            biggest.sort()
            cur = bfs(num[1][0], num[1][1])
            if cur > min(biggest):
                biggest[0] = cur

    # print(biggest)
    return biggest[0] * biggest[1] * biggest[2]

print(solve1())
print(solve2())




def step1(octos):
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            octos[x][y] += 1

def flash(x, y, octos, flashed):
    
    if x > 0:
        octos[y][x-1] += 1
        if octos[y][x-1] > 9 and (y, x-1) not in flashed:
            flashed.append((y, x-1))
            flash(x-1, y, octos, flashed)
    if x > 0 and y > 0:
        octos[y-1][x-1] += 1
        if octos[y-1][x-1] > 9 and (y-1, x-1) not in flashed:
            flashed.append((y-1, x-1))
            flash(x-1, y-1, octos, flashed)
    if y > 0:
        octos[y-1][x] += 1
        if octos[y-1][x] > 9 and (y-1, x) not in flashed:
            flashed.append((y-1, x))
            flash(x, y-1, octos, flashed)
    if x < len(octos)-1 and y > 0:
        octos[y-1][x+1] += 1
        if octos[y-1][x+1] > 9 and (y-1, x+1) not in flashed:
            flashed.append((y-1, x+1))
            flash(x+1, y-1, octos, flashed)
    if x < len(octos)-1:
        octos[y][x+1] += 1
        if octos[y][x+1] > 9 and (y, x+1) not in flashed:
            flashed.append((y, x+1))
            flash(x+1, y, octos, flashed)
    if x < len(octos)-1 and y < len(octos)-1:
        octos[y+1][x+1] += 1
        if octos[y+1][x+1] > 9 and (y+1, x+1) not in flashed:
            flashed.append((y+1, x+1))
            flash(x+1, y+1, octos, flashed)
    if y < len(octos)-1:
        octos[y+1][x] += 1
        if octos[y+1][x] > 9 and (y+1, x) not in flashed:
            flashed.append((y+1, x))
            flash(x, y+1, octos, flashed)
    if x > 0 and y < len(octos)-1:
        octos[y+1][x-1] += 1
        if octos[y+1][x-1] > 9 and (y+1, x-1) not in flashed:
            flashed.append((y+1, x-1))
            flash(x-1, y+1, octos, flashed)

def step2(octos, flashed):
    for y in range(len(octos)):
        for x in range(len(octos[0])):
            if octos[y][x] > 9 and (y, x) not in flashed:
                flashed.append((y, x))
                flash(x, y, octos, flashed)
    return len(flashed)

def step3(octos, flashed):
    for i in flashed:
        octos[i[0]][i[1]] = 0

def challenge1(nums):
    octos = []
    counter = 0
    for y in range(len(nums)):
        octos.append([])
        for x in range(len(nums[0])):
            octos[y].append(int(nums[y][x]))
    for i in range(100):
        step1(octos)
        flashed = []
        counter += step2(octos, flashed)
        step3(octos, flashed)
    return counter


def challenge2(nums):
    octos = []
    counter = 0
    flashing = 0
    for y in range(len(nums)):
        octos.append([])
        for x in range(len(nums[0])):
            octos[y].append(int(nums[y][x]))
    while flashing != 100:
        step1(octos)
        flashed = []
        flashing = step2(octos, flashed)
        step3(octos, flashed)
        counter += 1
    return counter

f = open("Input.txt", 'r')
nums = []
for line in f:
    nums.append(line.strip())
f.close()
print(challenge1(nums))
print(challenge2(nums))

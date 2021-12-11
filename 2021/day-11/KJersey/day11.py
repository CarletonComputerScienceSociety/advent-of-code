data = [line.strip() for line in open("day11.txt", 'r')]

octopi = []
counter = 0

def printOctopi():
    for row in octopi:
        for c in row:
            print(c[0], end = '')
        print()
    print()

def step(inc):
    flashed = False
    c = 0
    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if inc:
                octopi[i][j][0] += 1

            if not octopi[i][j][1] and octopi[i][j][0] > 9:
                flashed = True
                octopi[i][j][1] = True
                c += 1

                if i > 0 and j > 0:
                    octopi[i - 1][j - 1][0] += 1

                if i > 0:
                    octopi[i - 1][j + 0][0] += 1

                if i > 0 and j < len(octopi[i]) - 1:
                    octopi[i - 1][j + 1][0] += 1

                if j > 0:
                    octopi[i + 0][j - 1][0] += 1

                if j < len(octopi[i]) - 1:
                    octopi[i + 0][j + 1][0] += 1

                if i < len(octopi) - 1 and j > 0:
                    octopi[i + 1][j - 1][0] += 1

                if i < len(octopi) - 1:
                    octopi[i + 1][j + 0][0] += 1

                if i < len(octopi) - 1 and j < len(octopi[i]) - 1:
                    octopi[i + 1][j + 1][0] += 1
                
    return c, flashed

for line in data:
    row = []
    for c in line:
        row.append([int(c), False])
    octopi.append(row)

s = 1

while True:
    c, flashed = step(True)

    while flashed:
        c2, flashed = step(False)
        c += c2

    counter += c

    if s == 100:
        print(counter)

    if c == len(octopi) * len(octopi[0]):
        break

    for i in range(len(octopi)):
        for j in range(len(octopi[i])):
            if octopi[i][j][0] > 9:
                octopi[i][j][0] = 0
            octopi[i][j][1] = False

    s += 1

print(s)
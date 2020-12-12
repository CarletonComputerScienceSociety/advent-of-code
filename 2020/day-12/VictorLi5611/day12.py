data = [line.strip() for line in open("input.txt", 'r')]


def solve1(data):
    x, y = 0, 0
    dir = 0
    for line in data:
        action = line[:1]
        arg = int(line[1:])
        if action == 'F':
            if dir % 360 == 0:
                action = 'E'
            if dir % 360 == 90:
                action = 'N'
            if dir % 360 == 180:
                action = 'W'
            if dir % 360 == 270:
                action = 'S'
        if action == 'N':
            y += arg
        if action == 'E':
            x += arg
        if action == 'S':
            y -= arg
        if action == 'W':
            x -= arg
        if action == 'L':
            dir += arg
        if action == 'R':
            dir -= arg
    print("Part 1:", abs(x) + abs(y))

def solve2(data):
    x, y = 0, 0
    wx, wy = 10, 1
    for line in data:
        action = line[:1]
        arg = int(line[1:])
        if action == 'F':
            x += wx * arg
            y += wy * arg
        if action == 'N':
            wy += arg
        if action == 'E':
            wx += arg
        if action == 'S':
            wy -= arg
        if action == 'W':
            wx -= arg
        if action == 'L':
            while arg != 0:
                wx, wy = -wy, wx
                arg -= 90
        if action == 'R':
            while arg != 0:
                wx, wy = wy, -wx
                arg -= 90



    print("Part 2:" , abs(x) + abs(y))

solve1(data)
solve2(data)

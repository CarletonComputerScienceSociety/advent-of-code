import math

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [10, 1]
direction = 90
ship = [0, 0]


def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


for i, value in enumerate(data):
    rule = value[0]
    amount = int(value[1:])

    if rule == "N":
        pos[1] += amount
    elif rule == "S":
        pos[1] -= amount
    elif rule == "E":
        pos[0] += amount
    elif rule == "W":
        pos[0] -= amount
    elif rule == "L":
        x, y = rotate((0, 0), (pos[0], pos[1]), math.radians(amount))
        pos[0] = round(x)
        pos[1] = round(y)
    elif rule == "R":
        x, y = rotate((0, 0), (pos[0], pos[1]), -1 * math.radians(amount))
        pos[0] = round(x)
        pos[1] = round(y)
    elif rule == "F":
        ship[0] += pos[0] * amount
        ship[1] += pos[1] * amount

print(abs(ship[0]) + abs(ship[1]))

# this is for part 2

highestID = 0
allSeats = []
rows = [x for x in range(0, 128)]
cols = [x for x in range(0, 8)]

file = open("day_5_input.txt", "r")

for seat in file.readlines():
    rows = [x for x in range(0, 128)]
    cols = [x for x in range(0, 8)]
    for char in seat[:7]:
        if char == "F":
            rows = rows[:len(rows)//2]
        elif char == "B":
            rows = rows[len(rows)//2:]

    for char in seat[7:]:
        if char == "L":
            cols = cols[:len(cols)//2]
        elif char == "R":
            cols = cols[len(cols)//2:]
    row = rows[0]
    col = cols[0]

    seatID = 8 * row + col
    if seatID > highestID:
        highestID = seatID
    allSeats.append([row, col])

for i in range(128):
    for j in range(8):
        if [i, j] not in allSeats:
            print([i, j])

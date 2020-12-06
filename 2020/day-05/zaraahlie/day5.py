def check(p):
    start = 0
    end = 127
    done = True
    while done:
        for c in p:
            if c == "F":
                end = (start + end) // 2
            elif c == "B":
                start = (start + end)//2 + 1
            else:  
                done = False
    column = checkrow(p[7:], start)
    seatnumb = seatnum(start, column)
    return seatnumb


def checkrow(p, number):
    start = 0
    end = 7
    done = True
    for c in p:
        if c == "L":
            end = (start + end) // 2
        elif c == "R":
            start = (start + end)//2 + 1
    return start

def seatnum(row, column):
    seatnumb = row * 8 + column
    return seatnumb

filein = open("input.txt", "r")
file = filein.read()

passes = file.split()
seatidlist = []
missingidlist = []
highest = 0
for item in passes:
    seatid = check(item)
    if seatid > highest:
        highest = seatid
    seatidlist.append(seatid)

for i in range(0, highest+1):
    if i not in seatidlist:
        missingidlist.append(i)

print(missingidlist)

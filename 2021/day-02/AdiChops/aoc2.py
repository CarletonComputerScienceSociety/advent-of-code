HORIZONTAL = 0
DEPTH = 1
pos = [0,0]

data = [line.strip().split(" ") for line in open("input.txt", 'r')]

for line in data:
    num = int(line[1])
    if line[0]=="up":
        pos[DEPTH] -= num
    elif line[0]=="down":
        pos[DEPTH] += num
    else:
        pos[HORIZONTAL] += num 

print(pos[HORIZONTAL]*pos[DEPTH])

# Part 2

AIM = 2
pos = [0,0,0]

for line in data:
    num = int(line[1])
    if line[0]=="up":
        pos[AIM] -= num
    elif line[0]=="down":
        pos[AIM] += num
    else:
        pos[HORIZONTAL] += num
        pos[DEPTH] += pos[AIM]*num

print(pos[HORIZONTAL]*pos[DEPTH])
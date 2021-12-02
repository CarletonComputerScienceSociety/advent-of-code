data = [line.strip() for line in open("day2.txt", 'r')]

counter = 0
pos = [0, 0, 0]


for i in range(0, len(data)):
    words = data[i].split(" ")
    if words[0] == "forward":
        pos[0] += int(words[1])
        pos[1] += pos[2] * int(words[1])
    elif words[0] == "down":
        pos[2] += int(words[1])
    elif words[0] == "up":
        pos[2] -= int(words[1])

print(pos[0] * pos[1])
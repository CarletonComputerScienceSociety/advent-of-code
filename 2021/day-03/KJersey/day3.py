data = [line.strip() for line in open("day3.txt", 'r')]

counter = 0
pos = [0, 0, 0, 0]

for i in range(len(data[0])):
    for j in range(len(data)):
        if data[j][i] == "0":
            counter += 1
        else:
            counter -= 1

    nums = data
    if counter > 0:
        pos[0] += (0 << (len(data[0]) - i - 1))
        pos[1] += (1 << (len(data[0]) - i - 1))
    else:
        pos[0] += (1 << (len(data[0]) - i - 1))
        pos[1] += (0 << (len(data[0]) - i - 1))

    counter = 0

min = data
max = data

for i in range(len(data[0])):
    for j in range(len(max)):
        if max[j][i] == "0":
            counter += 1
        else:
            counter -= 1

    
    if counter > 0:
        max = list(filter(lambda n: n[i] == "0", max))
    else:
        max = list(filter(lambda n: n[i] == "1", max))

    if len(max) == 1:
        print(max)
        pos[2] = int(max[0], 2)
        break

    counter = 0

for i in range(len(data[0])):
    for j in range(len(min)):
        if min[j][i] == "0":
            counter += 1
        else:
            counter -= 1

    if counter > 0:
        min = list(filter(lambda n: n[i] == "1", min))
    else:
        min = list(filter(lambda n: n[i] == "0", min))

    
    if len(min) == 1:
        print(min)
        pos[3] = int(min[0], 2)
        break

    counter = 0

print(pos[0] * pos[1])
print(pos[2] * pos[3])
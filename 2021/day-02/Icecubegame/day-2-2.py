input = open("input-2.txt", 'r')

x = 0
y = 1
aim = [0, 0]
pos = [0, 0]

for line in input.readlines():
    (command, value) = line.split(" ")
    value = int(value)
    if command == "forward":
        pos[x] += value
        pos[y] += aim[y] * value
    elif command == "down":
        aim[y] += value
    elif command == "up":
        aim[y] -= value
    else:
        print("Command \"" + command + "\" does not exist!")

print(pos[x]*pos[y])

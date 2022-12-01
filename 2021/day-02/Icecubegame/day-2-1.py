input = open("input-2.txt", 'r')

x = 0
y = 0

for line in input.readlines():
    (command, value) = line.split(" ")
    value = int(value)
    if command == "forward":
        x += value
    elif command == "down":
        y += value
    elif command == "up":
        y -= value
    else:
        print("Command \"" + command + "\" does not exist!")

print(x*y)

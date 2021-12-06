with open('input.txt', 'r') as infile:
    instructions = [command.strip() for command in infile.readlines()]

commands = {
    "forward": (0, 1),
    "down": (1, 1),
    "up": (1, -1)
}

position = [0, 0]
for command in instructions:
    instruction = command.split(' ')
    manip = commands[instruction[0]]
    movement = int(instruction[1])
    position[manip[0]] += (movement * manip[1])
print(position[0] * position[1])
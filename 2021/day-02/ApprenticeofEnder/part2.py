with open('D:\\RBFiles\\University\\CCSS\\advent-of-code\\2021\\day-02\\ApprenticeofEnder\\input.txt', 'r') as infile:
    instructions = [command.strip() for command in infile.readlines()]

commands = {
    "forward": (0, 1),
    "down": (1, 1),
    "up": (1, -1)
}

position = [0, 0]
aim = 0
for command in instructions:
    instruction = command.split(' ')
    manip = commands[instruction[0]]
    movement = int(instruction[1])
    if manip[0] == 0:
        position[0] += movement
        position[1] += movement * aim
    else: 
        aim += movement * manip[1]
print(position[0] * position[1])
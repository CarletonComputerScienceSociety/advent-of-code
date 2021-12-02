# Thomas Selwyn
# 02-Dec-2021

commands = []

# Read data input
with open('data/day_2.txt') as data_file:
    read_lines = data_file.readlines()
    data_file.close()

    for current in read_lines:
        commands.append(current.strip())

print(commands)

# PART ONE
# Calculate final position
forward_pos = 0
vertical_pos = 0

for i in range(len(commands)):
    split_string = commands[i].split(" ")
    value = int(split_string[1])

    if split_string[0] == "down":
        vertical_pos -= value
    if split_string[0] == "up":
        vertical_pos += value
    if split_string[0] == "forward":
        forward_pos += value

print("The position is forward {} and vertical {}!".format(forward_pos, vertical_pos))
print("Final answer is " + str(abs(forward_pos) * abs(vertical_pos)))

# PART TWO
# Calculate depth with new aim
horizontal_pos = 0
depth = 0
aim = 0

for i in range(len(commands)):
    split_string = commands[i].split(" ")
    value = int(split_string[1])

    if split_string[0] == "down":
        aim += value
    if split_string[0] == "up":
        aim -= value
    if split_string[0] == "forward":
        horizontal_pos += value
        depth += aim * value

print("The horizontal pos of {}, depth of {}, with aim of {}!".format(horizontal_pos, depth, aim))
print("Final answer is " + str(horizontal_pos * depth))
f = open("input.txt", "r")

file = f.readlines()

current_index = 0
total = 0

for line in file:
  if line[current_index] == "#":
    total = total + 1
  current_index = current_index + 3
  if current_index > 30:
    current_index = current_index - 31
print (total)
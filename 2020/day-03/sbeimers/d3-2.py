inp = open("input.txt", "r")
file = inp.readlines()

def f (num, file):
  current_index = 0
  total = 0

  for line in file:
    if line[current_index] == "#":
      total = total + 1
    current_index = current_index + num
    if current_index > 30:
      current_index = current_index - 31
  print ("right " + str(num) + " down 1: " + str(total))
  return total

current_index = 0
total = 0
cline = 1
for line in file:
  cline = cline + 1
  if (cline % 2 == 0):
    if line[current_index] == "#":
      total = total + 1
    current_index = current_index + 1
    if current_index > 30:
      current_index = current_index - 31
print ("right 1 down 2: " + str(total))

print(total * f(1, file) * f(3, file) * f(5, file) * f(7, file))
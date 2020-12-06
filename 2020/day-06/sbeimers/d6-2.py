f = open("input.txt", "r")
file = f.readlines()
total = 0
cline = 0
current = []
for line in file:
  cline = cline + 1
  if line == "\n":
    total = total + len(current)
    current = []
    cline = 0
  elif cline == 1:
    line = line.strip()
    for char in line:
      current.append(str(char))
  else:
    line = line.strip()
    tempcurrent = []
    for char in line:
      if char in current:
        tempcurrent.append(str(char))
    current = tempcurrent

print (total + len(current))
f = open("input.txt", "r")
file = f.readlines()
total = 0
current = []
for line in file:
  if line == "\n":
    total = total + len(current)
    current = []
  else:
    line = line.strip()
    tempcurrent = []
    for char in line:
      if char not in current:
        current.append(str(char))
print (total + len(current))
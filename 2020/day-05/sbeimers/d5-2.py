f = open("input.txt", "r")
file = f.readlines()

lower = 0
upper = 127
best = 0

l = []

for line in file:
  lower = 0
  upper = 127
  left = 0
  right = 7
  for char in line:
    if char == "F":
      if (lower+upper) % 2 != 0:
        upper = upper - 1
      upper = upper - ((upper - lower) // 2)
    elif char == "B":
      if (lower+upper) % 2 != 0:
        lower = lower + 1
      lower = lower + ((upper - lower) // 2) 
    ############
    elif char == "L":
      if (left+right) % 2 != 0:
        right = right - 1
      right = right - ((right - left) // 2)
    elif char == "R":
      if (left+right) % 2 != 0:
        left = left + 1
      left = left + ((right - left) // 2)
  idd = (upper * 8 + left)
  l.append(idd)
  if idd > best:
    best = idd
l.sort()
last = l[0]
for i in l:
  if i-last == 2:
    print(i)
  last = i
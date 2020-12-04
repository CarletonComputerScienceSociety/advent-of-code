f = open("input.txt", "r")
file = f.readlines()
for line in file:
  x = int(line.strip())
  for j in file:
    y = int(j.strip())
    for k in file:
      z = int(k.strip())
      if (x + y + z == 2020 and x != y and y != z and x != z):
        print(x*y*z)
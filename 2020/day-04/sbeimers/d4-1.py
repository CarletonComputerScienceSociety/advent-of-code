f = open("input.txt", "r")
file = f.readlines()

total = 0

byr = -1
iyr = -1
eyr = -1
hgt = -1
hcl = -1
ecl = -1
pid = -1
cid = -1

for line in file:
  
  if line == "\n":
    if (byr != str(-1) and iyr != str(-1) and eyr != str(-1) and hgt != str(-1) and hcl != str(-1) and ecl != str(-1) and pid != str(-1)):
      total = total + 1
    byr = "-1"
    iyr = "-1"
    eyr = "-1"
    hgt = "-1"
    hcl = "-1"
    ecl = "-1"
    pid = "-1"
    cid = "-1"
  else:
    current = line.split()
    print (current)
    for item in current:
      items = item.split(":")
      print (items)
      if items[0] == "byr":
        byr = str(items[1])
      elif items[0] == "iyr":
        iyr = str(items[1])
      elif items[0] == "eyr":
        eyr = str(items[1])
      elif items[0] == "hgt":
        hgt = str(items[1])
      elif items[0] == "hcl":
        hcl = str(items[1])
      elif items[0] == "ecl":
        ecl = str(items[1])
      elif items[0] == "pid":
        pid = str(items[1])
      elif items[0] == "cid":
        cid = str(items[1])

print (total)
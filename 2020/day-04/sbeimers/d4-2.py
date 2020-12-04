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
      if int(byr) >= 1920 and int(byr) <= 2002:
        if int(iyr) >= 2010 and int(byr) <= 2020:
          if int(eyr) >= 2020 and int(eyr) <= 2030:
            hgt = str(hgt)
            x = hgt.replace ("cm", " c")
            x = x.replace("in", " i")
            x = x.split()
            print("------------------")
            print(x)
            if len(x) == 2:
              if((str(x[1]) == "c" and int(x[0]) >= 150 and int(x[0]) <= 193) or (str(x[1]) == "i" and int(x[0]) >= 59 and int(x[0]) <= 76)):
                hcl = str(hcl)
                if hcl[0] == "#":
                  if len(hcl) == 7:
                    if ((str(hcl[1]) == "a" or str(hcl[1]) == "b" or str(hcl[1]) == "c" or str(hcl[1]) == "d" or str(hcl[1]) == "e" or str(hcl[1]) == "f") or (int(hcl[1]) >= 0 and int(hcl[1]) <= 9)):
                      if ((str(hcl[2]) == "a" or str(hcl[2]) == "b" or str(hcl[2]) == "c" or str(hcl[2]) == "d" or str(hcl[2]) == "e" or str(hcl[2]) == "f") or (int(hcl[2]) >= 0 and int(hcl[2]) <= 9)):
                        if ((str(hcl[3]) == "a" or str(hcl[3]) == "b" or str(hcl[3]) == "c" or str(hcl[3]) == "d" or str(hcl[3]) == "e" or str(hcl[3]) == "f") or (int(hcl[3]) >= 0 and int(hcl[3]) <= 9)):
                          if ((str(hcl[4]) == "a" or str(hcl[4]) == "b" or str(hcl[4]) == "c" or str(hcl[4]) == "d" or str(hcl[4]) == "e" or str(hcl[4]) == "f") or (int(hcl[4]) >= 0 and int(hcl[4]) <= 9)):
                            if ((str(hcl[5]) == "a" or str(hcl[5]) == "b" or str(hcl[5]) == "c" or str(hcl[5]) == "d" or str(hcl[5]) == "e" or str(hcl[5]) == "f") or (int(hcl[5]) >= 0 and int(hcl[5]) <= 9)):
                              if ((str(hcl[6]) == "a" or str(hcl[6]) == "b" or str(hcl[6]) == "c" or str(hcl[6]) == "d" or str(hcl[6]) == "e" or str(hcl[6]) == "f") or (int(hcl[6]) >= 0 and int(hcl[6]) <= 9)):
                                ecl = str(ecl)
                                if (ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth"):
                                  pid = str(pid)
                                  if len(pid) == 9:
                                    count = 0
                                    for i in pid:
                                      if int(i) >= 0 and int(i) <=9:
                                        count = count + 1
                                    if count == 9:
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
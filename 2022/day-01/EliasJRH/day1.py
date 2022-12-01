inf = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""

lines = inf.split("\n")

def solve1():
  max = 0
  cur = 0
  for line in lines:
    if line == "":
      if cur > max:
        max = cur
      cur = 0
    else:
      line = int(line)
      cur += line

  print(max)

def solve2():
  cur = 0
  all = []
  for line in lines:
    if line == "":
      all.append(cur)
      cur = 0
    else:
      line = int(line)
      cur += line

  all.sort(reverse=True)
  print(all[0] + all[1] + all[2])

solve1()
solve2()

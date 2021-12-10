from aoc import AOC

aoc = AOC(year=2021, day=2)
data = aoc.load()

# Part 1

x, y = 0, 0
for command, value in data.parse(r"(\w+) (\d+)"):
  if command == "forward":
    x += value
  if command == "down":
    y += value
  if command == "up":
    y -= value

aoc.p1(x * y)

# Part 2

x, y, aim = 0, 0, 0
for command, value in data.parse(r"(\w+) (\d+)"):
  if command == "forward":
    x += value
    y += aim * value
  if command == "down":
    aim += value
  if command == "up":
    aim -= value

aoc.p2(x * y)

inf = """input"""

inf2 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

nums = []

for line in inf.split("\n"):
    nums.append(line)

horpos = 0
depth = 0
aim = 0

for line in nums:
    arr = line.split()
    if arr[0] == "forward":
        horpos += int(arr[1])
        depth += (aim * int(arr[1]))
    if arr[0] == "up":
        aim -= int(arr[1])
    if arr[0] == "down":
        aim += int(arr[1])

print(depth * horpos)

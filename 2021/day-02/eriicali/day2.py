# part 2

file = open("day2.txt")
aim = 0
horPos = 0
depth = 0
for line in file:
    info = line.split(" ")
    if info[0] == "forward":
        horPos += int(info[1].strip())
        depth += (aim * int(info[1].strip()))
        
    elif info[0] == "down":
        aim += int(info[1].strip())
        
    elif info[0] == "up":
        aim -= int(info[1].strip())
        
print(depth * horPos)
    

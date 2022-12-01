data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
hori = 0
depth = 0
aim = 0

for i, line in enumerate(data):
    words = line.split(" ")
    if (words[0] == "forward"):
        hori += int(words[1])
        depth = depth + (aim * int(words[1]))
    if(words[0] == "down"):
        aim += int(words[1])
    if(words[0] == "up"):
       aim -= int(words[1])

 
print(hori *depth)

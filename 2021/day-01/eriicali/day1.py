# part 1

lastLine = 0
file = open("day1p1.txt")
count = 0
for line in file:
    if int(line.strip()) > lastLine:
        count += 1
    lastLine = int(line.strip())
print(count - 1)


# part 2
file = open("day1p1.txt")
windowSum = 0
i = 0
lastLine = 0
secondLastLine = 0
prevWindowSum = 0
count = 0
for line in file:
    print(line, lastLine, secondLastLine)
    
    if i > 2:
        prevWindowSum = windowSum
        windowSum = int(line.strip()) + int(lastLine.strip()) + int(secondLastLine.strip())
        print(windowSum)
        if windowSum > prevWindowSum:
            count += 1
    secondLastLine = lastLine
    lastLine = line
    i += 1
print(count)

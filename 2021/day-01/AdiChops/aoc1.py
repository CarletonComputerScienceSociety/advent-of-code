# Part 1

data = [int(line.strip()) for line in open("input.txt", 'r')]

counter = 0

inc = 0
dec = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        inc += 1
    elif  data[i] < data[i-1]:
        dec -= 1

print(inc)

# Part 2

lastSum = 0
inc = 0
dec = 0
for i in range(2, len(data)):
    winSum = data[i-2] + data[i-1] + data[i]
    if winSum > lastSum:
        inc+=1
    elif winSum < lastSum:
        dec+=1
    lastSum = winSum
inc -= 1
print(inc)
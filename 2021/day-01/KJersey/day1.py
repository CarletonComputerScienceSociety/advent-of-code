data = [line.strip() for line in open("day1.txt", 'r')]

counter = 0
pos = [0, 0]

num = 3
prev = 0

for i in range(num):
    prev += int(data[i])

for i in range(num, len(data)):
    
    n = prev + int(data[i]) - int(data[i - num])

    if n > prev:
        counter += 1
    prev = n

    

print(counter)
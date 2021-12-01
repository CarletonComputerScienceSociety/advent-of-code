input = open("input-1.txt", 'r')

count = 0

previous = int(input.readline())
for line in input.readlines():
    current = int(line)
    if previous < current:
        count += 1
    previous = current

input.close()
print(count)

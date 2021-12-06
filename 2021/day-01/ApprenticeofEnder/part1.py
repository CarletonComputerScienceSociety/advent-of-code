with open('input.txt', 'r') as infile:
    data = [int(point) for point in infile.readlines()]

increases = 0
for index, point in enumerate(data):
    if index == 0: continue
    if point > data[index - 1]: increases += 1
print(increases)
data = list(map(lambda x : int(x), open("day6.txt", 'r').readline().split(',')))

counter = 256

fish = []

for i in range(9):
    fish.append(data.count(i))


for _ in range(counter):
    n = fish[0]

    for i in range(1, len(fish)):
        fish[i - 1] = fish[i]

    fish[6] += n
    fish[8] = n
    
counter = 0
for n in fish:
    counter += n

print(counter)
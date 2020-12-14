data = [int(x) for x in [line.strip()
                         for line in open("input.txt", 'r')][0].split(",")]

seen = {}
for i, item in enumerate(data):
    seen[item] = i

for i in range(len(data), 30000000):
    if data[i-1] in seen and seen[data[i-1]] != i:
        data.append(i - 1 - seen[data[i-1]])
        seen[data[i-1]] = i-1
    else:
        data.append(0)
        seen[data[i-1]] = i-1

    if i % 3000000 == 0:
        print(i)

print(i, data[-1])

with open("input.txt") as file:
    data = [int(x) for x in file]

incr = 0
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        incr += 1
print(incr)

incr = 0
for i in range(len(data) - 3):
    if sum(data[i : i + 3]) < sum(data[i + 1 : i + 4]):
        incr += 1
print(incr)

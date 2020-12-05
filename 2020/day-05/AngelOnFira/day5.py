data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]

# map_in = {}
# for i, line in enumerate(data):
#     for j, character in enumerate(line):
#         map_in[(j, i)] = character

passports = []
curr = {}

max_id = 0
ids = []
for i, line in enumerate(data):
    l2 = 0
    u2 = 7

    l1 = 0
    u1 = 127
    for char in line:
        # print(l1, u1, l2, u2)
        if char == 'F':
            u1 = int((u1 - l1) / 2) + l1
        elif char == 'B':
            l1 = int((u1 - l1) / 2) + 1 + l1
        elif char == 'L':
            u2 = int((u2 - l2) / 2) + l2
        elif char == 'R':
            l2 = int((u2 - l2) / 2) + 1 + l2

    # print(l1, u1, l2, u2)

    test = l1 * 8 + l2
    if test > max_id:
        max_id = test

    ids.append(test)


print(max_id)

ids.sort()

last = 0
for i in ids:
    if i - last == 2:
        print(i)
    last = i

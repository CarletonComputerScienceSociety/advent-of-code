data = [line.strip() for line in open("input.txt", 'r')]

file = open("input.txt")


line = file.read()

count = 0
pos = [0, 0]

# map_in = {}
# for i, line in enumerate(data):
#     for j, character in enumerate(line):
#         map_in[(j, i)] = character

# ids = []
# for i, line in enumerate(data):
#     pass

for i in line.split("\n\n"):
    b = []
    x = set()
    for line2 in i.split("\n"):
        c = set()
        for char in line2:
            c.add(char)
            # x.add(char)
        b.append(c)

    if len(b) > 1:
        # print(b[0], b[1])
        init = b[0].intersection(b[1])
        # print(init)
        for item in b:
            # print(init, item)
            init = init.intersection(item)
        # print(init)

        len(init)

        count += len(init)
    else:
        count += len(b[0])
        print("113")

    # print(count)
    # print(i)
    # print("-----")

print(count)

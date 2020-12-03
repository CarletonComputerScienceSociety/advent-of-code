data = [line.strip() for line in open("input.txt", 'r')]

counter = 0
pos = [0, 0]

for i, line in enumerate(data):
    a = line.split(" ")
    password = a[-1]

    rule = a[1][0]
    count = a[0]
    c = count.split("-")

    if (password[int(c[0]) - 1] == rule) ^ (password[int(c[1]) - 1] == rule):
        counter += 1

    # if password.count(rule) >= int(c[0]) and password.count(rule) <= int(c[1]):
print(counter)

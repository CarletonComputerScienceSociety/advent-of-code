import re
import datetime
import string


data = [line.strip() for line in open("input.txt", 'r')]

count = 0

print(data[0:20])

ranges = set()
for i, value in enumerate(data[0:20]):
    ranges_in = value.split(": ")[1].split(" or ")
    r1 = int(ranges_in[0].split("-")[0])
    r2 = int(ranges_in[0].split("-")[1])
    r3 = int(ranges_in[1].split("-")[0])
    r4 = int(ranges_in[1].split("-")[1])
    for i in range(r1, r2 + 1):
        ranges.add(i)

    for i in range(r3, r4 + 1):
        ranges.add(i)

new_data = []
for line in data[25:270]:
    bad_ticket = False
    for num in line.split(","):
        if not int(num) in ranges:
            bad_ticket = True
            count += int(num)

    if not bad_ticket:
        new_data.append(line)

# p1 sol
print(count)

count = 0

ranges = {}
for i, value in enumerate(data[0:20]):
    ranges_in = value.split(": ")[1].split(" or ")
    r1 = int(ranges_in[0].split("-")[0])
    r2 = int(ranges_in[0].split("-")[1])
    r3 = int(ranges_in[1].split("-")[0])
    r4 = int(ranges_in[1].split("-")[1])

    ranges[value.split(": ")[0]] = [r1, r2, r3, r4]

tickets = []

for line in new_data:
    count += 1
    ticket = []
    for num in line.split(","):
        ticket.append(int(num))
    tickets.append(ticket)

my_ticket = [int(
    x) for x in "71,127,181,179,113,109,79,151,97,107,53,193,73,83,191,101,89,149,103,197".split(",")]

length = len(new_data)
slim = {}

for range_type, value in ranges.items():
    possible = {}
    for ticket in tickets:
        for i, num in enumerate(ticket):
            if value[0] <= num <= value[1] or value[2] <= num <= value[3]:
                if i not in possible:
                    possible[i] = 0
                possible[i] += 1

    new_slim = []
    for k, v in possible.items():
        if v == length:
            new_slim.append(k)

    slim[range_type] = new_slim

total = 1
print(slim)
for i in range(len(slim.keys())):
    value = 0
    for k, v in slim.items():
        if v != None and len(v) == 1:
            print(k, v)
            if k.startswith("depart"):
                total *= my_ticket[v[0]]
            value = v[0]
            break

    print("")

    for k in slim.keys():
        if slim[k] != None and value in slim[k]:
            slim[k].remove(value)


print(total)

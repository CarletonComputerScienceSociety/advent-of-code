inpt = "739862541"
#part 1
cups = list(map(int,inpt))

for _ in range(100):
    tc = cups[1:4]
    dest = cups[0] - 1
    if dest == 0:
        dest = 9
    while dest in tc:
        dest -= 1
        if dest == 0:
            dest = 9
    new_cups = cups[:1] + cups[4:]
    n_idx = new_cups.index(dest)
    new_cups = new_cups[:n_idx+1] + tc + new_cups[n_idx+1:]
    cups = new_cups[1:] + new_cups[:1]

print("part 1:" , "".join(map(str,cups[cups.index(1)+1:] + cups[:cups.index(1)])))

#part 2
class Group:
    pass

vals = [int(x) for x in list(inpt.strip())] + list(range(10,1000000+1))
groups = [Group() for _ in vals]
for group, other, val in zip(groups, groups[1:] + groups, vals):
    group.right = other
    group.value = val
lookup = {group.value: group for group in groups}

cur = groups[0]
for _ in range(10000000):
    three = cur.right, cur.right.right, cur.right.right.right
    cur.right = three[-1].right
    n = cur.value - 1
    if n == 0:
        n = 1000000
    while n not in range(1, 1000000+1) or any(group.value == n for group in three):
        n -= 1
        if n == 0:
            n = 1000000
    dest = lookup[n]
    three[2].right = dest.right
    dest.right = three[0]
    cur = cur.right

print("part 2:" , lookup[1].right.value * lookup[1].right.right.value)

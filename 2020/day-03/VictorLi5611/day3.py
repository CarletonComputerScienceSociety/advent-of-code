part1 = 0
part2 = 1
l = []
for s in open("input.txt"):
    s = s.strip()
    l.append(s)
r = len(l[0])
b = len(l)

for xi,yi in [(3,1),(1,1),(5,1),(7,1),(1,2)]:
    x , y=0,0
    tree = 0
    while y< b-1:
        x = (x+xi)%r
        y = (y+yi)%b
        if l[y][x] == "#":
            tree += 1


    if (xi,yi) == (3,1):
        part1 = tree
    part2 *= tree

print(part1)
print(part2)

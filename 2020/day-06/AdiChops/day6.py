f= open('inputday6.txt', 'r')
inp_string = f.read()
f.close()
inp_list_groups = inp_string.split("\n\n")

vals = []
big = []
for g in inp_list_groups:
    vals = []
    ppl = list(g.strip())
    for p in ppl:
        if p != '\n':
            vals.append(p)
    vals = set(vals)
    big.append(vals)

total = 0
for b in big:
    total += len(b)

print(total)

# PART 2

vals = []
big = []
for g in inp_list_groups:
    vals = []
    ppl = list(g.strip())
    tot = 1
    for p in ppl:
        if p != '\n':
            vals.append(p)
        else:
            tot += 1
    counted = []
    for v in vals:
        if vals.count(v) == tot and v not in counted:
            counted.append(v)
    big.append(len(counted))

total = 0
for b in big:
    total += b

print(total)


r = open('input.txt','r').read()
data = r.splitlines()
data[1] = data[1].split(',')


#Part 1
found = False
time = int(data[0])
while not found:
    for bus in data[1]:
        if bus != 'x' and time % int(bus) == 0:
            found = True
            print("Part 1:",(time-int(data[0]))*int(bus))
    time = time + 1


#part 2 
#used chinese-remainder-theorem 
#https://brilliant.org/wiki/chinese-remainder-theorem/
def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * (b ** (mx-2) % mx)
        total %= M
    return total

pairs = []
start = int(data[0])
for i, n in enumerate(data[1]):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n-i,n))

print("Part 2:" ,crt(pairs))



data = list(map(lambda x : int(x), open("day7.txt", 'r').readline().split(',')))

def d1(x, x0 = 0):
    return abs(x - x0)

def d2(x, x0 = 0):
    n = abs(x - x0)
    return n * (n + 1) // 2


m = 10000000000
p = 0

s = int(sum(data)/len(data))

for i in range(s - 1, s + 1):
    counter = 0
    for n in data:
        counter += d2(n, i)

    if counter <= m:
        m = counter
        p = i

print(m)
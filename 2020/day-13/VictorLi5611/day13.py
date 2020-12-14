data = [line.strip() for line in open("input.txt", 'r')]

def domask(arg, mask):
    #using bitwize operators 
    arg |= int(mask.replace('X', '0'), 2)
    arg &= int(mask.replace('X', '1'), 2)
    return arg

#https://medium.com/code-python/what-does-the-keyword-yield-do-in-python-94b93b1b45ee
def allmasks(pos, mask):
    if not mask:
        yield 0
    else:
        if mask[-1] == '0':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + pos % 2
        if mask[-1] == '1':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + 1
        if mask[-1] == 'X':
            for m in allmasks(pos // 2, mask[:-1]):
                yield 2*m + 0
                yield 2*m + 1

mem = {}

for line in data:
    op, arg = line.split(' = ')
    if op == 'mask':
        mask = arg
    else:
        pos = int(op[4:-1])

        #part 1
        #mem[pos] = domask(int(arg), mask)

        #part 2
        for m in allmasks(pos, mask):
            mem[m] = int(arg)
print(sum(mem.values()))

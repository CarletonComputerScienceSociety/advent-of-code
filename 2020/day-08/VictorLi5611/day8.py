data = [line.strip().split() for line in open("input.txt", 'r')]

def solve1 (data):
    acc, i = 0, 0
    seen = [False] * len(data)

    while not seen[i]:
        seen[i] = True
        op, arg = data[i]
        arg = int(arg)
        if op == 'acc':
            acc += arg
        elif op == 'jmp':
            i += arg - 1
        i += 1
    
    return acc

def solve2(data):
    def solve(data):
        acc, i = 0, 0
        seen = [False] * len(data)
        while i < len(data) and not seen[i]:
            seen[i] = True
            op, arg = data[i]
            arg = int(arg)
            #if opeator is acc add to arg
            if op == 'acc':
                acc += arg
            #if operator is jump, increase the increments
            elif op == 'jmp':
                i += arg - 1
            i += 1
        #return the valude if we reach the end of the all of the operations
        return acc if i == len(data) else -1

    ans = -1
    for i in range(len(data)):
        #if operation is not a increment
        if data[i][0] != 'acc':
            #for each of the jmp operation, if it starts switching, find acc
            data[i][0] = 'jmp' if data[i][0] == 'nop' else 'nop'
            ans = solve(data)
            data[i][0] = 'jmp' if data[i][0] == 'nop' else 'nop'
        if ans != -1:
            break
    return ans


print(solve1(data))
print(solve2(data))

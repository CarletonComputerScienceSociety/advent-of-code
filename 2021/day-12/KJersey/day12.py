data = [line.strip() for line in open("day12.txt", 'r')]

counter = 0

big = {}
small = {}

for line in data:
    start, end = line.split("-")
    
    if start.isupper():
        if start in big:
            big[start].append(end)
        else:
            big[start] = [end]
    else:
        if start in small:
            small[start].append(end)
        else:
            small[start] = [end]

    if end.isupper():
        if end in big:
            big[end].append(start)
        else:
            big[end] = [start]
    else:
        if end in small:
            small[end].append(start)
        else:
            small[end] = [start]



def genPaths(node, smallVisited, c = 0):
    if node in smallVisited:
        smallVisited[node] += 1
    
    path.append(node)

    if node == "end":
        c += 1
    else:
        if node.isupper():
            search = big
        else:
            search = small

        for newNode in search[node]:
            if newNode in big:
                c = genPaths(newNode, smallVisited, c)
            elif smallVisited[newNode] < 1:
                c = genPaths(newNode, smallVisited, c)
            elif smallVisited[newNode] < 2 and not newNode in ["start", "end"]:
                skip = False
                for n in smallVisited:
                    if not n == newNode and smallVisited[n] == 2:
                        skip = True
                        break
                if not skip:
                    c = genPaths(newNode, smallVisited, c)
                 
    path.pop()

    if node in smallVisited:
        smallVisited[node] -= 1

    return c
    
smallVisited = {}
for n in small:
    smallVisited[n] = 0

path = []
counter = genPaths("start", smallVisited)
print(counter)
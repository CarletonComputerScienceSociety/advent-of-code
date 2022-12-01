inf = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

paths = {}

for line in inf.split("\n"):
    line = line.split("-")
    if line[0] not in paths:
        paths[line[0]] = []
    if line[1] not in paths:
        paths[line[1]] = []
    paths[line[0]].append(line[1])
    paths[line[1]].append(line[0])

for key in paths:
    route = paths[key]
    for x in range(len(route)):
        if route[x] == 'end':
            route[x], route[-1] = route[-1], route[x]
        elif route[x] == 'start':
            route[x], route[0] = route[0], route[x]

pathCount = 0
pathCount2 = 0
curPath = []

def dfs1(node):
    global pathCount
    curPath.append(node)
    route = paths[node]
    for nod in route:
        if nod != 'start' and nod != 'end':
            if nod.islower() and nod not in curPath:
                dfs1(nod)
            elif nod.isupper():
                dfs1(nod)
        if nod == 'end':
            pathCount += 1
            curPath.pop()
            return
    curPath.pop()

def exists_two(path):
    occurs = {}
    for place in path:
        if place.islower():
            if place not in occurs:
                occurs[place] = 0
            occurs[place] += 1

    for key in occurs:
        if occurs[key] == 2:
            return True

def more_than_one(path, nod):
    occurs = {}
    for place in path:
        if place.islower():
            if place not in occurs:
                occurs[place] = 0
            occurs[place] += 1

    return nod not in occurs
    
def dfs2(node):
    global pathCount2
    curPath.append(node)
    route = paths[node]
    for nod in route:
        if nod != 'start' and nod != 'end':
            two = exists_two(curPath)
            if nod.islower():
                if not two:
                    dfs2(nod)
                elif two:
                    if more_than_one(curPath, nod):
                        dfs2(nod)
            elif nod.isupper():
                dfs2(nod)
        if nod == 'end':
            pathCount2 += 1
            curPath.pop()
            return
    curPath.pop()

dfs1('start')
dfs2('start')
print(pathCount)
print(pathCount2)

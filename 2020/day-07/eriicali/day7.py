rules = {}
allColours = []

file = open("day_7_input.txt", "r")


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


for line in file.readlines():
    splitLine = line.strip().split(" ")
    colour = splitLine[0] + " " + splitLine[1]
    rules[colour] = []
    i = 5
    while i < len(splitLine)-1:
        if "no" in splitLine:
            i += 4
            continue
        rules[colour].append(splitLine[i] + " " + splitLine[i+1])
        i += 4

for colour in rules.keys():
    for currentPath in find_all_paths(rules, colour, "shiny gold"):
        allColours += currentPath

print(len(set(allColours)) - 1)

import re

f= open('inputday7.txt', 'r')
inp_string = f.read()
f.close()
inp_list = inp_string.split("\n")

vals = []
big = []
count = 0

# Part 1

colors = {}
for g in inp_list:
    color = g[:g.find(" bags")]
    if g.find("shiny gold") != -1 and color != "shiny gold":
        number = int(g[g.find(" shiny gold")-1])
        colors[color] = number

for i in range(len(inp_list)):
    for g in inp_list:
        for k in colors:
            color = g[:g.find(" bags")]
            if k in g and color not in colors:
                number = int(g[g.find(f' {k}') - 1])
                colors[color] = number * colors[k]
                break

# Part 2
colors = []


def find_children(col, parent_num):
    for g in inp_list:
        color = g[:g.find(" bags contain")]
        results = []
        if color == col:
            results = re.findall("([^,]+)", g)
        for r in results:
            r = r.strip()
            if r.find("contain") != -1:
                r = r[r.find("contain")+len("contain")+1:]
            color = r[r.find(" ") + 1:r.find(" bag")]
            num = r[r.find(f' {color}') - 1]
            if num != 'o':
                number = int(num)*parent_num
                colors.append(number)
                find_children(color, number)


find_children("shiny gold", 1)
print(sum(colors))

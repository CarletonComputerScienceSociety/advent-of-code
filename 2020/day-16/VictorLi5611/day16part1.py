def parse_tickets():
    global rules, nearby, your
    rules = {}
    with open("input.txt") as f:
        while True:
            text = f.readline()
            if text.startswith("\n"):
                break
            k, v = text.split(": ")
            rules[k] = v[:-1].split(" or ")
        for k, v in rules.items():
            v = [tuple(map(int, x.split("-"))) for x in v]            
            rules[k] = v
        f.readline()  
        your = list(map(int, f.readline().split(",")[:-1]))
        f.readline()  
        f.readline()  
        nearby = f.read().splitlines()
        nearby = [tuple(map(int, x.split(","))) for x in nearby]

def is_possible(n, rules):
    for v in rules.values():
        for x, y in v:
            if x <= n <= y:
                return True
    return False

parse_tickets()

impossible = 0

for ticket in nearby:
    for num in ticket:
        if not is_possible(num, rules):
            impossible += num

print(impossible)

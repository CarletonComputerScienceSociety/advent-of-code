import re
#https://www.guru99.com/python-regular-expressions-complete-tutorial.html 

class Operate(int):
    def __mul__(self, b):
        return Operate(int(self) + b)
    def __add__(self, b):
        return Operate(int(self) + b)
    def __sub__(self, b):
        return Operate(int(self) * b)

def solve1(expr):
    expr = re.sub(r"(\d+)", r"Operate(\1)", expr)
    expr = expr.replace("*", "-")
    return eval(expr, {}, {"Operate": Operate})

def solve2(expr):
    expr = re.sub(r"(\d+)", r"Operate(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, {"Operate": Operate})


data = open('input.txt').read().splitlines()
print("Part 1:", sum(solve1(line) for line in data))
print("Part 2:", sum(solve2(line) for line in data))

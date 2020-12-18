from copy import deepcopy
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

def match_brackets(s):
	stack = [[]]
	for c in s:
		if c == "(":
			new = []
			stack[-1].append(new)
			stack.append(new)
		elif c == ")":
			if len(stack) == 1:
				return False, "unmatched close bracket"
			stack = stack[:-1]
		elif len(stack[-1]) == 0:
			stack[-1].append(c)
		elif isinstance(stack[-1][-1], list):
			stack[-1].append(c)
		else:
			stack[-1][-1] += c
	if len(stack) > 1:
		return False, "unmatched open bracket"
	return stack[0]

def tokenize(expr):
	result = []
	for tk in expr:
		if isinstance(tk, list):
			result.append(tokenize(tk))
		else:
			tokens = tk.split(" ")
			for tk in tokens:
				if not tk: pass
				elif tk.isdigit(): result.append(int(tk))
				else: result.append(tk)
	return result

exprs = []
for line in lines:
	matched = match_brackets(line)
	expr = tokenize(matched)
	exprs.append(expr)

def resolve(tk, evaluater):
	if isinstance(tk, list):
		return evaluater(tk)
	return tk

def evaluate(expr):
	while len(expr) > 1:
		op = expr[1]
		arg0 = resolve(expr[0], evaluate)
		arg1 = resolve(expr[2], evaluate)
		if op == "+":
			result = arg0 + arg1
		elif op == "*":
			result = arg0 * arg1
		else:
			print(op)
			assert False
		del expr[2]
		del expr[0]
		expr[0] = result
	return expr[0]

def evaluate2(expr):
	while len(expr) > 1:
		chosen = None
		chosen_idx = None
		for i, tk in enumerate(expr):
			if chosen == None and tk == "*":
				chosen = tk
				chosen_idx = i
			elif (chosen == None or chosen == "*") and tk == "+":
				chosen = tk
				chosen_idx = i
		arg0 = resolve(expr[chosen_idx - 1], evaluate2)
		arg1 = resolve(expr[chosen_idx + 1], evaluate2)
		if chosen == "+":
			result = arg0 + arg1
		elif chosen == "*":
			result = arg0 * arg1
		else: assert False
		del expr[chosen_idx + 1]
		del expr[chosen_idx - 1]
		expr[chosen_idx - 1] = result
	return expr[0]

x = 0
y = 0
for expr in exprs:
	x += evaluate(deepcopy(expr))
	y += evaluate2(deepcopy(expr))
print(x)
print(y)
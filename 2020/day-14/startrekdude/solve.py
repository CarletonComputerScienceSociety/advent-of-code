import re

from collections import defaultdict, namedtuple
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

MASK_X = "X"
MASK_0 = "0"
MASK_1 = "1"

def apply_mask(val, mask):
	for i, c in enumerate(mask):
		i = 35 - i
		m = 1 << i
		if c == MASK_0:
			val &= ~m
		elif c == MASK_1:
			val |= m
	return val

Op = namedtuple("Op", ("loc", "val"))

op_match = re.compile(r"mem\[(\d+)\] = (\d+)")
def assemble(lines):
	ops = []
	for line in lines:
		if line.startswith("mask"):
			ops.append(line[7:])
			continue
		match = op_match.match(line)
		ops.append(Op(int(match.group(1)), int(match.group(2))))
	return ops

ops = assemble(lines)

def execprog1(ops, vm):
	mask = "X" * 36
	for op in ops:
		if isinstance(op, str):
			mask = op
			continue
		vm[op.loc] = apply_mask(op.val, mask)

vm = defaultdict(lambda: 0)
execprog1(ops, vm)

print(sum(vm.values()))

def apply_loc_mask(loc, mask):
	loc = list("{:036b}".format(loc))
	for i, c in enumerate(mask):
		if c == MASK_1 or c == MASK_X:
			loc[i] = c
	
	floating_count = loc.count("X")
	if floating_count == 0:
		yield int("".join(loc), 2)
		return
	
	for i in range(2**floating_count):
		binary = ("{:0" + str(floating_count) + "b}").format(i)
		j = 0
		new_loc = loc.copy()
		for i, c in enumerate(loc):
			if c == MASK_X:
				new_loc[i] = binary[j]
				j += 1
		yield int("".join(new_loc), 2)

def execprog2(ops, vm):
	mask = None
	for op in ops:
		if isinstance(op, str):
			mask = op
			continue
		for loc in apply_loc_mask(op.loc, mask):
			vm[loc] = op.val

vm = defaultdict(lambda: 0)
execprog2(ops, vm)

print(sum(vm.values()))
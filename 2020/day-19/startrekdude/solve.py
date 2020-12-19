import re

from enum import Enum
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

class RuleType(Enum):
	LITERAL = 1
	SEQUENCE = 2
	ANY = 3

class Rule:
	def __init__(self, type, data):
		self.type = type
		self.data = data
	def __repr__(self):
		return "Rule({!r}, {!r})".format(self.type, self.data)
	def to_re(self):
		if self.type == RuleType.LITERAL:
			return self.data
		elif self.type == RuleType.SEQUENCE:
			return "".join(rules[i].to_re() for i in self.data)
		elif self.type == RuleType.ANY:
			return "({}|{})".format(rules[self.data[0]].to_re(), rules[self.data[1]].to_re())

rules = {}
i = -1
while line := lines.pop(0):
	num, line = line.split(":")
	line = line[1:]
	num = int(num)
	
	if line.startswith('"'):
		rules[num] = Rule(RuleType.LITERAL, line.replace('"', ''))
	elif "|" in line:
		sub_rules = [s.strip() for s in line.split("|")]
		data = []
		for sub in sub_rules:
			seq = [int(x) for x in sub.split(" ")]
			rules[i] = Rule(RuleType.SEQUENCE, seq)
			data.append(i)
			i -= 1
		rules[num] = Rule(RuleType.ANY, data)
	else:
		seq = [int(x) for x in line.split(" ")]
		rules[num] = Rule(RuleType.SEQUENCE, seq)

re_str = "^" + rules[0].to_re() + "$"
rules_match = re.compile(re_str)

count = 0
for line in lines:
	match = rules_match.match(line)
	if match:
		count += 1
print(count)

def count_matches(regex, line):
	count = 0
	while match := regex.match(line):
		start, end = match.span()
		line = line[end:]
		count += 1
	return count, line

r42 = re.compile("^" + rules[42].to_re())
r31 = re.compile("^" + rules[31].to_re())
count = 0
for line in lines:
	x42, rest = count_matches(r42, line)
	x31, rest = count_matches(r31, rest)
	valid = rest == "" and x42 > x31 and x31 >= 1 and x42 >= 2
	if valid: count += 1
print(count)
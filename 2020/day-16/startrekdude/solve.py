import re

from collections import defaultdict, namedtuple
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

FieldRule = namedtuple("FieldRule", ("name", "ranges"))

range_match = re.compile(r"(\d+)-(\d+)")
rules = []
while (line := lines.pop(0)) != "":
	name, rest = line.split(":")
	ranges = []
	for match in range_match.finditer(rest):
		ranges.append((int(match.group(1)), int(match.group(2))))
	rules.append(FieldRule(name, tuple(ranges)))

tickets = []
for line in lines:
	if line and line[0].isdigit():
		tickets.append(tuple(int(s) for s in line.split(",")))

invalid_sum = 0
invalid_tickets = []
for ticket in tickets:
	for x in ticket:
		valid = False
		for rule in rules:
			for rrange in rule.ranges:
				if rrange[0] <= x <= rrange[1]:
					valid = True
		if not valid:
			invalid_sum += x
			invalid_tickets.append(ticket)
print(invalid_sum)

tickets = [x for x in tickets if x not in invalid_tickets]

possible_indices = defaultdict(set)
for i in range(len(tickets[0])):
	for rule in rules:
		rule_valid = True
		for ticket in tickets:
			x = ticket[i]
			x_valid = False
			for interval in rule.ranges:
				if interval[0] <= x <= interval[1]:
					x_valid = True
					break
			if not x_valid:
				rule_valid = False
				break
		if rule_valid:
			possible_indices[rule.name].add(i)

assigned_indices = set()
indices = {}
while len(possible_indices):
	to_delete = []
	for rule in possible_indices:
		possible = possible_indices[rule]
		possible -= assigned_indices
		if len(possible) == 1:
			indices[rule], = possible
			to_delete.append(rule)
			assigned_indices.add(indices[rule])
	for key in to_delete:
		del possible_indices[key]

my_ticket = tickets[0]
departure_product = 1
for rule, index in indices.items():
	if rule.startswith("departure"):
		departure_product *= my_ticket[index]
print(departure_product)
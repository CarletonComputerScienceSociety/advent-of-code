import re

from collections import namedtuple
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

all_nodes = {}

ChildRef = namedtuple("ChildRef", ("name", "count"))

class Node:
	def __init__(self, name, refs):
		self.name = name
		self.refs = refs
	@property
	def children(self):
		return [(all_nodes[name], count) for name, count in self.refs]
	def __repr__(self):
		return "Node({!r}, {!r})".format(self.name, self.refs)

bag_rule = re.compile(r"(\d)+ (.+?) bag")

def parse_bag_rule(rule):
	root, stem = rule.split(" bags contain ")
	refs = []
	for match in bag_rule.finditer(stem):
		refs.append(ChildRef(match.group(2), int(match.group(1))))
	
	node = Node(root, refs)
	all_nodes[root] = node
	return node

for line in lines:
	parse_bag_rule(line)

def dfs(src, dest):
	if src is dest:
		return 0
	for child, count in src.children:
		if (i := dfs(child, dest)) > -1:
			return i + 1
	return -1

count = 0
for name, node in all_nodes.items():
	if name != "shiny gold":
		val = dfs(node, all_nodes["shiny gold"])
		if val > -1: count += 1

print(count)

def count_children(node):
	overall = 0
	for child, count in node.children:
		overall += (count_children(child) + 1) * count
	return overall

print(count_children(all_nodes["shiny gold"]))

import os.path
import subprocess

from io import BytesIO
from itertools import islice
from os import chdir, listdir, mkdir
from os.path import splitext
from shutil import rmtree
from subprocess import check_output
from sys import argv as args, exit

from PIL import Image

class Node:
	def __init__(self, id, refs, graph):
		self.id = id
		self.refs = refs
		self.graph = graph
		self.value = None
	def __repr__(self):
		return "Node({!r}, {!r})".format(self.id, self.refs)
	@property
	def children(self):
		return [self.graph[ref] for ref in self.refs]

class Graph(dict):
	def new_node(self, id, refs):
		self[id] = Node(id, refs, self)
		return self[id]

def load_jolts(path):
	with open(path) as f:
		jolts = sorted(int(s) for s in f)
	return [0] + jolts + [jolts[-1] + 3]

def jolts_to_graph(jolts):
	graph = Graph()
	joltset = set(jolts)
	for jolt in reversed(jolts):
		refs = tuple(x for x in range(jolt+3, jolt, -1) if x in joltset)
		graph.new_node(jolt, refs)
	return graph

def viz_frame(graph, msg, hl1=None, hl2=None):
	s = [
		"digraph G {",
		'size="192,108!"',
		"dpi=10",
		"overlap=false",
		'lp="180,90"',
		"node [penwidth=2]",
		"edge [penwidth=2]",
	]
	label = msg.replace("\n", "<br/>")
	label = 'label=<<font face="Open Sans" point-size="48">{}</font>>'.format(label)
	s.append(label)
	
	for node in reversed(graph.values()):
		properties = {}
		if node is hl1:
			properties["color"] = "red"
		elif node is hl2:
			properties["color"] = "blue"
		
		label = '<<font face="Open Sans" point-size="36">{}<br/><font point-size="24"><b>{{}}</b></font></font>>'.format(node.id)
		if node.value:
			properties["label"] = label.format("Value {}".format(node.value))
		else:
			properties["label"] = label.format("&nbsp;"*15)
		
		x = "{} [".format(node.id)
		for k, v in properties.items():
			x += "{}={};".format(k, v)
		x += "]"
		s.append(x)
		
		for ref in node.refs:
			s.append("{} -> {} [color={}]".format(node.id, ref, "blue" if node is hl1 and hl2 and ref == hl2.id else "black"))
	s.append("}")
	return "\n".join(s)

def out_frame(graph, msg, hl1=None, hl2=None):
	path = "tmp/{:05d}.dot".format(out_frame.index)
	out_frame.index += 1
	with open(path, "w") as f:
		f.write(viz_frame(graph, msg, hl1, hl2))
out_frame.index = 0

def solve(graph):
	def make_message(lines, counter):
		new_lines = lines.copy()
		new_lines.insert(1, "Running total: {}".format(counter))
		return "\n".join(new_lines)
	
	first = next(iter(graph.values()))
	first.value = 1
	
	for node in islice(graph.values(), 1, None):
		counter = 0
		lines = ["Processing {}...".format(node.id)]
		out_frame(graph, make_message(lines, counter), hl1=node)
		lines.append("Summing paths...")
		
		for parent in node.children:
			lines.append("    Adding {} from {}".format(parent.value, parent.id))
			counter += parent.value
			out_frame(graph, make_message(lines, counter), hl1=node, hl2=parent)
		node.value = counter
		
		lines.append("Value for {}: {}".format(node.id, node.value))
		out_frame(graph, make_message(lines, counter), hl1=node)
	
	return counter

def render_graphs():
	names = listdir("tmp")
	images = []
	largest_y = 0
	
	for i, name in enumerate(names):
		print("\r       \r{}/{}".format(i+1, len(names)), end="")
		
		root, ext = splitext(name)
		path = os.path.join("tmp", name)
		dest = os.path.join("tmp", root + ".png")
		
		data = check_output(["dot", "-Tpng", "-Kcirco", path])
		img = Image.open(BytesIO(data))
		images.append((dest, img))
		largest_y = max(largest_y, img.size[1])
	print()
	
	yloc = (1080 - largest_y) // 2
	i = 0
	for dest, img in images:
		print("\r     \r{}".format(i), end="")
		i += 1
		
		im = Image.new("RGB", (1920, 1080), (255, 255, 255))
		im.paste(img, (0, yloc))
		im.save(dest)

def to_video(dest):
	chdir("tmp")
	subprocess.call(["ffmpeg", "-r", "1", "-i", "%05d.png", "-filter:v", "fps=1", "-c:v", "libx264",
		"-crf", "18", "-movflags", "faststart", "../"+dest])

def main():
	if len(args) < 3:
		print("Usage: viz <input.txt> <vid.mp4>")
		exit(-1)
	
	rmtree("tmp", ignore_errors=True)
	mkdir("tmp")
	
	path = args[1]
	vid = args[2]
	
	jolts = load_jolts(path)
	graph = jolts_to_graph(jolts)
	solution = solve(graph)
	print("Solution: {}".format(solution))
	
	render_graphs()
	to_video(vid)

if __name__ == "__main__":
	main()
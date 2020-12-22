from collections import defaultdict
from copy import deepcopy
from math import sqrt
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n\n")

tiles = {}
for data in lines:
	data = data.split("\n")
	id = int(data[0][5:9])
	rows = [list(row) for row in data[1:]]
	tiles[id] = rows

def all_edges(tile):
	return set((
		"".join(tile[0]),
		"".join(tile[-1]),
		"".join(row[0] for row in tile),
		"".join(row[-1] for row in tile),
	))

def all_edges_and_rotations(tile):
	edges = all_edges(tile)
	result = set()
	for edge in edges:
		result.add(edge)
		result.add(edge[::-1])
	return result

class Tile:
	def __init__(self, id, rotation):
		self.id = id
		self.rotation = rotation
		self.top = None
		self.bottom = None
		self.left = None
		self.right = None
	def __repr__(self):
		return "Tile({!r}, {!r}, {!r}, {!r}, {!r}, {!r})".format(self.id,
			self.rotation, self.top, self.bottom, self.left, self.right)

border_count = defaultdict(lambda: 0)
connections = defaultdict(list)
for id, tile in tiles.items():
	edges = all_edges(tile)
	
	for partner_id, partner_tile in tiles.items():
		if id == partner_id: continue
		
		partner_edges = all_edges_and_rotations(partner_tile)
		for edge in edges:
			if any(partner_edge == edge for partner_edge in partner_edges):
				border_count[id] += 1
				connections[id].append(partner_id)

product = 1
corners = []
for k, v in border_count.items():
	if v == 2:
		product *= k
		corners.append(k)
print(product)

def rotations(tile):
	return (
		tile,
		tile[::-1],
		[[tile[j][i] for j in range(len(tile))] for i in range(len(tile))],
		[[tile[j][i] for j in range(len(tile))] for i in range(len(tile))][::-1],
	)

def rotations_and_flips(tile):
	data = rotations(tile)
	result = []
	for option in data:
		result.append(option)
		result.append(option[::-1])
		result.append([row[::-1] for row in option])
	return result

def place_all_tiles(r):
	graph = {}
	graph[k] = Tile(k, r)
	remaining_tiles = deepcopy(tiles)
	del remaining_tiles[k]

	while len(remaining_tiles) > 0:
		found = False
		for id in remaining_tiles:
			for conn in connections[id]:
				if conn in graph:
					found = True
					break
			if found:
				break
		
		current = rotations_and_flips(tiles[conn])[graph[conn].rotation]
		for i, rotation in enumerate(rotations_and_flips(tiles[id])):
			if "".join(rotation[0]) == "".join(current[-1]):
				graph[conn].bottom = id
				node = Tile(id, i)
				node.top = conn
				graph[id] = node
				del remaining_tiles[id]
				break
			elif "".join(rotation[-1]) == "".join(current[0]):
				graph[conn].top = id
				node = Tile(id, i)
				node.bottom = conn
				graph[id] = node
				del remaining_tiles[id]
				break
			elif "".join(row[0] for row in rotation) == "".join(row[-1] for row in current):
				graph[conn].right = id
				node = Tile(id, i)
				node.left = conn
				graph[id] = node
				del remaining_tiles[id]
				break
			elif "".join(row[-1] for row in rotation) == "".join(row[0] for row in current):
				graph[conn].left = id
				node = Tile(id, i)
				node.right = conn
				graph[id] = node
				del remaining_tiles[id]
				break
	return graph

def conncalc(node):
	result = [node.left, node.top, node.bottom, node.right]
	return [c for c in result if c != None]

jigsaw_length = int(sqrt(len(tiles)))
def try_build_jigsaw(graph, corner):
	jigsaw = [([None] * jigsaw_length) for _ in range(jigsaw_length)]
	
	locations = {}
	locations[corner] = (0, 0)
	to_place = conncalc(graph[corner])
	
	while to_place:
		id = to_place.pop()
		if id in locations: continue
		
		node = graph[id]
		to_place.extend(conncalc(node))
		
		if node.left and node.left in locations:
			loc = locations[node.left]
			locations[id] = (loc[0], loc[1] + 1)
		elif node.right and node.right in locations:
			loc = locations[node.right]
			locations[id] = (loc[0], loc[1] - 1)
		elif node.bottom and node.bottom in locations:
			loc = locations[node.bottom]
			locations[id] = (loc[0] - 1, loc[1])
		elif node.top and node.top in locations:
			loc = locations[node.top]
			locations[id] = (loc[0] + 1, loc[1])
	
	try:
		for id, (y, x) in locations.items():
			assert 0 <= y < jigsaw_length
			assert 0 <= x < jigsaw_length
			jigsaw[y][x] = rotations_and_flips(tiles[id])[graph[id].rotation]
	except:
		return False
	
	return jigsaw

graph = place_all_tiles(0)
jigsaw = None
for corner in corners:
	result = try_build_jigsaw(graph, corner)
	if result:
		jigsaw = result
		break

def print_jigsaw(jigsaw):
	for row in jigsaw:
		for y in range(10):
			for tile in row:
				print("".join(tile[y]) + " ", end="")
			print()
		print()

def remove_borders(jigsaw):
	result = ""
	for row in jigsaw:
		for y in range(1,9):
			for tile in row:
				result += "".join(tile[y][1:9])
			result += "\n"
	return result[:-1]

picture = remove_borders(jigsaw)
picture = [list(line) for line in picture.split("\n")]
pictures = rotations_and_flips(picture)

with open("sea_monster.txt") as f:
	monster_image = [list(line) for line in f.read().split("\n")]

def print_picture(picture):
	for row in picture:
		print("".join(row))

progress_total = 8 * jigsaw_length * 12
progress = 0

def find_sea_monsters(picture):
	global progress
	pic_with_monsters = deepcopy(picture)
	monster_count = 0
	
	for y in range(len(picture)):
		for x in range(len(picture[y])):
			
			monster = True
			pic_with_monster = deepcopy(pic_with_monsters)
			
			for ydelta, row in enumerate(monster_image):
				for xdelta, c in enumerate(row):
					y_check = y + ydelta
					x_check = x + xdelta
					if y_check not in range(len(picture)) or x_check not in range(len(picture[y])):
						monster = False
						break
					
					if c == " ": continue
					
					if c == "#" and picture[y_check][x_check] == "#":
						pic_with_monster[y_check][x_check] = "O"
					elif c == "#":
						monster = False
						break
					
				if not monster: break
			if monster:
				monster_count += 1
				pic_with_monsters = pic_with_monster
		progress += 1
		print("\r              \r{}/{}".format(progress, progress_total), end="")
	return monster_count, pic_with_monsters

best_pic = None
best_count = 0
for i in range(len(pictures)):
	count, pic = find_sea_monsters(pictures[i])
	
	if count > best_count:
		best_count = count
		best_pic = pic

print("\r                 \r{}".format("".join("".join(row) for row in best_pic).count("#")))
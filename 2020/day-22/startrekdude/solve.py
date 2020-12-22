from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

lines = lines[1:]

def read_cards(lines):
	cards = []
	while line := lines.pop(0):
		cards.append(int(line))
	return cards

p1_start = read_cards(lines)
lines = lines[1:]
p2_start = read_cards(lines)

p1 = p1_start.copy()
p2 = p2_start.copy()

def play_round(p1, p2):
	card1 = p1.pop(0)
	card2 = p2.pop(0)
	if card1 > card2:
		p1.append(card1)
		p1.append(card2)
	else:
		p2.append(card2)
		p2.append(card1)

while p1 and p2:
	play_round(p1, p2)

def calculate_score(deck):
	score = 0
	for i, v in enumerate(reversed(deck)):
		score += v * (i + 1)
	return score

if p1:
	score = calculate_score(p1)
else:
	score = calculate_score(p2)

print(score)


p1 = p1_start.copy()
p2 = p2_start.copy()

def rec_combat(p1, p2):
	previous_rounds = set()
	while p1 and p2:
		key = (tuple(p1), tuple(p2))
		if key in previous_rounds:
			return 1
		previous_rounds.add(key)
		
		card1 = p1.pop(0)
		card2 = p2.pop(0)
		if len(p1) >= card1 and len(p2) >= card2:
			copy1 = p1[:card1]
			copy2 = p2[:card2]
			winner = rec_combat(copy1, copy2)
			if winner == 1:
				p1.append(card1)
				p1.append(card2)
			else:
				p2.append(card2)
				p2.append(card1)
		elif card1 > card2:
			p1.append(card1)
			p1.append(card2)
		else:
			p2.append(card2)
			p2.append(card1)
	if p1: return 1
	if p2: return 2

rec_combat(p1, p2)
if p1:
	score = calculate_score(p1)
else:
	score = calculate_score(p2)
print(score)
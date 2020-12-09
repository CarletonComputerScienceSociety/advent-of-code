from itertools import combinations
from sys import argv as args, exit

path = args[1]
lookback = int(args[2])
with open(path) as f:
	lines = f.read().split("\n")

ct = [int(line) for line in lines]

def first_invalid_num(ct):
	for i in range(lookback,len(ct)):
		buf = ct[i-lookback:i]
		found = False
		z = ct[i]
		
		for x, y in combinations(buf, 2):
			if x + y == z:
				found = True
				break
		
		if not found:
			return z

invalid = first_invalid_num(ct)
print(invalid)

for start in range(len(ct)):
	for end in range(start+1,len(ct)):
		buf = ct[start:end]
		z = sum(buf)
		if z == invalid:
			print(min(buf) + max(buf))
			exit(0)
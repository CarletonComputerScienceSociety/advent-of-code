from collections import namedtuple
from functools import reduce
from operator import and_
from sys import argv as args

path = args[1]
with open(path) as f:
	lines = f.read().split("\n")

Food = namedtuple("Food", ("ingredients", "allergens"))

foods = set()
ingredients = set()
allergens = set()

for line in lines:
	stem, leaf = line.split("(")
	ingredient = tuple(stem.split(" ")[:-1])
	allergen = tuple(leaf[9:-1].split(", "))
	for ing in ingredient: ingredients.add(ing)
	for alg in allergen: allergens.add(alg)
	foods.add(Food(ingredient, allergen))

def first(x):
	return next(iter(x))

forward = {}
reverse = {}

assigned = True
while assigned:
	assigned = False
	for alg in allergens:
		if alg in forward: continue
		
		foods_with = tuple(food for food in foods if alg in food.allergens)
		common = reduce(and_, (set(food.ingredients) for food in foods_with))
		common -= set(reverse.keys())
		if len(common) == 1:
			forward[alg] = first(common)
			reverse[first(common)] = alg
			assigned = True

safe_count = 0
for food in foods:
	for ing in food.ingredients:
		if ing not in reverse:
			safe_count += 1
print(safe_count)

print(",".join(x[1] for x in sorted(forward.items())))
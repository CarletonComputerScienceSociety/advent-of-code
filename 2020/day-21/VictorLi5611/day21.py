import collections
# https://stackabuse.com/lambda-functions-in-python/#:~:text=In%20Python%2C%20a%20lambda%20function%20is%20a%20single-line,is%20passed%20as%20an%20argument%20to%20another%20function.
# https://www.geeksforgeeks.org/python-collections-module/

ALL_INGRED = collections.Counter()
POSSIBLE_INGRED = collections.defaultdict(set)

for line in open("input.txt").read().splitlines():
    ingredients, allergy = line.rstrip(")").split(" (contains ")
    ingredients = ingredients.split()
    allergy = allergy.split(", ")
    ALL_INGRED.update(ingredients)
    
    for allergen in allergy:
        if not POSSIBLE_INGRED[allergen]:
            POSSIBLE_INGRED[allergen] = set(ingredients)
        else:
            POSSIBLE_INGRED[allergen] &= set(ingredients)

fixed = {}
while POSSIBLE_INGRED:
    allergen, ingredients = min(POSSIBLE_INGRED.items(), key=lambda el: len(el[1]))
    fixed[allergen] = list(ingredients)[0]
    for other in POSSIBLE_INGRED.values():
        other -= {fixed[allergen]}
    del POSSIBLE_INGRED[allergen]

print("part1:", sum(ALL_INGRED[i] for i in ALL_INGRED if i not in fixed.values()))
print("part2:", ",".join([ingredient for _, ingredient in sorted(fixed.items())]))

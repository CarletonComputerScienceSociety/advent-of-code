import re
import datetime
import string

alphabet_lower = string.ascii_lowercase

data = [line.strip() for line in open("input.txt", 'r')]

count = 0
pos = [0, 0]


rules = {}
ids = []
first = ""


def recurse2(rules, search, price):
    if len(rules[search].items()) == 0:
        return price

    counter = 0
    for k, v in rules[search].items():
        counter += int(recurse2(rules, k, int(v)))

    return counter * price + price


def recurse(rules, search):
    # print(search)
    if len(rules[search].items()) == 0:
        # print(search)
        return False
    if "shiny gold" in rules[search].keys():
        return True

    for thing in rules[search].keys():
        if recurse(rules, thing):
            return True

    return False


for i, line in enumerate(data):

    args = line.split(", ")

    for j, rule in enumerate(args):
        end = re.search(r'(.* .*) bags contain no other bags.', rule)
        if end is not None:
            rules[end.groups(1)[0]] = {}
            continue

        if j == 0:
            groups = re.search(r'(.* .*) bags contain (.*) (.* .*) .*', rule)
            first = groups.group(1)
            num = groups.group(2)
            second = groups.group(3)
            rules[first] = {
                second: num
            }
        else:
            groups = re.search(r'(.*) (.* .*) .*', rule)
            num = groups.group(1)
            second = groups.group(2)
            rules[first][second] = num

for item in rules:
    if recurse(rules, item):
        count += 1


print(count)
print(recurse2(rules, "shiny gold", 1) - 1)

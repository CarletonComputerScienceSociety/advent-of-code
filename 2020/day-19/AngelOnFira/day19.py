import re

data = [line.strip() for line in open("input.txt", 'r')]

count = 0

rules = {}
for i, value in enumerate(data[0:134]):
    line = value.split(": ")
    if "a" in line[1] or "b" in line[1]:
        rules[line[0]] = " {a} ".format(a=line[1].replace('"', ""))
    else:
        rules[line[0]] = "( {a} )".format(a=line[1].replace(' ', "  "))

# Comment out for p1
rules['8'] = "(  42  |  42  8  )"
rules['11'] = "(  42  31  |  42  11  31  )"

todo_list = [key for key in rules.keys()]

while True:
    for_removal = []

    for key in todo_list:
        bad_count = 0
        this_in = rules[key].replace(f" {key} ", "d")

        for character in this_in:
            if character not in ' ()abd|':
                bad_count += 1

        if bad_count == 0:
            for_removal.append(key)
            if key in rules[key]:
                curr_string = this_in
                # Turns out infinite repeats can be as low as 4
                for i in range(4):
                    curr_string = rules[key].replace(f" {key} ", curr_string)
                rules[key] = curr_string

            for k in rules.keys():
                rules[k] = rules[k].replace(
                    f" {key} ", " {} ".format(rules[key]))

            rules[key] = rules[key].replace(" ", "")

    for key in for_removal:
        todo_list.remove(key)

    if len(todo_list) == 0:
        break

regex = re.compile(r"^{}$".format(rules['0']))
for check in data[135:555]:
    if regex.match(check):
        count += 1

print(count)

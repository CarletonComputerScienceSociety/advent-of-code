data = []
with open("input.txt", 'r') as f:
    for lines in f:
        line = lines.strip()
        data.append(line)

def parse_line(line):
    parts = line.split(" ")
    nums = parts[0].split("-")
    min = int(nums[1])
    max = int(nums[1])
    letter = parts[1][0]
    string = parts[2]
    return min, max, letter, string

def count_valid(data):
    valid = 0
    for i in data:
        min, max, letter, string = parse_line(i)
        letterCount = string.count(letter)
        if letterCount  >= min and letterCount  <= max:
            valid += 1
    return valid

def count_valid_2(data):
    valid = 0
    for i in data:
        pos1 = False
        pos2 = False
        min, max, letter, string = parse_line(i)
        index1 = min - 1
        index2 = max - 1
        if string[index1] == letter:
            pos1 = True
        if string[index2] == letter:
            pos2 = True
        if pos1 != pos2:
            valid += 1
    return valid
    
print(count_valid(data))
print(count_valid_2(data))

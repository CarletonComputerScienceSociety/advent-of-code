def read_input():
    input_arr = []
    with open("input/input3.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append(line)
    return input_arr

def part1(input_arr):
    res = 0
    for s in input_arr:
        mid = len(s)//2
        first = set(s[:mid])
        second = set(s[mid:])
        c = (first & second).pop()
        if c.isupper():
            res += ord(c)-ord('A')+27
        else:
            res += ord(c)-ord('a')+1
    return res

def part2(input_arr):
    res = 0
    for i in range(0, len(input_arr), 3):
        first  = set(input_arr[i])
        second = set(input_arr[i+1])
        third  = set(input_arr[i+2])
        c = (first & second & third).pop()
        if c.isupper():
            res += ord(c)-ord('A')+27
        else:
            res += ord(c)-ord('a')+1
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()

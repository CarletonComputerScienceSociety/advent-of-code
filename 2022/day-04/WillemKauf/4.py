def read_input():
    input_arr = []
    with open("input/input4.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            a, b = line.split(",")
            input_arr.append([int(i) for i in a.split("-")] + [int(i) for i in b.split("-")])
    return input_arr

def part1(input_arr):
    res = 0
    for p in input_arr:
        a, b, c, d = p
        if a <= c and b >= d:
            res += 1
        elif c <= a and d >= b:
            res += 1
    return res

def part2(input_arr):
    res = 0
    for p in input_arr:
        a, b, c, d = p
        start = max(a,c)
        end   = min(b,d)
        if start <= end:
            res += 1
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()

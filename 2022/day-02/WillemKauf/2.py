def read_input():
    input_arr = []
    with open("input/input2.txt", "r") as input_file:
        for line in input_file.readlines():
            line = line.rstrip()
            input_arr.append([i for i in line.split(" ")])
    return input_arr

def part1(input_arr):
    mp      = {"X":1, "Y":2, "Z":3}
    win_mp  = {"Y":"A", "X":"C", "Z":"B"}
    lose_mp = {"A":"Z", "B":"X", "C":"Y"}
    res = 0
    for a,b in input_arr:
        if win_mp[b] == a:
            res += 6 + mp[b]
        elif lose_mp[a] == b:
            res += mp[b]
        else:
            res += 3 + mp[b]
    return res

def part2(input_arr):
    mp      = {"X":1, "Y":2, "Z":3}
    win_mp  = {"A":"Y", "C":"X", "B":"Z"}
    lose_mp = {"A":"Z", "B":"X", "C":"Y"}
    draw_mp = {"A":"X", "B":"Y", "C":"Z"}
    res = 0
    for a,b in input_arr:
        if b == "X":
            res += mp[lose_mp[a]]
        if b == "Y":
            res += 3 + mp[draw_mp[a]]
        if b == "Z":
            res += 6 + mp[win_mp[a]]
    return res

def main():
    input_arr = read_input()
    print(part1(input_arr))
    print(part2(input_arr))

if __name__ == "__main__":
    main()

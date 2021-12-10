from collections import deque

def read_input():
    input_lst = []
    with open("input/input10.txt") as input_file:
        for line in input_file:
            input_lst.append([c for c in line.rstrip()])
    return input_lst

def part_1(input_lst):
    hsh_map   = {"[":"]", "(":")", "{":"}", "<":">"}
    score_map = {")":3, "]":57, "}":1197, ">":25137}
    res = 0
    for line in input_lst:
        lst = deque(line[0])
        for i in range(1, len(line)):
            next_c = line[i]
            if next_c in hsh_map:
                lst.appendleft(next_c)
            else:
                curr_c = lst.popleft()
                expected_c = hsh_map[curr_c]
                if next_c != expected_c:
                    res += score_map[next_c]
                    break
    return res

def part_2(input_lst):
    hsh_map   = {"[":"]", "(":")", "{":"}", "<":">"}
    score_map = {")":1, "]":2, "}":3, ">":4}
    incomplete_lst = []
    for line in input_lst:
        lst = deque(line[0])
        flag = True
        for i in range(1, len(line)):
            next_c = line[i]
            if next_c in hsh_map:
                lst.appendleft(next_c)
            else:
                curr_c = lst.popleft()
                expected_c = hsh_map[curr_c]
                if next_c != expected_c:
                    flag = False
                    break
        if flag:
            incomplete_lst.append(line)

    scrs = []
    for line in incomplete_lst:
        lst = deque(line[0])
        for i in range(1, len(line)):
            next_c = line[i]
            if next_c in hsh_map:
                lst.appendleft(next_c)
            else:
                lst.popleft()

        scr = 0
        for c in lst:
            scr *= 5
            scr += score_map[hsh_map[c]]
        scrs.append(scr)
    return sorted(scrs)[len(scrs)//2]


def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()

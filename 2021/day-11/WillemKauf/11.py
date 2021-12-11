import itertools
from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input11.txt") as input_file:
        for line in input_file:
            input_lst.append([int(i) for i in line.rstrip()])
    return input_lst

ddir = [comb for comb in itertools.product([-1, 0, 1], repeat=2,) if abs(comb[0]) + abs(comb[1]) < 3]

def flash(i,j, input_lst, seen):
    seen.add((i,j))
    for di,dj in ddir:
        if ((i+di),(j+dj)) in seen:
            continue
        if 0 <= i+di < len(input_lst[j]) and 0 <= j+dj < len(input_lst):
            input_lst[j+dj][i+di] += 1
            if input_lst[j+dj][i+di] > 9:
                input_lst, seen = flash(i+di, j+dj, input_lst, seen)
    return input_lst, seen

def part_1(input_lst):
    res = 0
    for k in range(0, 100):
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                input_lst[j][i] += 1

        seen = set()
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                if input_lst[j][i] > 9 and (i,j) not in seen:
                    input_lst, seen = flash(i,j, input_lst, seen)
        for ii,jj in seen:
            input_lst[jj][ii] = 0
        res += len(seen)
    return res

def part_2(input_lst):
    res = 0
    cnt = 0
    while True:
        cnt += 1
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                input_lst[j][i] += 1

        seen = set()
        for j in range(0, len(input_lst)):
            for i in range(0, len(input_lst[j])):
                if input_lst[j][i] > 9 and (i,j) not in seen:
                    input_lst, seen = flash(i,j, input_lst, seen)
        for ii,jj in seen:
            input_lst[jj][ii] = 0
        if len(seen) == len(input_lst)*len(input_lst[j]):
            return cnt
    return res

def main():
    print(part_1(read_input()))
    print(part_2(read_input()))

if __name__ == "__main__":
    main()

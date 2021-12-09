from collections import deque

def read_input():
    input_lst = []
    with open("input/input9.txt") as input_file:
        for line in input_file:
            input_lst.append([int(c) for c in line.rstrip()])
    return input_lst

def part_1(input_lst):
    ddir = [-1, 0, 1]
    res = []
    low_points = []
    for j, row in enumerate(input_lst):
        for i,c in enumerate(row):
            flag = True
            neighbours = []
            for dx in ddir:
                for dy in ddir:
                    if abs(dx)+abs(dy) != 1:
                        continue
                    if not 0 <= i+dx < len(row) or not 0 <= j+dy < len(input_lst):
                        continue
                    neighbours.append(input_lst[j+dy][i+dx])
            for neighbour in neighbours:
                if c >= neighbour:
                    flag = False
                    break
            if flag == True:
                res.append(c)
                low_points.append((i,j))
    return sum([r+1 for r in res]), low_points

def part_2(input_lst, low_points):
    ddir   = [-1, 0, 1]
    basins = []
    for (i,j) in low_points:
        c = input_lst[j][i]
        queue = deque([(i,j)])
        seen = set()
        while len(queue):
            (curr_i, curr_j) = queue.popleft()
            seen.add((curr_i, curr_j))
            for dx in ddir:
                for dy in ddir:
                    if abs(dx)+abs(dy) != 1:
                        continue
                    if not 0 <= curr_i+dx < len(input_lst[j]) or not 0 <= curr_j+dy < len(input_lst[i]):
                        continue
                    neighbour = input_lst[curr_j+dy][curr_i+dx]
                    if (curr_i+dx, curr_j+dy) not in seen and neighbour != 9:
                        queue.appendleft((curr_i+dx,curr_j+dy))
        basins.append(len(seen))

    res = 1
    for i in range(0, 3):
        res *= sorted(basins)[::-1][i]
    return res

def main():
    res_1, low_points = part_1(read_input())
    print(res_1)
    print(part_2(read_input(), low_points))

if __name__ == "__main__":
    main()

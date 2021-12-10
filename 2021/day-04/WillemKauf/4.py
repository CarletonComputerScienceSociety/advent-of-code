import numpy as np

def read_input():
    grid_lst = []
    num_lst = []
    with open("input/input4.txt") as input_file:
        num_lst = [int(i) for i in input_file.readline().rstrip().split(",")]
        curr_lst = []
        line = input_file.readline()
        for line in input_file:
            line = line.rstrip()
            if line == "":
                grid_lst.append(np.array(curr_lst, dtype=np.float16))
                curr_lst = []
                continue
            curr_lst.append([int(i) for i in line.split()])
        if len(curr_lst):
            grid_lst.append(np.array(curr_lst, dtype=np.float16))
    return num_lst, grid_lst

def grid_won(grid):
    rows = [list(grid[j,:]) for j in range(0, len(grid))]
    cols = [list(grid[:,i]) for i in range(0, len(grid[0]))]
    return any([any([np.nansum(row) == 0 for row in rows]), any([np.nansum(col) == 0 for col in cols])])

def part_1(num_lst, grid_lst):
    for num in num_lst:
        for k in range(0, len(grid_lst)):
            for j in range(0, len(grid_lst[k])):
                for i in range(0, len(grid_lst[k][j])):
                    if grid_lst[k][j][i] == num:
                        grid_lst[k][j][i] = np.nan

        for k in range(0, len(grid_lst)):
            grid = grid_lst[k]
            if grid_won(grid):
                return int(np.nansum(grid)*num)

def part_2(num_lst, grid_lst):
    won_lst = set()
    for num in num_lst:
        for k in range(0, len(grid_lst)):
            for j in range(0, len(grid_lst[k])):
                for i in range(0, len(grid_lst[k][j])):
                    if grid_lst[k][j][i] == num:
                        grid_lst[k][j][i] = np.nan

        for k in range(0, len(grid_lst)):
            grid = grid_lst[k]
            if grid_won(grid):
                won_lst.add(k)
                if len(won_lst) == len(grid_lst):
                    return int(np.nansum(grid)*num)

def main():
    input_lsts = read_input()
    print(part_1(*input_lsts))
    print(part_2(*input_lsts))

if __name__ == "__main__":
    main()


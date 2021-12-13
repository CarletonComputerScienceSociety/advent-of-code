import colorama
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize, linewidth=100000)

def read_input():
    input_lst = []
    instruct_lst = []
    with open("input/input13.txt") as input_file:
        for line in input_file:
            line = line.rstrip()
            if line == "":
                pass
            elif line[0:4] == "fold":
                line = line.split("=")
                instruct_lst.append((line[0][-1], int(line[1])))
            else:
                line = line.split(',')
                input_lst.append([int(line[0]), int(line[1])])
    return input_lst, instruct_lst

def part_1(input_lst, instruct_lst):
    instruct_lst = [instruct_lst[0]]
    x_max = max([i[0] for i in input_lst])+1
    y_max = max([i[1] for i in input_lst])+1
    arr = np.zeros((y_max, x_max), dtype=np.int32)
    for x,y in input_lst:
        arr[y][x] = 1
    for cmd, val in instruct_lst:
        if cmd == "y":
            flip_arr = np.flip(arr[val+1:][:], 0)
            arr = arr[:val][:] + flip_arr
        if cmd == "x":
            flip_arr = np.flip(arr[:, val+1:], 1)
            arr = arr[:, :val] + flip_arr
    return np.sum(np.clip(arr, 0, 1))

def part_2(input_lst, instruct_lst):
    x_max = max([i[0] for i in input_lst])+1
    y_max = max([i[1] for i in input_lst])+1
    arr = np.zeros((y_max, x_max), dtype=np.int32)
    for x,y in input_lst:
        arr[y][x] = 1
    for cmd, val in instruct_lst:
        if cmd == "y":
            flip_arr = np.flip(arr[val+1:][:], 0)
            arr = arr[:val][:] + flip_arr
        if cmd == "x":
            flip_arr = np.flip(arr[:, val+1:], 1)
            arr = arr[:, :val] + flip_arr

    for row in np.clip(arr,0,1):
        print(" ".join([colorama.Fore.RED + str(i) if i == 1 else colorama.Fore.GREEN + colorama.Back.GREEN + str(i) for i in row]))
    colorama.Style.RESET_ALL

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()

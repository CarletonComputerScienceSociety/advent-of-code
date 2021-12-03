from copy import deepcopy

def read_input():
    input_lst = []
    with open("input/input3.txt") as input_file:
        for line in input_file:
            input_lst.append(line.rstrip())
    return input_lst

def part_1(input_lst):
    max_res = ""
    min_res = ""
    for i in range(0, len(input_lst[0])):
        hsh_map = {"0":0, "1":0}
        for j in range(0, len(input_lst)):
            hsh_map[input_lst[j][i]] += 1
        if hsh_map["0"] > hsh_map["1"]:
            max_res += str(0)
            min_res += str(1)
        else:
            max_res += str(1)
            min_res += str(0)
    return int(max_res, 2)*int(min_res,2)

def part_2(input_lst):
    oxygen_lst = deepcopy(input_lst)
    for i in range(0, len(oxygen_lst[0])):
        if oxygen_lst.count(None) == len(oxygen_lst)-1:
            break
        hsh_map = {"0":0, "1":0}
        for j in range(0, len(oxygen_lst)):
            if oxygen_lst[j] != None:
                hsh_map[oxygen_lst[j][i]] += 1
        if hsh_map["0"] > hsh_map["1"]:
            max_res = str(0)
        else:
            max_res = str(1)
        for k, num in enumerate(oxygen_lst):
            if oxygen_lst.count(None) == len(oxygen_lst)-1:
                break
            if num == None:
                continue
            if num[i] != max_res:
                oxygen_lst[k] = None
    oxygen = [i for i in oxygen_lst if i != None][0]

    dioxide_lst = deepcopy(input_lst)
    for i in range(0, len(dioxide_lst[0])):
        if dioxide_lst.count(None) == len(dioxide_lst)-1:
            break
        hsh_map = {"0":0, "1":0}
        for j in range(0, len(dioxide_lst)):
            if dioxide_lst[j] != None:
                hsh_map[dioxide_lst[j][i]] += 1
        if hsh_map["0"] > hsh_map["1"]:
            min_res = str(1)
        else:
            min_res = str(0)
        for k, num in enumerate(dioxide_lst):
            if dioxide_lst.count(None) == len(dioxide_lst)-1:
                break
            if num == None:
                continue
            if num[i] != min_res:
                dioxide_lst[k] = None
    dioxide = [i for i in dioxide_lst if i != None][0]

    return int(oxygen, 2)*int(dioxide,2)

def main():
    input_lst = read_input()
    print(part_1(input_lst))
    print(part_2(input_lst))

if __name__ == "__main__":
    main()


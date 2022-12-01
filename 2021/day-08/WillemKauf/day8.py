#This is hilariously bad
import itertools

def read_input():
    keywords_lst = []
    output_lst   = []
    with open("input/input8.txt") as input_file:
        for line in input_file:
            line = line.rstrip().split(" | ")
            keywords = line[0].split()
            output   = line[1].split()
            keywords_lst.append(keywords)
            output_lst.append(output)
    return keywords_lst, output_lst

def part_1(keywords_lst, output_lst):
    #This was not needed
    lst = [["a"]*4, ["b"]*2, ["c"]*2, ["d"]*4, ["e"]*2, ["f"]*2, ["g"]*4]
    dct = {0:[lst[0], lst[1], lst[2], lst[4], lst[5], lst[6]],
           1:[lst[2], lst[5]],
           2:[lst[0], lst[2], lst[3], lst[4], lst[6]],
           3:[lst[0], lst[2], lst[3], lst[5], lst[6]],
           4:[lst[1], lst[2], lst[3], lst[5]],
           5:[lst[0], lst[1], lst[3], lst[5], lst[6]],
           6:[lst[0], lst[1], lst[3], lst[4], lst[5], lst[6]],
           7:[lst[0], lst[2], lst[5]],
           8:[lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6]],
           9:[lst[0], lst[1], lst[2], lst[3], lst[5], lst[6]]}
    res = 0
    for line in output_lst:
        for word in line:
            for k in dct:
                if len(word) == len(dct[k]):
                    if k in [1,4,7,8]:
                        res += 1
    return res

def part_2(keywords_lst, output_lst):
    #This ~was~ needed
    dct = {0:["X"]*3 + [None] + ["X"]*3,
           1:[None]*2 + ["X"] + [None]*2 + ["X"] + [None],
           2:["X"] + [None] + ["X"]*3 + [None] + ["X"],
           3:["X"] + [None] + ["X"]*2 + [None] + ["X"]*2,
           4:[None] + ["X"]*3 + [None] + ["X"] + [None],
           5:["X"]*2 + [None] + ["X"] + [None] + ["X"]*2,
           6:["X"]*2 + [None] + ["X"]*4,
           7:["X"] + [None] + ["X"] + [None]*2 + ["X"] + [None],
           8:["X"]*7,
           9:["X"]*4 + [None] + ["X"]*2}
    for k, v in dct.items():
        assert(len(v) == 7)

    res = 0
    for index, line in enumerate(keywords_lst):
        for perm in itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]):
            valid_dct = {}
            for word in line:
                for k, v in dct.items():
                    check_lst = [None]*7
                    for i, c in enumerate(perm):
                        if c in word:
                            check_lst[i] = "X"
                    if check_lst == v:
                        valid_dct["".join(sorted(word))] = k
            if len(valid_dct) == 10:
                num = ""
                for word in output_lst[index]:
                    num += str(valid_dct["".join(sorted(word))])
                res += int(num)
    return res

def main():
    print(part_1(*read_input()))
    print(part_2(*read_input()))

if __name__ == "__main__":
    main()

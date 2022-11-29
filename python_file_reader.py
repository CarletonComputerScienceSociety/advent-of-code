def twod_read_input(mylist, file_name):  # returns text from given file in a 2d list
    f = open(file_name, "r")
    file_data = f.read()
    input_text_block = file_data.strip().split("\n")
    for line in input_text_block:
        row = []
        for char in line:
            row.append(char)
        mylist.append(row)
    f.close()


def oned_read_input(mylist, file_name):  # returns text from given file in a 1d list
    f = open(file_name, "r")
    file_data = f.read()
    input_text_block = file_data.strip().split("\n")
    for line in input_text_block:
        for char in line:
            mylist.append(char)
    f.close()


def line_by_line_input(mylist, file_name):  # returns text line by line in a 1d list
    f = open(file_name, "r")
    file_data = f.read()
    input_text_block = file_data.strip().split("\n")
    for line in input_text_block:
        mylist.append(line)
    f.close()


file_name = "input.txt"

twod_list = []
twod_read_input(twod_list, file_name)
print("twod_read_input input parsing")
print(twod_list)

print()

oned_list = []
print("oned_read_input input parsing")
oned_read_input(oned_list, file_name)
print(oned_list)

print()

line_by_line_list = []
print("line_by_line_input input parsing")

line_by_line_input(line_by_line_list, file_name)
print(line_by_line_list)

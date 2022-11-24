def twod_read_input(mylist, file_name): #returns text from given file in a 2d list
    f = open(file_name, 'r')
    file_data = f.read()
    input_text_block = file_data.strip().split('\n')
    for line in input_text_block:
        row = []
        for char in line:
            row.append(char)
        mylist.append(row)

def oned_read_input(mylist, file_name): #returns text from given file in a 1d list
    f = open(file_name, 'r')
    file_data = f.read()
    input_text_block = file_data.strip().split('\n')
    for line in input_text_block:
        for char in line:
            mylist.append(char)


file_name = 'input.txt'

twod_list =[]
twod_read_input(twod_list, file_name)
print(twod_list);

print()

oned_list =[]
oned_read_input(oned_list, file_name)
print(oned_list)


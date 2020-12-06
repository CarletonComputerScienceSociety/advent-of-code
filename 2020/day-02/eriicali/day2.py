validPasswords = 0

file = open("day_2_input.txt")
for line in file.readlines():
    allInfo = line.split(" ")
    indices = [int(num) for num in allInfo[0].split("-")]
    letter = allInfo[1][0]
    password = allInfo[2]
    if password[indices[0]-1] == letter and not password[indices[1]-1] == letter:
        validPasswords += 1
    elif not password[indices[0]-1] == letter and password[indices[1]-1] == letter:
        validPasswords += 1

print(validPasswords)

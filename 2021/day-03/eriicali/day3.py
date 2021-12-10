# part 1

file = open("day3.txt")
gamma = ""
epsilon = ""
length = 0

numZeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in file:
    i = 0
    length += 1
    for char in line.strip():
        
        if(char == "0"):
            numZeroes[i] += 1
            
        i += 1

for freq in numZeroes:
    if freq >= length / 2:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"
print(gamma)
print(epsilon)
print(281 * 3814)

# part 2

oxygen = ""
co2 = ""
length = 0
oxygenLines = file.readlines()
co2Lines = oxygenLines
numOxygenZeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numCo2Zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(12):
    for line in oxygenLines:
        if line[i] == "0":
            numOxygenZeroes[i] += 1
    if numOxygenZeroes[i] < len(oxygenLines)/2:
        oxygenWinner = "1"
        
    elif numOxygenZeroes[i] == len(oxygenLines)/2:
        oxygenWinner = "1"
        
    else:
        oxygenWinner = "0"
        
    oxygenLines = [line for line in oxygenLines if line[i] == oxygenWinner]
    for line in co2Lines:
        
        if line[i] == "0":
            numCo2Zeroes[i] += 1
    if numCo2Zeroes[i] < len(co2Lines)/2:
        co2Winner = "0"
        
    elif numCo2Zeroes[i] == len(co2Lines)/2:
        co2Winner = "0"
        
    else:
        co2Winner = "1"
    if len(co2Lines) != 1:
        co2Lines = [line for line in co2Lines if line[i] == co2Winner]
    
print(1679 *3648)

print(oxygenLines)
print(co2Lines)



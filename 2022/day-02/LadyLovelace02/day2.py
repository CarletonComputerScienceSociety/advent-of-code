
def calcScore(pInput, oInput):
    score = 0
    if pInput == 'X':
        score += 1
        if oInput == 'A':#draw
            score += 3
        elif oInput == 'C':
            score += 6
    elif pInput == 'Y':
        score += 2
        if oInput == 'B':#draw
            score += 3
        elif oInput == 'A':#won
            score += 6
    else:
        score += 3
        if oInput == 'C':#draw
            score += 3
        elif oInput == 'B':#won
            score += 6
    return score

def part1():
    totalScore = 0
    file = open('input.txt', 'r')
    line = file.readline()
    while line != '':#while not EOF
        opponetInput = line[0]
        playerInput = line[2]
        totalScore += calcScore(playerInput, opponetInput)
        line = file.readline()
    print(totalScore)

def calcScore2(outcome, oInput):
    score = 0
    if outcome == 'X':#loose
        if oInput == "A":#play scissors to loose
            score += 3
        elif oInput == "B":#play rock to loose
            score += 1
        else:
            score += 2
    elif outcome == 'Y':#draw
        score += 3
        score += ord(oInput)-64#add ascii value minus 64 to get 1, 2, or 3
    else:#win
        score += 6
        if oInput == 'A':
            score += 2#play paper
        elif oInput == 'B':
            score += 3#play scissors
        else:
            score += 1#play rock
    return score

def part2():
    totalScore = 0
    file = open('input.txt', 'r')
    line = file.readline()
    while line != '':#while not EOF
        opponetInput = line[0]
        outcome = line[2]
        totalScore += calcScore2(outcome, opponetInput)
        line = file.readline()
    print(totalScore)

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()

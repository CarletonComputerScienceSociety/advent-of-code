file = open("./day5.txt", mode="r")
boarding_passes = file.readlines()

w, h = 8, 128
flight_plan = [[0 for x in range(w)] for y in range(h)]

possible_rows = list(range(0, 128))
possible_seats = list(range(0,7))

maxID = 0

for boarding_pass in boarding_passes:
    boarding_pass.strip("\n")
    thisRow = list(range(0,128))
    thisSeat = list(range(0,8))
    print(boarding_pass) #print current pass so we know which one we're dealing with
    letters = list(boarding_pass)
    if letters[0] == "F":
        thisRow = thisRow[0:64]
    elif letters[0] == "B":
        thisRow = thisRow[64:int(max(thisRow)+1)]
    if letters[1] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[1] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    if letters[2] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[2] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    if letters[3] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[3] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    if letters[4] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[4] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    if letters[5] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[5] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    if letters[6] == "F":
        thisRow = thisRow[0:int(len(thisRow)/2)]
    elif letters[6] == "B":
        thisRow = thisRow[int(len(thisRow)/2):int(len(thisRow))]
    thisRow = int(thisRow[0])
    #seats start here
    if letters[7] == "L":
        thisSeat = thisSeat[0:int(len(thisSeat)/2)]
    elif letters[7] == "R":
        thisSeat = thisSeat[int(len(thisSeat)/2):int(len(thisSeat))]
    if letters[8] == "L":
        thisSeat = thisSeat[0:int(len(thisSeat)/2)]
    elif letters[8] == "R":
        thisSeat = thisSeat[int(len(thisSeat)/2):int(len(thisSeat))]
    if letters[9] == "L":
        thisSeat = thisSeat[0:int(len(thisSeat)/2)]
    elif letters[9] == "R":
        thisSeat = thisSeat[int(len(thisSeat)/2):int(len(thisSeat))]
    thisSeat = int(thisSeat[0])
    thisID = (thisRow * 8) + thisSeat
    print(thisID)
    if thisID > maxID:
        maxID = thisID
    flight_plan[thisRow][thisSeat] = thisID
        
print(maxID)
print(flight_plan)

#part 2, just gonna print the 2D array and find it visually lol; mine was 657
print('\n'.join([''.join(['{:8}'.format(seat) for seat in row]) 
       for row in flight_plan]))
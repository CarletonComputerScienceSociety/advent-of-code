def solve1(input):
    # Check every seat for highest ID
    highest = 0
    for seat in input:
        row, col = findPosition(seat, 0, 127, 0, 7)
        highest = max(highest, row*8+col)
    print(highest)

def solve2(input):
    # All nums 0..922
    seen = [i for i in range(923)]
    for seat in input:
        row, col = findPosition(seat, 0, 127, 0, 7)
        # Remove from list if we see the ID
        seen.remove(row*8+col)
    print([i for i in seen if (i+1 not in seen) and (i-1 not in seen)][0])

def findPosition(seat, rowlo, rowhi, collo, colhi):
    # Base case (one possible seat left)
    if (rowlo == rowhi and collo == colhi) or len(seat) == 0:
        return (rowlo, collo)
    
    if seat[0] == 'F':
        return findPosition(seat[1:], rowlo, (rowhi+rowlo)//2, collo, colhi)
    elif seat[0] == 'B':
        return findPosition(seat[1:], (rowhi+rowlo+1)//2, rowhi, collo, colhi)
    if seat[0] == 'L':
        return findPosition(seat[1:], rowlo, rowhi, collo, (colhi+collo)//2)
    elif seat[0] == 'R':
        return findPosition(seat[1:], rowlo, rowhi, (collo+colhi+1)//2, colhi)


with open('input.txt') as f:
    data = f.read().splitlines()
    solve1(data)
    solve2(data)

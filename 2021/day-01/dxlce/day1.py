
def main():

    with open("input.txt", "r") as file:

        prevLine = -1
        increased = 0
        

        for line in file:
            if (prevLine == -1):
                prevLine = line.rstrip()
                continue

            if (int(prevLine) < int(line.rstrip())):
                increased = increased + 1

            prevLine = line.rstrip()
       
    
        print(increased)
      
    with open("input.txt", "r") as file:
        lines = file.readlines()

        increased = 0
        prevSum = 0
        currSum = 0
        for i in range(0, len(lines) - 2):

            if (prevSum == 0):
                prevSum = int(lines[i].rstrip()) + int(lines[i + 1].rstrip()) + int(lines[i + 2].rstrip())
                continue

            currSum = int(lines[i].rstrip()) + int(lines[i + 1].rstrip()) + int(lines[i + 2].rstrip())

            if (prevSum < currSum):
                increased = increased + 1
            
            prevSum = currSum

        
        print(increased)

if __name__ == "__main__":
    main()

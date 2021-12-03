def main():

    with open("input.txt", "r") as file:

        gamma = 0
        ep = 0
        length = 0

        ones = 0
        zero = 0
        counter = 0
        lines = file.readlines()
        length = len(lines[0])
        # length = len(file.readlines()[0])

        for i in range(0, length -1):
            for line in lines:
                if (int(line[i]) == 1):
                    ones = ones + 1
                else:
                    zero = zero + 1
                
            if (ones > zero):
                gamma = gamma + 2**(length - 2 - counter)
            else:
                ep = ep + 2**(length - 2 - counter)

            ones = 0
            zero = 0
            counter = counter + 1
        
        print(gamma*ep)
        
        
   with open("input.txt", "r") as file:

        oxygen = 0
        c0 = 0
        length = 0

        ones = 0
        zero = 0
        
        lines = file.readlines()

        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()

        copy = []

        for line in lines:
            copy.append(line)


        linesZero = []
        linesOne = []

        length = len(lines[0])

        for i in range(0, length):

            if (len(lines) == 1):
                break
            for line in lines:
                if (int(line[i]) == 1):
                    linesOne.append(line)
                    ones = ones + 1
                else:
                    linesZero.append(line)
                    zero = zero + 1

            if (ones > zero):
                for value in linesZero:
                    lines.remove(value)
            elif (zero > ones):
                for value in linesOne:
                    lines.remove(value)
        
            else:
                for value in linesZero:
                    lines.remove(value)

            linesOne.clear()
            linesZero.clear()

            ones = 0
            zero = 0
        
        for i in range(0, length):
            if (int(lines[0][i]) == 1):
                
                oxygen = oxygen + 2**(length - 1 - i)

        ones = 0
        zero = 0
        lines = copy

        linesOne.clear()
        linesZero.clear()
        for i in range(0, length):

            if (len(lines) == 1):
                break
            for line in lines:
                if (int(line[i]) == 1):
                    linesOne.append(line)
                    ones = ones + 1
                else:
                    linesZero.append(line)
                    zero = zero + 1

            if (ones > zero):
                for value in linesOne:
                    lines.remove(value)
            elif (zero > ones):
                for value in linesZero:
                    lines.remove(value)
        
            else:
                for value in linesOne:
                    lines.remove(value)

            linesOne.clear()
            linesZero.clear()

            ones = 0
            zero = 0
        
        for i in range(0, length):
            if (int(lines[0][i]) == 1):
                
                c0 = c0 + 2**(length - 1 - i)


        print(oxygen*c0)     
        


if __name__ == "__main__":
    main()

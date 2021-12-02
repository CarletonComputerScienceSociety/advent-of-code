
def main():

   #Day 2 part 1
    with open("input.txt", "r") as file:

        
        horizontal = 0
        depth = 0
        for line in file:
            direction = line.split()[0]
            unit = int(line.split()[1])
            
            if (direction == "forward"):
                horizontal = horizontal + unit
            elif (direction == "down"):
                depth = depth + unit
            elif (direction == "up"):
                depth = depth - unit

        print(horizontal*depth)
       
      
  #Day 2 part 2
  with open("input.txt", "r") as file:

        
        horizontal = 0
        depth = 0
        aim = 0
        for line in file:
            direction = line.split()[0]
            unit = int(line.split()[1])
            
            if (direction == "forward"):
                horizontal = horizontal + unit
                depth = depth + (aim*unit)

            elif (direction == "down"):
                # depth = depth + unit
                aim = aim + unit

            elif (direction == "up"):
                # depth = depth - unit
                aim = aim - unit

        print(horizontal*depth)
            

if __name__ == "__main__":
    main()

inf = """input"""

inf2 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

input = [line for line in inf2.split("\n")]

def solve1(input):
    count = 0

    easy = [2, 3, 4, 7]

    for line in input:
        vals = line.split(" | ")[1]
        for val in vals.split():
            if len(val) in easy:
                count += 1

    print(count)


def solve2(input):
    nums = [""] * 10

    sum = 0

    for line in input:
        vals = line.split(" | ")
        #first find 1, 4, 7 and 8
        for val in vals[0].split():
            if len(val) == 2:
                nums[1] = val
            elif len(val) == 3:
                nums[7] = val
            elif len(val) == 4:
                nums[4] = val
            elif len(val) == 7:
                nums[8] = val

        #then find 3
        for val in vals[0].split():
            if len(val) == 5:
                threeFound = True
                for char in nums[1]:
                    if char not in val:
                        threeFound = False
                        break
                if (threeFound):
                    nums[3] = val
                    break
        
        #now we can find 2 and 5
        for val in vals[0].split():
            if len(val) == 5 and val != nums[3]:
                matchCount = 0
                for char in nums[4]:
                    if char in val: matchCount += 1
                if matchCount == 2: nums[2] = val
                elif matchCount == 3: nums[5] = val

        #we can use 1 to find 6
        for val in vals[0].split():
            if len(val) == 6:
                matchCount = 0
                for char in nums[1]:
                    if char in val: matchCount += 1
                if matchCount == 1:
                    nums[6] = val
                    break

        #finally use 4 to find 0 and 9
        for val in vals[0].split():
            if len(val) == 6 and val != nums[6]:
                matchCount = 0
                for char in nums[4]:
                    if char in val: matchCount += 1
                if matchCount == 4: nums[9] = val
                elif matchCount == 3: nums[0] = val

        #now that all the numbers have been found, we can determine the combo with regex
        code = vals[1].split()

        tempCode = ""

        for val in code:
            for count, num in enumerate(nums):
                if len(val) == len(num):
                    matchCount = 0
                    for char in num:
                        if char in val: matchCount += 1
                    if matchCount == len(num): 
                        tempCode += str(count)
                        break
        sum += int(tempCode)


    print(sum)

solve1(input)
solve2(input)

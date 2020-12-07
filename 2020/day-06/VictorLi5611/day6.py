inp = open('input.txt').read().strip()

alpha = ["a","b","c","d", "e","f", "g", "h", "i", "j","k", "l","m","n","o","p","q","r","s", "t","u","v","w","x","y","z"]

def solve1 (data):
    s = 0
    inpu = data.split("\n\n")
    for x in inpu:
        tot = sum(1 for y in alpha if y in x)
        s += tot

    return s


def solve2 (data):
    s = 0
    inpu = inp.split("\n\n")
    for x in inpu:
        line = x.split("\n")
        for letter in alpha:
            if all([letter in z for z in line ]):
                s+=1
    return s

print (solve1(inp))
print (solve2(inp))

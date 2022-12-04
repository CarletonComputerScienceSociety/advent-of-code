data = []
with open("day4.txt") as f:
    data = [x.strip() for x in f.readlines()]

p1 = 0
p2 = 0
for line in data:
    one,two = line.split(',')
    s1,e1= one.split('-')
    s2,e2= two.split('-')
    s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
    
    if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2:
        p1 += 1
  
    if not (e1 < s2 or s1 > e2):
        p2 += 1
print(p1)
print(p2)

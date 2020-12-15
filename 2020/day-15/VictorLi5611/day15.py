data = [13,0,10,12,1,5,8]
lastInded = {}

for i,n in enumerate(data):
    if i != len(data)-1:
        lastInded[n] = i

#part 1
while len(data) != 2020:
    prev = data[-1]
    prevPrev = lastInded.get(prev, -1)
    lastInded[prev] = len(data)-1
    if prevPrev == -1:
        next_ = 0
    else:
        next_ = len(data) - 1 - prevPrev
    data.append(next_)    
print(next_)

#part 2 
lastInded = {}
while len(data) < 30000000:
    prev = data[-1]
    prevPrev = lastInded.get(prev, -1)
    lastInded[prev] = len(data)-1
    if prevPrev == -1:
        next_ = 0
    else:
        next_ = len(data) - 1 - prevPrev
    data.append(next_)    
print(data[-1])

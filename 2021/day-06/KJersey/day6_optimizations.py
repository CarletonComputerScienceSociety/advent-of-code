import cProfile
import numpy as np

data = list(map(lambda x : int(x), open("day6.txt", 'r').readline().split(',')))

def naive(days):
    fish = []

    for i in range(9):
        fish.append(data.count(i))


    for _ in range(days):
        n = fish[0]

        for i in range(1, 9):
            fish[i - 1] = fish[i]

        fish[6] += n
        fish[8] = n
        
    counter = 0
    for n in fish:
        counter += n
        
    return counter

def circular(days):

    fish = []
    newfish = [0, 0]

    for i in range(7):
        fish.append(data.count(i))

    for i in range(days + 1):
        n = newfish[(i + 1) % 2]
        newfish[(i + 1) % 2] = fish[(i + 6) % 7]
        fish[(i + 6) % 7] += n

    counter = 0
    for n in fish:
        counter += n

    counter += newfish[0] + newfish[1]

    return counter

def matrix(days):
    mat = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0]
    ], dtype=object)

    fish = []
    for i in range(9):
        fish.append(data.count(i))

    return np.sum(np.dot(np.linalg.matrix_power(mat, days), fish))

#cProfile.run('naive(2**24)')
#cProfile.run('circular(2**24)')
#cProfile.run('matrix(2**24)')

print(naive(256))
print(circular(256))
print(matrix(256))
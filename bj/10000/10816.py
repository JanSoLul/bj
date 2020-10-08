from sys import stdin
N = int(input())
numL = list(map(int, stdin.readline().split()))
M = int(input())
checkL = list(map(int, stdin.readline().split()))
uniqueL = list(set(numL))
numD = dict()
for i in numL:
    if i in numD:
        numD[i] += 1
    else:
        numD[i] = 1
uniqueL.sort()
for i in checkL:
    if i in numD:
        print(numD[i], end=' ')
    else:
        print('0', end=' ')


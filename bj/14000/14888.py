from sys import stdin
N = int(input())
numL = list(map(int, stdin.readline().split()))
opN = list(map(int, stdin.readline().split()))
opL = [-1 for _ in range(N-1)]
opCount = 0
resultMax = -1000000000
resultMin = 1000000000

for i in opN:
    opCount += i

def putOp(arg):
    global resultMax
    global resultMin
    global opCount
    if arg == opCount:
        tmp = calOp()
        if tmp > resultMax:
            resultMax = tmp
        if tmp < resultMin:
            resultMin = tmp
    else:
        for i in range(4):
            if opN[i] > 0:
                opL[arg] = i
                opN[i] -= 1
                putOp(arg+1)
                opN[i] += 1
                opL[arg] = -1

def calOp():
    global opCount
    copyNum = numL[:]
    for i in range(opCount):
        if opL[i] == 0:
            copyNum[i+1] = copyNum[i] + copyNum[i+1]
        elif opL[i] == 1:
            copyNum[i+1] = copyNum[i] - copyNum[i+1]
        elif opL[i] == 2:
            copyNum[i+1] = copyNum[i] * copyNum[i+1]
        else:
            minusCheck = False
            if copyNum[i] < 0:
                copyNum[i] = -copyNum[i]
                minusCheck = True
            copyNum[i+1] = copyNum[i] // copyNum[i+1]
            if minusCheck:
                copyNum[i+1] = -copyNum[i+1]
    return copyNum[-1]


putOp(0)
print(resultMax)
print(resultMin)

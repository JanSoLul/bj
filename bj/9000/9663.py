import sys
sys.setrecursionlimit(100000)

N = int(input())
queenList = []
count = 0
tmpX = 0
tmpY = 0

def checkNext(n):
    global count
    global tmpX
    global tmpY
    if n == N:
        count += 1
    else:
        for i in range(N):
            for j in range(len(queenList)):
                tmpX = queenList[j][0] - n
                tmpY = queenList[j][1] - i
                if tmpY == 0 or abs(tmpX) == abs(tmpY):
                    break
                if j == len(queenList) - 1:
                    queenList.append([n, i])
                    checkNext(n+1)
                    queenList.pop()

for i in range(N):
    queenList.append([0, i])
    checkNext(1)
    queenList.pop()

print(count)

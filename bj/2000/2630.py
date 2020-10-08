import sys

def calSquare(left, right, top, bottom):
    global blueCount
    global whiteCount
    isBlue = False
    isBreak = False
    for i in range(top, bottom):
        for j in range(left, right):
            if i==top and j==left:
                if sq[i][j] == 1:
                    isBlue = True
            if isBlue:
                if sq[i][j] == 0:
                    isBreak = True
                    break
                if i==bottom-1 and j==right-1:
                    blueCount += 1
                    return 0
            elif not isBlue:
                if sq[i][j] == 1:
                    isBreak = True
                    break
                if i==bottom-1 and j==right-1:
                    whiteCount += 1
                    return 0
        if isBreak:
            break
    calSquare(left, right//2, top, bottom//2)
    calSquare(left, right//2, bottom//2, bottom)
    calSquare(right//2, right, top, bottom//2)
    calSquare(right//2, right, bottom//2, bottom)


sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline())
sq = []
blueCount = 0
whiteCount = 0
for _ in range(N):
    sq.append(list(map(int, sys.stdin.readline().split())))
calSquare(0, N, 0, N)
print(whiteCount)
print(blueCount)

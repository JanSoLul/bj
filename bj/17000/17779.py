from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    A = []
    for _ in range(N):
        A.append(list(map(int, read().split())))


    def divideArea(x, y, d1, d2):
        areaSize = [0 for _ in range(6)]
        saveArea = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(d1+1):
            saveArea[x+i][y-i] = 5
            saveArea[x+d2+i][y+d2-i] = 5
        for i in range(d2+1):
            saveArea[x+i][y+i] = 5
            saveArea[x+d1+i][y-d1+i] = 5
        for i in range(x+1, x+d1+d2):
            isTrue = False
            for j in range(N):
                if saveArea[i][j] == 5:
                    if isTrue:
                        break
                    isTrue = not isTrue
                if isTrue:
                    saveArea[i][j] = 5
        for cx in range(N):
            for cy in range(N):
                if saveArea[cx][cy]==0:
                    if cx<x+d1 and cy<=y:
                        areaSize[1] += A[cx][cy]
                    elif cx<=x+d2 and y<cy:
                        areaSize[2] += A[cx][cy]
                    elif x+d1<=cx and cy<y-d1+d2:
                        areaSize[3] += A[cx][cy]
                    elif x+d2<cx and y-d1+d2<=cy:
                        areaSize[4] += A[cx][cy]
                elif saveArea[cx][cy]==5:
                    areaSize[5] += A[cx][cy]
        areaSize = sorted(areaSize[1:])
        return areaSize[-1]-areaSize[0]

    minDiff = 10**8
    for x in range(N-2):
        for y in range(1, N-1):
            d1Max = min(N-x,y)
            d2Max = min(N-x, N-y)
            for d1 in range(1, d1Max+1):
                for d2 in range(1, d2Max+1):
                    if 1<x+d1+d2<N and 0<=y-d1<y+d2<N:
                        minDiff = min(minDiff, divideArea(x, y, d1, d2))
    print(minDiff)


if __name__ == '__main__':
    solve()

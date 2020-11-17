from sys import stdin
from collections import deque
from copy import deepcopy
read = lambda : stdin.readline()


def solve():
    N, M = list(map(int, read().split()))
    laboratory = []
    for _ in range(N):
        laboratory.append(list(map(int, read().split())))
    checkL = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    safeArea = [0]
    virusL = []
    maxSafeArea = [0]
    for i in range(N):
        for j in range(M):
            if laboratory[i][j] == 0:
                safeArea[0] += 1
            if laboratory[i][j] == 2:
                virusL.append((i, j))


    def spreadVirus(copyLaboratory):
        virusQ = deque()
        spreadNum = 0
        for virusX, virusY in virusL:
            virusQ.append((virusX, virusY))
        while virusQ:
            virusX, virusY = virusQ.popleft()
            for addX, addY in checkL:
                nextX = virusX + addX
                nextY = virusY + addY
                if nextX < 0 or nextY < 0 or nextX == N or nextY == M:
                    continue
                if copyLaboratory[nextX][nextY] == 0:
                    spreadNum += 1
                    copyLaboratory[nextX][nextY] = 2
                    virusQ.append((nextX, nextY))
        tmp = safeArea[0] - spreadNum - 3
        maxSafeArea[0] = max(maxSafeArea[0], tmp)


    def buildWall(N, M, start, wallCount):
        if wallCount == 3:
            spreadVirus(deepcopy(laboratory))
            return
        for i in range(start, N*M):
            checkX = i // M
            checkY = i % M
            if laboratory[checkX][checkY] == 0:
                laboratory[checkX][checkY] = 1
                buildWall(N, M, i+1, wallCount+1)
                laboratory[checkX][checkY] = 0

    buildWall(N, M, 0, 0)
    print(maxSafeArea[0])


if __name__ == '__main__':
    solve()

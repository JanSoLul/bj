from sys import stdin
from copy import deepcopy
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, M = map(int, read().split())
    laboratory = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    remainSpace = 0
    for i in range(N):
        laboratory.append(list(map(int, read().split())))
        for j in range(N):
            if laboratory[i][j] == 0:
                remainSpace += 1
    minRet = [10 ** 6]


    def spreadbfs(virusL):
        tmpL = deepcopy(laboratory)
        saveSpace = remainSpace
        visited = [[False for _ in range(N)] for _ in range(N)]
        q = deque()
        for x, y in virusL:
            q.append((x, y, 0, False))
        maxTime = 0
        while q:
            cx, cy, time, isSpace = q.popleft()
            if visited[cx][cy]:
                continue
            maxTime = max(maxTime, time)
            if isSpace:
                saveSpace -= 1
            if saveSpace == 0:
                break
            visited[cx][cy] = True
            tmpL[cx][cy] = -1
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0<=nx<N and 0<=ny<N:
                    if tmpL[nx][ny] == 0:
                        q.append((nx, ny, time+1, True))
                    elif tmpL[nx][ny] == 2:
                        q.append((nx, ny, time+1, False))
        if saveSpace == 0:
            return maxTime
        else:
            return -1


    def setVirus(start, count, virusL):
        if count == M:
            tmpRet = spreadbfs(virusL)
            if tmpRet > -1:
                minRet[0] = min(tmpRet, minRet[0])
            return
        for index in range(start, N**2):
            i = index // N
            j = index % N
            if laboratory[i][j] == 2:
                virusL.append((i, j))
                setVirus(index+1, count+1, virusL)
                virusL.pop()

    setVirus(0, 0, [])
    if minRet[0] == 10**6:
        print(-1)
    else:
        print(minRet[0])


if __name__ == '__main__':
    solve()

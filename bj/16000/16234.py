from sys import stdin
from copy import deepcopy
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, L, R = map(int, read().split())
    nation = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for _ in range(N):
        nation.append(list(map(int, read().split())))

    def isPopulationCheck():
        unionCount = 0
        unionL = []
        for i in range(N):
            for j in range(N):
                visited[i][j] = False
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    visited[i][j] = True
                    tmpL = bfs(i, j)
                    if tmpL:
                        unionL.append(tmpL)
                        unionCount += 1
        return unionL


    def bfs(x, y):
        q = deque()
        q.append((x, y))
        union = []
        while q:
            curX, curY = q.popleft()
            for i in range(4):
                nextX = curX + dx[i]
                nextY = curY + dy[i]
                if 0<=nextX<N and 0<=nextY<N:
                    if not visited[nextX][nextY]:
                        tmp = abs(nation[nextX][nextY] - nation[curX][curY])
                        if L<=tmp<=R:
                            visited[nextX][nextY] = True
                            q.append((nextX, nextY))
                            union.append((nextX, nextY))
        if union:
            union.append((x, y))
            return union
        return None


    day = 0
    while True:
        BorderOpen = isPopulationCheck()
        if BorderOpen:
            for tmpUnion in BorderOpen:
                nationCount = len(tmpUnion)
                populationSum = 0
                for curX, curY in tmpUnion:
                    populationSum += nation[curX][curY]
                finalPopulation = populationSum // nationCount
                for curX, curY in tmpUnion:
                    nation[curX][curY] = finalPopulation
            day += 1
            '''
            print()
            print(day)
            for i in range(N):
                print(nation[i])
            '''
        else:
            print(day)
            break


if __name__ == '__main__':
    solve()

from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N = int(read())
    mapL = []
    shark = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    fishCount = 0
    for i in range(N):
        mapL.append(list(map(int, read().split())))
        for j in range(N):
            if mapL[i][j] == 9:
                shark = [i, j]
                mapL[i][j] = 0
            elif mapL[i][j] > 0:
                fishCount += 1
    timeCount = 0
    sharkSize = 2
    remainFood = 2
    while fishCount > 0:
        saveFishLoc = []
        minD = 10**6
        visited = [[False for _ in range(N)] for _ in range(N)]
        q = deque()
        q.append((shark[0], shark[1], 0))
        visited[shark[0]][shark[1]] = True
        while q:
            cx, cy, move = q.popleft()
            if move > minD:
                break
            if 0<mapL[cx][cy]<sharkSize:
                minD = move
                saveFishLoc.append([cx, cy])
            for ai in range(4):
                nx = cx + dx[ai]
                ny = cy + dy[ai]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    if mapL[nx][ny] <= sharkSize:
                        q.append((nx, ny, move+1))
                        visited[nx][ny] = True
        if saveFishLoc == []:
            break
        sortedFish = sorted(saveFishLoc, key = lambda x : (x[0], x[1]))
        tmpx, tmpy = sortedFish[0][0], sortedFish[0][1]
        mapL[tmpx][tmpy] = 0
        shark[0] = tmpx
        shark[1] = tmpy
        timeCount += minD
        remainFood -= 1
        fishCount -= 1
        if remainFood == 0:
            sharkSize += 1
            remainFood = sharkSize
    print(timeCount)


if __name__ == '__main__':
    solve()

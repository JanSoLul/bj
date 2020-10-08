from sys import stdin
from collections import deque

M, N, H = list(map(int, stdin.readline().split()))
tomato = []
queue = deque()
visited = [[[-2 for _ in range(M)] for _ in range(N)] for _ in range(H)]
checkL = [[0, 1], [1, 0], [0, -1], [-1, 0]]
isPossible = False
for h in range(H):
    tomato.append([])
    for i in range(N):
        tomato[h].append(list(map(int, stdin.readline().split())))
        for j in range(M):
            if tomato[h][i][j] == -1:
                visited[h][i][j] = -1
            elif tomato[h][i][j] == 1:
                queue.append((h, i, j, 0))

while queue:
    h, x, y, day = queue.popleft()
    if visited[h][x][y] == -2:
        visited[h][x][y] = day
        tomato[h][x][y] = 1
        for xDiff, yDiff in checkL:
            tmpX = x + xDiff
            tmpY = y + yDiff
            if tmpX >= 0 and tmpY >= 0 and tmpX < N and tmpY < M:
                if tomato[h][x+xDiff][y+yDiff] == 0:
                    queue.append((h, x+xDiff, y+yDiff, day+1))
        if h>0:
            if tomato[h-1][x][y] == 0:
                queue.append((h-1, x, y, day+1))
        if h<H-1:
            if tomato[h+1][x][y] == 0:
                queue.append((h+1, x, y, day+1))
maxDay = 0
for h in range(H):
    for i in range(N):
        if min(visited[h][i]) == -2:
            print(-1)
            exit(0)
        else:
            tmpMax = max(visited[h][i])
            if tmpMax > maxDay:
                maxDay = tmpMax
        if i==N-1:
            isPossible = True
if isPossible:
    print(maxDay)

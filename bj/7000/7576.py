from sys import stdin
from collections import deque

M, N = list(map(int, stdin.readline().split()))
tomato = []
queue = deque()
visited = [[-2 for _ in range(M)] for _ in range(N)]
checkL = [[0, 1], [1, 0], [0, -1], [-1, 0]]
isPossible = False
for i in range(N):
    tomato.append(list(map(int, stdin.readline().split())))
    for j in range(M):
        if tomato[i][j] == -1:
            visited[i][j] = -1
        elif tomato[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    x, y, day = queue.popleft()
    if visited[x][y] == -2:
        visited[x][y] = day
        tomato[x][y] = 1
        for xDiff, yDiff in checkL:
            tmpX = x + xDiff
            tmpY = y + yDiff
            if tmpX >= 0 and tmpY >= 0 and tmpX < N and tmpY < M:
                if tomato[x+xDiff][y+yDiff] == 0:
                    queue.append((x+xDiff, y+yDiff, day+1))
maxDay = 0
for i in range(N):
    if min(visited[i]) == -2:
        print(-1)
        break
    else:
        tmpMax = max(visited[i])
        if tmpMax > maxDay:
            maxDay = tmpMax
    if i==N-1:
        isPossible = True
if isPossible:
    print(maxDay)

from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().split()))
mapL = []
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
checkL = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for _ in range(N):
    mapL.append(stdin.readline()[:-1])
queue = deque()
queue.append((0, 0, False, 1))
while queue:
    curx, cury, isCrush, day = queue.popleft()
    if not isCrush:
        if visited[0][curx][cury] == 0:
            visited[0][curx][cury] = day
        else:
            continue
    if visited[1][curx][cury] == 0 or visited[1][curx][cury] > day:
        visited[1][curx][cury] = day
    elif isCrush:
        continue
    for checkx, checky in checkL:
        tmpx = curx + checkx
        tmpy = cury + checky
        if tmpx >= 0 and tmpy >= 0 and tmpx < N and tmpy < M:
            if not isCrush:
                if mapL[tmpx][tmpy] == '1':
                    queue.append((tmpx, tmpy, True, day+1))
            if mapL[tmpx][tmpy] == '0':
                queue.append((tmpx, tmpy, isCrush, day+1))

if visited[1][-1][-1] == 0:
    print(-1)
else:
    print(visited[1][-1][-1])
'''
for i in range(2):
    print()
    for j in range(N):
        print(visited[i][j])
'''

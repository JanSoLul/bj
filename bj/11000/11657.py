from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().split()))
maxNum = 10**7
adj = []
for _ in range(M):
    x, y, w = list(map(int, stdin.readline().split()))
    adj.append((x, y, w))

dist = [maxNum for _ in range(N+1)]
dist[1] = 0
for i in range(1, N):
    for x, y, w in adj:
        if dist[x] == maxNum:
            continue
        if dist[y] > dist[x] + w:
            dist[y] = dist[x] + w

for x, y, w in adj:
    if dist[x] == maxNum:
        continue
    if dist[y] > dist[x] + w:
        print(-1)
        exit(0)

for i in range(2, N+1):
    if dist[i] < maxNum/2:
        print(dist[i])
    else:
        print(-1)


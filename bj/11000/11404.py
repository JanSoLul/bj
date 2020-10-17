from sys import stdin
from heapq import heappush, heappop

N = int(stdin.readline())
M = int(stdin.readline())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, w = list(map(int, stdin.readline().split()))
    adj[x].append((y, w))

dist = [0 for _ in range(N+1)]
heap = []
maxNum = 100000 * N+1
def dijkstra(start):
    for i in range(N+1):
        dist[i] = maxNum
    dist[start] = 0
    heappush(heap, [0, start])
    while heap:
        curw, curv = heappop(heap)
        for nextv, nextw in adj[curv]:
            nextw += curw
            if nextw < dist[nextv]:
                dist[nextv] = nextw
                heappush(heap, [nextw, nextv])

for i in range(1, N+1):
    dijkstra(i)
    for j in range(1, len(dist)):
        if dist[j] == maxNum:
            print('0', end=' ')
        else:
            print(dist[j], end=' ')
    print()

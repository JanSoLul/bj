from sys import stdin
from heapq import heappush, heappop

V, E = list(map(int, stdin.readline().split()))
adj = [[] for _ in range(V+1)]
maxNum = 200001
start = int(stdin.readline())
for _ in range(E):
    x, y, p = list(map(int, stdin.readline().split()))
    adj[x].append((y, p))

dist = [maxNum for _ in range(V+1)]
dist[start] = 0
heap = []
heappush(heap, [0, start])

while heap:
    w, cur = heappop(heap)
    for nextV, nextW in adj[cur]:
        nextW += w
        if nextW < dist[nextV]:
            dist[nextV] = nextW
            heappush(heap, [nextW, nextV])


for i in range(1, V+1):
    if dist[i] != maxNum:
        print(dist[i])
    else:
        print('INF')


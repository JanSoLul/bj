from sys import stdin
from heapq import heappush, heappop

V, E = list(map(int, stdin.readline().split()))
adj = [[] for _ in range(V+1)]
maxNum = 10 ** 9
dist = [maxNum for _ in range(V+1)]
for _ in range(E):
    x, y, w = list(map(int, stdin.readline().split()))
    adj[x].append((y, w))
    adj[y].append((x, w))

def dijkstra(start):
    heap = []
    if dist[1] != maxNum:
        for i in range(1, V+1):
            dist[i] = maxNum
    heappush(heap, [0, start])
    dist[start] = 0
    while heap:
        curW, curV = heappop(heap)
        for nextV, nextW in adj[curV]:
            nextW += curW
            if dist[nextV] > nextW:
                dist[nextV] = nextW
                heappush(heap, [nextW, nextV])


x, y = list(map(int, stdin.readline().split()))
route = [0, 0]
dijkstra(1)
route[0] = dist[x]
route[1] = dist[y]
dijkstra(x)
route[0] += dist[y]
route[1] += dist[V]
dijkstra(y)
route[0] += dist[V]
route[1] += dist[x]
tmp = min(route)
if tmp < maxNum:
    print(tmp)
else:
    print(-1)

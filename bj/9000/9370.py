from sys import stdin
from heapq import heappush, heappop

t = int(stdin.readline())
maxNum = 10**8
heap = []

def dijkstra(start):
    global isFirst
    heappush(heap, [0, start])
    dist[start] = 0
    for i in range(1, N+1):
        dist[i] = maxNum
    dist[start] = 0
    while heap:
        curw, curv = heappop(heap)
        for nextv, nextw in adj[curv]:
            nextw += curw
            if nextw < dist[nextv]:
                dist[nextv] = nextw
                heappush(heap, [nextw, nextv])


for _ in range(t):
    N, M, T = list(map(int, stdin.readline().split()))
    start, g, h = list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(N+1)]
    dist = [maxNum for _ in range(N+1)]
    isFirst = True
    route=[0, 0]
    ret = []
    end = []
    save = []
    for _ in range(M):
        x, y, w = list(map(int, stdin.readline().split()))
        adj[x].append((y, w))
        adj[y].append((x, w))

    for _ in range(T):
        end.append([int(stdin.readline()), 0, 0])
    dijkstra(start)
    for i in end:
        ret.append(dist[i[0]])
    route[0] = dist[g]
    route[1] = dist[h]
    dijkstra(g)
    route[0] += dist[h]
    for i in range(len(end)):
        end[i][2] = dist[end[i][0]]
    dijkstra(h)
    route[1] += dist[g]
    for i in range(len(end)):
        end[i][1] = dist[end[i][0]]
    for i in range(len(end)):
        tmpret = min(route[0]+end[i][1], route[1]+end[i][2])
        if tmpret == ret[i]:
            save.append(end[i][0])
    save = sorted(save)
    for i in save:
        print(i, end=' ')
    print()

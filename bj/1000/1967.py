from sys import stdin
from heapq import heappush, heappop

maxNum = 10**8
def dijkstra(start, adj, N):
    h = []
    heappush(h, [0, start])
    dist = [maxNum for _ in range(N+1)]
    dist[start] = 0
    while h:
        curw, curv = heappop(h)
        for nextv, nextw in adj[curv]:
            nextw += curw
            if nextw < dist[nextv]:
                dist[nextv] = nextw
                heappush(h, [nextw, nextv])
    return dist


def solve():
    N = int(stdin.readline())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        x, y, w = list(map(int, stdin.readline().split()))
        adj[x].append((y, w))
        adj[y].append((x, w))
    dist = dijkstra(1, adj, N)
    maxTree = 0
    maxV = 0
    for i in range(1, N+1):
        if dist[i] != maxNum and dist[i] > maxTree:
            maxTree = dist[i]
            maxV = i
    dist = dijkstra(maxV, adj, N)
    maxTree = 0
    for i in range(1, N+1):
        if dist[i] != maxNum and dist[i] > maxTree:
            maxTree = dist[i]
    print(maxTree)


if __name__ == '__main__':
    solve()

from sys import stdin

N, M = list(map(int, stdin.readline().split()))
maxNum = 10**7
adj = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, w = list(map(int, stdin.readline().split()))
    adj[x].append((y, w))
dist = [maxNum for _ in range(N+1)]
dist[1] = 0
isCycle = False

def dfs(start):

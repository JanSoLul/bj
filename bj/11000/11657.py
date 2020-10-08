from sys import stdin
from collections import deque

N, M = list(map(int, stdin.readline().split()))
maxNum = 10**7
adj = [[maxNum for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x, y, w = list(map(int, stdin.readline().split()))
    adj[x][y] = w
class Node:
    def __init__(self, w):
        self.parents = []
        self.w = w
        self.children = []

    def addParents(self, parent):
        self.parents.append(parent)

    def addChild(self, child):
        self.children.append(child)

    def isCycls:

dist = [Node(maxNum) for i in range(N+1)]
dist[1].w = 0

for i in range(1, N):
    for j in range(1, N+1):
        if adj[x][y] != maxNum:
            dist[j].
            if dist[j].w > dist[i].w + adj[i][j]:
                dist[j].w = dist[i].w + adj[i][j]



for i in range(2, N+1):
    if dist[i] < maxNum/2:
        print(dist[i])
    else:
        print(-1)


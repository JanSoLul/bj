from sys import stdin

N, M = list(map(int, stdin.readline().split()))
adj = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
check = [False for _ in range(N+1)]
for _ in range(M):
    x, y, w = list(map(int, stdin.readline().split()))
    adj[x].append((y, w))
count = 0
isMinus = False
maxNum = 10**7
dist = [maxNum for _ in range(N+1)]
def dfs(u, num):
    global isMinus
    global count
    if visited[u]:
        return True
    if check[u]:
        return False
    check[u] = True
    visited[u] = True
    count += num
    for i in adj[u]:
        if count + i[1] < 0 :
            isMinus = True
        if dist[i[0]] > dist[u] + i[1]:
            dist[i[0]] = dist[u] + i[1]
        if dfs(i[0], i[1]):
            if isMinus:
                return True
    count -= num
    visited[u] = False
    check[u] = False
    return False

dist[1] = 0
if dfs(1, 0):
    print(-1)
else:
    for i in range(2, N+1):
        if dist[i] < maxNum//2:
            print(dist[i])
        else:
            print(-1)

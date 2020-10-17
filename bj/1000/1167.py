from sys import stdin

def solve():
    V = int(stdin.readline())
    adj = [[] for _ in range(V+1)]
    for _ in range(V):
        save = list(map(int, stdin.readline().split()))[:-1]
        x = save[0]
        save = save[1:]
        i = 0
        lenSave = len(save)
        while i < lenSave:
            adj[x].append((save[i], save[i+1]))
            adj[save[i]].append((x, save[i+1]))
            i += 2
    maxNum = 10 ** 8
    dist = [maxNum for _ in range(V+1)]
    q = []
    q.append(1)
    dist[1] = 0
    while q:
        curv = q.pop()
        for nextv, nextw in adj[curv]:
            if dist[nextv] != maxNum:   continue
            dist[nextv] = dist[curv] + nextw
            q.append(nextv)
    maxTree = 0
    index = 0
    for i in range(1, V+1):
        if dist[i] != maxNum and maxTree < dist[i]:
            maxTree = dist[i]
            index = i
    for i in range(1, V+1):
        dist[i] = maxNum
    q.append(index)
    dist[index] = 0
    while q:
        curv = q.pop()
        for nextv, nextw in adj[curv]:
            if dist[nextv] != maxNum:   continue
            dist[nextv] = dist[curv] + nextw
            q.append(nextv)

    maxTree = 0
    for i in range(1, V+1):
        if dist[i] != maxNum and maxTree < dist[i]:
            maxTree = dist[i]
    print(maxTree)



if __name__ == '__main__':
    solve()

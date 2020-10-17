from sys import stdin

def solve():
    maxNum = 10 ** 7
    V, E = list(map(int, stdin.readline().split()))
    dist = [[maxNum for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        x, y, w = list(map(int, stdin.readline().split()))
        dist[x][y] = w

    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if i==j:    continue
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    minRoute = maxNum
    for i in range(1, V+1):
        for j in range(1, V+1):
            if i==j:    continue
            minRoute = min(minRoute, dist[i][j] + dist[j][i])


    if minRoute == maxNum:
        print(-1)
    else:
        print(minRoute)


if __name__ == '__main__':
    solve()

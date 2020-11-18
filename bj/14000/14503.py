from sys import stdin, setrecursionlimit
read = lambda : stdin.readline()
setrecursionlimit(10 ** 6)


def solve():
    global N
    global M
    N, M = list(map(int, read().split()))
    x, y, d = list(map(int, read().split()))
    moveL = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    backL = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    visited = [[False for _ in range(M)] for _ in range(N)]
    mapL = []
    maxClean = [0]
    for _ in range(N):
        mapL.append(list(map(int, read().split())))

    def dfs(x, y, curD, cleanCount):
        if not visited[x][y]:
            visited[x][y] = True
            cleanCount += 1
            maxClean[0] = max(maxClean[0], cleanCount)
        nextD = curD
        while True:
            nextD -= 1
            if nextD < 0:
                nextD = 3
            nextX = x + moveL[nextD][0]
            nextY = y + moveL[nextD][1]
            if nextX < 0 or nextY < 0 or nextX == N or nextY == M:
                continue
            if mapL[nextX][nextY] == 0 and not visited[nextX][nextY]:
                cleanCount = dfs(nextX, nextY, nextD, cleanCount)
                return cleanCount
            if nextD == curD:
                nextX = x + backL[nextD][0]
                nextY = y + backL[nextD][1]
                if 0 <= nextX < N and 0 <= nextY < M and mapL[nextX][nextY] == 0:
                    cleanCount = dfs(nextX, nextY, nextD, cleanCount)
                return cleanCount

    dfs(x, y, d, 0)
    print(maxClean[0])


if __name__ == '__main__':
    solve()


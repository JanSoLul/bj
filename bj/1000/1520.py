from sys import stdin, setrecursionlimit
read = lambda : stdin.readline()
setrecursionlimit(10**7)

def solve():
    M, N = list(map(int, read().split()))
    mapL = []
    checkL = [[0, -1], [0, 1], [1, 0], [-1, 0]]
    for _ in range(M):
        mapL.append(list(map(int, read().split())))
    dp = [[-1 for _ in range(N)] for _ in range(M)]
    def dfs(x, y):
        if x==M-1 and y==N-1:
            return 1
        saveRet = 0
        for checkx, checky in checkL:
            nextx = x + checkx
            nexty = y + checky
            if nextx >= 0 and nexty >= 0 and nextx < M and nexty < N:
                if mapL[x][y] > mapL[nextx][nexty]:
                    if dp[nextx][nexty] == -1:
                        saveRet += dfs(nextx, nexty)
                    else:
                        saveRet += dp[nextx][nexty]
        dp[x][y] = saveRet
        return dp[x][y]


    dp[0][0] = 0
    print(dfs(0, 0))


if __name__ == '__main__':
    solve()

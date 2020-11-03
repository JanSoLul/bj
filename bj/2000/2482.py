from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    K = int(read())
    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
    dp[1][1] = 1
    dp[2][1] = 2
    div = 10 ** 9 + 3
    for i in range(3, N+1):
        for j in range(1, i//2+1):
            if j>K:
                break
            if i/j == 2:
                dp[i][j] = 2
            elif j==1:
                dp[i][j] = i
            else:
                dp[i][j] = (dp[i-1][j] + dp[i-2][j-1]) % div
    print(dp[N][K])


if __name__ == '__main__':
    solve()

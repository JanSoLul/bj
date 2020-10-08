N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N+1)]
maxNum = 10**9
dp[1] = [1 for _ in range(10)]
dp[1][0] = 0
for i in range(1, N):
    for j in range(10):
        if j==0:
            dp[i+1][1] += dp[i][0] % maxNum
        elif j==9:
            dp[i+1][8] += dp[i][9] % maxNum
        else:
            dp[i+1][j-1] += dp[i][j] % maxNum
            dp[i+1][j+1] += dp[i][j] % maxNum
print(sum(dp[N])%maxNum)

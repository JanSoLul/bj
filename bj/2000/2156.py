from sys import stdin
N = int(stdin.readline())
amount = [int(stdin.readline()) for _ in range(N)]
amount = [0] + amount
dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    if i>1:
        dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + amount[i]
    elif i==1:
        dp[i][1] = amount[i]
    dp[i][1] = max(dp[i][1], dp[i-1][0] + amount[i])
    dp[i][2] = dp[i-1][1] + amount[i]
print(max(dp[i][0], dp[N][1], dp[N][2]))

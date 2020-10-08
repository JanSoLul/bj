from sys import stdin

N = int(stdin.readline())
stairs = [int(stdin.readline()) for _ in range(N)]
stairs = [0] + stairs
dp = [[0 for _ in range(3)] for _ in range(N+1)]

for i in range(1, N+1):
    if i > 1:
        dp[i][1] = max(dp[i][1], max(dp[i-2][1], dp[i-2][2]) + stairs[i])
    elif i==1:
        dp[i][1] = stairs[1]
    dp[i][2] = max(dp[i][2], dp[i-1][1] + stairs[i])

print(max(dp[N][1], dp[N][2]))

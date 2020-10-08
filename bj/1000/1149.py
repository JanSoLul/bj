from sys import stdin
cost = []
N = int(stdin.readline())
MAX = N*1000
for _ in range(N):
    cost.append(list(map(int, stdin.readline().split())))
dp = [[MAX for _ in range(3)] for _ in range(N+1)]

dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0
for i in range(N):
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + cost[i][0]
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + cost[i][1]
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + cost[i][2]
print(min(dp[N][0], dp[N][1], dp[N][2]))

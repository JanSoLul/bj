from sys import stdin

N = int(stdin.readline())
cost = [[]]
dp = [[]]
for i in range(1, N+1):
    cost.append(list(map(int, stdin.readline().split())))
    dp.append([0 for _ in range(i)])

dp[1][0] = cost[1][0]
for i in range(2, N+1):
    for j in range(i):
        if j==0:
            dp[i][j] = dp[i-1][j] + cost[i][j]
        elif j==i-1:
            dp[i][j] = dp[i-1][j-1] + cost[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + cost[i][j]
print(max(dp[N][:]))

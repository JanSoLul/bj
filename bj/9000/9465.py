from sys import stdin
maxNum = 10**6+1
T = int(stdin.readline())
for _ in range(T):
    value = []
    N = int(stdin.readline())
    for _ in range(2):
        value.append(list(map(int, stdin.readline().split())))
    dp = [[0, 0, 0] for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = max(dp[i+1][0], dp[i][0], dp[i][1], dp[i][2])
        dp[i+1][1] = max(dp[i+1][1], max(dp[i][0], dp[i][2]) + value[0][i])
        dp[i+1][2] = max(dp[i+1][2], max(dp[i][0], dp[i][1]) + value[1][i])
    print(max(dp[N][0], dp[N][1], dp[N][2]))

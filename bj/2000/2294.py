n, k = list(map(int, input().split()))
value = []
IMPOSSIBLE = 10**8
for _ in range(n):
    value.append(int(input()))

dp = [[IMPOSSIBLE for _ in range(k+1)] for _ in range(n+1)]

for i in range(n):
    dp[i][0] = 0
    for j in range(k+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        jj = j + value[i]
        if jj <= k:
            dp[i][jj] = min(dp[i][jj], dp[i][j] + 1)

if dp[n-1][k] == IMPOSSIBLE:
    print('-1')
else:
    print(dp[n-1][k])


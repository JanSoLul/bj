N = int(input())
dp = [0 for _ in range(N+1)]

dp[0] = 1
for i in range(N):
    dp[i+1] = (dp[i] + dp[i+1]) % 15746
    if i != N-1:
        dp[i+2] = (dp[i] + dp[i+2]) % 15746
print(dp[N])

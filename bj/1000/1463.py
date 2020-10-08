MIN = lambda a,b: a if a<b else b
N = int(input())
maxNum = 10**6
dp = [maxNum for _ in range(N + 1)]

dp[1] = 0
for i in range(1, N):
    dp[i+1] = MIN(dp[i+1], dp[i]+1)
    if i*2 <= N:
        dp[i*2] = MIN(dp[i*2], dp[i]+1)
    if i*3 <= N:
        dp[i*3] = MIN(dp[i*3], dp[i]+1)

print(dp[N])

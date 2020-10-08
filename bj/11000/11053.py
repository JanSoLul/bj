from sys import stdin
N = int(stdin.readline())
numL = list(map(int, stdin.readline().split()))
numL = [0] + numL
dp = [0 for _ in range(N+1)]

dp[1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        if numL[i]>numL[j] and dp[i] < dp[j] +1:
            dp[i] = dp[j] + 1
        if j == i-1 and dp[i] == 0:
            dp[i] = 1
print(dp)
print(max(dp))

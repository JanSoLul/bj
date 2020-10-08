from sys import stdin
N, K = list(map(int, stdin.readline().split()))
value = [0]
for _ in range(N):
    value.append(int(stdin.readline()))
dp = [0 for _ in range(K+1)]

dp[0] = 1
for i in range(1, N+1):
    for j in range(value[i], K+1):
        dp[j] += dp[j-value[i]]
print(dp[K])

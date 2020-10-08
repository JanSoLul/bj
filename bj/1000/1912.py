from sys import stdin
N = int(stdin.readline())
numL = list(map(int, stdin.readline().split())) 
dp = [0 for _ in range(N)]
dp[0] = numL[0]
for i in range(1, N):
    dp[i] = max(numL[i], numL[i]+dp[i-1])
print(max(dp))

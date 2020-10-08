from sys import stdin
N, W = list(map(int, stdin.readline().split()))
v = [0]
w = [0]
for _ in range(N):
    tmpW, tmpV = list(map(int, stdin.readline().split()))
    w.append(tmpW)
    v.append(tmpV)
dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, W+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])

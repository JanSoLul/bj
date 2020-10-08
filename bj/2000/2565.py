from sys import stdin
N = int(stdin.readline())
numL = [[0, 0] for _ in range(N)]
for i in range(N):
    numL[i] = list(map(int, stdin.readline().split()))
numL.sort()
dp = [0 for _ in range(N)]
maxNum = 1
for i in range(N):
    tmpMax = 0
    for j in range(i):
        if tmpMax < dp[j] and numL[j][1] < numL[i][1]:
            tmpMax = dp[j]
    dp[i] = tmpMax + 1
    maxNum = max(maxNum, dp[i])
print(N-max(dp))

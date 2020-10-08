from sys import stdin

N, W = list(map(int, stdin.readline().split()))
item = []
dp = [[W]]
valueD = dict()
valueD[(0, W)] = 0
maxNum = 0
for _ in range(N):
    item.append(list(map(int, stdin.readline().split())))
    dp.append([])
for i in range(1, N+1):
    for j in dp[i-1]:
        if (i, j) in valueD:
            if valueD[(i, j)] < valueD[(i-1, j)]:
                valueD[(i, j)] = valueD[(i-1, j)]
        else:
            valueD[(i, j)] = valueD[(i-1, j)]
        if not j in dp[i]:
            dp[i].append(j)
        if j >= item[i-1][0]:
            tmpNum = valueD[(i-1, j)] + item[i-1][1]
            if maxNum < tmpNum:
                maxNum = tmpNum
            if (i, j-item[i-1][0]) in valueD:
                if valueD[(i, j-item[i-1][0])] < tmpNum:
                    valueD[(i, j-item[i-1][0])] = tmpNum
            else:
                valueD[(i, j-item[i-1][0])] = tmpNum
            if not j-item[i-1][0] in dp[i]:
                dp[i].append(j-item[i-1][0])

print(maxNum)

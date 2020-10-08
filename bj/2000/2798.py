N, M = list(map(int, input().split()))
BJ = list(map(int, input().split()))

curMax = 0
for i in range(N-2):
    for j in range(i+1, N):
        for k in range(j+1, N):
            tmp = BJ[i] + BJ[j] + BJ[k]
            if curMax < tmp and tmp <= M:
                curMax = tmp
print(curMax)


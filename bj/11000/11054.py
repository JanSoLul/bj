from sys import stdin
N = int(stdin.readline())
numL = list(map(int, stdin.readline().split()))
numL = [0] + numL
incDP = [0 for _ in range(N+1)]
decDP = [0 for _ in range(N+1)]
incDP[1] = 1
decDP[-1] = 1
for i in range(2, N+1):
    for j in range(1, i):
        if numL[i] > numL[j] and incDP[i] < incDP[j] + 1:
            incDP[i] = incDP[j] + 1
        elif j==i-1 and incDP[i]==0:
            incDP[i] = 1
    decArg = -i
    for j in range(-1, decArg, -1):
        if numL[decArg] > numL[j] and decDP[decArg] < decDP[j] + 1:
            decDP[decArg] = decDP[j] + 1
        elif j==decArg+1 and decDP[decArg]==0:
            decDP[decArg] = 1
saveMax = 0
for i in range(1, N+1):
    tmp = incDP[i] + decDP[i]
    if tmp > saveMax:
        saveMax = tmp
print(saveMax-1)

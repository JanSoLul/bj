from sys import stdin

T = int(stdin.readline())
maxNum = 10 ** 7
for _ in range(T):
    N, M, K = list(map(int, stdin.readline().split()))
    adj = [[] for _ in range(N+1)]
    for _ in range(K):
        x, y, c, w = list(map(int, stdin.readline().split()))
        adj[x].append((y, w, c))
    dp = [[maxNum for _ in range(M+1)] for _ in range(N+1)]
    dp[1][0] = 0

    for i in range(M+1):
        for j in range(1, N+1):
            if dp[j][i] == maxNum:  continue
            for nextv, nextw, nextc in adj[j]:
                if nextc + i > M:   continue
                dp[nextv][nextc+i] = min(dp[nextv][nextc+i], dp[j][i]+nextw)
    ret = min(dp[N])
    if ret != maxNum :
        print(ret)
    else:
        print('Poor KCM')

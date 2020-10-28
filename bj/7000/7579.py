from sys import stdin
from heapq import heappush, heappop

def solve():
    N, M = list(map(int, stdin.readline().split()))
    mem = list(map(int, stdin.readline().split()))
    cost = list(map(int, stdin.readline().split()))
    sumC = sum(cost)
    maxNum = 10**7  * 2
    dp = [[0 for _ in range(sumC+1)] for _ in range(N)]
    result = maxNum
    for i in range(N):
        for j in range(1, sumC+1):
            if j < cost[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(mem[i] + dp[i-1][j-cost[i]], dp[i-1][j])

            if dp[i][j] >= M:
                result = min(result, j)
    if M != 0:
        print(result)
    else:
        print(0)


if __name__ == '__main__':
    solve()

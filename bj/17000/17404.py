from sys import stdin
read = lambda : stdin.readline()

def solve():
    cost = []
    N = int(read())
    MAX = N*1000
    for _ in range(N):
        cost.append(list(map(int, read().split())))
    result = MAX
    for color in range(3):
        dp = [[MAX for _ in range(3)] for _ in range(N+1)]
        for i in range(3):
            if i==color:
                dp[1][i] = cost[0][i]
        for i in range(1, N):
            dp[i+1][0] = min(dp[i][1], dp[i][2]) + cost[i][0]
            dp[i+1][1] = min(dp[i][0], dp[i][2]) + cost[i][1]
            dp[i+1][2] = min(dp[i][0], dp[i][1]) + cost[i][2]
            if i == N-1:
                dp[i+1][color] = MAX
        result = min(min(dp[N][0], dp[N][1], dp[N][2]), result)
    print(result)


if __name__ == '__main__':
    solve()

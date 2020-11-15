from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    schedule = []
    for _ in range(N):
        schedule.append(list(map(int, read().split())))
    dp = [0 for _ in range(N+1)]
    for i in range(N):
        t, p = schedule[i]
        day = i
        if i>0:
            dp[day] = max(dp[day], dp[day-1])
        finDay = day + t
        if finDay > N:
            continue
        dp[finDay] = max(dp[finDay], dp[day]+p)
    print(max(dp[N-1], dp[N]))


if __name__ == '__main__':
    solve()

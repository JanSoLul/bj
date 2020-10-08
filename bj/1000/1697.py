from collections import deque

N, K = list(map(int, input().split()))
dp = [-1 for _ in range(100001)]
checkL = [-1, 1, 0]
queue = deque()
queue.append((N, 0))
while True:
    pos, day = queue.popleft()
    if pos==K:
        print(day)
        break
    dp[pos] = day
    for i in checkL:
        tmpPos = pos + i
        if i==0:
            tmpPos = pos * 2
        if tmpPos >= 0 and tmpPos < 100001:
            if dp[tmpPos] == -1:
                queue.append((tmpPos, day+1))



from sys import stdin

N, k = list(map(int, stdin.readline().split()))
coin = []
count = 0
for i in range(N):
    tmp = int(stdin.readline())
    coin.append(tmp)
coinLen = len(coin)
while True:
    for i in range(coinLen):
        tmp = k - coin[coinLen - i - 1]
        if tmp >= 0:
            k -= coin[coinLen - i - 1]
            break
    count += 1
    if k <= 0:
        break
print(count)

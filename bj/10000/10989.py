from sys import stdin
from sys import stdout


N = int(stdin.readline())
countL = [0 for _ in range(10001)]
tmpN = 0
for i in range(N):
    tmpN = int(stdin.readline())
    countL[tmpN] += 1

for i in range(1, 10001):
    for j in range(countL[i]):
        stdout.write(str(i) + '\n')

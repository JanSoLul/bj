from sys import stdin
from sys import stdout

N = int(stdin.readline())
mapL = [list(map(int, stdin.readline().split())) for _ in range(N)]
mapL.sort(key = lambda x : (x[1], x[0]))
for x, y in mapL:
    stdout.write(str(x) + " " + str(y) + "\n")

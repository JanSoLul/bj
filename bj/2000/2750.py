from sys import stdin
N = int(input())
numL = [int(stdin.readline()) for _ in range(N)]
numL.sort()
for i in numL:
    print(i)

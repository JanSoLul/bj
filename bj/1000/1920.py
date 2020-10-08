from sys import stdin
N = int(input())
numL = list(map(int, stdin.readline().split()))
M = int(input())
checkL = list(map(int, stdin.readline().split()))
numL.sort()
for i in checkL:
    left = 0
    right = len(numL)-1
    isPrint = False
    while left <= right:
        mid = (left+right)//2
        if numL[mid] == i:
            print('1')
            isPrint = True
            break
        elif numL[mid] > i:
            right = mid-1
        else:
            left = mid+1
    if not isPrint:
        print('0')

from sys import stdin

N, M = list(map(int, stdin.readline().split()))
tree = list(map(int, stdin.readline().split()))
maxTree = max(tree)
minTree = 0
result = 0
while minTree<=maxTree:
    tmpSum = 0
    curHeight = (maxTree + minTree)//2
    for i in tree:
        if i>curHeight:
            tmpSum += i-curHeight
    if tmpSum >= M:
        if curHeight > result:
            result = curHeight
        minTree = curHeight+1
    else:
        maxTree = curHeight-1
print(result)

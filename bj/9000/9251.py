strA = input()
strB = input()
lenA = len(strA)
lenB = len(strB)
dp = [[0 for _ in range(lenB)] for _ in range(lenA)]
for i in range(lenA):
    for j in range(lenB):
        if strA[i] == strB[j]:
            if i>0 and j>0:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 1
        elif i>0 and j>0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i>0:
            dp[i][j] = dp[i-1][j]
        elif j>0:
            dp[i][j] = dp[i][j-1]
print(dp[-1][-1])
''' # debug
print('   ', end='')
for i in range(lenB):
    print(strB[i] + '  ', end='')
print()
for i in range(lenA):
    print(strA[i], end=' ')
    print(dp[i])
'''

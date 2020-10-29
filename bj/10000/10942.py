from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    numL = list(map(int, read().split()))
    numL = [0] + numL
    Q =  int(read())
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][i] = 1
    for _ in range(Q):
        start, end = list(map(int, read().split()))
        isPalindrome = False
        dpList = []
        while True:
            if dp[start][end] == 1:
                isPalindrome = True
                break
            elif numL[start] != numL[end]:
                break
            else:
                dpList.append((start, end))
                start += 1
                end -= 1
                if start > end:
                    isPalindrome = True
                    break
        if isPalindrome:
            for tmpStart, tmpEnd in dpList:
                dp[tmpStart][tmpEnd] = 1
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    solve()

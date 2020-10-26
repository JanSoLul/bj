from sys import stdin
read = lambda : stdin.readline()

def solve():
    N = int(read())
    matrix = []
    for _ in range(N):
        M, K = list(map(int, read().split()))
        matrix.append((M, K))

    def multipleMatrix(x, y, z):
        return matrix[x][0] * matrix[y][1] * matrix[z][1]


    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N-1):
        dp[i][i+1] = multipleMatrix(i, i, i+1)
        for j in range(i+2, N):
            dp[i][j] = dp[i][j-1] + multipleMatrix(i, j-1,  j)


    for d in range(2, N):
        for i in range(N-d):
            j = i+d
            minimum = [dp[i][k]+dp[k+1][j]+multipleMatrix(i,k,j) for k in range(i, j)]
            dp[i][j] = min(minimum)

    print(dp[0][N-1])


if __name__ == '__main__':
    solve()

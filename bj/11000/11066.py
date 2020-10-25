from sys import stdin
read = lambda : stdin.readline()

def solve():
    T = int(read())
    for _ in range(T):
        K = int(read())
        page = list(map(int, read().split()))

        table = [[0 for _ in range(K)] for _ in range(K)]
        for i in range(K-1):
            table[i][i+1] = page[i] + page[i+1]
            for j in range(i+2, K):
                table[i][j] = table[i][j-1] + page[j]

        for d in range(2, K):
            for i in range(K-d):
                j = i+d
                minimum = [table[i][k] + table[k+1][j] for k in range(i, j)]
                table[i][j] += min(minimum)

        print(table[0][K-1])



if __name__ == '__main__':
    solve()

from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, M, K = map(int, read().split())
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, -1, 1, 1, -1]
    food = [[5 for _ in range(N)] for _ in range(N)]
    if N == 1:
        A = [[int(read())]]
    else:
        A = []
        for _ in range(N):
            A.append(list(map(int, read().split())))
    tree = [[deque() for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, z = map(int, read().split())
        tree[x-1][y-1].appendleft(z)

    year = 0

    while year < K:
        # Spring
        deadList = []
        for i in range(N):
            for j in range(N):
                saveTree = deque()
                while tree[i][j]:
                    curTree = tree[i][j].pop()
                    if food[i][j] >= curTree:
                        food[i][j] -= curTree
                        saveTree.appendleft(curTree+1)
                    else:
                        deadList.append((i, j, curTree))
                tree[i][j] = saveTree

        # Summer
        while deadList:
            tmpx, tmpy, tmpa = deadList.pop()
            food[tmpx][tmpy] += tmpa // 2

        # Fall
        for i in range(N):
            for j in range(N):
                if tree[i][j]:
                    for k in range(len(tree[i][j])):
                        if tree[i][j][k]%5 == 0:
                            for add in range(8):
                                nextX = i + dx[add]
                                nextY = j + dy[add]
                                if 0<=nextX<N and 0<=nextY<N:
                                    tree[nextX][nextY].append(1)

        # Winter
        for i in range(N):
            for j in range(N):
                food[i][j] += A[i][j]
        year += 1
        '''
        print('tree', year)
        for i in range(N):
            print(tree[i])
        print('food')
        for i in range(N):
            print(food[i])
        '''


    totalTree = 0
    for i in range(N):
        for j in range(N):
            totalTree += len(tree[i][j])
    print(totalTree)


if __name__ == '__main__':
    solve()

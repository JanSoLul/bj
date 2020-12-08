from sys import stdin
from collections import deque
from copy import deepcopy
read = lambda : stdin.readline()

def solve():
    N, M, T = map(int, read().split())
    circle = []
    rotate = []
    neighbor = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for _ in range(N):
        circle.append(deque(list(map(int, read().split()))))
    isFirst = [True]


    def calAvg():
        ret = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if circle[i][j] > 0:
                    ret += circle[i][j]
                    count += 1
        if count == 0:
            return -1
        else:
            return ret/count


    def removeNeighbor(rx):
        #print(rx)
        circleCopy = deepcopy(circle)
        if isFirst[0]:
            isFirst[0] = False
            rx = []
            for i in range(N):
                rx.append(i)
        isChange = True
        for i in rx:
            for j in range(M):
                isRemove = False
                if circleCopy[i][j] > 0:
                    for ax, ay in neighbor:
                        nx = i + ax
                        ny = j + ay
                        if 0<=nx<N and 0<=ny<M:
                            if circleCopy[nx][ny]==circleCopy[i][j]:
                                isRemove = True
                                circle[nx][ny] = 0
                    if j==0 or j==M-1:
                        if circleCopy[i][M-1] == circleCopy[i][0]:
                            isChange = False
                            circle[i][M-1] = 0
                            circle[i][0] = 0
                    if isRemove:
                        isChange = False
                        circle[i][j] = 0
        if isChange:
            #print('Change')
            avg = calAvg()
            if avg == -1:
                print(0)
                exit(0)
            for i in range(N):
                for j in range(M):
                    if circle[i][j] > 0:
                        if circle[i][j] > avg:
                            circle[i][j] -= 1
                        elif circle[i][j] < avg:
                            circle[i][j] += 1
            isFirst[0] = True


    for _ in range(T):
        x, d, k = map(int, read().split())
        rotateL = []
        start = x-1
        for i in range(start, N, x):
            rotateL.append(i)
        for _ in range(k):
            for i in rotateL:
                if d==0:
                    circle[i].appendleft(circle[i].pop())
                else:
                    circle[i].append(circle[i].popleft())
        '''
        print('before remove')
        for i in range(N):
            print(circle[i])
        '''
        removeNeighbor(rotateL)
        '''
        print('after remove')
        for i in range(N):
            print(circle[i])
        '''
    result = 0
    for i in range(N):
        result += sum(circle[i])
    print(result)


if __name__ == '__main__':
    solve()

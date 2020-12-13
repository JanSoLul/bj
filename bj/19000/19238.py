from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    N, M, F = map(int, read().split())
    mapL = []
    checkL = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for _ in range(N):
        mapL.append(list(map(int, read().split())))
    start = list(map(int, read().split()))
    start[0] -= 1
    start[1] -= 1
    passenger = []
    destination = []
    for i in range(M):
        px, py, dx, dy = map(int, read().split())
        px -= 1
        py -= 1
        dx -= 1
        dy -= 1
        passenger.append([px, py])
        destination.append([dx, dy])


    # 각 승객으로부터의 bfs
    def bfs(st):
        visited = [[False for _ in range(N)] for _ in range(N)]
        q = deque()
        st.append(0)
        q.append(st)
        tmpRet = []
        destCount = 0
        while q:
            cx, cy, count = q.popleft()
            if visited[cx][cy]:
                continue
            if cx==start[0] and cy==start[1]:
                tmpRet.append([-1, count])
                destCount += 1
            for i in range(M):
                if cx==destination[i][0] and cy==destination[i][1]:
                    tmpRet.append([i, count])
                    destCount += 1
            if destCount == M+1:
                return tmpRet
            visited[cx][cy] = True
            for ax, ay in checkL:
                nx = cx + ax
                ny = cy + ay
                if 0<=nx<N and 0<=ny<N:
                    if mapL[nx][ny] != 1:
                        q.append((nx, ny, count+1))
        return tmpRet

    dp = []
    minD = 10 ** 6
    startLoc = None
    startpass = -1
    for i in range(M):
        dp.append(bfs([passenger[i][0], passenger[i][1]]))
        if len(dp[i]) < M+1:
            print(-1)
            exit(0)
        dp[i] = deque(sorted(dp[i], key=lambda x:x[0]))
    # 첫 승객 정하기
    for i in range(M):
        check = dp[i].popleft()
        if minD > check[1]:
            startPass = i
            startLoc = passenger[i]
            minD = check[1]
        elif minD == check[1]:
            if startLoc[0] > passenger[i][0]:
                startLoc = passenger[i]
                startPass = i
            elif startLoc[0] == passenger[i][0]:
                if startLoc[1] > passenger[i][1]:
                    startLoc = passenger[i]
                    startPass = i
    F -= minD
    taxiCount = 0
    finDrive = [False for _ in range(M)]
    while True:
        finDrive[startPass] = True
        F -= dp[startPass][startPass][1]
        if F < 0:
            print(-1)
            exit(0)
        F += 2 * dp[startPass][startPass][1]
        taxiCount += 1
        if taxiCount == M:
            print(F)
            exit(0)
        minD = 401
        tmpLoc = None
        tmpPass = 0
        for i in range(M):
            if finDrive[i]:
                continue
            if minD > dp[i][startPass][1]:
                tmpLoc = passenger[i]
                tmpPass = i
                minD = dp[i][startPass][1]
            elif minD == dp[i][startPass][1]:
                if tmpLoc[0] > passenger[i][0]:
                    tmpLoc = passenger[i]
                    tmpPass = i
                elif tmpLoc[0] == passenger[i][0]:
                    if tmpLoc[1] > passenger[i][1]:
                        tmpLoc = passenger[i]
                        tmpPass = i
        F -= minD
        if F < 0:
            print(-1)
            exit(0)
        startPass = tmpPass



if __name__ == '__main__':
    solve()

from sys import stdin
from collections import deque
read = lambda : stdin.readline()

def solve():
    R, C, T = map(int, read().split())
    mapL = []
    airCleaner = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(R):
        mapL.append(deque(map(int, read().split())))
        if mapL[i][0] == -1:
            mapL[i][0] = 0
            airCleaner.append(i)
    for _ in range(T):
        # 미세먼지 확산
        saveExpand = [[0 for _ in range(C)] for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if mapL[i][j] >= 5:
                    minusSave = 0
                    for a in range(4):
                        nx = i + dx[a]
                        ny = j + dy[a]
                        if 0<=nx<R and 0<=ny<C:
                            if ny==0 and (nx==airCleaner[0] or nx==airCleaner[1]):
                                continue
                            saveExpand[nx][ny] += mapL[i][j]//5
                            minusSave += 1
                    mapL[i][j] -= minusSave * (mapL[i][j] // 5)
        for i in range(R):
            for j in range(C):
                mapL[i][j] += saveExpand[i][j]
        # 공기청정기 작동
        # 위쪽 공기청정기
        for i in range(airCleaner[0], -1, -1):
            if i == airCleaner[0]:
                prev = mapL[i].pop()
                mapL[i].appendleft(0)
            elif i == 0:
                mapL[i].append(prev)
                mapL[i+1].appendleft(mapL[i].popleft())
            else:
                tmp = mapL[i].pop()
                mapL[i].append(prev)
                prev = tmp
                if i+1 == airCleaner[0]:
                    mapL[i].popleft()
                else:
                    mapL[i+1].appendleft(mapL[i].popleft())
        # 아래쪽 공기청정기
        for i in range(airCleaner[1], R):
            if i == airCleaner[1]:
                prev = mapL[i].pop()
                mapL[i].appendleft(0)
            elif i == R-1:
                mapL[i].append(prev)
                mapL[i-1].appendleft(mapL[i].popleft())
            else:
                tmp = mapL[i].pop()
                mapL[i].append(prev)
                prev = tmp
                if i-1 == airCleaner[1]:
                    mapL[i].popleft()
                else:
                    mapL[i-1].appendleft(mapL[i].popleft())
    fineDust = 0
    for i in range(R):
        fineDust += sum(mapL[i])
    print(fineDust)


if __name__ == '__main__':
    solve()

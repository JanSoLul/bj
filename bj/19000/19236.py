from sys import stdin
from collections import deque
from copy import deepcopy
read = lambda : stdin.readline()


def solve():
    # 8방향 체크하는 리스트
    checkL = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

    # map 저장하는 리스트
    mapL = [[] for _ in range(4)]

    # 각 물고기의 위치를 저장하는 리스트 (해당 물고기가 죽으면 0으로 바꿈)
    save = [None for _ in range(16)]
    for i in range(4):
        tmpL = list(map(int, read().split()))
        for j in range(4):
            mapL[i].append([tmpL[j*2]-1, tmpL[j*2+1]-1])
            save[tmpL[j*2]-1] = [i, j]
    save[mapL[0][0][0]] = 0
    shark = [0, 0]
    mapL[0][0][0] = 16
    maxPoint = [0]


    # 이동하는 함수 (dfs)
    def move(copyMap, copyPos):
        '''
        print()
        for i in range(4):
            for j in range(4):
                print(copyMap[i][j][0], end=' ')
            print()
        '''
        # 각 물고기들이 이동한다
        for i in range(16):
            if copyPos[i]==0:
                continue
            fx, fy = copyPos[i]
            fd = copyMap[fx][fy][1]
            for _ in range(8):
                nx = fx + checkL[fd][0]
                ny = fy + checkL[fd][1]
                if 0<=nx<4 and 0<=ny<4 and copyMap[nx][ny][0]<16:
                    nextFishNum = copyMap[nx][ny][0]
                    copyMap[fx][fy][1] = fd
                    if nextFishNum==-1:
                        copyPos[i] = [nx, ny]
                    else:
                        copyPos[i], copyPos[nextFishNum] = copyPos[nextFishNum], copyPos[i]
                    copyMap[fx][fy], copyMap[nx][ny] = copyMap[nx][ny], copyMap[fx][fy]
                    '''
                    print(i, nextFishNum)
                    for i in range(4):
                        print(copyMap[i])
                    '''
                    break
                else:
                    fd += 1
                    if fd==8:
                        fd = 0

        # 상어가 이동한다
        sx, sy = shark
        sd = copyMap[sx][sy][1]
        isChange = False
        for i in range(1, 4):
            nx = sx + checkL[sd][0]*i
            ny = sy + checkL[sd][1]*i
            if 0<=nx<4 and 0<=ny<4:
                if copyMap[nx][ny][0]!=-1:
                    nextMap = deepcopy(copyMap)
                    nextPos = deepcopy(copyPos)
                    diedFish = nextMap[nx][ny][0]
                    nextMap[sx][sy][0] = -1
                    nextMap[nx][ny][0] = 16
                    shark[0], shark[1] = nx, ny
                    nextPos[diedFish] = 0
                    isChange = True
                    move(nextMap, nextPos)
            else:
                # 해당 방향 바로 다음이 영역 밖이거나 해당 방향의 물고기를 모두 잡았을 때
                # 지금까지 잡을 물고기의 합을 구함
                if i==1 or (i==3 and not isChange):
                    tmpPoint = 0
                    for j in range(16):
                        if copyPos[j]==0:
                            tmpPoint += j+1
                    maxPoint[0] = max(maxPoint[0], tmpPoint)
    move(deepcopy(mapL), deepcopy(save))
    print(maxPoint[0])


if __name__ == '__main__':
    solve()

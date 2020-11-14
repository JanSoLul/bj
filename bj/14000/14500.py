from sys import stdin
read = lambda : stdin.readline()

def solve():
    N, M = list(map(int, read().split()))
    mapL = []
    for i in range(N):
        mapL.append(list(map(int, read().split())))

    def checkL1(x, y):
        # ㅁ   ㅁㅁ   ㅁ ㅁㅁ
        # ㅁ     ㅁ   ㅁ ㅁ
        # ㅁㅁ   ㅁ ㅁㅁ ㅁ
        if x > N-3 or y > M-2:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x+1][y]+mapL[x+2][y]+mapL[x+2][y+1],
                    mapL[x][y]+mapL[x][y+1]+mapL[x+1][y+1]+mapL[x+2][y+1],
                    mapL[x][y+1]+mapL[x+1][y+1]+mapL[x+2][y]+mapL[x+2][y+1],
                    mapL[x][y]+mapL[x][y+1]+mapL[x+1][y]+mapL[x+2][y])
        return tmpMax


    def checkL2(x, y):
        # ㅁㅁㅁ ㅁㅁㅁ ㅁ         ㅁ
        # ㅁ         ㅁ ㅁㅁㅁ ㅁㅁㅁ
        if x > N-2 or y > M-3:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x][y+1]+mapL[x][y+2]+mapL[x+1][y],
                mapL[x][y]+mapL[x][y+1]+mapL[x][y+2]+mapL[x+1][y+2],
                mapL[x][y]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+1][y+2],
                mapL[x][y+2]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+1][y+2])
        return tmpMax


    def checkI1(x, y):
        # ㅁㅁㅁㅁ
        if y > M-4:
            return -1
        return mapL[x][y]+mapL[x][y+1]+mapL[x][y+2]+mapL[x][y+3]


    def checkI2(x, y):
        # ㅁ
        # ㅁ
        # ㅁ
        # ㅁ
        if x > N-4:
            return -1
        return mapL[x][y]+mapL[x+1][y]+mapL[x+2][y]+mapL[x+3][y]


    def checkO(x, y):
        # ㅁㅁ
        # ㅁㅁ
        if x > N-2 or y > M-2:
            return -1
        return mapL[x][y]+mapL[x][y+1]+mapL[x+1][y]+mapL[x+1][y+1]


    def checkZ1(x, y):
        # ㅁㅁ     ㅁㅁ
        #   ㅁㅁ ㅁㅁ
        if x > N-2 or y > M-3:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x][y+1]+mapL[x+1][y+1]+mapL[x+1][y+2],
                mapL[x][y+1]+mapL[x][y+2]+mapL[x+1][y]+mapL[x+1][y+1])
        return tmpMax


    def checkZ2(x, y):
        # ㅁ     ㅁ
        # ㅁㅁ ㅁㅁ
        #   ㅁ ㅁ
        if x > N-3 or y > M-2:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+2][y+1],
                mapL[x][y+1]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+2][y])
        return tmpMax


    def checkV1(x, y):
        # ㅁㅁㅁ   ㅁ
        #   ㅁ   ㅁㅁㅁ
        if x > N-2 or y > M-3:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x][y+1]+mapL[x][y+2]+mapL[x+1][y+1],
                mapL[x][y+1]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+1][y+2])
        return tmpMax


    def checkV2(x, y):
        # ㅁ     ㅁ
        # ㅁㅁ ㅁㅁ
        # ㅁ     ㅁ
        if x > N-3 or y > M-2:
            return -1
        tmpMax = max(mapL[x][y]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+2][y],
                mapL[x][y+1]+mapL[x+1][y]+mapL[x+1][y+1]+mapL[x+2][y+1])
        return tmpMax

    maxNum = 0
    for i in range(N):
        for j in range(M):
            tmpL = [checkL1(i,j), checkL2(i,j), checkI1(i,j), checkI2(i,j), checkO(i,j),
                    checkZ1(i,j), checkZ2(i,j), checkV1(i,j), checkV2(i,j)]
            maxNum = max(maxNum, max(tmpL))
    print(maxNum)


if __name__ == '__main__':
    solve()

